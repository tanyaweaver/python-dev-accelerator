*******************************
Python Learning Journal: Step 3
*******************************

In part one of this tutorial, you built the *data model* for a simple learning
journal web application using Flask and PostgreSQL. You deployed this work to
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
api* directly at the Python command line. Not so convenient, honestly. You need
a view that will:

* Accept incoming form data from a request
* Get the data for ``title`` and ``text``
* Create a new entry in the database
* Throw an appropriate HTTP error if that fails
* Show the user the list of entries when done.


Testing Add an Entry
--------------------

Again, first come the tests. Add this new code to ``test_journal.py``:

.. code-block:: python

    def test_add_entries(db):
        entry_data = {
            u'title': u'Hello',
            u'text': u'This is a post',
        }
        actual = app.test_client().post(
            '/add', data=entry_data, follow_redirects=True
        ).data
        assert 'No entries here so far' not in actual
        for expected in entry_data.values():
            assert expected in actual

**NOTES**

* You are using the ``db`` fixture to ensure that an initialized database is
  present.
* The ``post`` method of the Flask ``test_client`` sends an ``HTTP POST``
  request to the provided URL.
* The ``data`` argument provided represents form input data. In real life, the
  user would have entered data into HTML form elements.

Verify that your test fails as expected:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 6 items

    test_journal.py .....F

    =================================== FAILURES ===================================
    _______________________________ test_add_entries _______________________________

    db = None

        def test_add_entries(db):
            entry_data = {
                u'title': u'Hello',
                u'text': u'This is a post',
            }
            actual = app.test_client().post(
                '/add', data=entry_data, follow_redirects=True
            ).data
            assert 'No entries here so far' not in actual
            for expected in entry_data.values():
    >           assert expected in actual
    E           assert 'This is a post' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'

    test_journal.py:125: AssertionError
    ====================== 1 failed, 5 passed in 0.27 seconds ======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$


Implement Adding An Entry
-------------------------

You've already created the controller you need to write entries. All you lack
is a **view** function to do the work (in ``journal.py``):

.. code-block:: python

    # add imports
    from flask import abort
    from flask import request
    from flask import url_for
    from flask import redirect

    # and then down by the l
    @app.route('/add', methods=['POST'])
    def add_entry():
        try:
            write_entry(request.form['title'], request.form['text'])
        except psycopg2.Error:
            # this will catch any errors generated by the database
            abort(500)
        return redirect(url_for('show_entries'))

**NOTES**

* You can specify the HTTP methods that Flask will allow for any view. By
  default these are ``GET`` and ``HEAD``.
* Here you explicitly allow only ``POST`` requests.
* You can use the ``flask.abort()`` function to return an HTTP error response.
* You catch any errors generated by the database and use the HTTP error code
  ``500 Internal Server Error`` to signal the user that an unrecoverable
  problem occurred.
* The ``redirect`` method takes the URL of the page where you want your users
  to end up.
* The ``url_for`` method generates the correct URL for a given *view*,
  decoupling your code from specific URLs.

Try running your tests again.  This time they should all pass:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 6 items

    test_journal.py ......

    =========================== 6 passed in 0.21 seconds ===========================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

**Hooray!**

You're almost done. You can add entries and view them. But look at that
last view. Do you see a call to ``render_template`` in there at all?

There isn't one. That's because that view is never meant to be be visible.
Look carefully at the logic. What happens?

So where do the form values come from?

Create the Form
---------------

There's only one visible page in your app so far. Why not add a form there?
Open ``list_entries.html`` and add the following code:

.. code-block:: jinja

    {% block body %}  <!-- already there -->
    <aside>
    <form action="{{ url_for('add_entry') }}" method="POST" class="add_entry">
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

* Remember that Flask provides access to ``url_for()`` in templates.
* You can use the ``method`` attribute of a ``<form>`` tag to determine what
  HTTP method will be used when the form is submitted.
* You use the HTML5 ``<aside>`` tag to indicate that the form is not part of
  the main content of this page.

And that's it.  Your app is now finished (for now, at least). Start the app on
your local machine and make an entry or two to try it out:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ python journal.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

When you're done testing it, use ``^C`` to quit.


Authenticating a User
=====================

One thing you may have noticed while testing your app in a browser is that you
did not have to log in. Convenient, but not really all that safe. You probably
don't want to allow just anyone to post journal entries in your journal.

The process of verifying the identity of a user visiting your website is called
**authentication** (AuthN for short). The closely related, but different
process of determining what *rights* an authenticated user has in your website
is called **authorization** (AuthZ).

Next, you'll be adding *authentication* to your journal.  This will allow you
to display entries to the general public while reserving the ability to write
new entries to a known user (you).

Storing a User
--------------

You could implement an entire database table for the purpose of storing your
user information, but really that's overkill for a system that only has one
user. You should never implement more code than you need.

So how can you solve the problem of storing the data needed to authenticate a
user?

How about *configuration*?

Add the following lines to ``journal.py``:

.. code-block:: python

    # this configuratin setting is already there
    app.config['DATABASE'] = os.environ.get(
        'DATABASE_URL', 'dbname=learning_journal user=cewing'
    )
    # add the following two new settings just below
    app.config['ADMIN_USERNAME'] = os.environ.get(
        'ADMIN_USERNAME', 'admin'
    )
    app.config['ADMIN_PASSWORD'] = os.environ.get(
        'ADMIN_PASSWORD', 'admin'
    )

After this, your app will have configuration settings that represent the
*username* and *password* for your administrative user.

Because you are using the same pattern for this configuration as for the
database connection string, you'll be able to use *Environment Variables* on
your Heroku machine to store the username and password for your live site in a
reasonably secure fashion.

And when you are working locally, developing your app, you've got a nice,
simple fallback mechanism.


Logging In
----------

To authenticate a user, the most basic pattern is to confirm a username and
password. You'll need some sort of *controller* that will do this. It should:

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

Flask provides a mechanism for accomplishing this task, the ``flask.session``
object. This is another *local global* like ``flask.g`` that can hold
informatino that should be persisted between requests.

Start by writing a test for a controller method that meets this specification.
In ``test_journal.py`` add the following:

.. code-block:: python

    # at the top, add an import
    from flask import session

    # at the end, add new tests
    def test_do_login_success(req_context):
        username, password = ('admin', 'admin')
        from journal import do_login
        assert 'logged_in' not in session
        do_login(username, password)
        assert 'logged_in' in session


    def test_do_login_bad_password(req_context):
        username = 'admin'
        bad_password = 'wrongpassword'
        from journal import do_login
        with pytest.raises(ValueError):
            do_login(username, bad_password)


    def test_do_login_bad_username(req_context):
        password = admin
        bad_username = 'wronguser'
        from journal import do_login
        with pytest.raises(ValueError):
            do_login(bad_username, password)

Run your tests, and you should see that they fail:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 9 items

    test_journal.py ......FFF

    =================================== FAILURES ===================================
    ____________________________ test_do_login_success _____________________________

    req_context = None

        def test_do_login_success(req_context):
            username, password = ('admin', 'admin')
    >       from journal import do_login
    E       ImportError: cannot import name do_login

    test_journal.py:132: ImportError
    __________________________ test_do_login_bad_password __________________________

    req_context = None

        def test_do_login_bad_password(req_context):
            username = 'admin'
            bad_password = 'wrongpassword'
    >       from journal import do_login
    E       ImportError: cannot import name do_login

    test_journal.py:141: ImportError
    __________________________ test_do_login_bad_username __________________________

    req_context = None

        def test_do_login_bad_username(req_context):
            password = 'admin'
            bad_username = 'wronguser'
    >       from journal import do_login
    E       ImportError: cannot import name do_login

    test_journal.py:149: ImportError
    ====================== 3 failed, 6 passed in 0.24 seconds ======================

Now, we need to implement the ``do_login`` function. Back in ``journal.py`` add
the following:

.. code-block:: python

    # add an import at the top
    from flask import session

    def do_login(username='', passwd=''):
        if username != app.config['ADMIN_USERNAME']:
            raise ValueError
        if passwd != app.config['ADMIN_PASSWORD']:
            raise ValueError
        session['logged_in'] = True

**NOTES**

* Do not distinguish between a bad password and a bad username. To do so is to
  leak sensitive information.
* Do not store more information than is absolutely required in a session.
* The ``flask.session`` local global functions just like a dictionary.

Try running your tests again to see if they work:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 9 items

    test_journal.py ......F..

    =================================== FAILURES ===================================
    ____________________________ test_do_login_success _____________________________

    req_context = None

        def test_do_login_success(req_context):
            username, password = ('admin', 'admin')
            from journal import do_login
            assert 'logged in' not in session
    >       do_login(username, password)

    test_journal.py:134:

    ...

    E       RuntimeError: the session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.

    ../../../virtualenvs/learning_journal/lib/python2.7/site-packages/flask/sessions.py:126: RuntimeError
    ====================== 1 failed, 8 passed in 0.41 seconds ======================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

As it turns out, Flask will not allow using the session without having a
**secret key** configured.  This key is used to perform the encryption of the
cookie sent back to the user. Preventing you from using a session without one
is a good example of *secure by default*.

Back in ``journal.py`` go ahead and add a new configuration setting:

.. code-block:: python

    app.config['SECRET_KEY'] = os.environ.get(
        'FLASK_SECRET_KEY', 'sooperseekritvaluenooneshouldknow'
    )

And now running your tests will work:

.. code-block:: python

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 9 items

    test_journal.py .........

    =========================== 9 passed in 0.24 seconds ===========================
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

    if passwd != app.config['ADMIN_PASSWORD']:

This implies that the password you have stored on the server is in plain text.
**THIS IS A TERRIBLE IDEA**. Even when using environment variables to store a
password, plain text should never be an option.

For clarity:

**NEVER EVER EVER STORE PLAIN TEXT PASSWORDS IN ANY FORMAT ANYWHERE**

Instead, you should be hashing passwords for storage using a secure, one-way
algorithm, and comparing that value against the hash of the value the user
provides.

Python comes with a number of reasonable hashing algorithms, but I suggest
instead using an external library called `passlib`_. It provides
implementations of a large number of hashing algorithms, with a single unified
interface for interacting with them. It makes changing from one hashing
algorithm to another very simple.

.. _passlib: http://pythonhosted.org/passlib/

Start by installing the library in your virtual environment for this project:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ pip install passlib
    Downloading/unpacking passlib
      Downloading passlib-1.6.2.tar.gz (408kB): 408kB downloaded
      Running setup.py (path:/Users/cewing/virtualenvs/learning_journal/build/passlib/setup.py) egg_info for package passlib

    Installing collected packages: passlib
      Running setup.py install for passlib

    Successfully installed passlib
    Cleaning up...
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Next, you'll upgrade how you calculate the password for ``app.config`` in
``journal.py``:

.. code-block:: python

    # at the top, add a new import
    from passlib.hash import pbkdf2_sha256

    # then update the ADMIN_PASSWORD config setting:
    app.config['ADMIN_PASSWORD'] = os.environ.get(
        'ADMIN_PASSWORD', pbkdf2_sha256.encrypt('admin')
    )

**NOTES**

* You import the hashing algorithm you want to use from ``passlib.hash``
* Then you call the ``encrypt`` method passing the value you wish to hash
* Many hashing algorithms have options you can pass as additional arguments to
  ``<hash>.encrypt``, `read the documentation to see what's available`_.

.. _read the documentation to see what's available: http://pythonhosted.org/passlib/

If you run your tests at this point, you'll see that the successful login test
will now fail:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test -k "do_login_success"
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 9 items

    test_journal.py F

    =================================== FAILURES ===================================
    ____________________________ test_do_login_success _____________________________

    req_context = None

        def test_do_login_success(req_context):
            username, password = ('admin', 'admin')
            from journal import do_login
            assert 'logged_in' not in session
    >       do_login(username, password)

    test_journal.py:133:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    username = 'admin', passwd = 'admin'

        def do_login(username='', passwd=''):
            if username != app.config['ADMIN_USERNAME']:
                raise ValueError
            if passwd != app.config['ADMIN_PASSWORD']:
    >           raise ValueError
    E           ValueError

    journal.py:108: ValueError
    ================== 8 tests deselected by '-kdo_login_success' ==================
    ==================== 1 failed, 8 deselected in 0.34 seconds ====================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Updating the ``do_login`` function to use the same hashing algorithm should do
the trick:

.. code-block:: python

    def do_login(username='', passwd=''):
        if username != app.config['ADMIN_USERNAME']:
            raise ValueError
        if not pbkdf2_sha256.verify(passwd, app.config['ADMIN_PASSWORD']):
            raise ValueError
        session['logged_in'] = True

**NOTES**

* ``<hash>.verify`` is the other half of the passlib API
* The first argument is the unhashed value from the user, the second is the
  stored value
* The method returns ``True`` if they match, and ``False`` if not.

Now try that test again:

.. code-block:: bash

    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$ py.test -k "do_login_success"
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 9 items

    test_journal.py .

    ================== 8 tests deselected by '-kdo_login_success' ==================
    ==================== 1 passed, 8 deselected in 0.51 seconds ====================
    [learning_journal]
    [step3 *]
    heffalump:learning_journal cewing$

Sweeeeeet!


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

