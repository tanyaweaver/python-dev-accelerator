============================
Getting Started With Pyramid
============================

Make a directory to work in, I'll call it ``pyramid_lj``, and make a new virtual environment in that directory. Then navigate to that directory and activate the virtual environment. Then pip install the most recent versions of ``pip`` and ``setuptools``

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -U pip setuptools
    (pyramid_lj) bash-3.2$ pip install ipython

Installation
============

In order to begin working with Pyramid, we have to install it.

.. code-block:: bash
    
    (pyramid_lj) bash-3.2$ pip install pyramid

The version that should be pulled down is the latest version, 1.7. Note the other packages that get installed along with it, as it has dependencies. For example, WebOb handles HTTP responses, and Pyramid's response object inherits from this. Many other frameworks also use this package.

Along with its dependencies, Pyramid installs for you a bunch of new shell commands (``pcreate``, ``pshell``, ``prequest``, etc), and you can see them all in the ``bin`` directory of your virtual environment.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ls bin
    activate         easy_install-3.5 ipython3         pip3             pserve           python
    activate.csh     iptest           pcreate          pip3.5           pshell           python3
    activate.fish    iptest3          pdistreport      prequest         ptweens
    easy_install     ipython          pip              proutes          pviews


Writing a "Hello World" App
===========================

A lot of this is pretty much straight from `trypyramid.com <http://www.trypyramid.com>`_. First, make a directory for your "hello world" app called ``hello_world``. Within that directory create a file named ``app.py`` and type the following:

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

.. code-block:: bash

    (pyramid_lj) bash-3.2$ python app.py

Notice how the shell returns nothing. That means that the server you've set up through Pyramid is up and listening for requests.

Finally, open http://localhost:6543/ in your browser. This will simply connect you to the port that Pyramid is listening to.

This is an almost irresponsibly-simple web app. We'll be using Pyramid for somewhat more-complicated things. That being said, it's very easy to get a simple site up and running with Pyramid. 

Using the ``pcreate`` Command to Create a Scaffold
===================================================

``pcreate`` allows us to create a scaffold for a web app that includes the basic functionality and best practices of a Pyramid app. Before using this command, back out by one directory and create a new directory called ``scaffold``. Then, invoke ``pcreate`` like so:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pcreate -s alchemy learning_journal

This scaffold will use SQLAlchemy to connect to a database (hence "alchemy" in the command). Running this command will create a bunch of files and end with "Sorry for the convenience." **if you see this line, your scaffold was created just fine**. The entire scaffold will be encapsulated in the ``learning_journal`` directory that was just created. Navigate to it and initialize a git repository.

If you use git status you'll see all of the new files that were just created in this directory. Add this entire directory to your repository with ``git add .``. We want to make sure we don't track .pyc files or the .DS_Store file in this directory, so create a ``.gitignore`` file and add lines to ignore those files. Then add your ``.gitignore`` to the repository.

This project root directory will contain a bunch of files that are metadata for our application

.. code-block:: bash

    (pyramid_lj) bash-3.2$ tree .

    ├── CHANGES.txt - tracks what changes we've made to our app over time
    ├── MANIFEST.in - controls what files are actually present when we package our stuff together and upload it
    ├── README.txt - is our README file. We can change that to markdown without consequence.
    ├── development.ini - discussed later
    ├── production.ini - discussed later
    ├── pytest.ini - is the configuration for our setup, while...
    ├── setup.py - lets our directory become an installable python package

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
    setup(name='learning_journal',
        version='0.0',
        ... # package metadata
        install_requires=requires,
        entry_points="""\ # Entry points are ways that we can run our code once it has been installed
        [paste.app_factory]
        main = learning_journal:main 
        [console_scripts]
        initialize_learning_journal_db = learning_journal.scripts.initializedb:main
        """
    )

Don't forget to fill in the appropriate information about ``author``, ``author_email``, etc. Now, let's install it in editing mode so that the changes we make to this project will be implemented in the installed version.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -e .

One of the things produced after pip installing is a ``*.egg-info`` file. Let's modify our ``.gitignore`` to exclude those.

Pyramid is Python
=================

Navigate to the ``learning_journal`` directory in your project root and inspect it.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ls
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
    'sqlalchemy.url': 'postgres://Nick@localhost:5432/learning_journal', 
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

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ls models
    __init__.py     meta.py     mymodel.py

* ``meta.py``: determines the naming conventions that will go into your database via SQLAlchemy
* ``mymodel.py``: the file containing the model for your data. You can have many files like these, or you can have multiple models in the same file. Generic models will inherit from the ``Base`` class.
* ``__init__.py``: where the needs of the data models are called and fed into the Configurator with ``config.include('.models')``. This includes the setup of the SQLAlchemy interaction with our database, the creation of sessions, managing transactions between the database and Pyramid, and of course including our data models.

  
The Models
----------

In an MVC application, we define the *problem domain* by creating one or more **Models**. These capture relevant details about the information we want to preserve and how we want to interact with it.

In Python-based MVC applications, these **Models** are implemented as Python classes, inheriting from the ``Base`` class set up in ``meta.py``. The individual bits of data we want to know about are **attributes** of our classes. The actions we want to take using that data are **methods** of our classes. Together, we can refer to this as the **API** of our system.

The model provided by this scaffold, ``MyModel``, is fairly simple. 

.. code-block:: python

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)


    Index('my_index', MyModel.name, unique=True, mysql_length=255)

It will belong to the ``models`` table in our database, and every entry into that table will have attributes of ``id``, ``name``, and ``value``. This table will be indexed based on the name of the object using this model for data.

Data Persistence
~~~~~~~~~~~~~~~~

It's all well and good to have a set of Python classes that represent your system. But what happens when you want to *save* information? What happens to an instance of a Python class when you quit the interpreter? What about when your script stops running? The code in a website runs when an HTTP request comes in from a client. It stops running when an HTTP response goes back out to the client. So what happens to the data in your system in-between these moments? **The data must be persisted**.

There are a number of alternatives for persistence:

* Python Literals
* Pickle/Shelf
* Interchange Files (CSV, XML, ini)
* Object Stores (ZODB, Durus)
* NoSQL Databases (MongoDB, CouchDB)
* SQL Databases (sqlite, MySQL, PostGreSQL, Oracle, SQLServer, etc.)
  
Any of these might be useful for certain types of applications. On the web the two most used are NoSQL and SQL. For viewing/interacting with individual objects, a NoSQL storage solution might be the best way to go. In systems with objects that are related to each other, SQL-based Relational Databases are the better choice. We'll work with the latter, particularly ``PostGresSQL`` to start.

Python provides a specification for interacting directly with databases: `dbapi2 <https://www.python.org/dev/peps/pep-0249/>`_. And there are multiple Python packages that implement this specification for various databases:

* `sqlite3 <https://docs.python.org/2/library/sqlite3.html>`_
* `python-mysql <http://mysql-python.sourceforge.net/MySQLdb.html>`_
* `psycopg2 <https://pypi.python.org/pypi/psycopg2>`_

With these, you can write SQL to save your Python objects into your database, but that's a pain. SQL, while not impossible, is yet another language to learn. On top of that **you should never ever ever ever use raw SQL to manipulate your DB through your site!** An *Object Relational Manager (ORM)* provides a nice alternative.

An ORM provides a layer of *abstraction* between you and SQL. You instantiate Python objects and set attribtues on them, and the ORM converts the data from these objects into SQL statements (and back).

SQLAlchemy
----------

In our project we use the `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_0_9/>`_ ORM. You can find SQLAlchemy among the packages in the ``requires`` list in this site's ``setup.py``. When we ``pip`` installed our app, we installed SQLAlchemy along with the rest of the app and its dependencies.

Now that we know about ORMs, let's go back to our model...

.. code-block:: python

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)

Any class we create that inherits from this ``Base`` becomes a *model*. It'll be connected through the ORM to our 'models' table in the database (specified by the ``__tablename__`` attribute). Once an instance of this class is saved, it and its attributes will become a row in the ``models`` table, with its attributes that are instances of `Column <http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html#sqlalchemy.schema.Column>`_ occupying *columns* in the table. More on this in the `Declarative <http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/declarative/>`_ chapter of the SQLAlchemy docs.

Each instance of ``Column`` requires *at least* a specific `data type <http://docs.sqlalchemy.org/en/rel_0_9/core/types.html>`_ (such as Integer or Text). Some others will be able to be specified by other arguments, such as whether or not it's a primary key. In the style above, the name of the class attribute holding each Column will be the name of the column in the database. If you want a different name, you can specify that too.

Creating the Database
---------------------

We have a *model* which allows us to persist Python objects to an SQL database, but our database needs to actually exist so that we can store the data. We can do that with little trouble by modifying what ``pcreate`` provided upon the construction of our scaffold. First, open up ``setup.py`` and add ``psycopg2`` as one of the required packages.

.. code-block:: python 
    
    # ...
    requires = [
        # ...
        psycopg2, # <-- add this now
    ]

``pip install -e .`` to make this new required package stick. This will allow us to access PostGreSQL and use it as our database moving forward. 

We of course have to create the database that we want to use before we can use it. Fortunately, when we installed ``psycopg2`` we got a nice shell command that makes this easy.

.. code-block::  bash

    (pyramid_lj) bash-3.2$ createdb learning_journal

We must also alter our ``development.ini`` file, changing the ``sqlalchemy.url`` parameter to point to our spankin'-new ``learning_journal`` database.

.. code-block:: bash

    # in development.ini
    # ...
    # sqlalchemy.url = sqlite:///%(here)s/testapp.sqlite # <-- comment this line out
    sqlalchemy.url = postgres://<Your Username Here>@localhost:5432/learning_journal
    # ...

Now we need to initialize our database. Our scaffold gave us a way to do that right in ``setup.py``

.. code-block:: python

    # ...
    setup(name='learning_journal',
        ...
        entry_points="""\
        [paste.app_factory]
        main = learning_journal:main
        [console_scripts]
        initialize_learning_journal_db = learning_journal.scripts.initializedb:main
        """,

We see that ``setup.py`` sets up an entry point in ``console_script`` and provides us with the ``initialize_learning_journal_db`` console script. If we look at the code in ``initializedb.py`` we find the following:

.. code-block:: python

    # learning_journal/scripts/initializedb.py
    #...
    import transaction
    #...
    from ..models import MyModel
    #...
    def main(argv=sys.argv):
        if len(argv) < 2:
            usage(argv)
        config_uri = argv[1]
        options = parse_vars(argv[2:])
        setup_logging(config_uri)
        settings = get_appsettings(config_uri, options=options)

        engine = get_engine(settings)
        Base.metadata.create_all(engine)

        session_factory = get_session_factory(engine)

        with transaction.manager:
            dbsession = get_tm_session(session_factory, transaction.manager)

            model = MyModel(name='one', value=1)
            dbsession.add(model)

By connecting this function as one of the ``console_scripts``, our Python package makes this function available to us as a command when we install it. When we execute the script at the command line, this is the function that gets run.

When we run the ``initialize_learning_journal_db`` command, it'll run this ``main`` function and by default create a new ``MyModel`` instance and insert it into the database. 

For expedience, let's modify setup.py to change ``initialize_learning_journal_db`` to ``setup.db``:

.. code-block:: python 

    setup(name='learning_journal',
        ...
        entry_points="""\
        [paste.app_factory]
        main = learning_journal:main
        [console_scripts]
        setup_db = learning_journal.scripts.initializedb:main
        """,

Then reinstall your package, again in development mode. Let's try out this new command. We'll need to provide a configuration file name, so let's use ``development.ini`` since we're in development:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ setup_db development.ini 
    2016-06-30 17:05:47,050 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] select version()
    ...
    2016-06-24 14:29:23,046 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] 
    CREATE TABLE models (
        id INTEGER NOT NULL, 
        name TEXT, 
        value INTEGER, 
        CONSTRAINT pk_models PRIMARY KEY (id)
    )
    ...
    2016-06-24 14:29:23,067 INFO  [sqlalchemy.engine.base.Engine:686][MainThread] COMMIT

The ``[loggers]`` configuration in our ``.ini`` file sends a stream of INFO-level logging to sys.stdout as the console script runs. We've now created a table in our postgres database! Joy! We've made a lot of changes to this point, so it's time to add, commit, and push.

Now that we have our database hooked up to our models, let's finally see what this scaffold has provided us. To do this, we have to let Pyramid start up a local server for us using the ``pserve`` command, with settings set by whatever configuration ``.ini`` file we provide.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini --reload

Open up the browser at http://localhost:6543/ and investigate. There's like nothing here! Some debug stuff we'll get to later, but hey it's a simple one-pager that just let's you know that you've managed to hook this site to your localhost and can visit the result. It's just a scaffold so it's empty inside. Let's fill it with some data.

Interacting with SQLAlchemy Models and the ORM
----------------------------------------------

We can investigate and manipulate our models from the interpreter pretty easily. Let's first make a nicer interpreter available for our project. Pyramid has its own iPython and its own way of connecting iPython to the application code you are writing. First, install iPython and Pyramid's iPython extension.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install ipython pyramid_ipython

The ``pshell`` command lets us connect iPython to our application code. Let's fire up ``pshell`` and explore for a moment to see what we have at our disposal.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pshell development.ini
    Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
    Type "copyright", "credits" or "license" for more information.

    IPython 4.2.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    Environment:
      app          The WSGI application.
      registry     Active Pyramid registry.
      request      Active request object.
      root         Root of the default resource tree.
      root_factory Default root factory used to create `root`.

The ``environment`` created by ``pshell`` provides us with a few useful tools:

- ``app`` is our new ``learning_journal`` application.
- ``registry`` provides us with access to settings and other useful information.
- ``request`` is an artificial HTTP request we can use if we need to pretend we are listening to clients
  
Let's use this environment to build a database session and interact with our data:

.. code-block:: ipython 

    In [1]: from learning_journal.models import get_engine, MyModel
    In [2]: engine = get_engine(registry.settings) # default prefixes are 'sqlalchemy.'
    In [3]: from sqlalchemy.orm import sessionmaker
    In [4]: Session = sessionmaker(bind=engine)
    In [5]: session = Session()
    In [6]: session.query(MyModel).all()
    #...
    2016-06-27 19:53:57,390 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value 
    FROM models
    2016-06-27 19:53:57,390 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    Out[6]: [<learning_journal.models.mymodel.MyModel at 0x105546080>]    

We've stolen a lot of this from the ``initializedb.py`` script. Any interaction with the database requires a ``session``. This object *represents* the connection to the database. All database queries are phrased as methods of the session.

.. code-block:: ipython

    In [7]: query = session.query(MyModel)
    In [8]: type(query)
    Out[8]: sqlalchemy.orm.query.Query

The ``query`` method of the session object returns a ``Query`` object. Arguments to the ``query`` method can be a *model* class or even *columns* from a model class. You can iterate over a query object. The result depends on the args you passed.

.. code-block:: ipython 

    In [9]: query1 = session.query(MyModel)
    In [10]: for row in query1:
       ....:     print(row)
       ....:     print(type(row))
       ....:     
    2016-06-27 20:01:55,950 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value 
    FROM models
    2016-06-27 20:01:55,951 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    <learning_journal.models.mymodel.MyModel object at 0x105546080>
    <class 'learning_journal.models.mymodel.MyModel'>

.. code-block:: ipython 

    In [11]: query2 = session.query(MyModel.name, MyModel.id, MyModel.value)
    In [12]: for name, id, val in query2:
       ....:     print(name)
       ....:     print(type(name))
       ....:     print(id)
       ....:     print(type(id))
       ....:     print(val)
       ....:     print(type(val))
       ....:     
    2016-06-27 20:04:25,640 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.name AS models_name, models.id AS models_id, models.value AS models_value 
    FROM models
    2016-06-27 20:04:25,640 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    one
    <class 'str'>
    1
    <class 'int'>
    1
    <class 'int'>

Notice that when you try to print stuff from the queries, iPython prints out the actual SQL the ORM uses to interact with the DB. We can see the query on its own by looking at the string representation of the query.

.. code-block:: ipython 

    In [13]: str(query1)
    Out[13]: 'SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value \nFROM models'

    In [14]: str(query2)
    Out[14]: 'SELECT models.name AS models_name, models.id AS models_id, models.value AS models_value \nFROM models'

You can use this to check that the query the ORM is constructing looks like you expect. It can be very helpful in testing and debugging.

The methods of the ``Query`` object roughly fall into two categories:

1. Methods that return a new ``Query`` object
2. Methods that return *scalar* values or *model instances*
   
Let's start by looking quickly at a few methods from the second category. 

Methods Returning Values & Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A good example of this category of methods is ``get``, which returns one model instance only. It takes a primary key as an argument:

.. code-block:: ipython 

    In [15]: session.query(MyModel).get(1)
    Out[15]: <learning_journal.models.mymodel.MyModel at 0x105546080>

    In [16]: session.query(MyModel).get(10)
    In [17]:

If no item with that primary key is present, then the method returns ``None``. Another example is one we've already seen. ``query.all()`` returns a list of all rows returned by the database.

.. code-block:: ipython 
    
    In [17]: query1.all()
    Out[17]: [<learning_journal.models.mymodel.MyModel at 0x105546080>]

    In [18]: type(query1.all())
    Out[18]: list

``query.count()`` returns the number of rows that would have been returned by the query:

.. code-block:: ipython 

    In [19]: query1.count()
    Out[19]: 1

Before getting into the other category (i.e. returning a new ``Query`` object), let's learn how to create new objects. We can create new instances of our *model* just like normal Python objects:

.. code-block:: ipython 

    In [20]: new_model = MyModel(name="fred", value=3)
    In [21]: new_model
    Out[21]: <learning_journal.models.mymodel.MyModel at 0x1053f8710>

In this state, the instance is *ephemeral*; our ``session`` knows nothing about it:

.. code-block:: ipython 

    In [22]: session.new
    Out[22]: IdentitySet([])

For the database to know about our new object, we must add it to the session with the ``session.add()``

.. code-block:: ipython 

    In [23]: session.add(new_model)
    In [24]: session.new
    Out[24]: IdentitySet([<learning_journal.models.mymodel.MyModel object at 0x1053f8710>])

We can even bulk-add new objects with ``session.add_all()``:

.. code-block:: ipython 

    In [25]: new = []
    In [26]: for name, val in [('bob', 34), ('tom', 13)]:
       ....:     new.append(MyModel(name=name, value=val))
       ....:

    In [27]: session.add_all(new)
    In [28]: session.new
    Out[28]: Out[37]: IdentitySet([<learning_journal.models.mymodel.MyModel object at 0x1055e3048>, <learning_journal.models.mymodel.MyModel object at 0x1053f8710>, <learning_journal.models.mymodel.MyModel object at 0x1055cb390>])

Up until now, the changes you've made are not permanent. They're recognized by your session, but they haven't been saved into the database. In order for these new objects to be saved to the database, the session must be ``committed``:

.. code-block:: ipython 

    In [29]: other_session = Session()
    In [30]: other_session.query(MyModel).count()
    Out[30]: 1
    In [31]: session.commit()
    In [32]: other_session.query(MyModel).count()
    Out[32]: 4

When you are using a ``scoped_session`` in Pyramid, this action is automatically handled for you. The session that is bound to a particular HTTP request is committed when a response is sent back.

You can edit objects that are already part of a session, or that are fetched by a query. Simply change the values of a persisted attribute, the session will know it's been updated:

.. code-block:: ipython 

    In [33]: new_model
    Out[33]: <learning_journal.models.mymodel.MyModel at 0x1053f8710>
    In [34]: new_model.name
    Out[34]: 'fred'
    In [35]: new_model.name = 'larry'
    In [36]: session.dirty 
    Out[36]: IdentitySet([<learning_journal.models.mymodel.MyModel object at 0x1053f8710>])

Commit the session to persist the changes:

.. code-block:: ipython 

    In [37]: session.commit()
    In [38]: [model.name for model in other_session.query(MyModel)]
    Out[38]: ['one', 'larry', 'bob', 'tom']


Methods Returning Query Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returning to query methods, a good example of the second type is the ``filter`` method. This method allows you to reduce the number of results, based on criteria:

.. code-block:: ipython 

    In [39]: [(o.name, o.value) for o in session.query(MyModel).filter(MyModel.value < 20)]
    Out[39]: [('one', 1), ('larry', 3), ('tom', 13)]

Another typical method in this category is ``order_by``:

.. code-block:: ipython 

    In [40]: [o.value for o in session.query(MyModel).order_by(MyModel.value)]
    Out[40]: [1, 3, 13, 34]

    In [41]: [o.name for o in session.query(MyModel).order_by(MyModel.name)]
    Out[41]: ['bob', 'larry', 'one', 'tom']

Since methods in this category return Query objects, they can be safely ``chained`` to build more complex queries:

.. code-block:: ipython 

    In [42]: query1 = Session.query(MyModel).filter(MyModel.value < 20)
    In [43]: query1 = query1.order_by(MyModel.name)
    In [44]: [(o.name, o.value) for o in query1]
    Out[44]: [('larry', 3), ('one', 1), ('tom', 13)]

Note that you can do this inline as well (``Session.query(MyModel).filter(MyModel.value < 20).order_by(MyModel.name)``). Also note that when using chained queries like this, no query is actually sent to the database until you require a result.


