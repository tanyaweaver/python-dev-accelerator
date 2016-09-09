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
This should be increasingly familiar to us at this point.

Our next step is to create our first models for this application.
As a start, we'd like to have a model that represents the information we need to know about a library patron.
We can start with a simple model that contains only their library card number.
Let's begin by creating a Django *app* to hold this model:

.. code-block:: bash

    (library_project)$ ./manage.py startapp library_patron
    (library_project)$ ls
    library     library_patron  manage.py

In our editor, we'll sketch in the basic code needed to represent our patron profile.
We'd like it to have a one-to-one relationship to our ``AUTH_USER_MODEL``.
And we'd like it to have a library card number that is automatically generated and random.
Something like this:

.. code-block:: python

    # in library_patron/models.py
    from __future__ import unicode_literals
    import uuid
    from django.conf import settings
    from django.db import models
    from django.utils.encoding import python_2_unicode_compatible


    @python_2_unicode_compatible
    class PatronProfile(models.Model):
        """A profile representing a library patron"""

        card_number = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
        user = models.OneToOneField(settings.AUTH_USER_MODEL)

        def __str__(self):
            fn = self.user.get_full_name().strip() or self.user.get_username()
            return "{}: {}".format(fn, self.card_number)

Once we have a model, we need to make a migration in order to allow Django to build the database table(s) needed to support it.
But before we can make a migration, we have to be certain that Django will be aware of our model.
That requires adding our new app to the ``INSTALLED_APPS`` setting:

.. code-block:: python

    # in library/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'library_patron', #<-- Add this line
    ]

When that's all set, we can go ahead and create a new migration for our app.
The command is in the form ``python manage.py makemigrations <app_name>``.
We substitute the name of our app package for ``<app_name>``:

.. code-block:: bash

    (library_project)$ ./manage.py makemigrations library_patron
    Migrations for 'library_patron':
      library_patron/migrations/0001_initial.py:
        - Create model PatronProfile

We should pay attention to a few things about what just happened there.
First, notice that our migration is automatically named for us.
The filename that was created is ``0001_initial.py``.
The number is automatically generated, we don't have control over that.
But the name part (after the ``_``) can be controlled.
If you provide a name on the command line that will be used instead:

.. code-block:: bash

    (library_project)$ rm library_patron/migrations/0001_initial.py
    (library_project)$ ./manage.py makemigrations library_patron --name silly_name
    Migrations for 'library_patron':
      library_patron/migrations/0001_silly_name.py:
        - Create model PatronProfile

But that's a silly name, so let's put the original back.

.. code-block:: bash

    (library_patron)$ ./manage.py makemigrations library_patron
    Migrations for 'library_patron':
      library_patron/migrations/0001_initial.py:
        - Create model PatronProfile

One more thing we should notice about what we just did.
Until they have been applied, there's nothing particularly special about migrations.
We can create and delete them.
This will become important later.

What's In a Migration?
----------------------

Let's take a moment to look over and talk about what was generated by that ``makemigrations`` command.
There are a coupld of important aspects to the code there that we should understand.

.. code-block:: python

    # in library_patron/migrations/0001_initial.py
    
    class Migration(migrations.Migration):

        initial = True

        dependencies = [
            migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ]

Notice that our migration system generates ``Migration`` class objects.
These objects bear the methods that power the migration system.
The ``initial`` class attribute tells us whether this migration is the first one for an app.
The ``dependencies`` class attribute provides a list of the other migrations upon which this one depends.
Django uses these lists to assemble a graph of migrations that need to be run,
and to calculate the correct order in which to run them.

Moving on.

.. code-block:: python

    operations = [
        migrations.CreateModel(
            name='PatronProfile',
            fields=[
                ('card_number', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False
                )),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
    ]

The final class attribute is ``operations``.
This attribure is a list of *operation* instances from the ``django.db.migrations`` package.
There are operations for creating and deleting tables.
For adding, altering and dropping columns.
And even for running arbitrary Python and SQL code.

In our initial migration we can see there is only one operation.
We will be creating a table.
Notice that the field definitions from our model are replicated here.
Everything needed to create the SQL that will represent those fields is present on those model field instances.

It is always a good idea to review the operations generated by the ``makemigrations`` command.
The migration system is good, but it is not perfect.
There are times when it misses something.
And situations you can create that it cannot handle.
If what you see does not align with what you expect, try to figure out why before you apply the migration.
Remember that you can always delete this file and re-create the migration,
so long as you haven't yet applied it.

Applying Migrations
-------------------

Now that we have a better understanding of what we've created, it is time for us to do apply the migration.
To do so, we use the ``migrate`` Django management command.
The command takes the form ``./manage.py migrate <app_name> <migration_name>``.
Both the ``app_name`` and ``migration_name`` arguments are optional
Django will apply any migrations that need applying.
If we supply a specific `app_name`, only migrations from that app will be applied.
If we supply a specific migration name, then only that specific migration will be applied.

In general, we use only the basic form, and apply all available, unapplied migrations:

.. code-block:: bash

    (library_project)$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, library_patron, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying library_patron.0001_initial... OK
      Applying sessions.0001_initial... OK

Because we haven't ever migrated anything in this project our migration is applied in addition to all the other migrations that are needed for basic Django functionality.

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

