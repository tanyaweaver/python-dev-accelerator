************************
Django Lecture Structure
************************

Week 06 - Django Imager Data Model
==================================

* introduce Django
* discuss project vs. app structure
* create a project, a first app, and write tests to prove they are wired correctly
* introduce user stories as a driving mechanism for specifications
* introduce django testing (unittest-based approach)
* introduce model managers
* introduce querysets and the queryset api
* introduce factory models for testing
* introduce django models and model fields (and field data types)
* introduce signals and signal handling
* introduce django relationship fields
* introduce relationship managers
* introduce file handling
* mutating settings in test

Monday - Create Profile Model
-----------------------------

* create a virtualenv `mkdir dj-library; cd dj-library; git init; python3 -m venv ./`
* set up a project: `django-admin dj_library`

    - discuss what a project is, and what files are there, briefly
    - discuss the difference between the "project root" and the "configuration root"

* add tests to a project

    - create a tests file in the configuration root for the project
    - import TestCase and set up a `LibraryProjectTestCase`
    - discuss what things might need testing about a project (settings, installed apps, etc)

        + think about things that are required for the project to work
        + avoid things set in environment as these will be changing depending on where tests are run
        + installed apps is a good thing to test

    - Discuss AppConfig subclass, what is it, how does it work?
    - Write tests to verify that the contrib apps installed by default are present

        + could be argued that this is testing Django, but if your project depends on `auth`, then you should be certain it is present
        + installed apps = 'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles' (can discuss briefly what each one does)
        + write one or two tests, then refactor to share repeated code. (see example app in github for good examples)
        + do not loop to test, would not spot two missing installed apps if you do. (see TestCase.subTest from python unittest module)

* Generate user stories related to a "profile"

    - As a user I want to have a library patron profile so I can edit information about myself.
    - As a user I want to have a library card ID number associated with my profile so I can check out books.
    - As a user I want to pick my favorite genres so I can see book suggestions based on them.

* We will need a new app that implements our patron profile

    - `./manage.py startapp library_patron`
    - add test verifying that the patron app is installed, run and see it fail
    - add app to list of installed apps, run tests and see them pass

* Create initial patron profile model

    - Start by writing tests to prove the model exists

        + `mkdir library_patron/tests`
        + `touch library_patron/tests/__init__.py`
        + `mv library_patron/tests.py library_patron/tests/test_patron_profile.py`
        + add test method to TestCase subclass:

        .. code-block:: python

            def test_model_exists(self):
                from django.apps import apps
                try:
                    apps.get_model('library_patron', 'PatronProfile')
                except LookupError:
                    self.assertTrue(False, 'PatronProfile model does not exist')

    - Run tests, verify that this one fails
    - Create model (minimal, no specific fields) in library_patron/models.py

        + discuss models.Model superclass and what that does (in general)
        + all models _must_ inherit from this class

    - Make migrations: `./manage.py makemigrations library_patron` -> 0001_initial.py

        + discuss what a migration is, why it exists, and what it does
        + look at generated migration file
        + notice that a primary key field is automatically created, called 'id'

    - run tests, see them pass

* Work on library card number user story

    - Write test verifying that a card number exists
    - We'll use a "UUID" as the card number

        + random number from numeric space large enough that duplication is statistically unlikely
        + provided by Python stdlib `uuid` module
        + supported in Django by UUIDField
        + it should be set automatically and be un-editable.

    - write test proving field exists and is a UUID:

    .. code-block:: python

        import uuid

        class PatronProfileTestCase(TestCase):
            # ...

            def test_model_has_card_number(self):
                """assert that a profile automatically gets a UUID card_number"""
                profile_instance = self._make_one()
                try:
                    cardnum = profile_instance.card_number
                    self.assertTrue(isinstance(cardnum, uuid.UUID))
                except AttributeError:
                    self.fail("PatronProfile instance has no attribute card_number")

    - run tests, watch that one fail
    - Add field definition:

    .. code-block:: python

        import uuid

        class PatronProfile(models.Model):
            card_number = models.UUIDField(
                unique=True,
                db_index=True,
                editable=False,
                default=uuid.uuid4
            )

    - `./manage.py makemigrations library_patron`
    - run tests, watch them pass
    - Add tests verifying that uniqueness is enforced (see example app in github)
    - Add a profile `__str__` special method to show card number:

    .. code-block:: python

        def __str__(self):
            return 'Library Patron: card number {}'.format(self.card_number)

* Depending on time available, implement tests and user story re: genre choices (see choices option for db fields, nice to have, but not required)
* Interact with models a bit to demonstrate model managers.

    - `./manage.py migrate` to apply migrations and create a db.
    - `./manage.py shell` to enter interactive shell (if ipython installed, will be ipython shell)
    - We can create an instance of a model just like building any instance of any python class:

        .. code-block:: ipython

            In [1]: from library_patron.models import PatronProfile

            In [2]: bob = PatronProfile()

            In [3]: bob
            Out[3]: <PatronProfile: card number 591c1fe9-bc12-44ac-abe1-f46d379da01f>

            In [4]: bob.id

            In [5]: bob.save()

            In [6]: bob.id
            Out[6]: 1

            In [7]: PatronProfile.objects
            Out[7]: <django.db.models.manager.Manager at 0x10ad987b8>

            In [8]: PatronProfile.objects.all()
            Out[8]: <QuerySet [<PatronProfile: card number 591c1fe9-bc12-44ac-abe1-f46d379da01f>]>

        + Notice that the 'id' is not set until we `.save()` the instance. This inserts it into the db.
        + `cls.objects` is a *ModelManager*, provides interaction with the database
        + methods on the manager allow us to build `QuerySet` instances. `.all()` is simplest, equal to `select * from x;` in SQL

    - We can also use the model manager to create new instances (this *does not* invoke the model's `.save()` method, be aware of that!!!):

        .. code-block:: ipython

            In [9]: for i in range(10):
               ...:     PatronProfile.objects.create()
               ...:

            In [10]: len(PatronProfile.objects.all())
            Out[10]: 11

            In [11]: [obj.card_number for obj in PatronProfile.objects.all()]
            Out[11]:
            [UUID('591c1fe9-bc12-44ac-abe1-f46d379da01f'),
             UUID('b9b2dd23-709f-4772-9c8f-f5dd6cc951c9'),
             UUID('fa08cda1-f47e-4780-9266-a4b9f61dec1b'),
             UUID('eb21964b-3199-43e1-b6b9-c098bd629e69'),
             UUID('87a8b7c0-c81e-441a-aa8b-3dfc1f49a4a3'),
             UUID('8361e0c4-f964-421c-b893-7634b6c57870'),
             UUID('883df7e3-39f6-450f-88d8-f416a37b3232'),
             UUID('7871c1ed-d442-413f-a99e-9f8dfccff901'),
             UUID('2c5cff5a-687b-4ab5-bb19-f4ff35d31625'),
             UUID('59194ea3-f3cb-4627-af3d-31faf59a4aed'),
             UUID('e8dabd6e-efa5-429f-a023-704d8fb21337')]

            In [12]: [obj.pk for obj in PatronProfile.objects.all()]
            Out[12]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        + Notice that each object gets a card number by default, we don't have to set it.
        + Notice that by default the ordering appears to be by primary key

    - We can use the `.order_by()` query set API method to change the order in which things are listed:

        .. code-block:: ipython

            In [13]: [obj.card_number for obj in PatronProfile.objects.order_by('card_number')]
            Out[13]:
            [UUID('2c5cff5a-687b-4ab5-bb19-f4ff35d31625'),
             UUID('59194ea3-f3cb-4627-af3d-31faf59a4aed'),
             UUID('591c1fe9-bc12-44ac-abe1-f46d379da01f'),
             UUID('7871c1ed-d442-413f-a99e-9f8dfccff901'),
             UUID('8361e0c4-f964-421c-b893-7634b6c57870'),
             UUID('87a8b7c0-c81e-441a-aa8b-3dfc1f49a4a3'),
             UUID('883df7e3-39f6-450f-88d8-f416a37b3232'),
             UUID('b9b2dd23-709f-4772-9c8f-f5dd6cc951c9'),
             UUID('e8dabd6e-efa5-429f-a023-704d8fb21337'),
             UUID('eb21964b-3199-43e1-b6b9-c098bd629e69'),
             UUID('fa08cda1-f47e-4780-9266-a4b9f61dec1b')]

            In [14]: [obj.id for obj in PatronProfile.objects.order_by('card_number')]
            Out[14]: [9, 10, 1, 8, 6, 5, 7, 2, 11, 4, 3]

            In [15]: [obj.pk for obj in PatronProfile.objects.order_by('-card_number')]
            Out[15]: [3, 4, 11, 2, 7, 5, 6, 8, 1, 10, 9]

            In [16]: [obj.pk for obj in PatronProfile.objects.order_by('?')]
            Out[16]: [10, 7, 5, 2, 11, 9, 1, 3, 8, 4, 6]

        + `.order_by` takes at least one string argument which is the name of the field to use for ordering.
        + you can prefix the name with a `-` to reverse the ordering
        + you can use `?` in `.order_by` to get a random ordering

    - We can get single objects as well, using query set API methods that return scalar values:

        .. code-block:: ipython

            In [20]: PatronProfile.objects.first()
            Out[20]: <PatronProfile: card number 591c1fe9-bc12-44ac-abe1-f46d379da01f>

            In [21]: PatronProfile.objects.order_by('card_number').first()
            Out[21]: <PatronProfile: card number 2c5cff5a-687b-4ab5-bb19-f4ff35d31625>

            In [22]: PatronProfile.objects.order_by('-card_number').first()
            Out[22]: <PatronProfile: card number fa08cda1-f47e-4780-9266-a4b9f61dec1b>

            In [23]: PatronProfile.objects.get(pk=5)
            Out[23]: <PatronProfile: card number 87a8b7c0-c81e-441a-aa8b-3dfc1f49a4a3>

        + Notice that ordering applies, and changes the result for `.first()`
        + We can also use `.get()` with keyword arguments corresponding to fields and values to get a specific single object
        + If we ask for one that does not exist, or if more than one object matches our parameters, then we get an error.

    - We can filter our results using field expressions:

        .. code-block:: ipython

            In [25]: midpoint = _

            In [26]: midpoint.card_number
            Out[26]: UUID('87a8b7c0-c81e-441a-aa8b-3dfc1f49a4a3')

            In [27]: [obj.id for obj in PatronProfile.objects.filter(card_number__gt=midpoint.card_number)]
            Out[27]: [7, 2, 11, 4, 3]

            In [28]: [obj.id for obj in PatronProfile.objects.filter(card_number__lt=midpoint.card_number)]
            Out[28]: [9, 10, 1, 8, 6]

            In [29]: [obj.id for obj in PatronProfile.objects.filter(card_number__exact=midpoint.card_number)]
            Out[29]: [5]

        + Notice that field expressions are just Python keyword arguments.
        + They have a field name and then a *field lookup* expression, separated by a double underscore.
        + There are lots of field lookups.  Learn them.

* This should provide enough tools to accomplish the homework for Monday night: Build the basic profile model for the Imager app.

    - spec out user stories, what data should the profile store?
    - suggestions:

        + camera type (free-type text field)
        + photography genre (pick from a list of existing genres, provided by the app (use `choices`))
        + location (city, state, country, conceptual home)
        + student-supplied values

Tuesday - Connect Profiles to Users
-----------------------------------

Wednesday - Add Albums and Photos
---------------------------------

Thursday -
-----------



Week 07 - Django Views - pt 1
=============================



Week 08 - Django Views - pt 2
=============================
- -
    - `cls.objects` is a *ModelManager*, provides interaction with the database
    - methods on the manager allow us to build `QuerySet` instances. `.all()` is simplest, equal to `select * from x;` in SQL