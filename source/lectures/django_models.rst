********************
Django: Model Basics
********************

.. ifnotslides::

    We've now spent some time getting to know how to write web applications using the Pyramid framework.
    We've learned the basics of Model construction, routing, views and renderers.
    We've learned how to authenticate users and how to authorize them to take certain actions.
    And we've created our own first projects using this powerful and flexible tool.

    Now it's time for us to move on to using the current undisputed champion of the Python web frameworks: `Django <https://www.djangoproject.com/>`_

.. ifslides::

    Time to learn Django!

Starting a Django Project
=========================

.. ifnotslides::

    We'll begin by creating a new virtualenv in which to play.
    This one is temporary, just for exploring in class.
    Name it accoringly, and then install Django:

.. ifslides::

    .. rst-class:: left
    .. container::

        Begin with a virtualenv

        Just temporary

        Install Django

.. rst-class:: left
.. code-block:: bash

    $ python3 -m venv djplay
    ...
    $ cd djplay
    $ source bin/activate
    (djplay)$ pip install Django
    Downloading/unpacking Django
      Downloading Django-1.9.5-py2.py3-none-any.whl (6.6MB): 6.6MB downloaded
    Installing collected packages: Django
    Successfully installed Django
    Cleaning up...

``startproject``
----------------

.. ifnotslides::

    Once Django is installed, we can create a "project" to explore a bit.
    Django uses the term "project" to refer to the code that will make up one website.
    You always begin work on a Django website by creating a project.

.. code-block:: bash

    (djplay)$ django-admin startproject foo

.. ifslides::

    .. rst-class:: build
    .. container::

        Use ``django-admin`` to start a new project

        Django "project" == 1 website

.. nextslide::

.. ifnotslides::

    The ``startproject`` command works a bit like the ``pcreate`` command in Pyramid.
    It creates a bit of boilerplate code structure to make starting a new site easier.
    Let's take a moment to look over the ``foo`` directory it created.

.. code-block:: bash

    (djplay)$ tree foo
    foo
    ├── foo
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

.. ifslides::

    .. rst-class:: build
    .. container::

        ``startproject`` roughly equal to ``pserve``, makes boilerplate

        creates *project root*, can also be *repository root*

        nested *configuration root* is a Python package

        This contains configuration (``settings.py``, ``urls.py``)

        Also exposes the project WSGI application (``wsgi.py``)

.. ifnotslides::

    Notice it creates both an *outer* foo folder and an *inner* foo folder.
    The outer one is your *project home* (or *project root*).
    You should consider the contents of this outer folder the root of the project repository.

    Nested inside the *project root* is a folder we'll call the *configuration root*.
    This folder **must** be a proper Python package (with an ``__init__.py`` file).

    It contains your project settings file(s) ``settings.py``.
    This file contains configuration settings for a project.
    It plays a role similar to the ``development/production.ini`` files we've seen in Pyramid.

    It also contains a ``wsgi.py`` file, which exposes the wsgi application that contains your project.
    This file is roughly analagous to the ``paste.app_factory`` entry point in a Pyramid application.
    However, Django is not as closely tied to Python packaging as Pyramid.
    It makes much less use of packaging features like entry points, in favor of its own solutions.

    Finally, the configuration root contains a ``urls.py`` file.
    This file contains the top-level configuration of urls for your project.
    We'll talk more about this next week, but for now, understand that Django urls are analogous to Pyramid's *routes*.
    They provide the connection between the *path* of an incoming HTTP request and the code object that will generate an HTTP response.

``manage.py``
-------------

.. ifnotslides::

    The only other file created by ``startproject`` is ``manage.py``, in the *project root*.
    The file contains code which locates your project's ``settings.py`` file.
    It does this by setting the value of ``DJANGO_SETTINGS_MODULE`` in ``os.environ``.

    This file serves as a gateway to Django's command system.
    It is an executable python script (notice the ``if __name__ == "__main__":`` block and the *shebang* line at the top).

.. code-block:: python

    #!/usr/bin/env python
    import os
    import sys

    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foo.settings")

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)

.. ifslides::

    .. rst-class:: build
    .. container::

        Locates your project *settings* (``DJANGO_SETTINGS_MODULE``)

        Provides access to Django management commands


Managing Django
===============

.. ifnotslides::

    Django's management command system is accessed entirely through the ``manage.py`` script.
    When we execute this script, it uses additional values on the command line as command names and arguments for those commands.
    To get a list of the available management commands, run the script with no additional values:

.. rst-class:: left
.. code-block:: bash

    (djplay)$ cd foo
    (djplay)$ python manage.py

    Type 'manage.py help <subcommand>' for help on a specific subcommand.

    Available subcommands:

    [auth]
        changepassword
        createsuperuser
        ...

.. ifslides::

    .. rst-class:: build left
    .. container::

        Execute ``manage.py`` to get Django management commands

        Pass the name of a command after the script name to run it

        Use ``help`` to find out more about a command


``shell``
---------

.. ifnotslides::

    The first command that will be important to you is ``shell``.
    Running this command starts an interactive Python session with all of the packages in your Django project available for import.
    It's the Django version of ``pshell`` from Pyramid.
    And like ``pshell``, if you install iPython, it will automatically use the iPython interpreter (with tab completion and everything):

.. code-block:: bash

    (djplay)$ pip install iPython
    ...
    (djplay)$ python manage.py shell
    Python 3.5.1 (default, Jan 18 2016, 14:50:30)
    ...
    In [1]: import django.contrib.auth
    In [2]: django.contrib.auth.
    django.contrib.auth.BACKEND_SESSION_KEY
    django.contrib.auth.HASH_SESSION_KEY
    ...

.. ifslides::

    .. rst-class:: build
    .. container::

        Let's try ``shell`` (like Pyramid's ``pshell``)

        It also supports using iPython

        Install and fire it up!


Exploring Django's Models
=========================

.. ifnotslides::

    Django comes with its own ORM, and relies entirely on the idea of *models*.
    It comes with quite a few of these models already present.
    Django *requires* that you place models in a Python module named ``models.py``.
    We can use this knowledge to explore the models from Django's ``auth`` app.
    Here we will find the ``User`` model, the core of Django's authentication and authorization systems.

.. rst-class:: left
.. code-block:: ipython

    In [2]: django.contrib.auth.models.
    django.contrib.auth.models.AbstractBaseUser
    django.contrib.auth.models.AbstractUser
    ...
    django.contrib.auth.models.User
    ...

.. ifslides::

    .. rst-class:: build left
    .. container::

        Django has its own ORM, with *models*

        Models in Django **must** be defined in a ``models.py``

        We can see models defined in Django's own code, like the ``auth`` app

        The ``User`` model is the core of Django authn/authz


User
----

.. ifnotslides::

    Let's import and inspect the User model, so we can learn a bit about it.

.. code-block:: ipython

    In [2]: from django.contrib.auth.models import User
    In [3]: User?
    Init signature: User(self, *args, **kwargs)
    Docstring:
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    File:           ~/.virtualenvs/d35-imager/lib/python2.7/site-packages/django/contrib/auth/models.py
    Type:           ModelBase

.. ifslides::

    Import and inspect the User model

.. nextslide::

.. ifnotslides::

    So the ``User`` model has username, password and email.
    These are required attributes.
    But what else is there?

.. code-block:: ipython

    In [4]: dir(User)
    Out[4]:
    ['DoesNotExist',
    'Meta',
    'MultipleObjectsReturned',
    'REQUIRED_FIELDS',
    'USERNAME_FIELD',
    ...

.. ifslides::

    User has username, password and email

    We can read the rest of the attributes with ``dir``

.. nextslide:: Use The Source, Luke

.. ifnotslides::

    Wow, there's all sorts of stuff on that object!
    It might be better for us to go and take a look at the source code so we can start to get an idea of how this thing is built.
    Lets see where the `User` file lives:

.. code-block:: ipython

    In [5]: django.contrib.auth.models.__file__
    Out[5]: '.../djplay/lib/python2.7/site-packages/django/contrib/auth/models.pyc'

.. ifslides::

    Lots of attributes there, eh?

    Read the ``__file__`` attribute of the object

    Open the source file (remember to remove the ``c`` from the ``.pyc``)

.. nextslide::

.. ifnotslides::

    Reading the source file, we can find the ``User`` model.
    But the source for it is remarkably void of attributes.
    Where do all the attributes we saw in the shell come from?

.. code-block:: python

    class User(AbstractUser):
        """
        Users within the Django authentication system are represented by this
        model.

        Username, password and email are required. Other fields are optional.
        """
        class Meta(AbstractUser.Meta):
            swappable = 'AUTH_USER_MODEL'

.. ifslides::

    .. rst-class:: build
    .. container::

        Not a lot there, is there?

        Where do the attributes we saw before come from?

Subclassing
-----------

.. ifnotslides::

    Django makes extensive use of *subclassing* to share attributes among models.
    The ``User`` model inherits from ``AbstractUser``:

.. code-block:: python

    class AbstractUser(AbstractBaseUser, PermissionsMixin):
        """
        ...
        """
        username = models.CharField(
            _('username'),
            max_length=30,
            unique=True,
            help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
            ...
            )
        ...

.. ifslides::

    Django uses *subclassing* to share attributes

    ``User`` inherits from ``AbstractUser``

    This is where the core of the ``User`` model is found

Fields
------

.. ifnotslides::

    ``AbstractUser`` inherits from ``AbstractBaseUser`` and ``PermissionsMixin`` too, but here we can see ``username``.
    Notice the syntax used to define that attribute.
    It looks similar to SQLAlchemy, in that the attribute is bound to an instance of some kind of class.

    In SQLAlchemy we called these things ``Columns``.
    In Django, we call them ``Fields``.
    It can get confusing because there are Model fields and Form fields, but they are not the same thing.

    This ``username`` is a *model field*.
    Like SQLAlchemy ``Columns``, model fields are responsible for communicating between Python and the database.
    The `models.CharField` defines a text field inside the database.
    Values we set for this attribute of instances of the ``User`` model
    We can create a new ``User`` instance.
    We can set a value for the `username` attribute on that instance.
    And we can persist that value into a database.

    The biggest difference here from what we are used to has to do with the *semantics* of how we interact with the database.
    Django is ``model``\ -centric as opposed to ``session``\ -centric.
    Remember in SQLAlchemy we always started with a ``session``.
    We would use statements like ``session.query(Entry)`` to query a model.

    Django is different.
    We start with the model itself, ``User``.
    That class object will have an attribute called ``objects``.
    That attribute *is* the connection between the model class and the database.
    We will use that attribute to build queries.

.. ifslides::

    ``username`` is a ``Field`` object

    .. rst-class:: build
    .. container::

        Just like a SQLAlchemy ``Column``

        Converts values from Python to SQL and back

        Make a ``User``, set ``username`` and persist to DB

        Semantics are different, though

        Sqla uses ``session``, Django uses ``objects`` attribute of model

        Let's experiment with this

.. nextslide::

Let's create a new user `bob`:

.. code-block:: ipython

    In [2]: bob = User()
    In [3]: bob
    Out[3]: <User: >

By default, ``bob`` has empty attributes:

.. code-block:: ipython

    In [4]: bob.username
    Out[4]: u''
    In [5]: bob.email
    Out[5]: u''
    In [6]: print(bob.id)
    None

.. nextslide::

.. ifnotslides::

    Let's give bob some information.
    We saw before that `username`, `password`, and `email` are required.
    We'll start by setting values for those attributes.

.. ifslides::

    Set required attributes:

    ``username``, ``password``, ``email``

.. code-block:: ipython

    In [7]: bob.username = "bob"
    In [8]: bob.password = "foobar"
    In [9]: bob.email = "bob@bob_dobalina.com"
    In [10]: bob
    Out[10]: <User: bob>

.. ifslides::

    Does ``bob`` have an id?

.. ifnotslides::

    Now we have ``bob`` with a representation: ``<User: bob>``.
    Does bob have an ID now?

    .. code-block:: ipython

        In [11]: bob.id

.. nextslide::

.. ifnotslides::

    No.
    Nothing is returned.
    How did we add a new entry into our system in Pyramid?
    How did we make the database aware of something and preserve it?

.. ifslides::

    No id, indicates the DB doesn't know about this ``user`` instance

    .. rst-class:: build
    .. container::

        How did we tell the DB about an instance in Pyramid?

        .. code-block:: python

            session.add(instance)

        Django has no such concept.

        Instead, we do `bob.save()`

        But first, we have to make a database.

.. ifnotslides::

    .. code-block:: python

        session.add(instance)

    But not in Django.
    Remember, here the semantics are based on the instance itself.
    We can call ``save`` on the ``bob`` user instance.
    But we have to create the database first.

.. nextslide::

In another terminal, create our database tables:

.. code-block:: bash

    $ source bin/activate
    (djenv)$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, contenttypes, auth, sessions
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      ...

Basic Query API
---------------

Now we can save ``bob``:

.. code-block:: python

    In [12]: bob.save()
    In [13]: bob.id
    Out[13]: 1

And make even more users:

.. code-block:: python

    In [14]: sally = User(username="sally", email="sally@sally.com", password="secret")
    In [15]: sally.save()
    In [16]: sally.id
    Out[16]: 2

.. nextslide::

How about a list of all of our users?

.. code-block:: python

    In [17]: User.objects.all()
    Out[17]: [<User: bob>, <User: sally>]

We can filter the list:

.. code-block:: python

    In [18]: User.objects.filter(username='bob')
    Out[18]: [<User: bob>]

For Homework
============

.. ifnotslides::

    One of the first things we want to do is create a user model.
    Something that represents the user in our system.
    However, we are strongly encourged to use Django's own built in user model unless we have a very good reason not to.
    But the standard Django user model doesn't have everything that we want. It does have:

    .. code-block:: python

        class AbstractUser(AbstractBaseUser, PermissionsMixin):
            ...
            first_name = models.CharField(_('first name'), max_length=30, blank=True)
            last_name = models.CharField(_('last name'), max_length=30, blank=True)
            email = models.EmailField(_('email address'), blank=True)
            is_staff = models.BooleanField(
                _('staff status'),
                default=False,
                help_text=_('Designates whether the user can log into this admin site.'),
            )
            is_active = models.BooleanField(
                _('active'),
                default=True,
                help_text=_(
                    'Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.'
                ),
            )
            date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
            ...

.. ifslides::

    .. rst-class:: left
    .. container::

        We need a user model for our Django application

        .. rst-class:: build
        .. container::

            Django wants us to use their user

            But it doesn't have all the fields we might want

            .. rst-class:: build
            .. container::

                * username (from higher above)
                * first_name, last_name
                * email
                * is_staff (means user could login to the admin)
                * is_active (so you can turn them off without deleting)
                * date_joined

.. nextslide::

.. rst-class:: left
.. container::

    We also get a few fields from ``AbstractBaseUser``:

    .. code-block:: python

        class AbstractBaseUser(models.Model):
            password = models.CharField(_('password'), max_length=128)
            last_login = models.DateTimeField(_('last login'), blank=True, null=True)
            is_active = True
            ...

Our Needs
---------

.. ifnotslides::

    Our application will allow users to store and organize photos.
    We might want to have information about our users related to that purpose.
    Values like:

    - What kind of camera they have
    - Address
    - Link to a personal website
    - Type of photography (nature, urban, portrats?)
    - Social media keys

.. ifslides::

    We want users who are photographers, organizing photos

    .. rst-class:: build
    .. container::

        We might want to know:

        .. rst-class:: build

        - What kind of camera they have
        - Address
        - Link to a personal website
        - Type of photography (nature, urban, portrats?)
        - Social media keys

.. ifnotslides::

    The Django way of customizing a user is not to change the Django user model.
    You can do that, but you may break many things if you do that.
    Django wants you to move all of the other things into a `profile`.


    We'll need to create a new model of our own, a ``UserProfile``.
    Any given user will only need to have one profile.
    And any given profile will belong only to one user.
    The SQL relationship that represents this is called ``One to One``.
    It's represented in SQL by a foreign key combined with a unique constraint.

    In Django, there is a `ForeignKey <https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.ForeignKey>`_ field.
    It takes as its first argument the class to which you want to build a relationship.

    .. code-block:: python

        profile = models.ForeignKey(User, unique=True)

    But this is the old-fashioned way to do it.
    If we look at a profile object, and we want to find the user to which it is related, we say ``bob_profile.user``.
    We'd like the result of this call to be a user instance.
    If we use a ``ForeignKey`` with ``unique=True``, we'll get a list back that *contains* the user.
    Django also supplies a ``OneToOneField``.
    Using this will allow Django to expect--and return--only one value.

    You'll need to create an app to hold this profile.
    Call this new app ``imager_profile``.
    Use what you learned from the Django tutorial to accomplish this task.

Wrap Up
=======

.. ifnotslides::

    We've learned a bit now about how Django works.
    We learned about starting new applications, and managing them.
    We've learned about the Django ORM and how it works
    And we've learned about the built-in User model it provides.
    We've talked about how we can extend the functionality of this model using a ``Profile`` related to the User by a one-to-one relationship.
    You'll use this knowledge now to create a profile for the users of our Django Imager application.

.. ifslides::

    .. rst-class:: left
    .. container::

        Today, we've learned:

        .. rst-class:: build

        * creating and managing Django projects
        * how the Django ORM works
        * the User model
        * extending the user model with a profile
