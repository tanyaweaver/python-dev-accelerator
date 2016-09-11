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

Whoa! That's a lot of stuff.
We didn't create all those migrations.
What happened?
Because we haven't ever migrated anything in this project our migration is not alone.
Django detects that there are other migrations that need running, and applies them all.

Rollback and Retry
------------------

Let's now imagine that we decide that this simple patron profile we've built is not enough.
Perhaps we need to have an address for our patrons.
So we have to add a few fields to our model, perhaps like this:

.. code-block:: python

    # in library_patron/models.py

    class PatronProfile(models.Model):
        """A profile representing a library patron"""
        # ... other fields here
        address_1 = models.CharField(
            "Street Address 1",
            max_length=255,
            blank=True,
            null=True)
        address_2 = models.CharField(
            "Street Address 2",
            max_length=255,
            blank=True,
            null=True)
        city = models.CharField(
            max_length=128,
            blank=True,
            null=True)
        state = models.CharField(
            max_length=2,
            blank=True,
            null=True)
        post_code = models.CharField(
            max_length=5,
            blank=True,
            null=True)

Once we have updated our model code, we can create a new migration file and then apply it:

.. code-block:: bash

    (library_project)$ ./manage.py makemigrations library_patron --name add_address_fields
    Migrations for 'library_patron':
      library_patron/migrations/0002_add_address_fields.py:
        - Add field address_1 to patronprofile
        - Add field address_2 to patronprofile
        - Add field city to patronprofile
        - Add field post_code to patronprofile
        - Add field state to patronprofile
    (library_project)$ ./manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, library_patron, sessions
    Running migrations:
      Applying library_patron.0002_add_address_fields... OK

But wait, we've made a mistake.
As it turns out while ZIP-codes in the US have only 5 digits,
in Canada they have 6 (and a dash in the middle).
So our limit of 5 characters for the post code field is not sufficient.

We could fix this by updating the model and then making and applying a new migration,
but we haven't actually pushed this code yet.
Let's do something a bit more sophisticated.

We can also run our migrations in reverse, undoing the changes they made.
To do so, we specify the migration we want to be the last one applied.
In our case here, we can specify our initial migration to roll back to that state:

.. code-block:: bash

    (library_project)$ ./manage.py migrate library_patron 0001
    Operations to perform:
      Target specific migration: 0001_initial, from library_patron
    Running migrations:
      Rendering model states... DONE
      Unapplying library_patron.0002_add_address_fields... OK

Once our database has been changed back to the previous state,
we can edit our Django model code to make the required update:

.. code-block:: python

    # in library_patron/models.py

    post_code = models.CharField(
        max_length=7, # <-- update this
        blank=True,
        null=True)

And now we can remove the old migration file, create a new one and re-apply our changes:

.. code-block:: bash

    (library_project)$ rm library_patron/migrations/0002_add_address_fields.py
    (library_project)$ ./manage.py makemigrations library_patron --name add_address_fields
    Migrations for 'library_patron':
      library_patron/migrations/0002_add_address_fields.py:
        - Add field address_1 to patronprofile
        - Add field address_2 to patronprofile
        - Add field city to patronprofile
        - Add field post_code to patronprofile
        - Add field state to patronprofile
    (library_project)$ ./manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, library_patron, sessions
    Running migrations:
      Applying library_patron.0002_add_address_fields... OK

Please do note that some migrations cannot be undone.
If you have a migration that deletes a field that contained data,
it is not possible to fully undo that migration.
The data that had been held in that field is lost when the field is dropped.
Unless you took the extra step of migrating your data first.


Data Migrations
===============

Consider the following scenario.
We have now discovered that our Patron profile ought to allow for more than one address.
We could add a new set of fields for a second address,
but many (or perhaps most) of our patrons will only have one address.
We would end up with a lot of empty columns in our database, which is wasteful of space.
And what if a patron needs three addresses?  Or four?
When will the madness end?

Instead, let's break an address out as a separate model.
If we have a foreign key on that field to our profile, we can have as many addresses as we want associated with a single profile.

But we have a problem.
Our one-address form has been in use for some time now.
There is data in the database that we care about.
Should we leave the existing address fields in place?
That would be silly.
We'd have data about the same thing in two difference places.

Instead, let's migrate our data out of the fields on our patron profile.

We can create new address records to hold them.
We'll get our new storage format, and not lose any data along the way.

Let's begin with our new address class:

.. code-block:: python

    @python_2_unicode_compatible
    class PatronAddress(models.Model):
        """A physical address for a patron"""
        profile = models.ForeignKey(PatronProfile, related_name="addresses")
        address_1 = models.CharField(
            "Street Address 1",
            max_length=255)
        address_2 = models.CharField(
            "Street Address 2",
            max_length=255,
            blank=True,
            null=True)
        city = models.CharField(max_length=128)
        state = models.CharField(max_length=2)
        post_code = models.CharField(max_length=7)

Now, we *could* just remove the fields for addresses from the ``PatronProfile`` model and add this new model and make a migration.
After running it, we'd have our new model, and the old model would be cleaned up.
But we would have lost all the data about addresses that is already in our database.
What we need to do is create this model first, then move the data from one model to the other.
Finally, we can remove the original fields.

That middle step is a thing we call a **data migration**.
The data migration allows us to change the data in our database, as opposed to changing the schema of the database itself.
Data migrations are a powerful tool in managing a database over time.
They allow us to change where or how data is stored in our database.
This greatly increases our power to update the database to match new challenges.

So, let's create a migration to add this new model, and then think about how to address the problem of moving address data.

.. code-block:: bash

    (library_project)$ ./manage.py makemigrations library_patron --name add_address_model
    Migrations for 'library_patron':
      library_patron/migrations/0003_add_address_model.py:
        - Create model PatronAddress

Creating Data Migrations
------------------------

Data migrations are not different on the surface from standard migrations.
But the ORM cannot automatically detect what we want to do with our data.
So instead we have to create an *empty* migration and manually add the operations we need.
To do so, we issue an altered ``makemigrations`` command.
We use the ``--empty`` command flag to indicate that we don't want any operations to be generated for us.

.. code-block:: bash

    (library_project)$ ./manage.py makemigrations --empty --name move_address_fields library_patron
    Migrations for 'library_patron':
      library_patron/migrations/0004_move_address_fields.py:

Let's take a quick look at what we got:

.. code-block:: python

    # library_patron/migrations/0004_move_address_fields.py
    class Migration(migrations.Migration):

        dependencies = [
            ('library_patron', '0003_add_address_model'),
        ]

        operations = [
        ]

Our migration is dependent on the previous one we created,
the one that adds the address model.
This means that at the point when this migration runs, we can count on that model existing.

The reason that is important is because we need that model (and the table that stores its data) to exist.
That way we have a way to store the data we are moving from the existing ``PatronProfile`` instances.

So how do we move that data?
The key is in a special kind of operation provided by the migration system, ``RunPython``

The ``RunPython`` operation is a bit different from other operations.
The others we've seen so far are all aimed at making schema changes to our database.
This operation allows us to run an arbitrary Python function instead.
In this function we can write code to interact with instances of models in our application.

In our case, we'd like to work with instances of our ``PatronProfile``.
For each instance, we'd like to read the value of the fields that provide address information.
We'll create a new instance of our new ``PatronAddress`` model, and write the data to the corresponding field there.
Then, we'll relate the new address model instance to our existing profile instance.
Finally, we'll save these new model instances.

Let's write a function that will do this.
Functions that are run by the migrations ``RunPython`` operation *require* a particular argument signature.
They will be called with ``apps`` and ``schema_editor``.
The ``apps`` argument gives us tools to interact with installed applications.
The ``schema_editor`` argument provides tools for updating your database schema directly.
We will not likely need to use it directly.

Here's a function that fills our needs:

.. code-block:: python

    # in library_patron/migrations/0004_move_address_fields.py
    def move_address_data_to_address_model(apps, schema_editor):
        PatronProfile = apps.get_model('library_patron', 'PatronProfile')
        PatronAddress = apps.get_model('library_patron', 'PatronAddress')
        fields = ['address_1', 'address_2', 'city', 'state', 'post_code']
        for profile in PatronProfile.objects.all():
            if profile.address_1:
                address = PatronAddress(profile=profile)
                for fieldname in fields:
                    setattr(address, fieldname, getattr(profile, fieldname))
                address.save()

We use ``apps.get_model`` to retrieve the Model classes we need to interact with.
You should always do this, rather than importing the models directly.
There are subtle but significant differences in how the models are instrumented to interact with the database.

Once we have the Model classes, we can interact with them just as normal.
All the same query operations work just as they do in normal Django code.
So we can use the Python ``setattr`` and ``getattr`` functions to copy the values of specific attributes from one model to the other.
Also notice that if our Profile did not originally include address data, we do not create an address instance for it.
To apply our migration, we'll need to add this function as an operation, using ``RunPython``:

.. code-block:: python

    # in library_patron/migrations/0004_move_address_fields.py
    class Migration(migrations.Migration):

        dependencies = [
            ('library_patron', '0003_add_address_model'),
        ]

        operations = [  # add the following statement
            migrations.RunPython(
                move_address_data_to_address_model
            )
        ]


Applying Data Migrations
------------------------

Once we've got this set up, we can apply both our model migration and our new data migration in one shot.
But what if we want to undo the changes we made?
Schema migrations are in many cases self-reversing.
The opposite operation can be calculated by the ORM.
In data migrations this is not the case.

We *can* however, supply our own reverse operations.
The ``RunPython`` migration operation can take a second argument that is the function to be run to undo whatever changes were made.
If it is not possible to undo a data migration, then do not supply this argument.
The migration system will recognize this as a migration that cannot be undone and refuse to apply it.

Let's add a reverse function:

.. code-block:: python

    def move_address_data_back_to_profile(apps, schema_editor):
        PatronProfile = apps.get_model('library_patron', 'PatronProfile')
        fields = ['address_1', 'address_2', 'city', 'state', 'post_code']
        for profile in PatronProfile.objects.all():
            first_addr = profile.addresses.order_by('pk').first()
            if first_addr is not None:
                for fieldname in fields:
                    setattr(profile, fieldname, getattr(first_addr, fieldname))

Now we can add this reverse function as a second positional argument to our operation:

.. code-block:: python

    # in library_patron/migrations/0004_move_address_fields.py
    class Migration(migrations.Migration):

        dependencies = [
            ('library_patron', '0003_add_address_model'),
        ]

        operations = [  # add the following statement
            migrations.RunPython(
                move_address_data_to_address_model,
                move_address_data_back_to_profile, # <-- add this line
            )
        ]

Once this is set, we can apply our new migrations,
both forward and in reverse:

.. code-block:: bash

    (library_project)$ ./manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, library_patron, sessions
    Running migrations:
      Applying library_patron.0003_add_address_model... OK
      Applying library_patron.0004_move_address_fields... OK

.. code-block:: bash

    (library_project)$ ./manage.py migrate library_patron 0002
    Operations to perform:
      Target specific migration: 0002_add_address_fields, from library_patron
    Running migrations:
      Rendering model states... DONE
      Unapplying library_patron.0004_move_address_fields... OK
      Unapplying library_patron.0003_add_address_model... OK
    The following content types are stale and need to be deleted:

        library_patron | patronaddress

    Any objects related to these content types by a foreign key will also
    be deleted. Are you sure you want to delete these content types?
    If you're unsure, answer 'no'.

        Type 'yes' to continue, or 'no' to cancel: yes

Notice the extra work that Django is performing here.
When we create a model, Django adds an entry to the `content types` table.
This entry allows us to make dynamic references to our models classes.
When we remove models, Django tracks the fact, and alerts us that there are now entries,
both in that table and potentially in other tables that will be deleted.
In general, this is perfectly safe, but you will want to think about the state of your database.
You can prevent these deletions by answering `no` to the prompt.
It is always possible to clean up later, manually.

Other Uses for Data Migrations
------------------------------

Data migrations allow us to manage the *content* of our database, instead of the *structure*.
This is useful when we need to update the structure of an existing database.
We can move data from one table to another, change it from one type to another, and much more.

But we can also use data migrations to create data our system requires in order to run.
Imagine that we have a ``branch`` field on our ``PatronProfile`` model.
It might be a "ForeignKey" field that references an instance of a ``LibraryBranch`` model.
That way, we can associate a patron with the specific branch where they pick up and return books.
It might look something like this:

.. code-block:: python

    # in library_assets/models.py

    @python_2_unicode_compatible
    class Branch(models.Model):
        branch_name = models.CharField(max_length=128)

    # in library_patron/models.py on the PatronProfile class:

    branch = models.ForeignKeyField(
        "Branch",
        blank=True,
        null=True)

It would probably be nice to have a few branches available to choose from when a new patron signs up.
And we don't really want to have some employee manually type them all in.
We can use a data migration to inject a number of new ``Branch`` instances as part of the app upgrade process.

Older versions of Django documentation encourage using "initial data fixtures" to do this type of work.
The problem with that approach is that the data in a fixture is "frozen" to a particular version of a model.
If the model changes over time, the fixture needs to be updated as well.
But because data migrations are run in a specific position in your data migration,
you can rely on the items you insert being correct for the state of your models *at that point in time*.
And you can use later data migrations to make needed change to that initial data.


Wrapping Up
===========

In this lecture, we've learned about Django migrations.
We've learned that migrations help us to manage the changes in our database over time.
We've seen how to create migrations, and how to apply them.
And we've learned about data migrations.
We've seen that they can help us to make more complex changes to our database.
And that we can use them to inject initial data into our database.

A final word about migrations.
**They are absolutely a part of your source code**\ .
You **must** add them to your repository and keep them.


