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

Make sure to add ``tox`` to the required packages for testing.

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

Later on when we learn about `PostgreSQL <https://pypi.python.org/pypi/psycopg2>`_, we'll change value associated with this keyword to point to a Postgres database.

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
* **SQL Databases (sqlite, MySQL, PostgreSQL, Oracle, SQLServer, etc.)**

Any of these might be useful for certain types of applications. On the web the two most used are NoSQL and SQL. For viewing/interacting with individual objects, a NoSQL storage solution might be the best way to go. In systems with objects that are related to each other, SQL-based Relational Databases are the better choice. We'll work with the latter, particularly ``sqlite`` to start. Tomorrow we'll hit ``PostgreSQL``.

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

At a higher level, when ``main`` is called our Pyramid app will create a new ``MyModel`` instance and insert it into the database. 
To make that happen, it'll take a configuration file (held in the ``config_uri`` variable above) such as our ``development.ini`` and any options we may pass in.
``development.ini`` will tell Pyramid what to do when trying to initialize a database.

.. code-block:: ini
    
    # in development.ini
    [app:main]
    # ...
    sqlalchemy.url = sqlite:///%(here)s/learning_journal.sqlite

As mentioned before, this keyword tells Pyramid where to look for a database. 
Since we're currently using `SQLite <https://docs.python.org/2/library/sqlite3.html>`_, it'll create the database if one does not exist. 
This will not happen with ``PostgreSQL``. 
The string assigned to ``sqlalchemy.url`` will replace ``here`` with your project root.

.. code-block:: ini

    # still in development.ini
    [logger_sqlalchemy]
    level = INFO
    handlers =
    qualname = sqlalchemy.engine

These lines provide guidelines for how verbose Pyramid will be when it creates your database. 
``level = INFO`` means that it'll simply tell you what queries are being used.
This is great for development so that you know exactly what's going into and out of your database.
When in production, you want to set ``level = WARN``.

Let's return to ``learning_journal/scripts/initializedb.py``. 

.. code-block:: python

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

``engine`` is the connection to the database itself.
This ``engine`` gets used by ``Base.metadata.create_all`` to create all of the necessary tables in the database.
The information for those tables are of course stored in ``Base.metadata``.
The ``Base.metadata.create_all`` method will make sure to overlook any tables that have already been created.
This means that you should be able to add a new model to your Pyramid app without having to nuke your DB or overwrite existing tables.

.. code-block:: python

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        model = MyModel(name='one', value=1)
        dbsession.add(model)

This last bit of code isn't actually *necessary*. 
What it does is creates a database session and adds a new row that's an instance of the ``MyModel`` model.
It is in effect a way of checking that your database works the way that it's supposed to.
If this stays uncommented and you run ``initialize_db`` more than once, Pyramid will yell at you for trying to create a row that already exists.

Let's invoke ``initialize_db``.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ initialize_db development.ini
    2016-07-12 09:53:33,686 INFO  [sqlalchemy.engine.base.Engine:1192][MainThread] SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    ...
    2016-07-12 09:53:33,705 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    2016-07-12 09:53:33,708 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] 
    CREATE TABLE models (
        id INTEGER NOT NULL, 
        name TEXT, 
        value INTEGER, 
        CONSTRAINT pk_models PRIMARY KEY (id)
    )
    ...
    2016-07-12 09:53:33,719 INFO  [sqlalchemy.engine.base.Engine:686][MainThread] COMMIT

So what happened here? 

- Not visible in the stdout log messages, but the ``learning_journal.sqlite`` file was created in our project root.
- We created a table called ``models`` in our sqlite database, with columns ``id``, ``name``, and ``value``.
- We committed that creation to the database, effectively saving it.
- We created an index on the ``models`` table using its ``name`` column and committed that.
- We then created a new row, inserting a new ``MyModel`` instance into the table and committing that.

Now that we have our database hooked up to our models, we can view the site at http://localhost:6543/.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini --reload

It works enough to be viewed, but it's a scaffold so it's empty inside.
Let's fill it with some data.

Interacting with SQLAlchemy Models and the ORM
----------------------------------------------

We can investigate and manipulate our models from the interpreter pretty easily.
Let's fire up ``pshell`` and explore for a moment to see what we have at our disposal.

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

We had used ``pshell`` before to work with ``BeautifulSoup``, but we hadn't really looked at what ``pshell`` had to offer.
The ``environment`` created by ``pshell`` provides us with a few useful tools seen above:

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
    2016-07-12 10:19:02,254 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value 
    FROM models
    2016-07-12 10:19:02,254 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    Out[6]: [<learning_journal.models.mymodel.MyModel at 0x1054fe470>]

We've stolen a lot of this from the ``initializedb.py`` script. 
Any persisting interaction with the database requires a ``session``. 
This object *represents* the active, current connection to the database. 
All database queries are phrased as methods of the session.

.. code-block:: ipython

    In [7]: query = session.query(MyModel)
    In [8]: type(query)
    Out[8]: sqlalchemy.orm.query.Query

The ``query`` method of the session object returns a ``Query`` object. 
Arguments to the ``query`` method can be a *model* class or even *columns* from a model class.
Query objects are themselves iterable, with the result depending on the args you passed.

.. code-block:: ipython 

    In [9]: query1 = session.query(MyModel)
    In [10]: for row in query1:
       ....:     print(row)
       ....:     print(type(row))
       ....:     
    2016-07-12 10:22:32,165 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value 
    FROM models
    2016-07-12 10:22:32,166 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()

    # above this mark are the two lines representing SQL commands that retreive our data

    <learning_journal.models.mymodel.MyModel object at 0x1054fe470>
    <class 'learning_journal.models.mymodel.MyModel'>

    # these two lines are the result of the for loop

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
    2016-07-12 10:24:33,866 INFO  [sqlalchemy.engine.base.Engine:1097][MainThread] SELECT models.name AS models_name, models.id AS models_id, models.value AS models_value 
    FROM models
    2016-07-12 10:24:33,868 INFO  [sqlalchemy.engine.base.Engine:1100][MainThread] ()
    one
    <class 'str'>
    1
    <class 'int'>
    1
    <class 'int'>

We can see the SQL query on its own by looking at its string representation.

.. code-block:: ipython 

    In [13]: str(query1)
    Out[13]: 'SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value \nFROM models'

    In [14]: str(query2)
    Out[14]: 'SELECT models.name AS models_name, models.id AS models_id, models.value AS models_value \nFROM models'

You can use this to check that the query the ORM is constructing looks like what you expect. 
It can be very helpful for testing and debugging.

The methods of the ``Query`` object roughly fall into two categories:

1. Methods that return a new ``Query`` object
2. Methods that return *scalar* values or *model instances*
   
Let's start by looking quickly at a few methods from the second category. 

Methods Returning Values & Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A good example of this category of methods is ``get``, which returns one model instance only.
It takes a primary key as an argument:

.. code-block:: ipython 

    In [15]: session.query(MyModel).get(1)
    Out[15]: <learning_journal.models.mymodel.MyModel at 0x105546080>

    In [16]: session.query(MyModel).get(10)
    In [17]:

If no item with that primary key is present, then the method returns ``None``. 
Another example is one we've already seen. 
``query.all()`` returns a list of all rows matching the given query.

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

    In [25]: new_data = []
    In [26]: for name, val in [('bob', 34), ('tom', 13)]:
       ....:     new_data.append(MyModel(name=name, value=val))
       ....:

    In [27]: session.add_all(new_data)
    In [28]: session.new
    Out[28]: Out[37]: IdentitySet([<learning_journal.models.mymodel.MyModel object at 0x1055e3048>, <learning_journal.models.mymodel.MyModel object at 0x1053f8710>, <learning_journal.models.mymodel.MyModel object at 0x1055cb390>])

Up until now, the changes you've made are not permanent. 
They're recognized by your session, but they haven't been saved into the database. 
Just like we saw when we initialized the database, our current session must be **committed**.

.. code-block:: ipython 

    In [29]: other_session = Session()
    In [30]: other_session.query(MyModel).count()
    Out[30]: 1

Notice how this new DB session is completely unaware of the "changes" we've made.

.. code-block:: ipython

    In [31]: session.commit()
    In [32]: other_session.query(MyModel).count()
    Out[32]: 4

And now they're seen, as ``other_session``'s query is looking directly at the database when it queries.

When you are using a ``scoped_session`` in Pyramid, this action is automatically handled for you. 
The session that is bound to a particular HTTP request is committed when a response is sent back.

You can edit objects that are already part of a session, or that are fetched by a query.
Simply change the values of a persisted attribute, the session will know it's been updated:

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

Returning to query methods, a good example of the second type is the ``filter`` method.
This method allows you to reduce the number of results, based on criteria:

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

Note that you can do this inline as well (``Session.query(MyModel).filter(MyModel.value < 20).order_by(MyModel.name)``). 
Also note that when using chained queries like this, no query is actually sent to the database until you require a result.

Testing Models
==============

Look at the code in ``learning_journal/tests/tests.py``.
Notice that the tests are pretty significantly different.
A ``BaseTest`` class is declared that sets up the app and initializes a connection to the database. 
Other tests then inherit from this class to reduce repeating code.

Notice also that the ``tearDown`` method is actually useful.

.. code-block:: python

    def tearDown(self):
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)

Your tests will need to access and save data to the database to ensure all things are wired correctly.
You however do not want to save any of the data that you generate during testing.
At the end of your tests, drop all your changes.

``TestMyViewSuccessCondition`` initializes a new instance of the ``MyModel`` class and adds it to the session. 
The app then tests for the existence of this model in the ``response`` from the available view.

Connecting "M" to "VC"
======================

We now have four instances of ``MyModel`` in our database.
We should be able to see them on our site, and the way to make that happen is through Views.
Our scaffold already has a View in ``learning_journal/views/default.py`` accessing the DB and returning one of the model instances.

.. code-block:: python
    
    # ...
    from ..models import MyModel


    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def my_view(request):
        try:
            query = request.dbsession.query(MyModel)
            one = query.filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)
        return {'one': one, 'project': 'learning_journal'}

Notice that the database session is attached to the request object. 
That way, we don't need to create a new session as we did in the interpreter.
We refine the query to select only one model instance, and we then provide that instance to the template through the keyword ``one``.

Let's edit our template to display that object, and view our site again in the browser.

.. code-block:: html

    <!-- templates/mytemplate.jinja2 -->
    {% extends "layout.jinja2" %}

    {% block content %}
    <div class="content">
      <h1><span class="font-semi-bold">Pyramid</span> <span class="smaller">Alchemy scaffold</span></h1>
      <p class="lead">Welcome to <span class="font-normal">{{project}}</span>, an&nbsp;application generated&nbsp;by<br>the <span class="font-normal">Pyramid Web Framework 1.7</span>.</p>

      <!-- ADD THE NEXT TWO LINES BELOW-->

      <h2>This is the first Model instance we've made</h2>
      <p>{{one}}</p>

      <!-- THIS IS THE END OF OUR EDIT -->

    </div>
    {% endblock content %}

Notice that since ``one`` is an *Object*, we see the string representation of that object in the page.
If we want to see the actual attributes of the object, e.g. "name" or "value", we'd have to use ``one.name`` or ``one.value`` in the template.

Working with Forms in Pyramid
=============================

The whole point of creating a model is so that we can persist data across sessions.
However, how can we add new data if there is no interface in our web app that allows us to add new model instances? 
Forms allow for user input, and we can use the ``request`` method in a view to handle that input and create new data.

Let's create a template called ``edit-model.jinja2``.

.. code-block:: html

    {% extends "layout.jinja2" %}

    {% block content %}
    <div class="content">
        {% if data %}        
        <h1>{{ data.name }}</h1>
        {% endif %}
        <form action="{{ request.route_url('edit') }}" method="POST">
            <label for="name">New Instance Name: </label><br/>
            <input type="text" name="name"/><br/>
            <input type="submit" value="Submit"/>
        </form>
    </div>
    {% endblock content %}

We want to add data to our app and not just get data from our app.
Thus, the method on our form needs to be a ``POST`` method.

Let's also create the route that we intend to use.

.. code-block:: python

    # in routes.py

    def includeme(config):
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('home', '/')
        config.add_route('edit', '/edit')

And lets connect it to an appropriate view.

.. code-block:: python

    # in views/default.py

    @view_config(route_name="edit", renderer="../templates/edit-model.jinja2")
    def edit_view(request):
        return {"data": {"name": "A new form"}}

And because we've made some significant changes, reinstall the package.
Then start up the server and look at the page.

Here we have a simple form. 
We can fill out the input field and submit it, and the data that we sent goes...absolutely nowhere.
We can check our database and see that nothing new has been added.

.. code-block:: ipython

    In [1]: from learning_journal.models import get_engine, MyModel
    In [2]: engine = get_engine(registry.settings) # default prefixes are 'sqlalchemy.'
    In [3]: from sqlalchemy.orm import sessionmaker
    In [4]: Session = sessionmaker(bind=engine)
    In [5]: session = Session()
    In [6]: session.query(MyModel).count()
    Out[6]: 4

We need to configure our view such that it can do more than just display the form.
We need it to take the data submitted in the form and do something with it.
Let's get a hold on the data first.
For this we need to look at the ``request`` object.

We can inspect the ``request`` object in our interpreter and see it has tons of attributes and methods.

.. code-block:: ipython

    In [7]: request.
    Display all 120 possibilities? (y or n)
    request.GET                          request.is_body_seekable
    request.POST                         request.is_response
    ...                                  ...

If you submit a form, the data in the form will be a part of the ``method`` it was submitted with.
Whether it's a ``GET`` or a ``POST`` method, that data will come out in the form of a ``MultiDict`` object.
For our purposes it acts the same as a Python dictionary.
With the ``GET`` or ``POST`` multidict, the **name** of the form field will be a **key** in the multidict.

The ``request`` object also has an attribute called ``.method`` that holds the type of HTTP method used to call up the page. 
Note that no matter what, when we first load the page it'll be with a ``GET`` request. 
The only time we have a ``POST`` request is when we submit a form.

Knowing this, we can reconfigure our ``edit_view`` function to handle a first-rendering of the page, as well as a separate rendering if a form is submitted.

.. code-block:: python

    @view_config(route_name='edit', renderer="../templates/edit-model.jinja2")
    def edit_view(request):
        data = {"name": "A new form"}
        if request.method == "POST":
            data["name"] = request.POST["name"]

        return {"data": data}

Now when we load our edit page and submit a form with some data, that new data shows up right in the ``<h1>``.

Tonight you'll use the fact that you can harvest form data in a view to add new model instances to your site.

Recap
=====

Today handled a ton.
First, we spun up an entirely new scaffold in order to incorporate SQLAlchemy into our Pyramid app. 
We walked through all the parts of the Pyramid scaffold that were new, and saw specifically what parts of our Pyramid app included connections to the database.

We then went on to talk about data models. 
We saw how Pyramid converts model attributes to data for the database, and used the interpreter to persist that data across separate sessions. 
Most notably, we saw that while changes may be made with models being created and/or deleted, nothing persists without commitment.

We also saw how to test models, with significant changes in how we built up a test suite.
We have to now not only use an instance of our app. 
We must also call up a database session so that we can test models along with our view and fully functional Pyramid app.

Finally, we connected our "Models" to the "View" and "Controller" pieces of our Pyramid app. 
We created a template that uses a form to take user input, as well as a view that handles form data.
We investigated the ``request`` object in greater detail, seeing that its ``.method``, ``.POST``, and ``.GET`` attributes can allow us to produce different outputs on the same view and template.

Tonight you will use this new scaffold to add some persistence to your deployed Learning Journal by creating a data model for your learning journal entries.
You'll wire it all together with appropriate templates and views.
You'll also write a battery of tests, showing that your app can persist data in addition to the unit tests and functional tests you're already writing.

Coming up tomorrow: an introduction to ``PostgreSQL`` that allows us to persist data on a deployed Heroku site, and how we can use environment variables to hold all of our secret secrets.

