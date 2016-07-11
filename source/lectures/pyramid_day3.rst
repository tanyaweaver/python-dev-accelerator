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

This project root directory will have the same named files that we've come to know and love in our Pyramid app, however some of the interior has changed. Let's inspect ``setup.py``.

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
* ``transaction`` - 