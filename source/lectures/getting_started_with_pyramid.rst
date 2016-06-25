============================
Getting Started With Pyramid
============================

Make a directory to work in, I'll call it ``pyramid_test``, and make a new virtual environment in that directory. Then navigate to that directory and activate the virtual environment. Then pip install the most recent versions of ``pip`` and ``setuptools``

.. code-block::

    (pyramid_test) bash-3.2$ pip install -U pip setuptools
    (pyramid_test) bash-3.2$ pip install ipython

Installation
============

In order to begin working with Pyramid, we have to install it.

.. code-block::
    
    (pyramid_test) bash-3.2$ pip install pyramid

The version that should be pulled down is the latest version, 1.7. Note the other packages that get installed along with it, as it has dependencies. For example, WebOb handles HTTP responses, and Pyramid's response object inherits from this. Many other frameworks also use this package.

Along with its dependencies, Pyramid installs for you a bunch of new shell commands (``pcreate``, ``pshell``, ``prequest``, etc), and you can see them all in the ``bin`` directory of your virtual environment.

.. code-block::

    (pyramid_test) bash-3.2$ ls bin
    activate         easy_install-3.5 ipython3         pip3             pserve           python
    activate.csh     iptest           pcreate          pip3.5           pshell           python3
    activate.fish    iptest3          pdistreport      prequest         ptweens
    easy_install     ipython          pip              proutes          pviews


Writing a "Hello World" App
===========================

Pretty much straight from `trypyramid.com <http://www.trypyramid.com>`_. First, make a directory for your "hello world" app called ``hello_world``. Within that directory create a file named ``app.py`` and type the following:

.. code-block:: python

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.response import Response 


    def hello_world(request):
        return Response("Hello World!")

    if __name__ == '__main__':
        config = Configurator()
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 6543, app)
        server.serve_forever()

Save that file and run the following from the command line:

.. code-block::

    (pyramid_test) bash-3.2$ python app.py

Notice how the shell returns nothing. That means that the server you've set up through Pyramid is up and listening for requests.

Finally, open http://localhost:6543/ in your browser. This will simply connect you to the port that Pyramid is listening to.

This is an almost irresponsibly-simple web app. We'll be using Pyramid for somewhat more-complicated things. That being said, it's very easy to get a simple site up and running with Pyramid. 

Using the ``pcreate`` Command to Create a Scaffold
===================================================

``pcreate`` allows us to create a scaffold for a web app that includes the basic functionality and best practices of a Pyramid app. Before using this command, back out by one directory and create a new directory called ``scaffold``. Then, invoke ``pcreate`` like so:

.. code-block::

    (pyramid_test) bash-3.2$ pcreate -s alchemy testapp

This scaffold will use SQLAlchemy to connect to a database (hence "alchemy" in the command). Running this command will create a bunch of files and end with "Sorry for the convenience." **if you see this line, your scaffold was created just fine**. The entire scaffold will be encapsulated in the ``testapp`` directory that was just created. Navigate to it and initialize a git repository.

If you use git status you'll see all of the new files that were just created in this directory. Add this entire directory to your repository with ``git add .``. We want to make sure we don't track .pyc files or the .DS_Store file in this directory, so create a ``.gitignore`` file and add lines to ignore those files. Then add your ``.gitignore`` to the repository.

This project root directory will contain a bunch of files that are metadata for our application

* ``CHANGES.txt`` tracks what changes we've made to our app over time
* ``MANIFEST.ini`` controls what files are actually present when we package our stuff together and upload it
* ``README.txt`` is our README file. We can change that to markdown without consequence.
* ``development.ini`` discussed later 
* ``production.ini`` discussed later
* ``setup.cfg`` is the configuration for our setup, while...
* ``setup.py`` lets our directory become an installable python package

Inspecting ``setup.py`` reveals that this app requires Pyramid, ``Jinja2`` (a templating engine), and a few other packages to work. It also comes packed ready to install some packages for tests. Let's modify it so that it runs with ``tox`` as part of its test suite:

.. code-block:: python

    # in setup.py 
    ...
    requires = [
        'pyramid',
        'pyramid_jinja2',
        ... # other package dependencies
        'SQLAlchemy',
        ... # even more dependencies
    ]
    ...
    tests_require = [
        'WebTest >= 1.3.1',  # py3 compat
        'pytest',  # includes virtualenv
        'pytest-cov',
        'tox', # you have to add this one in
    ]
    ...
    setup(name='testapp',
        version='0.0',
        ... # package metadata
        install_requires=requires,
        entry_points="""\ # Entry points are ways that we can run our code once it has been installed
        [paste.app_factory]
        main = testapp:main 
        [console_scripts]
        initialize_testapp_db = testapp.scripts.initializedb:main
        """
    )

Don't forget to fill in the appropriate information about ``author``, ``author_email``, etc. Now, let's install it in editing mode so that the changes we make to this project will be implemented in the installed version.

.. code-block::

    (pyramid_test) bash-3.2$ pip install -e .

Pyramid is Python
=================

Navigate to the ``testapp`` directory in your project root and inspect it.

.. code-block::

    (pyramid_test) bash-3.2$ ls
    __init__.py models      scripts     templates   views
    routes.py   static      tests.py 

In the ``__init__.py`` file you'll find a ``main`` function, which runs when you use ``pserve`` to connect your site to the localhost.

.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

This looks vastly different from the ``app.py`` file we had created earlier. The machinery here is handling a lot of the stuff we had hard coded before. Let's look at this in detail.

.. code-block:: python 
    
    def main(global_config, **settings):

Configuration is passed into an application after being read from the specified ``.ini`` file. The settings come in through, you guessed it, ``**settings``. The ``.ini`` files contain sections (e.g. ``[app:main]``) containing ``name = value`` pairs of *configuration data*. This data is parsed with the Python `ConfigParser <https://docs.python.org/2/library/configparser.html>`_ module, which reads the configuration data and returns it as a dictionary. The result appears in ``settings`` as:

.. code-block:: python

    {'pyramid.default_locale_name': 'en', 
    'sqlalchemy.url': 'sqlite:////Users/Nick/Documents/codefellows/courses/code401_python/pyramid_test2/testapp/testapp.sqlite', 
    'pyramid.reload_templates': 'true',
    ...}

Those settings get read and handled on the next line after the docstring

.. code-block:: python 

    config = Configurator(settings=settings)

where the Configurator class object is instantiated with the appropriate settings.

We can also ``include`` configuration from other add-on packages and even other regions of the app we're inside of. That explains the next three lines:

.. code-block:: python

    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()

``Jinja2`` is our templating engine. We need to include the ``pyramid_jinja2`` package so that the templates we write with ``Jinja2`` syntax can be read and interpreted by Pyramid. The next line down imports settings from our package's ``models`` directory, specifically its own ``__init__.py``. We'll come back to ``models`` later, as we will ``routes``. Finally, the ``config.scan()`` line checks to make sure that there are no problems with how everything is wired together.

We'll return to the configuration of our application repeatedly over the next few sessions. For greater detail about configuration in Pyramid, check the `configuration chapter <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html>`_ documentation.


Pyramid Models
==============

The central component of MVC, the *model*, captures the behavior of the application in terms of its problem domain, independent of the user interface. **The model directly manages the data, logic, and rules of the application**

- from the Wikipedia article on `Model-View-Controller <https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_

The ``models`` Directory
-----------------------------------------------

The files in the models directory are few:

.. code-block::
    (pyramid_test) bash-3.2$ ls models
    __init__.py     meta.py     mymodel.py

* ``meta.py``: determines the naming conventions that will go into your database via SQLAlchemy
* ``mymodel.py``: the file containing the model for your data. You can have many files like these, or you can have multiple models in the same file. Generic models will inherit from the ``Base`` class.
* ``__init__.py``: where the needs of the data models are called and fed into the Configurator with ``config.include('.models')``. This includes the setup of the SQLAlchemy interaction with our database, the creation of sessions, managing transactions between the database and Pyramid, and of course including our data models.

  
Models and ORMs
---------------

In an MVC application, we define the *problem domain* by creating one or more *Models*. These capture relevant details about the information we want to preserve and how we want to interact with it.

In Python-based MVC applications, these *Models* are implemented as Python classes, inheriting from the ``Base`` class set up in ``meta.py``. The individual bits of data we want to know about are *attributes* of our classes. The actions we want to take using that data are *methods* of our classes. Together, we can refer to this as the *API* of our system.

The model provided by this scaffold, ``MyModel``, is fairly simple. 

.. code-block:: python

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)

It will belong to the ``models`` table in our database, and every entry into that table will have attributes of ``id``, ``name``, and ``value``.

.. .. ===========================================
.. .. ===========================================


.. Before we can investigate what the scaffold has given us as far as a full site, we have to set up our database. In ``setup.py`` we're given a console command that does this for us, ``initialize_testapp_db``. If we run that with the ``development.ini`` configuration file we'll see the following flow through our terminal:

.. .. code-block::

..     (pyramid_test) bash-3.2$ initialize_testapp_db development.ini 


.. Let's see what this scaffold has provided us using the ``pserve`` command on the project's configuration file.

.. .. code-block::

..     (pyramid-test) bash-3.2$ pserve development.ini --reload

.. Open up the browser at http://localhost:6543/ and investigate.



.. The vast majority of the changes we'll be making will take place in the project directory within ``testapp`` which is also called  ``testapp``. Within this one you'll find directories for "models", "views", and "templates" among other things.









