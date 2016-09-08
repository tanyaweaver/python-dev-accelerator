******************
Django: Migrations
******************

In which we learn how to manage a database schema over time


Why Migrations?
===============

.. ifnotslides::

    In a web application that is backed by a database, our data model represents all the things you care about persisting.
    The `schema <https://en.wikipedia.org/wiki/Database_schema>`_ of our database represents your data model.
    Establishing a solid data model and a good schema to hold it is key to building a good web application.
    But is the creation of a data model (and the associated schema) a one-and-done job?
    There are a number of reasons that the answer to that question should be **no**.

.. ifslides::

    Our data model is our world

    .. rst-class:: build
    .. container::

        The *schema* of our database defines how that model works

        A good schema is key to a good application

        But can we just *set it and forget it*?

        **NO**

.. nextslide::

.. ifnotslides::

    First, the form of our data is not static, over time it can change.
    Sometimes you can adapt this new form into an existing schema,
    but sometimes it's easier or better to adapt our schema to the change.
    Second, the problem we are trying to solve may change.
    New problems can lead to a need for new data models.
    We'll need to be able to update our model to solve new challenges as they arise.
    Third, our application may require new features.
    Often these features involve using data we have in ways we have not anticipated.
    Or, they may require integrating new data we didn't care to keep before.
    Finally, we may reach a scale where our current schema is no longer viable.
    Queries that work well at a small scale may not do so well when larger numbers are involved.
    Often, changing the shape of our data can help reduce the load.

    For all these reasons (and more) it is important that we be able to update our database.
    And it is important that we be able to do so *while there is data in it that we care about*.

.. ifslides::

    Why Not?

    .. rst-class:: build

    * Data changes over time
    * The problems we are solving change over time
    * Our feature set changes over time
    * Our scale changes over time

    .. rst-class:: build
    .. container::

        So we need to be able to change our database schema over time.

        And we need to be able to save the data that is there.

.. nextslide::

.. ifnotslides::

    Up until this point, when we have made changes to a database we have dropped our existing tables and replaced them with new ones.
    We've used code that looks like this in our database initialization scripts:

.. ifslides::

    So far, we've destroyed and rebuilt on each change

.. code-block:: python

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        for fields in starter_data:
            dbsession.add(Model(**fields))

.. nextslide::

.. ifnotslides::

    This is fine, so long as the only data we have in our database is what comes from ``starter_data``.
    But if we have a system where user-provided data is generated over time,
    or where our own system generates information we are keeping,
    it is not okay to simply throw that data away when we need to change our database.
    So how can we make changes to an existing database?

.. ifslides::

    Okay, as long as our data is limited to ``starter_data``

    .. rst-class:: build
    .. container::

        If users provide data, no good

        If system generates data, no good

        We can't throw away stuff we've created

        How do we save that stuff?


.. nextslide:: One Way Out?

.. ifnotslides::

    One possible solution is to store the SQL statements needed to build our database tables.
    Each time a change is made, we add two files.
    The first file is the SQL needed to build the new database tables.
    The second file is a series of SQL statements needed to make changes to the previous tables to transform them.
    Executing the former file will build a brand new database in the new state.
    Executing the latter will update an existing database to the new state.

.. ifslides::

    We could keep SQL files with required statements

    .. rst-class:: build
    .. container::

        One file holds all the current database schema definitions

        Run this file to build a new database with the new schema

        A second holds the statements to move from one state to another

        Run this file to update an existing database to the new schema

.. nextslide:: Is it the best?

.. ifnotslides::

    But we should ask ourselves a few questions here.
    First, how are we going to keep track of all these sql files.
    Can we build a naming scheme that makes it clear which is the right one, *right now*\ ?
    Second, are we really interested in writing all the SQL required to make these files.
    We are building models in Python, building our app in Python.

.. ifslides::

    Some questions need answering.

    .. rst-class:: build
    .. container::

        How to track these files?

        Can we name them to avoid confusion?

        Can we easily correlate them with the current state of our application code?

        Do we have the skill/time/interest for writing all that SQL?

        We are already defining models in Python.

What is a Migration?
====================

.. ifnotslides::

    The answer to our problem is to use Python to manage database change over time.
    A *migration* in Python uses the features of an ORM to provide tools to change our database.
    A migration system compares the current state of our application's models to the existing state of the database.
    When a difference is found, that difference can be described with a set of *operations*.
    These operations are saved into a python script that can be executed.
    When we run the script, the operations run one after another, and the database is updated.
    In the end, the state of the database is a match for the state of your models.

.. ifslides::

    A *migration* uses an ORM to provide tools to change our database.

    .. rst-class:: build
    .. container::

        Compares current state of models to existing state of database.

        Differences are described by *operations*

        Operations are combined into a *script*

        Running the script updates your database to match your models.

.. nextslide:: I can haz migrations?

.. ifnotslides::

    The dominant ORM systems for Python all support migrations.
    The `Alembic <http://alembic.zzzcomputing.com/en/latest/>`_ package provides migration support for the SQLAlchemy ORM.
    For the Django ORM, the ability is included in the Django distribution.
    The `django.db.migrations <https://docs.djangoproject.com/en/1.10/topics/migrations/>`_ package provides all the tools you need.
    This has not always been the case.
    Systems that use Django versions before 1.7 will use an add-on package called ``south`` instead.

.. ifslides::

    Python ORMs support migrations.

    .. rst-class:: build
    .. container::

        (At least, the dominant packages do)

        In SQLAlchemy, use ``Alembic``

        Django has its own ORM

        The migration system is built in (``django.db.migrations``)

        For old Django sites (pre v.1.7) use ``south``


Using Django Migrations
=======================

.. ifnotslides::

    Since migration support moved into the core of Django in version 1.7,
    they've been promoted as *the* right way to deal with setting up your models.
    There once was a way to create your database without migrations.
    That time is gone.
    You should always create migrations to set up your initial models.
    And you should make migrations to account for all changes you make to those models.
    The Django migration system should be as much a part of your development routine as version control and testing.

.. ifslides::

    Migrations are *the* way to create and manage your database.

    .. rst-class:: build
    .. container::

        There used to be a way to create the database without migrations.

        That time is gone.

        Always make migrations to create your initial models.

        Add migrations for any changes to your models.

        Add migrations for any new models you create.

        Add migrations when you remove models.

        Migrations are co-equal to testing and version control in your Django dev toolchain.


Creating Migrations
-------------------

As a concrete example, let's consider a simple application for a library.

We'll begin by creating our application using our well-worn path:

.. code-block:: bash

    $ python3 -m venv library_project
    $ cd library_project
    $ source ./bin/activate
    (library_project)$ django-admin start project library
    (library_project)$ cd library
    (library_project)$ ls
    library  manage.py

At this point, we've created a project called ``library``.
The ``library`` *project root* folder it created contains a ``manage.py`` script
and a ``library`` *configuration root*, which is a Python package.


In Process
==========

Basic Usage

    creating Migrations

    applying Migrations

Data Migrations

    creating

    applying

Migration Dependencies

    automatic dependencies

    Things to watch out for

    resolving parallel Migrations

