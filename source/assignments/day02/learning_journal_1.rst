*******************************
Python Learning Journal: Step 1
*******************************

In this tutorial we will begin the process of creating an online learning
journal using Python and the `Pyramid web framework`_.

The walk-through is intended to get you to a working application as quickly as
possible. There will be many questions left unanswered as we proceed. Fear not.
The answers will come as this course progresses. For now, simply focus on the
process and getting to a working application.

.. _Pyramid web framework: http://www.pylonsproject.org

Prerequisites
=============

In order to follow this tutorial, you will need to have several tools in place
before you begin.

1. `Python 2.7.x`_
2. `Virtualenv and Virtualenvwrapper`_ installed and properly configured
3. The `PostgreSQL Database Engine`_ installed and properly configured
4. A c compiler and Python development headers
5. An account with `GitHub`_
6. An account with `Heroku`_ (and the heroku toolbelt installed)

.. _Heroku: https://heroku.com

.. _GitHub: https://github.com
.. _PostgreSQL Database Engine: https://www.codefellows.org/blogs/how-to-install-postgresql
.. _Virtualenv and Virtualenvwrapper: ../../lectures/day01/virtualenv.html
.. _Python 2.7.x: https://www.python.org/download/


Create Your Environment
=======================

If all the pieces are in place, you are ready to proceed to the next level.


Set Up the Project Environment
------------------------------

Since you've installed and configured ``virtualenv`` and ``virtualenvwrapper``
properly, this step is simple. Open a command shell and type the following:

.. code-block:: bash

    $ mkproject learning_journal

You should see output that looks like this (though your prompt and path names
will look different):

.. code-block:: bash

    192:~ cewing$ mkproject learning_journal
    New python executable in learning_journal/bin/python
    Installing setuptools, pip...done.
    Creating /Users/cewing/projects/learning_journal
    Setting project for learning_journal to /Users/cewing/projects/learning_journal
    [learning_journal]
    192:learning_journal cewing$

This command will do a couple of things for you:

* create a new Python virtual environment called ``learning_journal`` in your
  configured ``$WORKON_HOME``
* install ``pip`` and ``setuptools`` in the new environment
* activate the new environment
* create a new project directory called ``learning_journal`` in your configured
  ``$PROJECT_HOME``
* change your current working directory to the new project directory

Now you have a clean and isolated environment in which to do your work.


Create a GitHub Project Repository
----------------------------------

Open a web browser and go to `GitHub`_. If you are not logged in, do so.

At the top left, find the small ``+`` icon next to your name and click it.
Select **New Repository** from the drop-down menu.

A form will load, allowing you to enter some information about your new
repository. 

.. image:: /_static/learning_journal_repo_setup.png
    :width: 90%

Enter the following values:

Repository Name:
  ``learning_journal``

Description:
  A lightweight Pyramid web journal.

Leave the new repository as **Public**

Check the box for initializing the repository with a README.

Select a Python ``.gitignore`` file from the first drop-down at the bottom.

Choose a reasonable license from the second drop-down (I used MIT).

Finally, click the **Create Repository** button.

.. _GitHub: https://github.com


Clone Your Repository
---------------------

Now that you have a repository for the application you will be writing, you'll
want to get a copy of that code to your local machine.

On ``GitHub``, while looking at your newly created repository, find the URL for
cloning your repository at the bottom of the menu on the right-hand side of the
page.

.. image:: /_static/learning_journal_clone_url.png
    :width: 35%

There are two versions of this URL, one for HTTPS and the other for SSH.

If you have `set up public key authentication`_ for your GitHub account (and
you really, really should), you will want to copy the SSH version of the URL.
Otherwise, you'll need to copy the HTTPS version.

.. _set up public key authentication: https://help.github.com/articles/generating-ssh-keys

Back in your terminal, make sure you are in your ``learning_journal`` project
directory:

.. code-block:: bash

    192:learning_journal cewing$ pwd
    /Users/cewing/projects/learning_journal
    [learning_journal]
    192:learning_journal cewing$

Then, use the ``git clone`` command to make a local copy of your new repository:

.. code-block:: bash

    [learning_journal]
    192:learning_journal cewing$ git clone <paste-your-copied-github-url-here>

Once that is complete, you should have a new directory called
``learning_journal`` inside the project directory you created earlier.  Your
filesystem should look something like this::

.. code-block:: bash

    [learning_journal]
    heffalump:learning_journal cewing$ tree -a -I .git .
    .                       # <- Your project directory
    └── learning_journal    # <- Your repository root
        ├── .gitignore      # <- Initial files from GitHub
        ├── LICENSE
        └── README.md


Create a Branch for Today's Work
--------------------------------

We want to maintain a clean ``master`` branch in our repository.  Any work you
do on adding features to a project should be done on a branch, evaluated and
tested there, and only merged to master once the work is complete.

To create a branch called ``step1`` for todays work, follow these steps:


.. code-block:: bash

    [learning_journal]
    192:learning_journal cewing$ cd learning_journal/
    [learning_journal]
    [master=]
    192:learning_journal cewing$ git branch
    * master
    [learning_journal]
    [master=]
    192:learning_journal cewing$ git checkout -b step1
    Switched to a new branch 'step1'
    [learning_journal]
    [step1]
    192:learning_journal cewing$ git branch
      master
    * step1

You have created and checked out a new branch called ``step1``. You'll do your
day's work here.

This new branch exists only on your local machine. When you finish today's
assignment you'll need to push this branch up to your GitHub repository. More
on that later.


Install Required Software
-------------------------

Before we begin, we'll need to install some Python packages to get the tools
we'll need to complete our project.

Make sure that your ``learning_journal`` virtual environment is active, and
that the ``pip`` command points to that environment (note the
``learning_journal`` in the pathname below):

.. code-block:: bash

    [learning_journal]
    192:learning_journal cewing$ which pip
    /Users/cewing/virtualenvs/learning_journal/bin/pip

Using the ``pip`` command, install the required software as follows:

.. code-block:: bash

    [learning_journal]
    192:learning_journal cewing$ pip install pyramid psycopg2 waitress
    Downloading/unpacking pyramid
    ...
    Successfully installed pyramid psycopg2 zope.interface translationstring PasteDeploy WebOb repoze.lru zope.deprecation venusian waitress
    Cleaning up...

If you are using Mac OS X you may see an error when installing Python code with
C extensions (like ``psycopg2``)::

.. code-block:: bash

    clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

If you see this, you may need to `follow the instructions here`_ due to a
issue in how the OS X command-line c compiler is configured.

.. _follow the instructions here: http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa


Preserve Your Installed Dependencies
------------------------------------

In order to make it easier to work with others, you want to create a record of
the additional packages you've installed.  You'll use ``pip`` to do that:

.. code-block:: bash

    [learning_journal]
    [step1]
    192:learning_journal cewing$ pip freeze > requirements.txt

Add that new file to your repository on this branch and commit the changes
locally:

.. code-block:: bash

    [learning_journal]
    [step1]
    192:learning_journal cewing$ git add requirements.txt
    [learning_journal]
    [step1]
    192:learning_journal cewing$ git commit -m "add a requirements file"
    [learning_journal]
    [step1]
    192:learning_journal cewing$ git status
    On branch step1
    nothing to commit, working directory clean

After creating this new file, you're file system layout should look like this::

    ./learning_journal/
    └── learning_journal
        ├── .gitignore
        ├── LICENSE
        ├── README.md
        └──  requirements.txt

Don't forget to add ``requirements.txt`` to your repository and commit your
changes.


Create a Database
-----------------

Finally, in order to preserve the journal entries you'll write throughout the
class, you'll need to have a database. You can use the ``createdb`` command
provided by ``PostgreSQL`` to accomplish this task. For development purposes it
is fine for you to own the database yourself.

Make sure that your database engine is running and then issue the following
command:

.. code-block:: bash

    [learning_journal]
    [step1]
    192:projects cewing$ createdb learning_journal


Building the Data Layer
=======================

You'll start your learning journal by building the data layer.  This layer of
the application will be responsible for persisting entries to and retrieving
entries from the database you just created.

The ``entries`` Table
---------------------

You need first to define what an *entry* for our microblog might look like.
Keep it simple for now.

In your ``learning_journal`` repository root, right where you see
``README.md``, add a new file called ``journal.py``.  In it, add the following
lines:



.. code-block:: python

    # -*- coding: utf-8 -*-

    DB_SCHEMA = """
    CREATE TABLE IF NOT EXISTS entries (
        id serial PRIMARY KEY,
        title VARCHAR (127) NOT NULL,
        text TEXT NOT NULL,
        created TIMESTAMP NOT NULL
    )
    """

This will create a single database table called ``entries`` that has four
columns.  There will be a primary key, a title and some text, and a ``created``
column that will hold a timestamp.

The App Skeleton
----------------

We'll also need a basic Pyramid app skeleton to work from.

Still in ``journal.py``, add the following:

.. code-block:: python

    # add this at the top, just below the 'coding' line
    import os
    import logging
    from pyramid.config import Configurator
    from pyramid.session import SignedCookieSessionFactory
    from pyramid.view import view_config
    from waitress import serve

    # add this just below the SQL table definition we just created
    logging.basicConfig()
    log = logging.getLogger(__file__)


    @view_config(route_name='home', renderer='string')
    def home(request):
        return "Hello World"


    if __name__ == '__main__':
        # configuration settings
        settings = {}
        settings['reload_all'] = True
        settings['debug_all'] = True
        # secret value for session signing:
        secret = os.environ.get('JOURNAL_SESSION_SECRET', 'itsaseekrit')
        session_factory = SignedCookieSessionFactory(secret)
        # configuration setup
        config = Configurator(
            settings=settings,
            session_factory=session_factory
        )
        config.add_route('home', '/')
        config.scan()
        # serve app
        app = config.make_wsgi_app()
        port = os.environ.get('PORT', 5000)
        serve(app, host='0.0.0.0', port=port)



App Configuration
-----------------

For any but the most trivial applications, you'll need configuration. It's a
way of letting your app know about the world around it.

In your case, you have one thing you need to configure: a way to connect to the
database.

Pyramid gives many options for dealing with configuration, but in this case you
are going to set values directly in the ``settings`` dictionary. Add the
following to your ``journal.py``:

.. code-block:: python

    # in the "if name == __main__:" block:
    settings['reload_all'] = True # <- ALREADY THERE
    settings['debug_all'] = True # <- ALREADY THERE
    # ADD THIS
    settings['db'] = os.environ.get(
        'DATABASE_URL', 'dbname=learning_journal user=cewing'
    )

In your own project, you won't want to use my name, but rather the name of the
user on your local server who will connect to the database. Other values such
as a password may be required in order to make this work. This value is called
a ``libpq connection string`` and you can `read more about it`_ and
`how it is used to make a connection to the database`_.

.. _how it is used to make a connection to the database: http://initd.org/psycopg/docs/module.html
.. _read more about it: http://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-CONNSTRING`


Initialize the Database
-----------------------

Now that you have an app skeleton and the configuration you require, you are
ready to initialize the database. Above, you created an empty database using
the ``createdb`` command. Initializing it will create the required table and
index needed to store your journal entries.

The first step is to connect to the database. You'll add a function that opens
a connection and returns it for use by other functions. In ``journal.py`` add
the following code:

.. code-block:: python

    # add this up at the top
    import psycopg2

    # add this function before the "if __name__ == '__main__':" block
    def connect_db(settings):
        """Return a connection to the configured database"""
        return psycopg2.connect(settings['db'])


Now that you can get an open connection to the database, you'll set up a
function that can initialize the database by running the SQL you added above.
Add this code to ``journal.py`` next:

.. code-block:: python

    # add this import at the top
    from contextlib import closing

    # add this function after the connect_db function
    def init_db():
        """Create database dables defined by DB_SCHEMA

        Warning: This function will not update existing table definitions
        """
        settings = {}
        settings['db'] = os.environ.get(
            'DATABASE_URL', 'dbname=learning_journal user=cewing'
        )
        with closing(connect_db(settings)) as db:
            db.cursor().execute(DB_SCHEMA)
            db.commit()


You'll need to have a working database for our app, so go ahead and run this
function "in real life". With your project virtual environment active, fire up
a python interpreter:

.. code-block:: bash

    [learning_journal]
    [step1 *]
    192:learning_journal cewing$ python
    Python 2.7.5 (default, Mar  9 2014, 22:15:05)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Then, at the prompt, import your app to set up the configuration, and run the
``init_db`` function:

.. code-block:: pycon

    >>> from journal import init_db
    >>> init_db()
    >>>

If that function returns silently, you've succeeded. Exit the interpreter with
``^D``.

Next, take a look at the database directly. Use the ``psql`` command to open an
interactive session with your database:

.. code-block:: bash

    [learning_journal]
    [step1 *]
    192:learning_journal cewing$ psql -U cewing -d learning_journal
    psql (9.3.2)
    Type "help" for help.

    learning_journal=#

Again, you may require more, or different connection parameters to connect to
your database.

Use the ``\d`` command in the psql shell to see a list of the *relations* in
your database:

.. code-block:: psql

    learning_journal=# \d
                  List of relations
     Schema |      Name      |   Type   | Owner
    --------+----------------+----------+--------
     public | entries        | table    | cewing
     public | entries_id_seq | sequence | cewing
    (2 rows)

You can provide a table name argument to that command to see the information
about the ``entries`` table

.. code-block:: psql

    learning_journal=# \d entries
                                        Table "public.entries"
     Column  |            Type             |                      Modifiers
    ---------+-----------------------------+------------------------------------------------------
     id      | integer                     | not null default nextval('entries_id_seq'::regclass)
     title   | character varying(127)      | not null
     text    | text                        | not null
     created | timestamp without time zone | not null
    Indexes:
        "entries_pkey" PRIMARY KEY, btree (id)

If your results look more-or-less like this, then you've succeeded. Now it is
time to connect this app to Heroku.


App Deployment
==============

You are going to put your learning journal online using `Heroku`_, a service
that simplifies deploying web applications in a number of languages.

Moving on from here assumes that you have already created a Heroku account,
downloaded and installed the toolbelt, and successfully logged in to Heroku
from your command line. If that is not the case. Please `follow this tutorial`_
to get up to speed. You only need to do the first two steps (Introduction and
Set up)

.. _follow this tutorial: https://devcenter.heroku.com/articles/quickstart
.. _Heroku: https://heroku.com


Add a Procfile
--------------

Heroku uses a standard file to control how your app is built and served. This
file **must** be named ``Procfile`` (and capitalization counts). Go ahead and
create a new file by that name in your journal repository root.

Now your filesystem should look like this::

    learning_journal
    └── learning_journal
        ├── .gitignore
        ├── LICENSE
        ├── Procfile
        ├── README.md
        ├── journal.py
        └── requirements.txt

In your new ``Procfile``, type the following line of code:

.. code-block:: text

    web: python journal.py

This tells heroku that you will be running a ``web`` service and that the
service will be provided by executing the ``python journal.py``.

Once you've got that created, you should be able to use ``foreman``, provided
by the Heroku Toolbelt, to start up your application:

.. code-block:: bash

    [learning_journal]
    [step1]
    192:learning_journal cewing$ foreman start
    23:26:33 web.1  | started with pid 68019

With that process running in your terminal, start up your web browser and load
``http://127.0.0.1:5000``.  You should be able to see this:

.. image:: /_static/learning_journal_helloworld.png
    :width: 90%

If you do, then your ``Procfile`` is correct, and you are ready to go.


Submit a Pull Request
---------------------

For the class submission process, you will use GitHub pull requests. This
allows your instructors and TAs to easily find the work you did for any given
assignment.

Before you can make a pull request, you must first push the branch you created
for this assignment up to GitHub.  In your terminal, from inside your
``learning_journal`` repository, take the following steps:

.. code-block:: bash

    [learning_journal]
    [step1]
    192:learning_journal cewing$ git push -u origin step1
    Counting objects: 32, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (23/23), done.
    Writing objects: 100% (23/23), 3.41 KiB | 0 bytes/s, done.
    Total 23 (delta 14), reused 0 (delta 0)
    To git@github.com:cewing/learning_journal.git
     * [new branch]      step1 -> step1
    Branch step1 set up to track remote branch step1 from origin.
    [learning_journal]
    [step1=]
    192:learning_journal cewing$

Now, open a web browser and point it at your ``learning_journal`` repository in
GitHub.

On the right side of the homepage, find the **Pull Requests** menu item and
click it.

.. image:: /_static/lj_pull_request_menu.png
    :width: 35%

The page that opens should have a big green button for creating a new pull
request.  Click it.


.. image:: /_static/lj_new_pull_request.png
    :width: 90%

Next, in the page that opens, choose your ``master`` branch as the base and
your ``step1`` branch to compare (You may have to click an **edit** button in
the grey area to be able to change what is automatically selected).

.. image:: /_static/lj_editing_pull_request.png

When you have the right values selected, go ahead and click the big green
button to create your pull request.

Copy the URL for that pull request and use it to submit this assignment in
Canvas.

Merge to Master
---------------

Heroku prefers you to deploy from your ``master`` branch. That makes sense.
It's in keeping with standard gitflow to have ``master`` be the deployable
branch in your repository.

You've been doing your work on a branch, ``step1``.  Now that you are ready to
deploy, it's time to merge that work.

Make sure that you've committed and pushed all your work to-date before you
take this next set of actions.

When all is squared away, in your terminal, type the following:


.. code-block:: bash

    [learning_journal]
    [step1=]
    192:learning_journal cewing$ git checkout master
    Switched to branch 'master'
    Your branch is up-to-date with 'origin/master'.
    [learning_journal]
    [master=]
    192:learning_journal cewing$ git merge step1
    Adding journal.py
    Adding Procfile
    [master 179e695] Merge branch 'step1'
    192:learning_journal cewing$ git status
    On branch master
    Your branch is ahead of 'origin/master' by 7 commits.
      (use "git push" to publish your local commits)

    nothing to commit, working directory clean
    [learning_journal]
    [master>]
    192:learning_journal cewing$ git push origin master
    Counting objects: 7, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 342 bytes | 0 bytes/s, done.
    Total 3 (delta 2), reused 0 (delta 0)
    To git@github.com:cewing/learning_journal.git
       0774bf1..179e695  master -> master

By merging locally and then pushing, you have just closed the pull request you
opened a moment ago.  That's okay. It is still available for viewing and
comments, and that was the point of it.

At this point, then you have merged your ``step1`` work back into ``master``
and are ready to deploy your code.

Create a Heroku App
-------------------

The first step in deployment is to create a Heroku app to which you can deploy.
Use the ``create`` command from the Heroku toolbelt to accomplish this:

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ heroku create
    Creating fizzy-fairy-1234... done, stack is cedar
    http://fizzy-fairy-1234.herokuapp.com/ | git@heroku.com:fizzy-fairy-1234.git
    Git remote heroku added

This accomplishes a few things.  First, a special ``heroku`` remote is added to
your git repository.  You can see this:

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ git remote -v
    heroku  git@heroku.com:fizzy-fairy-1234.git (fetch)
    heroku  git@heroku.com:fizzy-fairy-1234.git (push)
    origin  git@github.com:cewing/learning_journal.git (fetch)
    origin  git@github.com:cewing/learning_journal.git (push)

Notice that the URL for this new remote is the same as the subdomain name
Heroku assigned to your app. You *can* control what this name is, but there's
no real need as you will be pointing your own URL at the app soon enough.  The
goofy names automatically created are just fine. for now.

Second, a place is created in Heroku's infrastructure for your application to
live.  When you push to the heroku remote, your app will be uploaded, built and
deployed so that it is visible online.

Before we're ready to do that, though we have to do one more thing.


Add PostgreSQL to Heroku
------------------------

Heroku provides a number of different options for data stores. In order to use
any of them, you'll need to set them up. Our app is designed to use PostgreSQL,
so we need to set up the Heroku add-on that allows us to use that database in
deployment. The Heroku toolbelt provides a command for this as well:

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ heroku addons:add heroku-postgresql:dev
    Adding heroku-postgresql:dev on fizzy-fairy-1234... done, v4 (free)
    Attached as HEROKU_POSTGRESQL_ONYX_URL
    Database has been created and is available
     ! This database is empty. If upgrading, you can transfer
     ! data from another database with pgbackups:restore.
    Use `heroku addons:docs heroku-postgresql` to view documentation.

Now our app on Heroku is set up to use a PostgreSQL database. A URL has been
created for us to connect to. The connection string is stored on Heroku as
``HEROKU_POSTGRESQL_ONYX_URL`` (yours will be different).

Our app expects something called ``DATABASE_URL`` to exist in our environment.
The Heroku toolbelt provides another tool that allows us to connect the value
they have us to the name we require.  Again, type this at your command line
(and don't forget to use *your* database color):

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ heroku pg:promote HEROKU_POSTGRESQL_ONYX_URL
    Promoting HEROKU_POSTGRESQL_ONYX_URL (DATABASE_URL) to DATABASE_URL... done

Great, now the connection URL for your Heroku database is available in the
environment variable you are expecting. That's it.  You're ready to deploy.


Deploy to Heroku
----------------

To deploy, simply use ``git`` to push your master branch to the ``heroku``
remote:

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ git push heroku master
    Initializing repository, done.
    Counting objects: 79, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (52/52), done.
    Writing objects: 100% (79/79), 11.37 KiB | 0 bytes/s, done.
    Total 79 (delta 37), reused 55 (delta 24)

    -----> Python app detected
    -----> No runtime.txt provided; assuming python-2.7.6.
    -----> Preparing Python runtime (python-2.7.6)
    -----> Installing Setuptools (2.1)
    -----> Installing Pip (1.5.4)
    -----> Installing dependencies using Pip (1.5.4)
           Downloading/unpacking Flask==0.10.1 (from -r requirements.txt (line 1))

           ....

           Successfully installed Flask Jinja2 MarkupSafe Werkzeug gunicorn itsdangerous psycopg2
           Cleaning up...
    -----> Discovering process types
           Procfile declares types -> web

    -----> Compressing... done, 31.5MB
    -----> Launching... done, v5
           http://fizzy-fairy-1234.herokuapp.com/ deployed to Heroku

    To git@heroku.com:fizzy-fairy-1234.git
     * [new branch]      master -> master

Load up the URL above (the one that was "deployed to Heroku").  You should see
your "Hello world!".

If you do, then hoorah.  All that remains is to initialize your database on
Heroku.

You can attach to a Python terminal running in your deployed environment using
the Heroku toolbelt:

.. code-block:: bash

    [learning_journal]
    [master=]
    192:learning_journal cewing$ heroku run python
    Running `python` attached to terminal... up, run.8229
    Python 2.7.6 (default, Jan 16 2014, 02:39:37)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

From there, it's just like what you did locally a short while ago:

.. code-block:: pycon

    >>> from journal import app
    >>> from journal import init_db
    >>> init_db()
    >>>

Use the standard ``^D`` to detatch from the terminal.

You may wish to verify that your initialization worked.  You can use the
``heroku pg`` command to connect to the database directly with ``psql``:

.. code-block:: bash

    [learning_journal]
    [master=]
    heffalump:learning_journal cewing$ heroku pg:psql
    ---> Connecting to HEROKU_POSTGRESQL_RED_URL (DATABASE_URL)
    psql (9.3.2, server 9.3.5)
    SSL connection (cipher: DHE-RSA-AES256-SHA, bits: 256)
    Type "help" for help.

    evening-brushlands-7955::RED=> \d
                      List of relations
     Schema |      Name      |   Type   |     Owner
    --------+----------------+----------+----------------
     public | entries        | table    | kaplujiadphtmg
     public | entries_id_seq | sequence | kaplujiadphtmg
    (2 rows)

    evening-brushlands-7955::RED=> \d entries
                                        Table "public.entries"
     Column  |            Type             |                      Modifiers
    ---------+-----------------------------+------------------------------------------------------
     id      | integer                     | not null default nextval('entries_id_seq'::regclass)
     title   | character varying(127)      | not null
     text    | text                        | not null
     created | timestamp without time zone | not null
    Indexes:
        "entries_pkey" PRIMARY KEY, btree (id)


This shows that your database does in fact have the ``entries`` table, and the
table is correctly configured. At this point you're safely done for the day.
Good work!

