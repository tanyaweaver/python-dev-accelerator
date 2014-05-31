*******************************
Python Learning Journal: Step 2
*******************************

In part one of this tutorial, you built the *data model* for a simple learning
journal web application using Flask and PostgreSQL. You deployed this work to
Heroku and confirmed that you could see a simple page.

In this second part, you'll build the *control layer* and the *view layer* for
this application. Along the way, you'll learn about Test-Driven Development and
unit testing in Python using the ``pytest`` package.

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
    192:learning_journal cewing$ git checkout -b step2
    Switched to a new branch 'step2'
    [learning_journal]
    [step2]
    192:learning_journal cewing$

You'll do your work for this part of the tutorial in this branch, and then when
your tests are passing, merge it back to your ``master`` branch. Building this
habit ensures that your ``master`` branch always contains code that is
deployable.


Managing DB Connections
=======================

Before you go to far, a word or two about the circle of life.


The Request/Response Cycle
--------------------------

Every interaction in an HTTP-based system is bounded by the interchange of one
*request* and one *response*. No HTTP application can do anything until some
client makes a request. And no action by such an application is complete until
a response has been sent back to the client.

This is the lifecycle of an http web application.

In a data-driven application, the database is the memory store for the
application. It makes sense to bind the lifecycle of a database connection to
this same request/response cycle.

Flask does not dictate that you write an application that uses a database.
Because of this, managing the lifecycle of database connection so that they are
connected to the request/response cycle is up to you.

Happily, Flask *does* provide a way to help you.


Request Boundary Decorators
---------------------------

The Flask *app* provides decorators we can use on our database lifecycle
functions:

``@app.before_request``:
  Any function decorated by this will be called before the cycle begins

``@app.after_request``:
  Any function decorated by this will be called after the cycle is complete.

  However, if an unhandled exception occurs, these functions are skipped.

``@app.teardown_request``:
  Any function decorated by this will be called at the end of the cycle,
  *even if* an unhandled exception occurs.


Context in Flask
----------------

Consider the following simple functions, meant to create and destroy a database
connection:

.. code-block:: python

    def get_database_connection():
        db = connect_db()
        return db

    @app.teardown_request
    def teardown_request(exception):
        db.close()

How does the ``db`` object get from one place to the other? It's not passed. It
isn't bound at module scope. Where does ``teardown_request`` find it?


You might be tempted to say "attach it to the Flask ``app`` since that's
global." But the Flask ``app`` is a *global* context, shared **across all
requests**. This won't work for a database connection.

Flask solves this problem by providing what it calls *local globals*. These
objects can be imported, as if they were part of the *global* context. But in
reality they are constructed *locally* for to each request.

The local global most useful for us in this situation is `flask.g`_. You can
set attributes on this object and since it can be imported anywhere, they can
be passed from function to function. Perfect for things like a database
connection.

.. _flask.g: http://flask.pocoo.org/docs/api/#flask.g,


Getting and Releasing A Connection
----------------------------------

With ``flask.g`` as a place to hold a connection, you're ready to rock. In
``journal.py`` add the following code:

.. code-block:: python

        # add this import at the top:
        from flask import g

        # add these function after init_db
        def get_database_connection():
            db = getattr(g, 'db', None)
            if db is None:
                g.db = db = connect_db()
            return db

        @app.teardown_request
        def teardown_request(exception):
            db = getattr(g, 'db', None)
            if db is not None:
                if exception:
                    # if there was a problem, rollback any existing transaction
                    db.rollback()
                else:
                    # otherwise, commit
                    db.commit()
                db.close()

Once you've written these functions, commit your changes with a comment about
what you've just done. "Commit early and commit often" is a good programmer's
motto.


Setting Up Testing
==================

In `Test Drive Development`_ you start by writing tests that demonstrate the
functionality you want to build. Once a test is written, you run it and see
that it fails. This proves that your application hasn't sneakily already
provided that functionality and robbed you of a job. Then you implement the
code needed to make the test pass.

.. _Test Drive Development: http://en.wikipedia.org/wiki/Test-driven_development,


Before you can write tests, though, you'll need to add a new package you'll be
using to run your tests: `pytest`_.  In your terminal, with your
``learning_journal`` virtualenv active, use ``pip`` to install ``pytest``:

.. _pytest: http://pytest.org/latest/contents.html

.. code-block:: bash

    [learning_journal]
    [step2]
    192:learning_journal cewing$ pip install pytest
    Downloading/unpacking pytest
      Downloading pytest-2.5.2.tar.gz (608kB): 608kB downloaded
      Running setup.py (path:/Users/cewing/virtualenvs/learning_journal/build/pytest/setup.py) egg_info for package pytest

      ...

    Successfully installed pytest py
    Cleaning up...
    [learning_journal]
    [step2]
    192:learning_journal cewing$

Then, you'll need to create a new file to hold your tests. Call it
``test_journal.py``:

.. code-block:: bash

    [learning_journal]
    [step2]
    192:learning_journal cewing$ touch test_journal.py
    [learning_journal]
    [step2]
    192:learning_journal cewing$

At this point, your project directory structure should look like this::

    ../../learning_journal/
    └── learning_journal
        ├── .gitignore
        ├── LICENSE
        ├── Procfile
        ├── README.md
        ├── journal.py
        ├── requirements.txt
        └── test_journal.py

The ``pytest`` module provides a new command, ``py.test``.  When you execute
that command in your terminal, the package uses a standard heuristic to find
tests.

* It starts in the directory where the command is invoked.
* It searches for Python files that start with ``test_``.
* It imports these files and finds functions that start with ``test_``.
* It executes those functions and reports the results.

To begin, add the following code in your ``test_journal.py`` file:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from contextlib import closing
    import pytest

    from journal import app
    from journal import connect_db
    from journal import get_database_connection
    from journal import init_db


    TEST_DSN = 'dbname=test_learning_journal user=cewing'


    def clear_db():
        with closing(connect_db()) as db:
            db.cursor().execute("DROP TABLE entries")
            db.commit()

**Notes**

* Remember to use the correct name for the user, mine is just an example.
* Notice that you'll be using a different ``dbname`` for testing. This prevents
  overwriting data you might want to save.

Take a moment to create that new database:

.. code-block:: bash

    [learning_journal]
    [step2]
    192:learning_journal cewing$ createdb test_learning_journal

You've created a ``clear_db`` function. It will be used for removing your test
database table when the tests are finished for isolation.

Creating Fixtures
-----------------

The ``pytest`` module does more than just test discovery. It supports
`fixtures`_. 

Fixtures help you to manage resources needed for your tests. You'll add a few
fixtures to help test your Flask app.

.. _fixtures: http://pytest.org/latest/fixture.html

The first fixture is responsible for configuring your Flask app for testing.
Add this code to ``test_journal.py``:

.. code-block:: python

    @pytest.fixture(scope='session')
    def test_app():
        """configure our app for use in testing"""
        app.config['DATABASE'] = TEST_DSN
        app.config['TESTING'] = True

**NOTES**: 

* The ``pytext.fixture`` decorator registers the ``test_app`` function as a
  fixture with pytest.
* The ``scope`` argument passed to the decorator determines how often a fixture
  is run.

  * ``session`` scope is run only once each time ``py.test`` is invoked.
  * ``module`` scope is run once for each module of tests (once per Python
    file).
  * ``function`` scope is run once for each test function.

* Configuration like this applies across all tests, so scope this fixture to
  ``session``.
* This fixture requires no teardown so there's no code written to clean up
  after tests are done.

The next fixture you'll write will handle initializing the database tables and
removing them after. Add the following to ``test_journal.py``:

.. code-block:: python

    @pytest.fixture(scope='session')
    def db(test_app, request):
        """initialize the entries table and drop it when finished"""
        init_db()

        def cleanup():
            clear_db()

        request.addfinalizer(cleanup)

**Notes**:

* The fixture function is defined with parameters.
* The names of the parameters must match *registered fixtures*.
* The fixtures named as parameters will be run surrounding the new fixture.
* You name ``test_app`` to ensure that configuration changes are in place when
  the database is set up.
* The ``request`` parameter is a fixture that ``pytest`` registers.
* You use it to connect the ``cleanup`` function to the ``db`` fixture.
* This means that ``cleanup`` will be run after tests are complete as a
  tear-down action.

The last fixture helps each test to run in isolation from other tests. Add the
following code to ``test_journal.py``:

.. code-block:: python

    @pytest.yield_fixture(scope='function')
    def req_context(db):
        """run tests within a test request context so that 'g' is present"""
        with app.test_request_context('/'):
            yield
            con = get_database_connection()
            con.rollback()

* Remember that your database lifecycle is bound to the *request/response
  cycle* 
* The database connection will be attached to ``flask.g``
* Flask creates ``g`` when a cycle begines, but tests **have no
  request/response cycle**.
* Flask's ``app.test_request_context`` is a *context provider*.
  * Used in a ``with``statement it creates a mock request/response cycle.
* The request only exists *inside* the ``with`` block, so the callback pattern
  used in the ``db`` fixture would not work.
* The `yield_fixture decorator`_ allows fixtures made from *generator functions*
* Because ``yield`` preserves internal state, the entire test happens **inside
  the context manager scope**!
* When control returns to the fixture, code after the ``yield`` statement is
  executed as the tear-down action.

.. _yield_fixture decorator: http://pytest.org/latest/yieldfixture.html


Writing and Reading Entries
===========================

Your journal's *data model* consists of *entries*. You've set up a simple
database schema to represent them:

.. code-block:: psql

    CREATE TABLE entries (
        id serial PRIMARY KEY,
        title VARCHAR (127) NOT NULL,
        text TEXT NOT NULL,
        created TIMESTAMP NOT NULL
    )

To write an entry, what would you need to do?

* Provide a title
* Provide some body text
* Set a date/time
* Write them to a row in the database


Test Writing An Entry
---------------------

Start by writing a test that demonstrates the desired functionality. In
``test_journal.py``, add the following:

.. code-block:: python

    def run_independent_query(query, params=[]):
        con = get_database_connection()
        cur = con.cursor()
        cur.execute(query, params)
        return cur.fetchall()


    def test_write_entry(req_context):
        from journal import write_entry
        expected = ("My Title", "My Text")
        write_entry(*expected)
        rows = run_independent_query("SELECT * FROM entries")
        assert len(rows) == 1
        for val in expected:
            assert val in rows[0]

**NOTES**

* ``pytest`` will only run functions that start with ``test_`` as tests.
* The ``run_independent_query`` is a *helper functions* you can re-use.

In your terminal, run the ``py.test`` command to see the expected failure:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 1 items

    test_journal.py F

    =================================== FAILURES ===================================
    _______________________________ test_write_entry _______________________________

    req_context = None

        def test_write_entry(req_context):
    >       from journal import write_entry
    E       ImportError: cannot import name write_entry

    test_journal.py:55: ImportError
    =========================== 1 failed in 0.16 seconds ===========================

Implement ``write_entry``
-------------------------

Next you need to make the test pass. Return to ``journal.py`` and add the
following:

.. code-block:: python

    # at the top of the file, add this import
    import datetime

    # below DB_SCHEMA add this new SQL query string:
    DB_ENTRY_INSERT = """
    INSERT INTO entries (title, text, created) VALUES (%s, %s, %s)
    """

    # add this just above the hello function near the bottom of the file.
    def write_entry(title, text):
        if not title or not text:
            raise ValueError("Title and text required for writing an entry")
        con = get_database_connection()
        cur = con.cursor()
        now = datetime.datetime.utcnow()
        cur.execute(DB_ENTRY_INSERT, [title, text, now])

**NOTES**

* The SQL statement will insert a new entry into your ``entries`` table.
* Although the ``%s`` placeholders in the SQL look like *string formatting*
  they are not.
* The call signature for ``.execute(query, params)`` calls for a second
  paramter that is a sequence of values to insert.
* Parameters passed this way are properly escaped and safe from SQL Injection.
* Only ever use this form to parameterize SQL queries in Python.

**NEVER USE PYTHON STRING FORMATTING WITH A SQL STRING**.

* Notice that ``write_entry`` does not require a value for the ``created``
  field.
* The field is required, so you build and provide it *inside* the function.
* You are creating a time value in UTC or `Coordinated Universal Time`_.
* It is best practice to store time values in UTC.

.. _Coordinated Universal Time: http://en.wikipedia.org/wiki/Coordinated_Universal_Time

Re-run your tests and verify that your work is correct:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 1 items

    test_journal.py .

    =========================== 1 passed in 0.17 seconds ===========================

What other tests might you implement here?


Test Reading Entries
--------------------

To read your journal, you'll need a method that returns entries. For now, the
controller function can return all of them for a simple listing page. Your
specs:

* The return value should be a list of entries.
* If there are no entries, the function should return an empty list.
* Each entry in the list should be a dictionary of at least 'title', 'text' and
  'created'
* The list should be ordered with the most recently created entries first.

Again, begin with tests. Back in ``test_journal.py`` add the following code:

.. code-block:: python

    def test_get_all_entries_empty(self):
        with self.app.test_request_context('/'):
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 0)
    
    def test_get_all_entries(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 1)
            for entry in entries:
                self.assertEquals(expected[0], entry['title'])
                self.assertEquals(expected[1], entry['text'])

Run your tests now to ensure that the two new tests fail:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 3 items

    test_journal.py .FF

    =================================== FAILURES ===================================
    __________________________ test_get_all_entries_empty __________________________

    req_context = None

        def test_get_all_entries_empty(req_context):
    >       from journal import get_all_entries
    E       ImportError: cannot import name get_all_entries

    test_journal.py:65: ImportError
    _____________________________ test_get_all_entries _____________________________

    req_context = None

        def test_get_all_entries(req_context):
    >       from journal import get_all_entries, write_entry
    E       ImportError: cannot import name get_all_entries

    test_journal.py:71: ImportError
    ====================== 2 failed, 1 passed in 0.25 seconds ======================


Implement ``get_all_entries``
-----------------------------

You need to implement ``get_all_entries``. Back in ``journal.py`` add the
following:

.. code-block:: python

    # add this new SQL string below the others
    DB_ENTRIES_LIST = """
    SELECT id, title, text, created FROM entries ORDER BY created DESC
    """

    def get_all_entries():
        """return a list of all entries as dicts"""
        con = get_database_connection()
        cur = con.cursor()
        cur.execute(DB_ENTRIES_LIST)
        keys = ('id', 'title', 'text', 'created')
        return [dict(zip(keys, row)) for row in cur.fetchall()]

**NOTES**

* You run a query using the database *cursor*, not the *connection*.
* After running the query, you must read the results.
  * Get all results with ``cursor.fetchall()``.
  * Get *n* results with ``cursor.fetchmany(size=n)``.
  * Get one result with ``cursor.fetchone()``.
* ``dict(zip(keys, vals))`` creates a dictionary from a pair of sequences.

Back in your terminal, your tests should now pass:
    
.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 3 items

    test_journal.py ...

    =========================== 3 passed in 0.15 seconds ===========================


You've now moved quite some distance in implementing your learning journal in
Flask.


* You've created code to initialize your database schema
* You've added functions to manage the lifecycle of your database connection
* You've put in place functions to write and read journal entries
* And, since it's tested, you are reasonably sure your code does what you think
  it does.

The next step will be to add a visible face to the journal.

Viewing Your Journal
====================

The last step in the second part of this tutorial is to put a view on the front
page of this journal so we can see it online.

You'll use `the Jinja2 templating language`_ and create a basic Flask view
function.

.. _the Jinja2 templating language: http://jinja.pocoo.org/docs/templates/

Templates In Flask
------------------

First, a detour into templates as they work in Flask.

Jinja2 templates use the concept of an *Environment* to:

* Figure out where to look for templates
* Set configuration for the templating system
* Add some commonly used functionality to the template *context*

Flask sets up a proper Jinja2 Environment when you instantiate your ``app``. It
uses the value you pass to the ``app`` constructor to calculate the root of
your application on the filesystem.

From that root, it expects to find templates in a directory name ``templates``.
This allows you to use the ``render_template`` command from ``flask`` like so:

.. code-block:: python

    from flask import render_template
    page_html = render_template('hello_world.html', name="Cris")

Keyword arguments you pass to ``render_template`` become the *context* passed
to the template for rendering (like the ``name`` keyword above).

Flask will add a few name/value pairs to this context.

* **config**: the current configuration object
* **request**: the current request object
* **session**: any session data that might be available
* **g**: the request-local object to which global variables are bound
* **url_for**: a function to *reverse* urls from within your templates
* **get_flashed_messages**: a function that returns messages you *flash* to
  your users (more on this later).


Set Up Your Templates
---------------------

In your ``learning_journal`` repository, add a new ``templates`` directory:

.. code-block:: bash

    [learning_journal]
    [step2]
    heffalump:learning_journal cewing$ mkdir templates
    [learning_journal]
    [step2]
    heffalump:learning_journal cewing$

In this directory create a new file ``base.html``:

.. code-block:: jinja

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Python Learning Journal</title>
        <!--[if lt IE 9]>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
      </head>
      <body>
        <header>
          <nav>
            <ul>
              <li><a href="/">Home</a></li>
            </ul>
          </nav>
        </header>
        <main>
          <h1>My Python Journal</h1>
          <section id="content">
          {% block body %}{% endblock %}
          </section>
        </main>
        <footer>
          <p>Created in the Code Fellows Python Dev Accelerator</p>
        </footer>
      </body>
    </html>

Template Inheritance
--------------------

You can combine templates in a number of different ways.

* you can make replaceable blocks in templates with blocks

  * ``{% block foo %}{% endblock %}``

* you can build on a template in a second template by extending

  * ``{% extends "layout.html" %}`` 
  * this *must* be the first text in the template

* you can re-use common structure with *include*:

  * ``{% include "footer.html" %}``


Displaying an Entries List
--------------------------

Keep it simple for now, create a new file, ``list_entries.html`` in
``templates``.  This will *extend* your ``base.html`` file, filling the *body*
block you created:

.. code-block:: jinja

    {% extends "base.html" %}
    {% block body %}
      <h2>Entries</h2>
      {% for entry in entries %}
      <article class="entry" id="entry={{entry.id}}">
        <h3>{{ entry.title }}</h3>
        <p class="dateline">{{ entry.created.strftime(%b. %d, %Y) }}
        <div class="entry_body">
          {{ entry.text|safe }}
        </div>
      </article>
      {% else %}
      <div class="entry">
        <p><em>No entries here so far</em></p>
      </div>
      {% endfor %}
    {% endblock %}

The template will loop over a set of ``entries``, showing each in an HTML5
``<article/>`` tag.

At this point, your project directory should look like this::

    /learning_journal
    └── learning_journal
        ├── .gitignore
        ├── LICENSE
        ├── Procfile
        ├── README.md
        ├── journal.py
        ├── requirements.txt
        ├── templates
        │   ├── base.html
        │   └── list_entries.html
        └── test_journal.py


To get entries to your template, you'll need to create a Python function that
will:

* build a list of entries
* pass the list to our template to be rendered
* return the result to a client's browser

In most web frameworks, a function that returns a response to the client is
called a **view**. So this new function will be the first element in the view
layer of our web app.


Test Viewing Entries
--------------------

As usual, you'll start by writing tests. First, you'll test to see that having
no entries results in the expected HTML. Add the following to
``test_journal.py``:

.. code-block:: python

    def test_empty_listing(db):
        actual = app.test_client().get('/').data
        expected = 'No entries here so far'
        assert expected in actual

**NOTES**

* ``app.test_client()`` returns a mock HTTP client, like a web browser for us
  to use.
* Because this test actually creates a request, we don't need to use the
  ``req_context`` fixture. Having an initialized database is enough
* The ``data`` attribute of the *response* returned by ``client.get()`` holds
  the full rendered HTML of our page, but we are only checking for the one
  thing we want to see.


Next, you'll test what happens when you have some entries. But to do so, you'll
need to create entries.

Remember, you want each test to be fully isolated from the rest, and so far
you've done fine by simply rolling back your database transaction between
tests. This test requires that data be written, because the test client will
get a connection of its own, separate from the one you use for writing.

The simplest solution is to write the entry and commit it, then delete it when
the test is over.

Let's make a ``function`` scoped fixture that will do that. Add this below the
other fixtures in your ``test_journal.py`` file:

.. code-block:: python

    @pytest.fixture(scope='function')
    def with_entry(db, request):
        from journal import write_entry
        expected = (u'Test Title', u'Test Text')
        with app.test_request_context('/'):
            write_entry(*expected)
            # manually commit transaction here to avoid rollback due to
            # handled exceptions
            get_database_connection().commit()

        def cleanup():
            with app.test_request_context('/'):
                con = get_database_connection()
                cur = con.cursor()
                cur.execute("DELETE FROM entries")
                # and here as well
                con.commit()
        request.addfinalizer(cleanup)

        return expected

**NOTES**

* You use a ``test_request_context`` in both setup and teardown to ensure that
  ``g`` exists.
* You allow the ``with`` blocks to close, committing the transactions for each
  test context.

Now, use this new fixture in a test of retrieving a listing of entries:

.. code-block:: python

    def test_listing(with_entry):
        expected = with_entry
        actual = app.test_client().get('/').data
        for value in expected:
            assert value in actual

If you run your tests with these two new ones added, you should see both fail:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 5 items

    test_journal.py ...FF

    =================================== FAILURES ===================================
    ______________________________ test_empty_listing ______________________________

    db = None

        def test_empty_listing(db):
            actual = app.test_client().get('/').data
            expected = 'No entries here so far'
    >       assert expected in actual
    E       assert 'No entries here so far' in 'Hello world!'

    test_journal.py:102: AssertionError
    _________________________________ test_listing _________________________________

    with_entry = ('Test Title', 'Test Text')

        def test_listing(with_entry):
            expected = with_entry
            actual = app.test_client().get('/').data
            for value in expected:
    >           assert value in actual
    E           assert 'Test Title' in 'Hello world!'

    test_journal.py:109: AssertionError
    ====================== 2 failed, 3 passed in 0.21 seconds ======================
    [learning_journal]
    [step2 *]
    192:learning_journal cewing$


Writing the List View
---------------------

Interesting. Your tests fail, but not because you haven't implemented a view
yet. Instead they fail because there *is* a view that is returning the wrong
thing.

You wrote this view in the previous tutorial step. Remember this:

.. code-block:: python

    @app.route('/')
    def hello():
        return u'Hello world!'

That's a *view*.  It's a simple function that returns something to the client.
You used the ``@app.route()`` decorator to say "show this view when the user
requests the url '/'".

You need to replace that stub view with a real one that fits your specs above.
Add this to ``journal.py``:

.. code-block:: python

    # at the top, import
    from flask import render_template

    # and replacing the 'hello' function from the previous step
    @app.route('/')
    def show_entries():
        entries = get_all_entries()
        return render_template('list_entries.html', entries=entries)

And now, all your tests should pass:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 5 items

    test_journal.py .....

    =========================== 5 passed in 0.22 seconds ===========================


