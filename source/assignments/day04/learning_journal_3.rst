*******************************
Python Learning Journal: Step 3
*******************************

In part one of this tutorial, you built the *data model* for a simple learning
journal web application using Pyramid and PostgreSQL. You deployed this work to
Heroku and confirmed that you could see a simple page.

In part two, you constructed the *control layer* needed to read and write
journal entries, and added the part of the *view layer* needed to read entries.
You also implemented a *testing harness* for your code so that you can use Test
Driven Development practices while creating your code. Again, you deployed the
work to Heroku and confirmed that you could view an entry created through the
Python command line.

Here in part three you'll implement the remaining portions of the *view layer*
allowing you to edit journal entries directly through the web. You'll also add
simple *authentication* to ensure that only you can write entries in your own
journal. Finally, you'll add a bit of *CSS* to begin making your journal your
own.

Ready?  Let's begin!

Preparing to Work
=================

In part 1, you created a *virtualenv project* to work in.  The first step for
starting a new work day on the app will be to return to that environment:

.. code-block:: bash

    cewing$ workon learning_journal
    [learning_journal]
    192:learning_journal cewing$

Next, you'll want to change directories into your ``git`` repository and make a
new branch for the work in this part of the tutorial:

.. code-block:: bash

    [learning_journal]
    192:learning_journal cewing$ cd learning_journal/
    [learning_journal]
    [master=]
    192:learning_journal cewing$ git checkout -b step3
    Switched to a new branch 'step3'
    [learning_journal]
    [step3]
    192:learning_journal cewing$

You'll do your work for this part of the tutorial in this branch, and then when
your tests are passing, merge it back to your ``master`` branch. Building this
habit ensures that your ``master`` branch always contains code that is
deployable.


Adding Journal Entries
======================

After deploying in the last part, you creted an entry by using your *controller
api* directly at the Python command line. Not so convenient, honestly. What you
really want is a *view function* that will:

* Accept incoming form data from a request
* Get the data for ``title`` and ``text``
* Create a new entry in the database
* Throw an appropriate HTTP error if that fails
* Show the user the list of entries when done.


Testing Add an Entry
--------------------

Again, first come the tests. Add this new code to ``test_journal.py``:

.. code-block:: python

    def test_post_to_add_view(app):
        entry_data = {
            'title': 'Hello there',
            'text': 'This is a post',
        }
        response = app.post('/add', params=entry_data, status='3*')
        redirected = response.follow()
        actual = redirected.body
        for expected in entry_data.values():
            assert expected in actual

**NOTES**

* You are using the ``app`` fixture because you want to ensure that you have an
  application to interact with.
* The ``post`` method of the WebTest ``app`` sends an ``HTTP POST``
  request to the provided URL.
* The ``params`` argument provided represents form input data. In real life, the
  user would have entered data into HTML form elements.
* The ``status`` argument asserts that the HTTP status code of the response
  matches. Here we are looking for a *redirect* response (why?).


Before you run this test, a word on the format of pytest output.  It's quite
verbose by default.  Sometimes it's easier to see what's going wrong if you
have less to look at. Luckily, pytest provides `a way to customize test
output`_.  We can use the ``--tb`` flag to control how output is presented.
The value ``native`` will simply print native Python tracebacks for a more
familiar look:

.. _a way to customize test output: http://pytest.org/latest/usage.html#modifying-python-traceback-printing

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 6 items

    test_journal.py .....F

    =================================== FAILURES ====================================
    _____________________________ test_post_to_add_view _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 163, in test_post_to_add_view
        response = app.post('/add', params=entry_data, status='3*')
      File "/Users/cewing/virtualenvs/learning_journal/lib/python2.7/site-packages/webtest/app.py", line 370, in post
        content_type=content_type)
      File "/Users/cewing/virtualenvs/learning_journal/lib/python2.7/site-packages/webtest/app.py", line 735, in _gen_request
        expect_errors=expect_errors)
      File "/Users/cewing/virtualenvs/learning_journal/lib/python2.7/site-packages/webtest/app.py", line 631, in do_request
        self._check_status(status, res)
      File "/Users/cewing/virtualenvs/learning_journal/lib/python2.7/site-packages/webtest/app.py", line 666, in _check_status
        "Bad response: %s (not %s)", res_status, status)
    AppError: Bad response: 404 Not Found (not 3*)
    ====================== 1 failed, 5 passed in 0.41 seconds =======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$


Implement Adding An Entry
-------------------------

You've already created the controller you need to write entries. All you lack
is a *view function* to do the work. Because a Pyramid view function must
either pass data to a renderer or return a value suitable as an HTTP response,
we cannot use the *controller* we wrote yesterday directly.  We need to add a
new *view function* (in ``journal.py``) that will:

* Pass the ``request`` to our ``write_entry`` function so that function can try
  writing an entry.
* Handle any exceptions raised by ``write_entry`` appropriately, returning a
  useful HTTP response.
* Send the viewer back to the home page if the entry was successfully written

We'll also need to configure a *route* that will connect to this new *view
function*.

.. code-block:: python

    # add imports
    from pyramid.httpexceptions import HTTPFound, HTTPInternalServerError

    # and then down below write_entry
    @view_config(route_name='add', request_method='POST')
    def add_entry(request):
        try:
            write_entry(request)
        except psycopg2.Error:
            # this will catch any errors generated by the database
            return HTTPInternalServerError
        return HTTPFound(request.route_url('home'))

    # finally, in the "main" function:
    config.add_route('home', '/') # <- already present
    config.add_route('add', '/add') # <- ADD THIS


**NOTES**

* You can specify the HTTP methods that Pyramid will allow for any view. By
  default any HTTP method will work, here you explicitly allow only ``POST``
  requests.
* The ``pyramid.httpexceptions`` module contains all sorts of useful HTTP
  Response types.
* You catch any errors generated by the database and use the HTTP error code
  ``500 Internal Server Error`` to signal the user that an unrecoverable
  problem occurred.
* The ``HTTPFound`` response requires the URL of the page where you want your
  users to end up.
* The ``route_url`` method of the ``request`` generates the correct URL for a
  given *route* by name, decoupling your code from specific URLs.

Try running your tests again.  This time they should all pass:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 6 items

    test_journal.py ......

    =========================== 6 passed in 0.40 seconds ============================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

This new view is a bit more complex than anything we've done before, but we
have only one test on it.  What more might we test? What are possible failure
modes for this view?  What happens if we try to use ``app.get('/add')``?  See
if you can't write a few other tests that better cover the possibilities.

HTML Forms
----------

You're almost done. You can add entries and view them. But look at that
last view. Is there a *renderer* associated with it at all?

There isn't one. That's because that view is never meant to be be visible.
Look carefully at the logic. What happens?

So where do the form values come from?

There's only one visible page in your app so far. Why not add a form there?
Open ``list_entries.html`` and add the following code:

.. code-block:: jinja

    {% block body %}  <!-- already there -->
    <aside>
    <form action="{{ request.route_url('add') }}" method="POST" class="add_entry">
      <div class="field">
        <label for="title">Title</label>
        <input type="text" size="30" name="title" id="title"/>
      </div>
      <div class="field">
        <label for="text">Text</label>
        <textarea name="text" id="text" rows="5" cols="80"></textarea>
      </div>
      <div class="control_row">
        <input type="submit" value="Share" name="Share"/>
      </div>
    </form>
    </aside>
    <h2>Entries</h2>  <!-- already there -->

**NOTES**

* The pyramid_jinja2 *renderer* provides access to the ``request`` instance.
  You can use the same ``route_url`` method in a jinja2 template to create URLs
  for form submission, links and so on.
* You can use the ``method`` attribute of a ``<form>`` tag to determine what
  HTTP method will be used when the form is submitted.
* You use the HTML5 ``<aside>`` tag to indicate that the form is not part of
  the main content of this page.

And that's it.  Your app is now finished (for now, at least). Start the app on
your local machine and make an entry or two to try it out:

.. code-block:: bash

    learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ python journal.py
    serving on http://0.0.0.0:5000

When you're done testing it, use ``^C`` to quit.


Controlling Access
==================

One thing you may have noticed while testing your app in a browser is that you
did not have to log in. Convenient, but not really all that safe. Knowing the
kind of place the internet is, you probably don't want to allow just anyone to
post journal entries in your journal.

The process of verifying the identity of a user visiting your website is called
**authentication** (AuthN for short). The closely related, but different
process of determining what *rights* an authenticated user has in your website
is called **authorization** (AuthZ).

Next, you'll be adding *authentication* and *authorization* to your journal.
This will allow you to display entries to the general public while reserving
the ability to write new entries to a known user (you).

Storing a User
--------------

You could implement an entire database table for the purpose of storing your
user information, but really that's overkill for a system that only has one
user. You should never implement more code than you need.

So how can you solve the problem of storing the data needed to authenticate a
user?

How about *configuration*?

Add the following lines to ``journal.py`` in the "main" function:

.. code-block:: python

    # this configuratin setting is already there
    settings['db'] = os.environ.get(
        'DATABASE_URL', 'dbname=learning_journal user=cewing'
    )
    settings['auth.username'] = os.environ.get('AUTH_USERNAME', 'admin')
    settings['auth.password'] = os.environ.get('AUTH_PASSWORD', 'secret')

After this, your app will have configuration settings that represent the
*username* and *password* for your administrative user.

Because you are using the same pattern for this configuration as for the
database connection string, you'll be able to use *Environment Variables* on
your Heroku machine to store the username and password for your live site in a
reasonably secure fashion.

And when you are working locally, developing your app, you've got a nice,
simple fallback mechanism.


Configuring AuthN/AuthZ
-----------------------

To *authenticate* a user, the most basic pattern is to confirm a username and
password. In general the steps are to:

* accept a username and password as arguments
* raise an appropriate error if either is missing
* raise an appropriate error if they cannot be confirmed to be correct
* persist the fact that the user is authenticated

HTTP is a **stateless** protocol.  That means that no individual request can
know anything about any other request. So how do you accomplish that fourth
goal?  The usual method is to send an encrypted *cookie* back to the user in an
HTTP response. This cookie is saved and re-transmitted to the server with each
successive request. This gets around the *stateless* nature of HTTP by sending
the required information back and forth.

In the Pyramid web framework, control of the process of *authentication* is
given to a class that implements the attributes and methods of an
**Authentication Policy**.  There are a few of these policies made available in
the `pyramid.authentication`_ package.

.. _pyramid.authentication: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authentication.html

For our authentication policy we'll be using the
``AuthTktAuthenticationPolicy``. This policy issues an encrypted,
`specially formatted cookie`_ to the user's browser. Whenever a new request
comes in, Pyramid unencrypts the cookie and establishes the identity of the
user from the data it contains.

.. _specially formatted cookie: http://stackoverflow.com/questions/1844623/what-is-the-auth-tkt-cookie-format

To set up this policy, we need to add some new configuration to our
application. In ``journal.py`` make the following changes:

.. code-block:: python

    # at the top, add a new import
    from pyramid.authentication import AuthTktAuthenticationPolicy

    # then in the "main" function add this
    def main():
        # ... the first two lines are already there
        # secret value for session signing:
        secret = os.environ.get('JOURNAL_SESSION_SECRET', 'itsaseekrit')
        session_factory = SignedCookieSessionFactory(secret)
        # add a secret value for auth tkt signing
        auth_secret = os.environ.get('JOURNAL_AUTH_SECRET', 'anotherseekrit')
        # and add a new value to the constructor for our Configurator:
        config = Configuration(
            settings=settings,
            session_factory=session_factory,
            authentication_policy=AuthTktAuthenticationPolicy(
                secret=auth_secret,
                hashalg='sha512'
            ),
        )

Once you know *who* someone is, you will also want to know *what rights* they
should be given in your website. Pyramid provides for this through an
**Authorization Policy**. There is a version of such a policy made available in
the `pyramid.authorization`_ package. It's called the
``ACLAuthorizationPolicy`` and it works by allowing you to specify permissions
that should be granted or denied to certain *principals*.

.. _pyramid.authorization: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authorization.html

To enable this policy we'll again need to update our configuration. Return to
``journal.py`` and the ``main`` function:

.. code-block:: python

    # add an import at the top of the file:
    from pyramid.authorization import ACLAuthorizationPolicy

    # and update our Configurator constructor like so:
    def main():
        # ...
        config = Configuration(
            settings=settings,
            session_factory=session_factory,
            authentication_policy=AuthTktAuthenticationPolicy(
                secret=auth_secret,
                hashalg='sha512'
            ),
            authorization_policy=ACLAuthorizationPolicy(),
        )


Testing Login
-------------

Before we implement login, we'll want to write some tests to cover what we want
to have happen. For login, remember, the steps are:

* accept a username and password from an incoming ``request``
* raise an appropriate error if either is missing
* raise an appropriate error if they cannot be confirmed to be correct

We'll need to have a fixture that provides a request with the proper settings
to verify a username and password. We can reproduce that from the configuration
in our ``main`` function.  In ``test_journal.py`` add the following:

.. code-block:: python

    @pytest.fixture(scope='function')
    def auth_req(request):
        settings = {
            'auth.username': 'admin',
            'auth.password': 'secret',
        }
        testing.setUp(settings=settings)
        req = testing.DummyRequest()

        def cleanup():
            testing.tearDown()

        request.addfinalizer(cleanup)

        return req

**NOTES**

* The keys to our settings dictionary match those we use in the real
  configuration of our application
* The ``setUp`` function from `pyramid.testing`_ provides the setup needed to
  make a ``DummyRequest`` act like a real one.
* The ``tearDown`` function reverses that process for good test isolation.
* The request we return will behave like a real request in that it will provide
  access to the settings we generated.

.. _pyramid.testing: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/testing.html

Next, we write a few tests that use our new fixture:

.. code-block:: python

    def test_do_login_success(auth_req):
        from journal import do_login
        auth_req.params = {'username': 'admin', 'password': 'secret'}
        assert do_login(auth_req)


    def test_do_login_bad_pass(auth_req):
        from journal import do_login
        auth_req.params = {'username': 'admin', 'password': 'wrong'}
        assert not do_login(auth_req)


    def test_do_login_bad_user(auth_req):
        from journal import do_login
        auth_req.params = {'username': 'bad', 'password': 'secret'}
        assert not do_login(auth_req)


    def test_do_login_missing_params(auth_req):
        from journal import do_login
        for params in ({'username': 'admin'}, {'password': 'secret'}):
            auth_req.params = params
            with pytest.raises(ValueError):
                do_login(auth_req)


Run your tests, and you should see that they fail:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 10 items

    test_journal.py ......FFFF

    =================================== FAILURES ====================================
    _____________________________ test_do_login_success _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 189, in test_do_login_success
        from journal import do_login
    ImportError: cannot import name do_login
    ____________________________ test_do_login_bad_pass _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 195, in test_do_login_bad_pass
        from journal import do_login
    ImportError: cannot import name do_login
    ____________________________ test_do_login_bad_user _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 201, in test_do_login_bad_user
        from journal import do_login
    ImportError: cannot import name do_login
    _________________________ test_do_login_missing_params __________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 207, in test_do_login_missing_params
        from journal import do_login
    ImportError: cannot import name do_login
    ====================== 4 failed, 6 passed in 0.41 seconds =======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Now, we need to implement the ``do_login`` function. Back in ``journal.py`` add
the following:

.. code-block:: python

    def do_login(request):
        username = request.params.get('username', None)
        password = request.params.get('password', None)
        if not (username and password):
            raise ValueError('both username and password are required')

        settings = request.registry.settings
        if username == settings.get('auth.username', ''):
            if password == settings.get('auth.password', ''):
                return True
        return False

**NOTES**

* Do not distinguish between a bad password and a bad username. To do so is to
  leak sensitive information.
* You can always get hold of the settings for your application from
  ``request.registry.settings``

Try running your tests again to see if they work:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 10 items

    test_journal.py ..........

    =========================== 10 passed in 0.42 seconds ===========================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$


Security
--------

Now you have a way to authenticate a user, but there's still something a bit
problematic here.

Notice that in your ``do_login`` function you compare the password received from the
user directly against the one stored:

.. code-block:: python

    if password == settings.get('auth.password', ''):

This implies that the password you have stored on the server is in plain text.
**THIS IS A TERRIBLE IDEA**. Even when using environment variables to store a
password, plain text should never be an option.

For clarity:

**NEVER EVER EVER STORE PLAIN TEXT PASSWORDS IN ANY FORMAT ANYWHERE**

Instead, you should be hashing passwords for storage using a secure, one-way
algorithm, and comparing that value against the hash of the value the user
provides.

Python comes with a number of reasonable hashing algorithms, but I suggest
instead using an external library called `cryptacular`_. It provides
implementations of a couple of hashing algorithms, with a single unified
interface for interacting with them.

.. _cryptacular: https://pypi.python.org/pypi/cryptacular/

Start by installing the library in your virtual environment for this project:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ pip install cryptacular
    Downloading/unpacking cryptacular
    ...

    Successfully installed cryptacular pbkdf2
    Cleaning up...
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Next, you'll upgrade how you calculate the password in ``main`` in
``journal.py``:

.. code-block:: python

    # at the top, add a new import
    from cryptacular.bcrypt import BCRYPTPasswordManager

    # then update the ADMIN_PASSWORD config setting:
    manager = BCRYPTPasswordManager()
    app.config['ADMIN_PASSWORD'] = os.environ.get(
        'ADMIN_PASSWORD', manager.encode('secret')
    )

**NOTES**

* You import the manager you want from one of the cryptacular modules
  (``bcrypt`` or ``pbkdf2``)
* Then you instantiate a manager instance
* Finally, you call the ``encode`` method of the manager instance to encrypt
  the value you pass in.

Finally, repeat that process for the settings you create for your ``auth_req``
fixture in ``test_journal.py``:

.. code-block:: python

    # the import
    from cryptacular.bcrypt import BCRYPTPasswordManager

    # and the fixture:
    @pytest.fixture(scope='function')
    def auth_req(request):
        manager = BCRYPTPasswordManager()
        settings = {
            'auth.username': 'admin',
            'auth.password': manager.encode('secret'),
        }
        # ...

If you run your tests at this point, you'll see that the successful login test
will now fail:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 10 items

    test_journal.py ......F...

    =================================== FAILURES ====================================
    _____________________________ test_do_login_success _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/learning_journal/learning_journal/test_journal.py", line 193, in test_do_login_success
        assert do_login(auth_req)
    AssertionError: assert <function do_login at 0x10cae3410>(<pyramid.testing.DummyRequest object at 0x10cd6a510>)
    ====================== 1 failed, 9 passed in 1.06 seconds =======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

To fix the failure, we have to update the ``do_login`` function we wrote in
``journal.py`` before:

.. code-block:: python

    def do_login(request):
        username = request.params.get('username', None)
        password = request.params.get('password', None)
        if not (username and password):
            raise ValueError('both username and password are required')

        settings = request.registry.settings
        # below here is changed
        manager = BCRYPTPasswordManager()
        if username == settings.get('auth.username', ''):
            hashed = settings.get('auth.password', '')
            return manager.check(hashed, password)

**NOTES**

* ``manager.check`` is the other half of the cryptacular manager API
* The first argument is the hashed value (stored in our settings), the second
  is the open value passed in from the request
* The method returns ``True`` if they match, and ``False`` if not.

Now try that test again:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test --tb=native
    ============================== test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.26 -- pytest-2.6.4
    collected 10 items

    test_journal.py ..........

    =========================== 10 passed in 1.05 seconds ===========================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Sweeeeeet!


*****************
FIXME STARTS HERE
*****************

avoid rendering errors
======================


Implement a Front-End
---------------------

Next, you'll need to provide a pair of *views* that will allow a user to log in
and log out. Start with the log in view. This view should:

* provide a form to fill in username and password
* reload with an error message if login fails
* redirect to the journal home page if login succeeds

Moreover, you'll want to update the journal home page to only show the form for
adding entries if the user is logged in.

Start with tests.  In ``test_journal.py`` add the following:

.. code-block:: python

    SUBMIT_BTN = '<input type="submit" value="Share" name="Share"/>'


    def login_helper(username, password):
        login_data = {
            'username': username, 'password': password
        }
        client = app.test_client()
        return client.post(
            '/login', data=login_data, follow_redirects=True
        )


    def test_start_as_anonymous(db):
        client = app.test_client()
        anon_home = client.get('/').data
        assert SUBMIT_BTN not in anon_home


    def test_login_success(db):
        username, password = ('admin', 'admin')
        response = login_helper(username, password)
        assert SUBMIT_BTN in response.data


    def test_login_fails(db):
        username, password = ('admin', 'wrong')
        response = login_helper(username, password)
        assert 'Login Failed' in response.data

If you run your tests now, you'll see three failures:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 12 items

    test_journal.py .........FFF

    =================================== FAILURES ===================================
    ___________________________ test_start_as_anonymous ____________________________

    db = None

        def test_start_as_anonymous(db):
            client = app.test_client()
            anon_home = client.get('/').data
    >       assert SUBMIT_BTN not in anon_home

    ...

    test_journal.py:170: AssertionError
    ______________________________ test_login_success ______________________________

    db = None

        def test_login_success(db):
            username, password = ('admin', 'admin')
            response = login_helper(username, password)
    >       assert SUBMIT_BTN in response.data
    
    ...

    test_journal.py:176: AssertionError
    _______________________________ test_login_fails _______________________________

    db = None

        def test_login_fails(db):
            username, password = ('admin', 'wrong')
            response = login_helper(username, password)
    >       assert 'Login Failed' in response.data
    
    ...

    test_journal.py:183: AssertionError
    ====================== 3 failed, 9 passed in 0.89 seconds ======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Fix these one at a time.  First, ensure that the form for adding an entry does
not appear when you are not logged in.  Add the following to
``list_entries.html``:

.. code-block:: jinja

    {% if session.logged_in %} <!-- ADD THIS LINE -->
    <aside>
    <form action="{{ url_for('add_entry') }}" method="POST" class="add_entry">
      ...
    </form>
    </aside>
    {% endif %} <!-- AND THIS ONE -->

Re-run your tests:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 12 items

    test_journal.py ..........FF

    =================================== FAILURES ===================================
    ______________________________ test_login_success ______________________________

    ...

    test_journal.py:176: AssertionError
    _______________________________ test_login_fails _______________________________

    ...

    test_journal.py:183: AssertionError
    ===================== 2 failed, 10 passed in 0.83 seconds ======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Great, that first failure is fixed.

Next you'll implement the login view to fix the remaining two failures. In
``journal.py`` add the following:

.. code-block:: python

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            try:
                do_login(request.form['username'].encode('utf-8'),
                         request.form['password'].encode('utf-8'))
            except ValueError:
                error = "Login Failed"
            else:
                return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)

**NOTES**

* This view is available *both* for ``GET`` and ``POST`` requests
* Any form that changes application state should only be processed on a
  ``POST`` request.
* On a simple ``GET`` just render the empty form
* On error, the login form is rendered again, passing the error to the user.
* On success, you redirect to the ``show_entries`` view.

In order for this view to work, you'll need also to have a ``login.html``
template. Add a new file by that name to your ``templates`` directory and write
the following to the new file:

.. code-block:: jinja

    {% extends "base.html" %}
    {% block body %}
      <h2>Login</h2>
      {% if error -%}
      <p class="error"><strong>Error</strong> {{ error }}
      {%- endif %}
      <form action="{{ url_for('login') }}" method="POST">
        <div class="field">
          <label for="username">Username</label>
          <input type="text" name="username" id="username"/>
        </div>
        <div class="field">
          <label for="password">Password</label>
          <input type="password" name="password" id="password"/>
        </div>
        <div class="control_row">
          <input type="submit" name="Login" value="Login"/>
        </div>
      </form>
    {% endblock %}

Now you should be able to run your tests with success:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 12 items

    test_journal.py ............

    ========================== 12 passed in 1.19 seconds ===========================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Logging Out
-----------

Logout is a much simpler prospect.  Just one simple view.  It should:

* remove the session data indicating that the user is logged in
* redirect the user back to the journal home page

Start with a test in ``test_journal.py``:

.. code-block:: python

    def test_logout(db):
        home = login_helper('admin', 'admin').data
        assert SUBMIT_BTN in home
        client = app.test_client()
        response = client.get('/logout')
        assert SUBMIT_BTN not in response.data
        assert response.status_code == 302

Run your test to see it fail:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 13 items

    test_journal.py ............F

    =================================== FAILURES ===================================
    _________________________________ test_logout __________________________________

    ...

    E       assert 404 == 200
    E        +  where 404 = <Response 233 bytes [404 NOT FOUND]>.status_code

    test_journal.py:191: AssertionError
    ===================== 1 failed, 12 passed in 1.42 seconds ======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

And then implement the view in ``journal.py``:

.. code-block:: python

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        return redirect(url_for('show_entries'))

And the tests will pass:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 13 items

    test_journal.py .............

    ========================== 13 passed in 1.40 seconds ===========================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Moving Around
-------------

Finally, though you now have views that can log you in and out, there is no way
for you to get to them without just typing the URLs in your browser. You should
add some UI in the page that lets you move around easily.

Open ``base.html`` and add the following:

.. code-block:: jinja

    <header> <!-- this is already in the file -->
      <aside id="user-controls">
        <ul>
        {% if not session.logged_in %}
          <li><a href="{{ url_for('login') }}">log in</a></li>
        {% else %}
          <li><a href="{{ url_for('logout') }}">log out</a></li>
        {% endif %}
        </ul>
      </aside>
      <nav> <!-- so is this -->

At this point you should be able to start up the app, log in through your
browser, add an entry or two and then log back out.  Try it:

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ python journal.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader


Adding Style
============

Great.  That worked.  Not very nice looking though, is it.

The last step is to add a minimal CSS stylesheet that will help out a bit.

Flask looks for **static resources** like stylesheets and javascript files in
much the same way it finds templates.  It looks for a ``static`` directory
located relative to the location of the flask app.

Go ahead and create a new directory, called ``static`` right in your repository
root, next to the ``journal.py`` file and the ``templates`` directory.

Inside that directory, add a new file called ``style.css`` and add the
following structural CSS rules:

.. code-block:: css

    body{
        color:#111;
        padding:0;
        margin:0}
    header{
        margin:0;
        padding:0 0.75em;
        width:100%;}
    header:after{
        content:"";
        display:table;
        clear:both;}
    header a{
        text-decoration:none}
    header aside{
        float:right;
        text-align:right;
        padding-right:0.75em}
    header ul{
        list-style:none;
        list-style-type:none;
        display:inline-block}
    header ul li{
        margin:0 0.25em 0 0}
    header ul li a{
        padding:0;
        display:inline-block}
    main{padding:0 0.75em 1em}
    main:after{
        content:"";
        display:table;
        clear:both}
    main article{
        margin-bottom:1em;
        padding-left:0.5em}
    main article h3{margin-top:0}
    main article .entry_body{
        margin:0.5em}
    main aside{float:right}
    main aside .field{
        margin-bottom:1em}
    main aside .field input,
    main aside .field label,
    main aside .field textarea{
        vertical-align:top}
    main aside .field label{
        display:inline-block;
        width:15%;
        padding-top:2px}
    main aside .field input,
    main aside .field textarea{
        width:83%}
    main aside .control_row input{
        margin-left:16%}

Finally, you'll need to tell ``base.html`` to look for this new stylesheet.
Make the following change to that file:

.. code-block:: jinja

    <head>
      <meta charset="utf-8">
      <title>Python Learning Journal</title>
      <!--[if lt IE 9]>
      <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
      <![endif]-->

      <!-- ADD THE FOLLOWING LINE ONLY -->
      <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" type="text/css">
    </head>

Now, if you go ahead and reload your journal in your browser, you should see
something like this:

.. image:: /_static/lj-final.png
    :width: 90%

And that, my friends, is a complete journal app in three steps!


Deploying Your Work
===================

The final reward for all this hard work is to see your app running live.

Repeat the steps you performed for the previous assignment to submit your work
and prepare for deployment. As a reminder, here's the outline:


1. push all local work on the ``step3`` branch up to GitHub
2. create a pull request in your GitHub repository from ``step3`` to
   ``master``
3. copy the URL for that pull request and submit your assignment in Canvas
4. locally, checkout ``master`` and merge your work from ``step2`` (remember,
   this will close your pull request, but that's fine)
5. push master to the heroku remote


That's well and good, but there's a bit more you need to do this time in order
to have full login and session capability on Heroku.

Remember, the username and password for your admin user, and the secret key
needed for using sessions are all supposed to be held in environment variables.
You'll need to set those in order for everything to work as expected.

The Heroku toolbelt provides a tool for setting, getting and unsetting
environment variables. The values are sent to the server via SSH, and so are
safe in transmission.

Use these tools now to set a username for your app:

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ heroku config:set ADMIN_USERNAME=cewing
    Setting config vars and restarting fizzy-fairy-1234... done, v8
    ADMIN_USERNAME: cewing
    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$

Next, you'll want to set your password.  Remember that you want it encrypted
using the same algorithm as in your app.  Use python to help. In your terminal,
fire up a Python interpreter:

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ python
    Python 2.7.5 (default, Mar  9 2014, 22:15:05)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Then, import the hashing algorithm and encrypt your password:

.. code-block:: pycon

    >>> from passlib.hash import pbkdf2_sha256 as hasher
    >>> my_password = 'secret password'
    >>> hasher.encrypt(my_password)
    '$pbkdf2-sha256$20000$FmLsPcd4D.Fcq5WyFkII4Q$6ykWQ1p5serGo.J3vzggeC8ebckL4xE0gXKbQ4SMzJE'
    >>> ^D

Copy that value and then use it to set the environment variable in Heroku
(remember, don't actually use 'secret password' for your password, please):

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ heroku config:set ADMIN_PASSWORD='$pbkdf2-sha256$20000$FmLsPcd4D.Fcq5WyFkII4Q$6ykWQ1p5serGo.J3vzggeC8ebckL4xE0gXKbQ4SMzJE'
    Setting config vars and restarting fizzy-fairy-1234... done, v9
    ADMIN_PASSWORD: $pbkdf2-sha256$20000$FmLsPcd4D.Fcq5WyFkII4Q$6ykWQ1p5serGo.J3vzggeC8ebckL4xE0gXKbQ4SMzJE
    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$

Finally, let's also use Python to set up a really nice, random value for the
secret key.  Fire up your interpreter again:

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ python
    Python 2.7.5 (default, Mar  9 2014, 22:15:05)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Now, use some convenient constants from the ``string`` module and a bit of
``set`` magic combined with ``random`` to generate a 128-character random
secret key:

.. code-block:: pycon

    >>> import string
    >>> import random
    >>> chars = string.letters + string.digits
    >>> specials = "".join(set(string.punctuation) - set("'`\""))
    >>> specials
    '!#%$&)(+*-,/.;:=<?>@[]\\_^{}|~'
    >>> chars += specials
    >>> chars
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%$&)(+*-,/.;:=<?>@[]\\_^{}|~'
    >>> secret_key = "".join(random.choice(chars) for _ in xrange(128))
    >>> secret_key
    'Xtkm!VU+Q5kYyjU{[N]r\\S.n2T&xSnxYF;Qu6JvygYi{T.ZM>nnW+hf6@2oyiB2Qp<XDv%4=KM!2S;#lNAfy8<=<RRbu7ST[B!)^OhA6(uQf-nclu22!tKgb=d8OI6v4'
    >>> ^D

Again, copy that value and use it to set the environment variable in Heroku:

.. code-block:: bash

    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$ heroku config:set SECRET_KEY='Xtkm!VU+Q5kYyjU{[N]r\\S.n2T&xSnxYF;Qu6JvygYi{T.ZM>nnW+hf6@2oyiB2Qp<XDv%4=KM!2S;#lNAfy8<=<RRbu7ST[B!)^OhA6(uQf-nclu22!tKgb=d8OI6v4'
    Setting config vars and restarting fizzy-fairy-1234... done, v10
    SECRET_KEY: Xtkm!VU+Q5kYyjU{[N]r\\S.n2T&xSnxYF;Qu6JvygYi{T.ZM>nnW+hf6@2oyiB2Qp<XDv%4=KM!2S;#lNAfy8<=<RRbu7ST[B!)^OhA6(uQf-nclu22!tKgb=d8OI6v4
    [learning_journal]
    [step3]
    heffalump:learning_journal cewing$

And that should do it.  You are now able to view your app live on Heroku, log
in, add posts, the whole nine yards!


Point DNS at Heroku
-------------------

Now that your app is ready, you should go ahead and point a real domain at it.

Use your DNS provider to set up a nice name.  I used
``pyjournal.crisewing.com``.

Once you've chosen and set up a good domain name,
`follow the instructions here`_ to set up a custom subdomain and point it at
your app on Heroku.

.. _follow the instructions here: https://devcenter.heroku.com/articles/custom-domains#custom-subdomains

When you're done, give the worlds DNS servers a few minutes to respond to your
chages (the exact amount of time will depend on your DNS settings) and then
visit your running Python Learning Journal at your very own domain.

