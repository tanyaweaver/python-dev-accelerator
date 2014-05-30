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

Consider the following functions:

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
global." But the Flask ``app`` is only really instantiated once. This means
that anything you attach to it will be shared **across all requests**.

This is called ``global`` context.

What happens if two clients make a request at the same time? Do they share a
connection? Who's data gets written first? Yikes!

Flask solves this problem by providing a construct it calls a ``local global``.
Each of these objects can be imported, as if it were part of the **global
context**. But in reality they are connected directly to each request, and so
they are really **local**.

There are a number of these objects built into Flask: ``flask.request``,
``flask.session``, and--most useful for us in this situation-- `flask.g`_.

.. _flask.g: http://flask.pocoo.org/docs/api/#flask.g, 

This is an object that *looks* global (you can import it anywhere). But in
reality, it is *local* to a single request. Resources tied to this object are
*not* shared among requests. Perfect for things like a database connection.


Getting and Releasing A Connection
----------------------------------

Knowing that we have such a place to put our database connection, we can now
write the functions we'll use to connect to our database. In ``journal.py`` add
the following code:

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

Creating Tests
--------------

In Test-Driven Development, you start by writing tests that demonstrate the
functionality you want to build. Once a test is written, you run it and see
that it fails. This proves that your application hasn't sneakily already
provided that functionality and robbed you of a job. Then you implement the
code needed to make the test pass.

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


Setting Up Tests
----------------

The ``pytest`` module provides a new command, ``py.test``.  When you execute
that command in your terminal, the package uses a configurable heuristic to
locate tests to run.

By default, it starts in whatever directory you happen to be in and searches
for files that begin with ``test_``. Once such files have been found, it
imports them and looks for functions in the namespace of the module that start
with the name ``test_``. It runs each of these functions as a test.

The ``pytest`` module also allows you to create `fixtures`_ that can help you
to set up required resources for your tests (a process called dependency
injection). We'll be using these to control the setup of our Flask app and our
database for testing.

.. _fixtures: http://pytest.org/latest/fixture.html

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

Again, you won't want to use my name for your database connection. Please use
the name of whatever user you have for connecting to your database.

Also, notice that you've specified a different ``dbname`` from the one in your
``journal.py`` file. You don't want to wreck your local development database by
testing, so you'll want a different one to test on.

Take a moment to create that new database:

.. code-block:: bash

    [learning_journal]
    [step2]
    192:learning_journal cewing$ createdb test_learning_journal

Finally, notice that you've created a ``clear_db`` function that is pretty much
the reverse of the ``init_db`` function you wrote previously. It will be used
for removing your test database table when the tests are finished. This helps
to ensure complete isolation between test runs.

Now we're ready to begin writing our ``fixtures``. Each one will be a function.
Fixtures are designed to be modular, so we want to do as little as possible in
each.

Set Up the App for Testing
--------------------------

Our first fixture will be responsible for fixing the configuration of our
application for testing.  Add this code to ``test_journal.py``:

.. code-block:: python

    @pytest.fixture(scope='session')
    def test_app():
        """configure our app for use in testing"""
        app.config['DATABASE'] = TEST_DSN
        app.config['TESTING'] = True

A few notes. 

The ``pytext.fixture`` decorator registers the ``test_app`` function as a
fixture with pytest.  This allows you to use the function name in a few special
ways.  You'll see that in a moment.

The ``scope='session'`` argument passed to the decorator determines how often
this particular fixture is re-run.  There are a few available scopes:

* fixtures scoped to ``session`` will be run only once each time ``py.test`` is
  run.
* fixtures scoped to ``module`` will be run once for each module of tests that
  run.
* fixtures scoped to ``function`` will be run once for each test function that
  is executed.

Your first fixture is pretty simple, all it does is alter the configuration of
our application to use the ``TEST_DSN`` and to let Flask know that you are in
fact running tests.  These types of actions need not happen more than once, so
you can scope this fixture to ``session``.

This first fixture also requires no teardown at the end of the testing session.
Since configuration happens each time the ``journal.py`` module is loaded, the
configuration will return to normal when you next run your app.


Set Up the Database for Testing
-------------------------------

The next fixture you'll write is a bit different.  Add the following to
``test_journal.py``:

.. code-block:: python

    @pytest.fixture(scope='session')
    def db(test_app, request):
        """initialize the entries table and drop it when finished"""
        init_db()

        def cleanup():
            clear_db()

        request.addfinalizer(cleanup)

Notice that this time, our fixture function is defined with parameters. One of
these is the fixture we defined previously. This is one of the special things
that happen when you use the decorator to register a fixture.  It becomes
available to be used as a parameter for other fixtures or for test functions.

By using your first fixture as a parameter for the second, you are telling
``pytest`` that you want the first fixture to run prior to every time this
fixture is run. Providing ``test_app`` here ensures that the configuration
changes you made in that fixture are in place when the database is initialized.

You may wonder about the ``request`` parameter. That is a special fixture that
``pytest`` registers for a few special purposes.

You are using the ``request`` fixture here to connect the ``cleanup`` function
to the ``db`` fixture as the function to be run when the ``session`` scope is
complete. It contains your cleaup code removing the database table.


Set Up a Request for Testing
----------------------------

The last fixture you will need helps to prepare each test to run in isolation
from other tests. Add the following code to ``test_journal.py``:

.. code-block:: python

    @pytest.yield_fixture(scope='function')
    def req_context(db):
        """run tests within a test request context so that 'g' is present"""
        with app.test_request_context('/'):
            yield
            con = get_database_connection()
            con.rollback()

Remember that in a data-driven web application, you want to bind the lifecycle
of the connection you make with your database to the lifecycle of the HTTP
request/response cycle. To accomplish this goal, you wrote a pair of functions
earlier: ``get_database_connection`` and ``teardown_request``.

The purpose of the ``get_database_connection`` was to attach a connection to
the ``flask.g`` object so that it would be available during the request. The
purpose of ``teardown_request`` was to finish the transaction bound to that
connection and close the connection.

When you are running your application, the ``flask.g`` object is created as
soon as a request/response cycle begins. But it testing **there is no
request**.

Flask provides you with the ``app.test_request_context`` method to solve this
problem. The method is a *context provider*, so it can be used in a ``with``
statement.  When execution enters the block defined by ``with``, a request will
be generated and the ``flask.g`` object will come into being. And when
execution leaves that block, the end of the request/response cycle will be
signaled, and your ``teardown_request`` method will be called.

This is great, but if you had to use the method for writing cleanup code you
used in the ``db`` fixture to write this fixture, you'd be out of luck. There's
no way to maintain containment in the ``with`` block under that scenario.

Happily, ``pytest`` `solves this problem`_ by allowing you to use a ``generator
function`` as a fixture. The ``yield`` above passes execution back to the
context where this fixture was called, but because it's a ``yield``, *the
internal state of the fixture is maintained*!  This means that you can use this
form with the context manager Flask gives you and have the tests that use this
fixture take place while contained in the ``with`` block.

.. _solves this problem: http://pytest.org/latest/yieldfixture.html

Nice!

When control returns to the fixture, the cleanup code after ``yield`` will be
called. Here, you can grab the local database connection and rollback the
transaction, wiping out the work done in a test so the next one can happen in a
fresh table.


Test Writing An Entry
---------------------

Now you're ready to write your first test. This test will ensure that writing
an entry works properly when the right parameters are passed. In
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

Remember that ``pytest`` will only run function that start with ``test_`` as
tests.  This allows you to create *helper functions* like
``run_independent_query`` that you can use in more than one test. Here you are
using it to select the entry you just wrote back from the database to ensure it
was correct.

The Test Driven Development philosophy states that you should write a test
first. You have. It also states that you should run that test and see it fail.
Do that now.  In your terminal, run the ``py.test`` command:

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

Fantastic!  Your test failed, just as you expected. Next you need to make it
pass.


Implement ``write_entry``
-------------------------

Return to ``journal.py`` and add the following:

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

You've now written an SQL statement that will insert a new entry into your
``entries`` table. Notice the ``%s`` placeholders in the SQL string. **Do not
be fooled** into thinking that these are for standard Python string formatting.

In fact, these are special placeholders that ``psycopg2`` uses to insert Python
values into an SQL string with proper escaping. If you use the ``%`` string
formatting operator to insert Python values into this string, you will be
opening yourself to SQL injection attacks.

**NEVER USE PYTHON STRING FORMATTING WITH A SQL STRING**.

Instead, pass a sequence of paramters as the second argument to
``cursor.execute`` and ``psycopg2`` will take care of the rest. You'll be safe
and sound and no kittens will die.

Also notice that you are not requiring the caller of ``write_entry`` to pass a
datetime value for your ``created`` field. You are creating that on your own.
Moreover, you are creating a time value in UTC or `Coordinated Universal
Time`_. It is a good idea to store time values in a database in this fashion,
as it implies no Time Zone and can easily be localized to any time zone.

.. _Coordinated Universal Time: http://en.wikipedia.org/wiki/Coordinated_Universal_Time

Now that you have the ``write_entry`` method implemented, you should be able to
run your tests successfully.  Try it:

.. code-block:: bash

    [learning_journal]
    [step2 *]
    192:learning_journal cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 1 items

    test_journal.py .

    =========================== 1 passed in 0.17 seconds ===========================

Outstanding!


Test Reading Entries
--------------------

You might also like to be able to read the entries in your journal. You'll need
a method that returns all of them for a simple listing page.

* The return value should be a list of entries
* If there are none, it should return an empty list
* Each entry in the list should be a dictionary of 'title', 'text' and
  'created'
* The list should be ordered by the datetime each entry was created such that
  the most recently created entries are listed first.

Again, begin by writing tests.

Back in ``test_journal.py`` add the following two tests:

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

Try running your tests now to ensure that these two new tests fail as expected:

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

You are ready to implement ``get_all_entries``. Back in ``journal.py`` add the
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

And back in your terminal, your tests should now pass:
    
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
