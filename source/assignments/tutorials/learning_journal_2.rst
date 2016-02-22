:orphan:

*******************************
Python Learning Journal: Step 2
*******************************

In part one of this tutorial, you built the *data model* for a simple learning
journal web application using Pyramid, PostgreSQL, and SQLAlchemy. You deployed
this work to Heroku and confirmed that you could initialize a database and see
a simple page.

In this second part, you'll build the *control layer* and the *view layer* for
this application. Along the way, you'll learn about Test-Driven Development and
unit testing in Python using the ``pytest`` package.

Ready?  Let's begin!

Preparing to Work
=================

In part 1, you created a *virtualenv project* to work in.  The first step for
starting a new work day on the app will be to return to that environment:

.. code-block:: bash

    cewing$ workon learning-journal
    [learning-journal]
    192:learning-journal cewing$

Next, you'll want to make a new branch for the work in this part of the
tutorial:

.. code-block:: bash

    [learning-journal]
    [master=]
    192:learning-journal cewing$ git checkout -b step2
    Switched to a new branch 'step2'
    [learning-journal]
    [step2]
    192:learning-journal cewing$

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

Pyramid does not dictate that you write an application that uses a database.
Because of this, managing the lifecycle of database connection so that they are
connected to the request/response cycle is up to you.

You could do this work manually, but happily there are add-ons available that
will take care of it on your behalf. You two of these in the first part of this
tutorial, ``pyramid-tm``, or the Pyramid Transaction Manager, and
zope.sqlalchemy.

The purpose of pyramid-tm is to create a new *transaction* at the beginning of
each request, and to determine what to do with that transaction at the end,
before a response is returned to the client. By default, if there was any error
raised by code run during the request-response cycle, then the transaction is
rolled back. Otherwise, the transaction is committed.

The purpose of zope.sqlalchemy is to join the sqlalchemy database session to
this transaction manager.  This means that any code that reads from or writes
to the database will exist within a transaction that will be automatically
committed or rolled back.  You don't need to worry about calling ``commit`` at
any time.

Adding Transaction Management
-----------------------------

To use this transaction management there are a couple of updates you must make
to your code.

First, you need to create a database session that uses the
``ZopeTransactionExtension`` from the ``zope.sqlalchemy`` package. Remember how
you created a session at the command line during class previously:

.. code-block:: pycon

    >>> from sqlalchemy.orm import sessionmaker # <- import a factory maker
    >>> Session = sessionmaker(bind=engine)     # <- create a factory for sessions
    >>> session = Session()                     # <- start a session

In your journal app, you'll do something quite similar, but you'll use a
special kind of session called a *scoped_session* which helps to maintain the
association of one session with one request, even when there are many many
requests happening all at once.

In ``journal.py`` add the following code:

.. code-block:: python

    # add these imports at the top of the file
    from sqlalchemy.orm import scoped_session, sessionmaker
    from zope.sqlalchemy import ZopeTransactionExtension

    # add this right below the imports
    DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

You've now bound a symbol at the module scope, one which is available to *all*
the code in your project, which is responsible for creating sessions for each
request.  This symbol will be your point of access to the database throughout
your appliation code.

Notice though that the session is not yet created. You've only created a
*factory* for making sessions. Nor does that factory know anything about which
database to connect to. Supplying that information is part of the job of
application configuration.

Remember in part one of this tutorial that you wrote a fully functional web
application. Part of that application code was a *factory function* responsible
for building and returning a configured app object to be served to clients.
That function is where the configuration of your application must happen, so
that function is where you will turn next.

Find the ``main`` function in ``journal.py``.  at the moment it should look
like this:

.. code-block:: python

    def main():
        """Create a configured wsgi app"""
        settings = {}
        debug = os.environ.get('DEBUG', True)
        settings['reload_all'] = debug
        settings['debug_all'] = debug
        # configuration setup
        config = Configurator(
            settings=settings
        )
        config.add_route('home', '/')
        config.scan()
        app = config.make_wsgi_app()
        return app

Just below where you set ``debug_all`` in the setting dictionary, add the
following code to create the database engine and the set up the session
factory:

.. code-block:: python

    def main():
        # ...
        settings['debug_all'] = debug          # <- already present, do not add
        if not os.environ.get('TESTING', False):
            # only bind the session if we are not testing
            engine = sa.create_engine(DATABASE_URL)
            DBSession.configure(bind=engine)
        # configuration setup

Finally, we'll need to tell our application that we want to use the transaction
management provided by ``pyramid-tm``. Pyramid allows add-ons to declare their
own configuration and allows you to simply include that configuration when you
want to use it. You do this using the ``.include()`` method of your
``Configurator`` instance. Again, in ``journal.py`` add the following line,
just below where you bind ``config`` for the first time, and above where you
add your first ``route``:

.. code-block:: python

    def main():
        # ...
        config = Configurator(
            # ...
        )
        config.include('pyramid_tm')

And that is all.  You've now created a session factory that will automatically
be thread-safe and local to a single request, and you've bound the lifecycle of
that session to a transaction that is started when a request arrives at your
application and closed when the response goes back to the client.

Now you want to prove that it works.

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
``learning-journal`` virtualenv active, use ``pip`` to install ``pytest``:

.. _pytest: http://pytest.org/latest/contents.html

.. code-block:: bash

    [learning-journal]
    [step2]
    192:learning-journal cewing$ pip install pytest
    Downloading/unpacking pytest
      Downloading pytest-2.5.2.tar.gz (608kB): 608kB downloaded
      Running setup.py (path:/Users/cewing/virtualenvs/learning-journal/build/pytest/setup.py) egg_info for package pytest

      ...

    Successfully installed pytest py
    Cleaning up...
    [learning-journal]
    [step2]
    192:learning-journal cewing$

Then, you'll need to create a new file to hold your tests. Call it
``test_journal.py``:

.. code-block:: bash

    [learning-journal]
    [step2]
    192:learning-journal cewing$ touch test_journal.py
    [learning-journal]
    [step2]
    192:learning-journal cewing$

At this point, your project directory structure should look like this::

    .
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

To begin, add the following code to your ``test_journal.py`` file:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals
    import os
    import pytest
    from sqlalchemy import create_engine
    from sqlalchemy.exc import IntegrityError

    TEST_DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        'postgresql://cewing:@localhost:5432/test-learning-journal'
    )
    os.environ['DATABASE_URL'] = TEST_DATABASE_URL
    os.environ['TESTING'] = "True"

    import journal

The order of things here looks odd, but it is very important. Make sure to
import your ``journal`` module last

**Notes**

* Remember to use **the correct name for your database user**, mine is just an
  example.
* Notice that you'll be using a different ``dbname`` for testing. This prevents
  overwriting data you might want to save.

Take a moment to create that new database:

.. code-block:: bash

    [learning-journal]
    [step2]
    192:learning-journal cewing$ createdb test-learning-journal


Creating Fixtures
-----------------

The ``pytest`` module does more than just test discovery. It supports a concept
called `fixtures`_.

Fixtures help you to manage resources needed for your tests. They are run
before and after your tests. You can use them to create and destroy resources
needed for testing. Fixtures help ensure that you have control over the
environment where your tests run.

You'll add a few fixtures to help test your Pyramid app.

.. _fixtures: http://pytest.org/latest/fixture.html

The first fixture is responsible for creating a connection to the database.  It
will be run once per testing session so that all tests use the same connection.

Add the following to ``test_journal.py``

.. code-block:: python

    @pytest.fixture(scope='session')
    def connection(request):
        engine = create_engine(TEST_DATABASE_URL)
        journal.Base.metadata.create_all(engine)
        connection = engine.connect()
        journal.DBSession.registry.clear()
        journal.DBSession.configure(bind=connection)
        journal.Base.metadata.bind = engine
        request.addfinalizer(journal.Base.metadata.drop_all)
        return connection

**NOTES**:

* The ``pytest.fixture`` decorator registers the ``connection`` function as a
  fixture with pytest.
* The ``scope`` argument passed to the decorator determines how often a fixture
  is run.

  * ``session`` scope is run only once each time ``py.test`` is invoked.
  * ``module`` scope is run once for each module of tests (once per Python
    file).
  * ``function`` scope is run once for each test function (this is the default).

* We'll want to have the same connection across all tests, so scope this
  fixture to ``session``.
* A fixture function may be defined with parameters.
* The names of the parameters must match *registered fixtures*.
* The fixtures named as parameters will be run surrounding the new fixture,
  like the layers of an onion
* The ``request`` parameter is a special fixture that ``pytest`` registers.
* You use it to add a method that will be run after this fixture goes out of
  scope using ``.addfinalizer()``
* By returning ``connection`` from this fixture, tests or fixtures that depend on
  it will be able to access the same connection created here.


The next fixture we create will be responsible for providing us with a database
session we can use in our tests. Add the following to ``test_journal.py``:

.. code-block:: python

    @pytest.fixture()
    def db_session(request, connection):
        from transaction import abort
        trans = connection.begin()
        request.addfinalizer(trans.rollback)
        request.addfinalizer(abort)

        from journal import DBSession
        return DBSession

**Notes**:

* Notice that this fixture requires not only the ``request`` fixture provided
  by pytest, but also the ``connection`` fixture you just wrote.
* You start a new transaction here in this fixture, mocking the actions usually
  handled by ``pyramid-tm``.
* You also add finalizers to rollback and then abort that transaction, which
  ensure that no work in the database will persist between tests
* This means that this fixture must be used for *each* test.  That is the
  default scope so we do not designate a scope for this fixture.

Writing and Reading Entries
===========================

Your journal's **data model** consists of *entries*. You've set up a simple
database schema to represent them using a SQLAlchemy ``model`` class.

To write an entry, what would you need to do?

* Provide a title
* Provide some body text
* Write them to a row in the database

This type of work is considered a **controller** because it connects client
input in the form of the title and text to the data model. The work should be
encapsulated in a function.  Moreover, to keep our application clean, it might
be a good idea to make this function a method of the ``Entry`` class you wrote
yesterday.  That way, the ``Entry`` class is responsible for writing new
entries. You probably don't want to have to have an existing entry in order to
write a new one, so this would be a good job for a *class method*.

Test Writing An Entry
---------------------

While you think a bit about how you might do that job, start by writing a test
that demonstrates the desired functionality. Often this can help you to think
more clearly about what such a method should do. In ``test_journal.py``, add
the following:

.. code-block:: python

    def test_write_entry(db_session):
        kwargs = {'title': "Test Title", 'text': "Test entry text"}
        kwargs['session'] = db_session
        # first, assert that there are no entries in the database:
        assert db_session.query(journal.Entry).count() == 0
        # now, create an entry using the 'write' class method
        entry = journal.Entry.write(**kwargs)

**NOTES**

* ``pytest`` will only run functions that start with ``test_`` as tests.
* You are passing *title*, *text*, **and** *session* to the ``write`` method.
  That way you can be sure that the method uses the session you carefully
  crafted in your fixture.

Stop there for a moment.  What is going to happen when you run this test?

Try it out and see:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py F

    =================================== FAILURES ===================================
    _______________________________ test_write_entry _______________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 46, in test_write_entry
        entry = journal.Entry.write(**kwargs)
    AttributeError: type object 'Entry' has no attribute 'write'
    =========================== 1 failed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

Yep.  As you probably expected, the test failed because there is no
``.write()`` method on the Entry class.

Fix that problem by adding such a method, in the simplest possible form. You
don't have to return anything from it for now, in fact, just make the method
body ``pass``. Think about the test you just wrote, what does this method
expect as arguments? See if you can add a ``.write()`` method to your ``Entry``
class in ``journal.py``. Once you've finished, open my example below and
compare them.

.. hidden-code-block:: python
    :label: Peek At A Solution

    class Entry(Base):
        # ... <- column attributes are defined here

        @classmethod
        def write(cls, title=None, text=None, session=None):
            pass

Now, you should be able to run your previously written test, without causing an
error:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py .

    =========================== 1 passed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

Wonderful!  But does it actually test anything? Only that such a method exists.
Your tests should be a bit more sophisticated than this. Let's add some
assertions about the outcome of calling ``Entry.write()``.  Add the following
to ``test_journal.py``

.. code-block:: python

    def test_write_entry(db_session): # <- extend this test

        # ... <- keep all the existing test content, just add the stuff below

        # the entry we get back ought to be an instance of Entry
        assert isinstance(entry, journal.Entry)
        # id and created are generated automatically, but only on writing to
        # the database
        auto_fields = ['id', 'created']
        for field in auto_fields:
            assert getattr(entry, field, None) is None


Now you're making some assertions about what this method ought to do.  You are
saying that the method should return an ``Entry`` instance.  And that it should
have no 'id' or 'created' attributes at first.

Try running your tests again, and see what you get:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py F

    =================================== FAILURES ===================================
    _______________________________ test_write_entry _______________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 48, in test_write_entry
        assert isinstance(entry, journal.Entry)
    AssertionError: assert isinstance(None, <class 'journal.Entry'>)
     +  where <class 'journal.Entry'> = journal.Entry
    =========================== 1 failed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

As expected, the test is failing again, because a new entry is *not* returned.
Let's move to fix that by altering how our method works. Back in ``journal.py``
change your method so that it creates and returns a new ``Entry`` object.

See if you can do this on your own.  Then check against my solution below:

.. hidden-code-block:: python
    :label: Peek At A Solution

    @classmethod
    def write(cls, title=None, text=None, session=None):
        instance = cls(title=title, text=text)
        return instance

Okay, now run the tests again to see what happens.

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py .

    =========================== 1 passed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

Terrific!  The test is passing again.  That's wonderful.  But wait, we want our
method to write this new entry into the database so it will be persisted,
right? Are we testing for that yet? Let's add a bit more and see what happens:

.. code-block:: python

    # in test_journal.py

    def test_write_entry(db_session): # <- extend this test

        # ... <- keep all the existing test content, just add the stuff below

        # flush the session to "write" the data to the database
        db_session.flush()
        # now, we should have one entry:
        assert db_session.query(journal.Entry).count() == 1
        for field in fields:
            if field != 'session':
                assert getattr(entry, field, '') == kwargs[field]
        # id and created should be set automatically upon writing to db:
        for auto in ['id', 'created']:
            assert getattr(entry, auto, None) is not None    

In your terminal, run the ``py.test`` command to see the expected failure:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py F

    =================================== FAILURES ===================================
    _______________________________ test_write_entry _______________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 57, in test_write_entry
        assert db_session.query(journal.Entry).count() == 1
    AssertionError: assert 0L == 1
     +  where 0L = <bound method Query.count of <sqlalchemy.orm.query.Query object at 0x10eae9dd0>>()
     +    where <bound method Query.count of <sqlalchemy.orm.query.Query object at 0x10eae9dd0>> = <sqlalchemy.orm.query.Query object at 0x10eae9dd0>.count
     +      where <sqlalchemy.orm.query.Query object at 0x10eae9dd0> = <bound method scoped_session.do of <sqlalchemy.orm.scoping.scoped_session object at 0x10e75c750>>(<class 'journal.Entry'>)
     +        where <bound method scoped_session.do of <sqlalchemy.orm.scoping.scoped_session object at 0x10e75c750>> = <sqlalchemy.orm.scoping.scoped_session object at 0x10e75c750>.query
     +        and   <class 'journal.Entry'> = journal.Entry
    =========================== 1 failed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

Alright.  Failing again.  This time because although you flushed your db
session, you got no entries back when you queried the database. It's time to
wrap this up and write this entry to the database. Do you remember how we did
that during class? Try adding that to your ``.write()`` method. When you're
done, check my solution below:

.. hidden-code-block:: python
    :label: Peek At A Solution

    @classmethod
    def write(cls, title=None, text=None, session=None):
        if session is None:
            session = DBSession
        instance = cls(title=title, text=text)
        session.add(instance)
        return instance

Now the purpose of passing the session becomes clear. If we don't bother
passing one, then the ``DBSession`` defined in our ``journal.py`` file is used.
If we do pass one, then it is preferred. This allows the method to work both
here in tests, and in production where we don't need (or want) to create a
special session.

Now, finally, run your test one last time and see it pass:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 1 items

    test_journal.py .

    =========================== 1 passed in 0.27 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

You have a test that exercises this method and ensures that it does what is
supposed to do. And you have a method that makes the test pass. The
back-and-forth you've done is sometimes called **Red-Green-Refactor** in honor
of the colors of output in your terminal when you run the tests. It's a great
way to iteratively develop functionality and at the same time ensure it is
tested properly.

What other tests might you implement here? Are there restrictions on the values
that ought to be placed in the database you wish to verify? How might you test
those restrictions?

Try your hand at writing a few tests of your own. Then you can peek at mine, if
you like:

.. hidden-code-block:: python
    :label: Peek At A Solution

    def test_entry_no_title_fails(db_session):
        bad_data = {'text': 'test text'}
        journal.Entry.write(session=db_session, **bad_data)
        with pytest.raises(IntegrityError):
            db_session.flush()

    def test_entry_no_text_fails(db_session):
        bad_data = {'title': 'test title'}
        journal.Entry.write(session=db_session, **bad_data)
        with pytest.raises(IntegrityError):
            db_session.flush()

Remember, when you are finished with this step, commit your changes to git so
you can preserve them.  Write a quality commit message explaining what you've
done and why.


Test Reading Entries
--------------------

To read your journal, you'll need a method that returns entries. For now, the
controller function can return all of them for a simple listing page. Your
specs:

* The return value should be a list of entries.
* If there are no entries, the function should return an empty list.
* The list should be ordered with the most recently created entries first.

Again, begin with tests. Back in ``test_journal.py`` add the following code:

.. code-block:: python

    def test_read_entries_empty(db_session):
        entries = journal.Entry.all()
        assert len(entries) == 0


    def test_read_entries_one(db_session):
        title_template = "Title {}"
        text_template = "Entry Text {}"
        # write three entries, with order clear in the title and text
        for x in range(3):
            journal.Entry.write(
                title=title_template.format(x),
                text=text_template.format(x),
                session=db_session)
            db_session.flush()
        entries = journal.Entry.all()
        assert len(entries) == 3
        assert entries[0].title > entries[1].title > entries[2].title
        for entry in entries:
            assert isinstance(entry, journal.Entry)

What would you expect to be the result of running these tests now? Run your
tests to ensure that the two new tests fail in the way you expect. If you get a
different result that you expected, ask yourself why:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 5 items

    test_journal.py ...FF

    =================================== FAILURES ===================================
    ___________________________ test_read_entries_empty ____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 80, in test_read_entries_empty
        entries = journal.Entry.all()
    AttributeError: type object 'Entry' has no attribute 'all'
    ____________________________ test_read_entries_one _____________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 94, in test_read_entries_one
        entries = journal.Entry.all()
    AttributeError: type object 'Entry' has no attribute 'all'
    ====================== 2 failed, 3 passed in 0.27 seconds ======================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$


Implement ``Entry.all()``
-------------------------

Now you are ready to implement the **controller** method that will make these
tests pass.  Look carefully at the tests you've written.  What do they tell you
about the method you need to write?

* It can take a database session as an optional argument
* It is a class method (no instance created or used, right?)
* It returns a list of things
* Those things should be ``Entry`` instances

Back in ``journal.py`` go ahead and work on implementing this function yourself.

.. hidden-code-block:: python
    :label: Peek At A Solution

    class Entry(Base):
        # ...

        @classmethod
        def all(cls, session=None):
            if session is None:
                session = DBSession
            return session.query(cls).order_by(cls.created.desc()).all()

**NOTES**

* Again, we can optionally pass a session in order to allow for easier testing.
* The simple query is now using an ``order_by`` clause to control the order in
  which items are returned.
* The argument to an ``order_by`` clause must be a ``Column`` instance
* ``Column`` instances have attributes that allow you to determine whether the
  sort order is ascending or descending.
  

Back in your terminal, your tests should now pass:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 5 items

    test_journal.py .....

    =========================== 5 passed in 0.31 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$

Where We Stand
--------------

You've now moved quite some distance in implementing your learning journal in
Pyramid.

* You've created a data model representing your entry
* You've written code to initialize your database schema
* You've put in place functions to write and read journal entries
* And, since it's tested, you are reasonably sure your code does what you think
  it does.

The next step will be to add a visible face to the journal.

Viewing Your Journal
====================

The last step in the second part of this tutorial is to put a view on the front
page of this journal so we can see it online.

You'll use `the Jinja2 templating language`_ and connect your *controllers* to
the *views* that will display the data they expose.

.. _the Jinja2 templating language: http://jinja.pocoo.org/docs/templates/


Renderers in Pyramid
--------------------

First, a detour into templates as they work in Pyramid.

Within the world of Pyramid, the data assembled by the **controller**\ s we
created above are passed off to a *renderer*.  A *renderer* is responsible for
taking that information, turning it into something that a client can use and
sending that off to be returned to the client. The data might be turned into an
HTML page, or a JSON response, or an XML document. For this reason, we consider
the *renderer* in Pyramid to fill the roll of the **View** in the **MVC**
pattern.

Installing a Renderer Add-On
----------------------------

Pyramid comes with a few simple renderers built-in: ``'string'``, ``'json'``,
and ``'jsonp'``.  You can add new renderers by installing additional packages
and configuring them. We want to use *Jinja2 Templates* as renderers, and so we
are going to install `pyramid_jinja2`_, which wraps the Jinja2 template
language in structures that Pyramid can use as renderers.

.. _pyramid_jinja2: http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/

Begin by installing the package into your virtual environment:

.. code-block:: bash

    [learning-journal]
    [step2 *]
    192:learning-journal cewing$ pip install pyramid_jinja2
    Downloading/unpacking pyramid-jinja2
    ...
    Successfully installed pyramid-jinja2 Jinja2 markupsafe
    Cleaning up...
    [learning-journal]
    [step2 *]
    192:learning-journal cewing$

Once this is complete, add the dependency to your requirements.txt file:

.. code-block:: bash

    [learning-journal]
    [step2 *]
    192:learning-journal cewing$ pip freeze > requirements.txt
    [learning-journal]
    [step2 *]
    192:learning-journal cewing$

That will ensure that Heroku will also be aware of these changes.

Finally, you'll need to inform your application that it should use this new
renderer.  Pyramid handles this using configuration. Like with ``pyramid-tm``,
``pyramid_jinja2`` provides configuration that can be included by an
application that depends on it. You add this using the ``include`` method of
the config object.

In ``journal.py`` make the following change:

.. code-block:: python

    def main():
        # ...
        # configuration setup
        config.include('pyramid_tm')
        config.include('pyramid_jinja2')  # <-- ADD THIS LINE HERE
        config.add_route('home', '/')

This will ensure that the configuration ``pyramid_jinja2`` requires to work
properly is in place.

Once you are done, commit your changes to ``git`` and make a good commit
message explaining what you've done and why.


Set Up Your Templates
---------------------

Jinja2 templates use the concept of an *Environment* to:

* Figure out where to look for templates
* Set configuration for the templating system
* Add some commonly used functionality to the template *context*

Pyramid has a number of ways of working with this *environment* to assist in
finding templates.  The simplest to use (and the default in Pyramid) is
`caller-relative template lookup`_.

.. _caller-relative template lookup: http://docs.pylonsproject.org/projects/pyramid-jinja2/en/latest/#caller-relative-template-lookup

In this scheme, templates are searched for in a path relative to the file in
which the calling code is found. Our entire application lives in a single file,
so we can establish a location adjacent to that file to hold our templates.

In your ``learning-journal`` repository, add a new ``templates`` directory:

.. code-block:: bash

    [learning-journal]
    [step2]
    heffalump:learning-journal cewing$ mkdir templates
    [learning-journal]
    [step2]
    heffalump:learning-journal cewing$

In this directory create a new file ``base.jinja2``:

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

This file represents the main structure of our website.  Individual pages will
be able to extend this structure through *template inheritance*

.. note::

    If you have a layout for your learning journal you'd like to use, perhaps
    the mockup you completed for pre-work, please feel free to use it here. You
    may wish to begin by using my simple layout above, to minimize confusion
    until you have the basics working.


Template Inheritance
--------------------

Jinja2 allows you to combine templates in a number of different ways.

* you can make replaceable blocks in templates with *blocks*:

  * ``{% block body %}{% endblock %}``

* you can build on a template from within a second template by *extending*:

  * ``{% extends "base.jinja2" %}``
  * this *must* be the first text in the template

* you can re-use common structure with *include*:

  * ``{% include "footer.jinja2" %}``


In our ``base.jinja2`` we added a ``block`` called body.  Now we can create a
template that will extend that.


Displaying an Entries List
--------------------------

Keep it simple for now, create a new file, ``list.jinja2`` in ``templates``.
This will *extend* your ``base.jinja2`` file, filling the *body* block in that
template:

.. code-block:: jinja

    {% extends "base.jinja2" %}
    {% block body %}
      <h2>Entries</h2>
      {% for entry in entries %}
      <article class="entry" id="entry={{entry.id}}">
        <h3>{{ entry.title }}</h3>
        <p class="dateline">{{ entry.created.strftime('%b. %d, %Y') }}
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

Notice that because of *caller-relative template lookup* we refer to the
``base.jinja2`` file without any directory reference.  Both that file and this
``list.jinja2`` file are in the same location so a relative lookup only needs
the filename.

The template will loop over a set of ``entries``, showing each in an HTML5
``<article/>`` tag.

At this point, your project directory should look like this::

    .
    ├── .gitignore
    ├── LICENSE
    ├── Procfile
    ├── README.md
    ├── journal.py
    ├── requirements.txt
    ├── templates
    │   ├── base.jinja2
    │   └── list.jinja2
    └── test_journal.py


This template we've just created will be a Pyramid *renderer*.  We've noted
that the *renderer* in Pyramid takes the *view* role in the *MVC* pattern. What
remains for us to do is to connect the *controller* functions to these new
*renderers* we are creating so that we can see the results of our hard work.

Test Viewing Entries
--------------------

Before we test viewing entries, we must first talk about different types of
tests.

The tests we've written so far are what you can call *unit tests*.  They
concentrate on small, simple functionality and *mock* or make up any
environment they require to function. *Unit tests* are designed to test
functions in isolation from a real system to ensure that they operate as
intended on their own.

The new tests we are going to write are *functional* tests.  They will require
that we engage all of Pyramid's functionality so that we can request a web page
and make assertions about the content that is returned to us.

To write functional tests we'll need to add a new dependency on a package
called `WebTest`_.  This package will set up a complete *WSGI* application and
provide us with machinery we can use to interact with it.

.. _WebTest: http://webtest.pythonpaste.org/en/latest/index.html

Begin by installing ``WebTest``:

.. code-block:: bash

    [learning-journal]
    [step2]
    heffalump:learning-journal cewing$ pip install WebTest
    ...
    Cleaning up...
    [learning-journal]
    [step2 *]
    heffalump:learning-journal cewing$

Next, we will have to create a *pytest fixture* that will set everything up for
us:

* The fixture will need to create a configured application
* The fixture will need to wrap that application in the WebTest server
* The fixture will return the wrapped application so tests can use it
* The fixture should be run for each test so that you get a fresh instance of
  the application each time

Between the WebTest documentation and code you've already written, you can try
writing this new fixture on your own.

.. hidden-code-block:: python
    :label: Peek At A Solution

    @pytest.fixture()
    def app():
        from journal import main
        from webtest import TestApp
        app = main()
        return TestApp(app)

Now that we have a fixture that will provide us with a functional app we can
interact with, we can write our first tests for the view of a list of entries.
Add the following to ``test_journal.py``:

.. code-block:: python

    def test_empty_listing(app):
        response = app.get('/')
        assert response.status_code == 200
        actual = response.body
        expected = 'No entries here so far'
        assert expected in actual

**NOTES**

* The ``app`` created by our fixture works as a mock HTTP client, like a web
  browser for us to use.
* The ``data`` attribute of the *response* returned by ``client.get()`` holds
  the full rendered HTML of our page, but we are only checking for the one
  thing we want to see.

Next, you'll test what happens when you have some entries. But to do so, you'll
need to create entries. The simplest solution is to write the entry and commit
it, then delete it when the test is over.

Try your hand at writing a ``function`` scoped fixture that will take care of
this for you. It'd be quite nice if it would return information about the entry
it writes as well, so you can use it to test against:

.. hidden-code-block:: python
    :label: Peek At A Solution

    @pytest.fixture()
    def entry(db_session):
        entry = journal.Entry.write(
            title='Test Title',
            text='Test Entry Text',
            session=db_session
        )
        db_session.flush()
        return entry

Now, use this new fixture in a test of retrieving a listing of entries.  See if
you can write this test yourself:

.. hidden-code-block:: python
    :label: Peek At A Solution

    def test_listing(app, entry):
        response = app.get('/')
        assert response.status_code == 200
        actual = response.body
        for field in ['title', 'text']:
            expected = getattr(entry, field, 'absent')
            assert expected in actual

If you run your tests with these two new tests added, you should see both fail:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 7 items

    test_journal.py .....FF

    =================================== FAILURES ===================================
    ______________________________ test_empty_listing ______________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 124, in test_empty_listing
        assert expected in actual
    AssertionError: assert 'No entries here so far' in 'Hello World'
    _________________________________ test_listing _________________________________
    Traceback (most recent call last):
      File "/Users/cewing/projects/codefellows/learning-journal/test_journal.py", line 133, in test_listing
        assert expected in actual
    AssertionError: assert 'Test Title' in 'Hello World'
    ====================== 2 failed, 5 passed in 0.37 seconds ======================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$


Writing the List View
---------------------

Interesting. Your tests fail, but not because you haven't implemented a
function yet. Instead they fail because there *is* a function found that is
returning the wrong thing: "Hello World"

This brings us to the topic of how Pyramid serves HTTP requests.

Every time a client requests a page from your Pyramid app (and this is what
happens when you call the ``get`` method of your ``app``) a process happens.

**Matching a Route**

The first step is that Pyramid looks for *routes* that have been configured and
tries to match one to the *path* of the request from the client. At this point,
you may say "But I never made any routes, I don't even know what one is".
You'd be at least partly wrong.

In the first step of our application, when you created the ``main`` function,
you included this line of configuration:

.. code-block:: python

    config.add_route('home', '/')

That code configures a single *route*.  The route has a *name* (``'home'``) and
a *pattern* (``'/'``). Pyramid tries to match the *path* of an incoming request
to that pattern.  Our tests both have this line of code:

.. code-block:: python

    response = app.get('/')

That line uses the app as a mock web browser to make a ``GET`` request for the
path ``'/'``!  This path matches the pattern for our ``'home'`` route, and so
that's the route that is selected.

**Selecting a View**

Once a *route* has been selected, the next step Pyramid takes is to select a
*view* that is configured to use that route. Again, you might think you have no
idea what a *view* is in Pyramid, but actually, you wrote one of these in the
first step of this tutorial as well:

.. code-block:: python

    @view_config(route_name='home', renderer='string')
    def home(request):
        return "Hello World"

The ``view_config`` decorator is used by Pyramid to decorate some function that
can serve as a *view function*.  The sole hard-and-fast requirement of a view
function is that it take ``request`` as an argument.

The ``view_config`` decorator can take a number of arguments. One that you must
provide is ``route_name``. This parameter serves to connect a *view function*
to a *route*.

When Pyramid matches the ``'home'`` route, it then seeks a view function that
is configured with that *route_name*. This ``home`` function is found, and it
is executed.

**Rendering a Response**

After the view is executed, the return value of the function is passed on to
any *renderer* configured by the ``view_config`` decorator.  That *renderer* is
responsible for turning the data from the *view function* into a response
suitable for sending back to a client.  In this case, the ``'string'`` renderer
takes whatever value is returned by the *view function* and sends it back to
the client as a plain text response.  This is why your test sees the body of
the response as "Hello World"!

For *template renderers*, like the one you've just created, a view is required
to return a dict instance that can serve as context for the template. This
means that any symbols used in the template must be present in the dict
returned by the view.

Notice that your list view template contains one symbol that isn't defined in
the scope of the template itself:

.. code-block:: jinja

    {% for entry in entries %}
     ...
    {% else %}
     ...
    {% endfor %}

Somehow, you'll need to provide a dictionary with the key `entries` in it to
this template *renderer*.

A view *can* be configured without a *renderer*.  If this is the case, the view
itself is responsible for returning a value suitable for returning to the
client.  We will see an example of this later.

A Word on Terminology
---------------------

Although the MVC pattern is a useful abstraction, it's not a perfect match for
the web world. There are a few differences in how things are named in Python
web frameworks, and a few ambiguities about where the edges are:

.. rst-class:: centered width-80%

+-------------------+-------------------------+
|  MVC Terminology  |  Python Web Frameworks  |
+===================+=========================+
| Model             | Model                   |
+-------------------+-------------------------+
| Conroller         | - View Function         |
|                   | - Class Based View      |
|                   | - Model methods         |
+-------------------+-------------------------+
| View              | - Renderer              |
|                   | - Template              |
|                   | - View Function         |
|                   | - Class Based View      |
|                   | - HTTP Response         |
+-------------------+-------------------------+

Note in particular that what *MVC* calls a *controller* is most directly
analogous to what Python calls a *view*. This will be a source of confusion, so
I will try to use the term *view function* to be more precise.

For more on this difference and why it exists, you can `read this`_ from the
Pyramid design documentation.

.. _read this: http://docs.pylonsproject.org/projects/pyramid/en/latest/designdefense.html#pyramid-gets-its-terminology-wrong-mvc

A Visual Exploration
--------------------

It's easiest to see the effects of this chain of operations by using a real
browser.

Take a moment to start up your application at the command line:

.. code-block:: bash

    [learning-journal]
    [step2 *]
    heffalump:learning-journal cewing$ python journal.py
    serving on http://0.0.0.0:5000

When it's running, point your web browser at this address:

http://localhost:5000

You should see something like this:

.. image:: /_static/flask_hello.png
    :align: center

Now, quit your application with ``^C`` (that's the *control* key and the letter
*c*). Then remove the following code from your ``journal.py`` file:

.. code-block:: python

    @view_config(route_name='home', renderer='string')
    def home(request):
        return "Hello World"

Restart your application as you did before.  Reload the same URL and you should
see this:

.. image:: /_static/pyramid_not_found.png
    :align: center

If a matched *route* has no *view* to pass the request to, it will raise a
**404** error.

Now, let's re-connect the ``'home'`` route to a *view function*. We need to create a
function that will take the ``request`` as an argument and will return a

Make the following changes to ``journal.py``:

.. code-block:: python

    @view_config(route_name='home', renderer='templates/list.jinja2')
    def list_view(request):
        entries = Entry.all()
        return {'entries': entries}

Finally, having saved this change, restart your application and again load the
URL:

http://localhost:5000

You should see something like this:

.. image:: /_static/pyramid_list_page_nostyle.png
    :align: center

You've now attached the ``'home'`` route to the ``read_entries`` function,
making it a *view* function. And you've configured it to use the
``list.jinja2`` *renderer* we created earlier. Review that template. Make sure
you understand why the page is appearing with "*No entries here so far*\ ".

Quit your application again and now all your tests should pass:

.. code-block:: bash

    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$ py.test --tb=native
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/cewing/projects/codefellows/learning-journal, inifile:
    collected 7 items

    test_journal.py .......

    =========================== 7 passed in 0.38 seconds ===========================
    [learning-journal]
    [pyramid/step2 *]
    Pratchett:learning-journal cewing$


Deploying Your Work
===================

It's no fun to do all this work without seeing what you've done.

Repeat the steps you performed for the previous assignment to submit your work
and prepare for deployment. As a reminder, here's the outline:


1. push all local work on the ``step2`` branch up to GitHub
2. create a pull request in your GitHub repository from ``step2`` to
   ``master``
3. copy the URL for that pull request and submit your assignment in Canvas
4. locally, checkout ``master`` and merge your work from ``step2`` (remember,
   this will close your pull request, but that's fine)
5. push master to the heroku remote

Create an Entry on Heroku
-------------------------

You really do want to see your first journal entry, don't you?

Go ahead and create one. Start by opening a python session with Heroku:

.. code-block:: bash

    [learning-journal]
    [master=]
    192:learning-journal cewing$ heroku run python
    Running `python` attached to terminal... up, run.9416
    Python 2.7.6 (default, Jan 16 2014, 02:39:37)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

And now, create a first entry:

.. code-block:: python

    >>> import os
    >>> from sqlalchemy import create_engine
    >>> from sqlalchemy.orm import sessionmaker
    >>> from journal import Entry
    >>> db_url = os.environ.get('DATABASE_URL')
    >>> engine = create_engine(db_url)
    >>> Session = sessionmaker(bind=engine)
    >>> session = Session()
    >>> entry = Entry(
    ...   title="My First Entry",
    ...   text="Today I learned you can write a journal entry from the command line in Heroku,  Neat!"
    ... )
    >>> session.add(entry)
    >>> session.commit()
    >>>

Once you're done, use the standard ``^D`` to detach from the Python terminal on
Heroku. At this point you are good to go. Well done!

At this point, you should actually be able to see your website running on
Heroku. You can open a browser and point immediately to the site using a
command from the Heroku toolbelt:

.. code-block:: bash

    [learning-journal]
    [master=]
    heffalump:learning-journal cewing$ heroku open
    Opening evening-brushlands-7955... done

Your browser should then open (or open a new tab) and you should see something
a bit like this:

.. image:: /_static/lj_heroku.png
    :width: 90%

If you see an error instead, here are some tools to use in debugging:

.. code-block:: bash

    [learning-journal]
    [master=]
    heffalump:learning-journal cewing$ heroku ps

The ``ps`` command should tell you if there are any *dynos* running.  You
should see output like this:

.. code-block:: bash

    [learning-journal]
    [master]
    heffalump:learning-journal cewing$ heroku ps
    === web (1X): `python journal.py`
    web.1: up 2015/01/28 19:28:17 (~ 2s ago)

If you see nothing instead you can use the ``scale`` command to start a new
*dyno*:

.. code-block:: bash

    [learning-journal]
    [master]
    heffalump:learning-journal cewing$ heroku scale web=1
    Scaling dynos... done, now running web at 1:1X.

You can also use the ``scale`` command to turn your website off.  Just scale
``web=0``.

If you get messages saying that your application crashed when you run ``ps``,
or if you see "internal server error" messages in your browser indicating
something is wrong with the code in your application, you can use the heroku
``logs`` command to see logfiles of the server:


.. code-block:: bash

    [learning-journal]
    [master]
    heffalump:learning-journal cewing$ heroku logs
    2015-01-26T04:30:17.767423+00:00 heroku[api]: Enable Logplex by c...
    2015-01-26T04:30:17.767423+00:00 heroku[api]: Release v2 created by c...
    ...

These log messages may be quite cryptic, but they will help you to debug
problems if you read them carefully.

Finally, remember that to help yourself figure out what is happening, you can
always open a Python interpreter in the Heroku environment:


.. code-block:: bash

    [learning-journal]
    [master=]
    192:learning-journal cewing$ heroku run python
    Running `python` attached to terminal... up, run.9416
    Python 2.7.6 (default, Jan 16 2014, 02:39:37)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

From there you can poke around at your journal code to see what might be wrong.

