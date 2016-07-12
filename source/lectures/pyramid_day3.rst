==============================
Models, Forms, and SQL Alchemy
==============================

The central component of MVC, the *model*, captures the behavior of the application in terms of its problem domain, independent of the user interface. **The model directly manages the data, logic, and rules of the application**. A model can be any "thing", e.g. an individual blog post on a blog, a photo or an album on a photo site, a user that visits and enrolls in the site, etc.

A model is most useful when the data that it describes is *persisted*. To do that, we'll be interacting with a SQL database and saving information to that database with SQL Alchemy. In order to have this all easily wired together for us, we're going to start a new scaffold that includes all of that SQL functionality. We'll also find that with this new scaffold, the MVC of our app is far more *explicity* separated into entire directories instead of individual files. Let's dip in.

The "Alchemy" Scaffold
======================

Before we use ``pcreate`` to construct a new scaffold to fill with our information and functionality, let's back out into the root directory housing Pyramid.  Call ``pcreate`` in this directory, but this time with the SQLAlchemy scaffold.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pcreate -s alchemy learning_journal

This scaffold sets us up to connect to any database that we specify via SQLAlchemy. Running this command creates a few more files and directories than we'd seen before. Before we investigate, navigate into the ``learning_journal`` directory and initialize a ``git`` repository. Provide this new repo with an appropriate ``.gitignore`` file. Now add everything in this directory to the repo and commit.

This project root directory will have the same named files that we've come to know and love in our Pyramid app, however some of their contents have changed. Let's inspect ``setup.py``.

.. code-block:: python

    # setup.py
    ...
    requires = [
        ...
        'SQLAlchemy',
        'transaction',
        'zope.sqlalchemy',
        ...
    ]
    ...
    setup(
        ... # same stuff until the end
        [console_scripts]
        initialize_learning_journal_db = learning_journal.scripts.initializedb:main
    )

This scaffold comes with dependencies for `SQLAlchemy <http://docs.sqlalchemy.org/en/latest/>`_, the `transaction package <http://zodb.readthedocs.io/en/latest/transactions.html>`_, and ``zope.sqlalchemy``.

* ``SQLAlchemy`` - as mentioned, allows us to interact directly with the DB without writing raw SQL
* ``transaction`` - a package that takes results of an HTTP response and executes other parts of your app that are aware of what the response is supposed to affect
* ``zope.sqlalchemy`` - integrates SQLAlchemy with the Pyramid transaction manager
  
The ``entry_points`` argument gets a new bit called ``console_scripts``. It declares...console scripts. In our current case, we have a script that initializes our database. This gets used when we create or change one of our data models. 

I find that ``initialize_learning_journal_db`` is an unreasonably long name for a console command that will be invoked fairly often. Let's shorten this to ``initialize_db`` such that our ``setup`` function ends with...

.. code-block:: python

    # setup.py
    # ...
    setup(
        ... # same stuff until the end
        [console_scripts]
        initialize_db = learning_journal.scripts.initializedb:main
    )

We need to make sure that this command is available to our app. To do so, install the app!

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -e .

And now our package has added ``transaction``, ``SQLAlchemy``, ``zope.sqlalchemy``, as well as our ``initialize_db`` command into our current environment. We won't initialize a database yet though until we've created our data model.

Another major change is found in our ``development.ini`` file. In the ``[app:main]`` section, there's a new keyword: ``sqlalchemy.url``. This keyword points sqlalchemy to the database that we want to use. Currently, it's pointed at a sqlite database that will be created in our project root when we call ``initialize_db``. 

.. code-block:: bash

    [app:main]
    ...
    sqlalchemy.url = sqlite:///%(here)s/learning_journal.sqlite
    ...

Later on when we learn about `PostGresSQL <https://pypi.python.org/pypi/psycopg2>`_, we'll change value associated with this keyword to point to a PostGres database.

The MVC/MVT Directory Tree
----------------------

If we investigate the ``learning_journal`` directory in our project root, what we see is going to be significantly different from what we'd built with our ``starter`` scaffold.

.. code-block:: bash

    (pyramid_lj) bash-3.2 tree learning_journal
    learning_journal
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   ├── meta.py
    │   └── mymodel.py
    ├── routes.py
    ├── scripts
    │   ├── __init__.py
    │   └── initializedb.py
    ├── static
    │   ├── pyramid-16x16.png
    │   ├── pyramid.png
    │   └── theme.css
    ├── templates
    │   ├── 404.jinja2
    │   ├── layout.jinja2
    │   └── mytemplate.jinja2
    ├── tests.py
    └── views
        ├── __init__.py
        ├── default.py
        └── notfound.py

To start, the app root only contains three files: ``__init__.py``, ``routes.py``, ``tests.py``. Aside from those three, *everything* else has been abstracted out directories. Let's follow this trend and push ``tests.py`` into its own ``tests`` directory, in case we want to separate our unit tests from our functional tests, or our model tests from our view tests, etc.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ cd learning_journal; mkdir tests; mv tests.py tests/

Let's investigate ``__init__.py``:

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

We have one line here that's different from what we had in our basic learning journal. We're including the ``models`` directory, which is what houses all of our data. Aside from that, pretty much everything is the same. We'll get to models in a bit, but let's look into ``views``:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ tree views
    views
    ├── __init__.py
    ├── default.py
    └── notfound.py

If you look at ``views/__init__.py`` it's entirely empty. That's on purpose. Recall that in order to create a Python module, you need an ``__init__.py`` file but it doesn't actually have to contain anything. All that's been done here is that ``views`` has been made into a Python module. The views themselves have been put into ``default.py`` and ``notfound.py``, where ``default.py`` holds a basic view created by the scaffold and ``notfound.py`` holds a view specifically for handling 404 HTTP status codes. We'll talk more about what's *in* the ``View`` seen in ``default.py`` after this next section.

Pyramid Models
==============

The central component of MVC, the *model*, captures the behavior of the application in terms of its problem domain, independent of the user interface. **The model directly manages the data, logic, and rules of the application**

- from the Wikipedia article on `Model-View-Controller <https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_

The ``models`` Directory
------------------------

The files in the models directory are few:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ tree models
    models
    ├── __init__.py
    ├── meta.py
    └── mymodel.py

* ``meta.py``: determines the naming conventions that will go into your database via SQLAlchemy. The important thing here is the ``Base`` object, which when inherited creates your models.
* ``mymodel.py``: the file containing the model for your data. You can have many files like these, or you can have multiple models in the same file. Generic models will inherit from the ``Base`` class.
* ``__init__.py``: where the needs of the data models are called and fed into the Configurator (where ``config.include('.models')`` calls the ``includeme`` function). This includes the setup of the SQLAlchemy interaction with our database, the creation of sessions, managing transactions between the database and Pyramid, and of course including our data models.

The Models
----------

In an MVC application, we define the *problem domain* by creating one or more **Models**. These capture relevant details about the information we want to preserve and how we want to interact with it.

In Python-based MVC applications, these **Models** are implemented as Python classes, inheriting from the ``Base`` class set up in ``meta.py``. The individual bits of data we want to know about are **attributes** of our classes. When the database is initialized, *every attribute* that instantiates the ``Column`` class will become a column in the database. The actions we want to take using that data are **methods** of our classes. Together, we can refer to this as the **API** of our system.

The model provided by this scaffold, ``MyModel``, is fairly simple. 

.. code-block:: python

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)


    Index('my_index', MyModel.name, unique=True, mysql_length=255)

It will belong to the ``models`` table in our database, and every entry into that table will have attributes of ``id``, ``name``, and ``value``. This table will be indexed based on the name of the object using this model for data. While great for instruction, you will want to make a model of your own for your own purposes.

Data Persistence
~~~~~~~~~~~~~~~~

It's all well and good to have a set of Python classes that represent your system. But what happens when you want to *save* information? What happens to an instance of a Python class when you quit the interpreter? What about when your script stops running? The code in a website runs when an HTTP request comes in from a client; it stops running when an HTTP response goes back out to the client. So what happens to the data in your system in-between these moments? **The data must be persisted**.

There are a number of alternatives for persistence:

* Python Literals
* Pickle/Shelf
* Interchange Files (CSV, XML, ini)
* Object Stores (ZODB, Durus)
* NoSQL Databases (MongoDB, CouchDB)
* **SQL Databases (sqlite, MySQL, PostGreSQL, Oracle, SQLServer, etc.)**

Any of these might be useful for certain types of applications. On the web the two most used are NoSQL and SQL. For viewing/interacting with individual objects, a NoSQL storage solution might be the best way to go. In systems with objects that are related to each other, SQL-based Relational Databases are the better choice. We'll work with the latter, particularly ``sqlite`` to start. Tomorrow we'll hit ``PostGreSQL``.

Python provides a specification for interacting directly with databases: `dbapi2 <https://www.python.org/dev/peps/pep-0249/>`_. And there are multiple Python packages that implement this specification for various databases:

* `sqlite3 <https://docs.python.org/2/library/sqlite3.html>`_
* `python-mysql <http://mysql-python.sourceforge.net/MySQLdb.html>`_
* `psycopg2 <https://pypi.python.org/pypi/psycopg2>`_

With these, you can write SQL to save your Python objects into your database, but that's a pain. SQL, while not impossible, is yet another language to learn. On top of that **you should never ever ever ever use raw SQL to manipulate your DB through your site!** 

Let me reiterate this, because this is a seriously important point. **YOU SHOULD NEVER. EVER EVER. EVER EVER. EVER EVER EVER EVER USE RAW SQL TO MANIPULATE YOUR DB THROUGH YOUR SITE!!!!**.

.. figure:: http://www.ededition.com/blogpics/300-1.jpg
    :width: 300px
    :alt: Source: http://www.ededition.com/blogpics/300-1.jpg
    :align: center

An *Object Relational Manager (ORM)* provides a nice alternative.

An *ORM* provides a layer of *abstraction* between you and SQL. You instantiate Python objects and set attribtues on them, and the ORM converts the data from these objects into SQL statements (and back).

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

We have a *model* which allows us to *persist* Python objects in an SQL database, but our database needs to actually exist so that we can store the data. This takes us back to the ``initialize_db`` console script we saw back in ``setup.py``.

.. code-block:: python

    # setup.py
    ...
    setup(
        ... # remember
        [console_scripts]
        initialize_db = learning_journal.scripts.initializedb:main
    )

That ``initialize_db`` command is tied to the ``main`` function in ``learning_journal/scripts/initializedb.py``, and will run that function when it is invoked. That function looks like this:

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

At a higher level, when ``main`` is called our Pyramid app will create a new ``MyModel`` instance and insert it into the database. In order to make that happen, it'll take a configuration file (held in the ``config_uri`` variable above) such as our ``development.ini`` and any options we may pass in.

``development.ini`` will tell Pyramid what to do when trying to initialize a database.

.. code-block:: ini
    
    # in development.ini
    [app:main]
    # ...
    sqlalchemy.url = sqlite:///%(here)s/learning_journal.sqlite

As mentioned before, this keyword tells Pyramid where to look for a database. Since we're currently using `SQLite <https://docs.python.org/2/library/sqlite3.html>`_, it'll create the database if one does not exist. It will not do that with ``PostGreSQL``. This string will replace "here" with your project root.

.. code-block:: ini

    # still in development.ini
    [logger_sqlalchemy]
    level = INFO
    handlers =
    qualname = sqlalchemy.engine

These lines provide guidelines for how verbose Pyramid will be when it creates your database. ``level = INFO`` means that it'll simply tell you what queries are being used. 

