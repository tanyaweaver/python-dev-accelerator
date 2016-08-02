===========================================
PostgreSQL and Working With the Environment 
===========================================

Thus far we've been able to add user input and view that input in the browser with templating.
Persisting data has been addressed to a point, but using Heroku gives us a different problem.
While data may persist for a given Heroku push, every sqlite database is saved on the file system.
Heroku uses an `ephemeral filesystem <https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem>`_.
At best, your sqlite database may last 24 hours.

Heroku `provides support <https://www.heroku.com/postgres>`_ for a persisted PostgreSQL database. 
Since we're deploying to Heroku, why not use that?

As we will see, Postgres uses *basically* the same language as sqlite3.
So integration into our app should be *pretty* straightforward.


PostgreSQL
===========

`PostgreSQL <https://www.postgresql.org/about/>`_ is an open-source object-relational database management system (ORDBMS).
It's available across most major platforms, and has a reputation for security and reliability.
Due to the large open-source community contributing to the project, it's also frequently maintained.
Not to mention, it's free.


Installation
------------

Heroku conveniently includes Postgres `as an add-on <https://www.heroku.com/postgres>`_.
Python also generously lets you ``pip install`` a package that interacts with a Postgres database.
We, however, still need to install it to our machines.

Installation is simple from the command line.
If you don't yet have Homebrew, download it `here <http://brew.sh/>`_.
Once you have Homebrew, the following command gives you all you need.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ brew install postgresql
	==> Installing dependencies for postgresql: openssl, readline
	==> Installing postgresql dependency: openssl
	...
	==> Installing postgresql
	==> Downloading https://homebrew.bintray.com/bottles/postgresql-9.5.3.el_capitan.bottle.tar.gz
	...
	To have launchd start postgresql now and restart at login:
	  brew services start postgresql
	Or, if you don't want/need a background service you can just run:
	  postgres -D /usr/local/var/postgres
	==> Summary
	/usr/local/Cellar/postgresql/9.5.3: 3,142 files, 35.0M    

To start using Postgres, we need to...start it up.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ brew services start postgresql
	==> Tapping homebrew/services
	Cloning into '/usr/local/Library/Taps/homebrew/homebrew-services'...
	remote: Counting objects: 7, done.
	remote: Compressing objects: 100% (6/6), done.
	remote: Total 7 (delta 0), reused 3 (delta 0), pack-reused 0
	Unpacking objects: 100% (7/7), done.
	Checking connectivity... done.
	Tapped 0 formulae (32 files, 46.1K)
	==> Successfully started `postgresql` (label: homebrew.mxcl.postgresql)

Now Postgres is available for fun and for profit. 
The final thing you'll need to do is create a database to work in.
If you try to start postgres without it, it'll throw you an error like this:

.. code-block:: bash

	(pyramid_lj) bash-3.2$ psql
	psql: FATAL:  database "<Your Username Here>" does not exist

So start by creating a database with the ``createdb`` command. 
Since we're working on our learning journal, call it ``learning_journal``

.. code-block:: bash

	(pyramid_lj) bash-3.2$ createdb <Your Username Here>

With our database created, we can enter the Postgres shell with the ``psql`` command.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ psql
	psql (9.5.3)
	Type "help" for help.

	<Your Username Here>=# 

Investigating your Postgres database will show that it's empty.
Let's fill it with data from our Pyramid app.


Postgres and Pyramid
--------------------

To integrate Postgres into our Pyramid app we need to change a few things.
To start, we should include the ``psycopg2`` package that lets Python interact with Postgres.
In ``setup.py`` add it to the ``requires`` list.

.. code-block:: python

	requires = [
		'pyramid',
		'pyramid_jinja2',
		'pyramid_debugtoolbar',
		'pyramid_tm',
		'SQLAlchemy',
		'transaction',
		'zope.sqlalchemy',
		'waitress',
		'psycopg2',
		]

``pip`` install your app so that ``psycopg2`` becomes available.

Next up, go investigate ``development.ini``.
You need to change where SQLAlchemy looks for a database to interact with.
Since we'll no longer be using ``sqlite``, replace

.. code-block:: ini

	sqlalchemy.url = sqlite:///%(here)s/learning_journal.sqlite

with

.. code-block:: ini

	sqlalchemy.url = postgres://<Your Username Here>@localhost:5432/learning_journal

With all these various pieces now wired together, let's re-initialize our database.
Keep in mind that since we're switching to a new database, any data we've saved prior to now will be gone.
This is why in ``learning_journal/scripts/initializedb.py`` we included these lines:

.. code-block:: python

	with transaction.manager:
		dbsession = get_tm_session(session_factory, transaction.manager)

		entries = [
			Entry(title="LJ - Day 10", body="Sample body text."),
			Entry(title="LJ - Day 11", body="Sample body text."),
			Entry(title="LJ - Day 12", body="Sample body text."),
		]

		dbsession.add_all(entries)

In this way, upon creation of a new database we're able to repopulate it with data we already know we want.
We can see that our database is populated with our default data above by inspecting the db.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ psql
	psql (9.5.3)
	Type "help" for help.

	Nick=# \l
									  List of databases
		   Name       | Owner | Encoding |   Collate   |    Ctype    | Access privileges 
	------------------+-------+----------+-------------+-------------+-------------------
	 Nick             | Nick  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
	 learning_journal | Nick  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
	 postgres         | Nick  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
	 template0        | Nick  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/Nick          +
					  |       |          |             |             | Nick=CTc/Nick
	 template1        | Nick  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/Nick          +
					  |       |          |             |             | Nick=CTc/Nick

	Nick=# \c learning_journal
	You are now connected to database "learning_journal" as user "Nick".

	learning_journal=# \dt
		   List of relations
	Schema |  Name   | Type  | Owner 
	--------+---------+-------+-------
	public | entries | table | Nick
	(1 row)

	learning_journal=# SELECT * FROM entries;
	 id |    title    |       body        |       creation_date        
	----+-------------+-------------------+----------------------------
	  1 | LJ - Day 10 | Sample body text. | 2016-07-14 09:27:16.674145
	  2 | LJ - Day 11 | Sample body text. | 2016-07-14 09:27:16.748319
	  3 | LJ - Day 12 | Sample body text. | 2016-07-14 09:27:16.750044
	(3 rows)

Once your database is back up and running, it's back to business as usual.


Environment Variables and Python
================================

One of the benefits to having used sqlite3 is that wherever our site was deployed, Pyramid would generate a new database.
A consequence of having switched to PostgreSQL is that our database is bound to the one we've set up on our local computer.
Once deployed, our ``sqlalchemy.url`` in ``development.ini`` will be pointing to the wrong place.

We could use ``production.ini`` to set up a ``sqlalchemy.url`` for a database on our production server.
However, this only works on a static server whose location we know. 
Heroku uses its own server to host its Postgres database, whose location we do not know.
Further, they may copy the database and move it elsewhere without our knowledge.
We want our data to persist no matter where it goes.

What we need is an `Environment Variable <http://www.tutorialspoint.com/unix/unix-environment.htm>`_.
This is something that will belong to whatever environment we launch our site in.
When you use the `postgres add-on in Heroku <https://devcenter.heroku.com/articles/heroku-postgresql#create-a-new-database>`_, an environment variable becomes available to you called ``DATABASE_URL``.
``DATABASE_URL`` holds the url for your Postgres database, and will be accessible no matter what Heroku does with it.

If we could create that variable on our local machine and call it into Pyramid, then we could use it in our app and be set.


Making and Seeing Environment Variables
---------------------------------------

Environment variables live in your environment's ``bin/activate`` file, as well as in your ``.bashrc`` and ``.bash_profile`` files.

You've already seen a few. For example, your ``PATH``.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ echo $PATH
	/Users/Nick/Documents/codefellows/courses/code401_python/pyramid_lj/bin:/Library/Frameworks/Python.framework/Versions/3.5/bin:/Users/Nick/:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/git/bin:/usr/texbin:/usr/local/bin:/Users/Nick/bin:/Applications/MAMP/Library/bin/:/Applications/mongodb/bin/:/Applications/Postgres.app/Contents/Versions/latest/bin

Your ``PATH`` variable holds all the places that your computer will look for console commands and Python packages.
You can inspect it using ``echo`` in the console.

You can create a new environment variable using the ``export`` command.
You define that variable with some name and attach it to some value, like a string.

.. code-block:: bash

	(pyramid_lj) bash-3.2$ export FOO="BAR"
	(pyramid_lj) bash-3.2$ echo $FOO
	BAR

Defining an environment variable in this way will not persist that variable across different terminal instances.
To create a lasting variable, you have to add it to your ``.bashrc``, ``.bash_profile``, or ``$VIRTUAL_ENV/bin/activate``. 
Note, if you add a variable to ``$VIRTUAL_ENV/bin/activate`` it'll only be accessible in that environment.

.. code-block:: bash

	# inside $VIRTUAL_ENV/bin/activate
	...
	export FOO="BAR"
	...

	# back to the command line, not in environment
	bash-3.2$ echo $FOO

	bash-3.2$ source bin/activate
	(pyramid_lj) bash-3.2$ echo $FOO
	BAR


Calling Environment Variables
-----------------------------

It's actually fairly simple to call environment variables into Python.
``os.environ`` returns a ``dict``-like object whose keys are the currently-available variables.
Pop open a ``pshell`` and investigate.

.. code-block:: python

	In [1]: import os
	In [2]: for key, value in os.environ.items():
		print(key + " = " + value)
	   ...:
	   # ... a bunch of other variables
	   # ...
	   FOO = BAR
	   # ...
	   # ... even more variables

	In [3]: os.environ["FOO"]
	Out[3]: 'BAR'

If we defined our ``DATABASE_URL`` variable in ``$VIRTUAL_ENV/bin/activate``, then we could call that out too.

.. code-block:: python

	In [4]: os.environ["DATABASE_URL"]
	Out[4]: 'postgres://Nick@localhost:5432/learning_journal'
	

Environment Variables in Pyramid
--------------------------------

What we ultimately want to do is dynamically set the ``sqlalchemy.url`` to the value of our ``DATABASE_URL`` environment variable.
``learning_journal/__init__.py`` is where our ``.ini`` file's configuration gets bound to our Pyramid app.
Before the current settings get added to the ``Configurator``, we can use os.environ to bring in our environment's ``DATABASE_URL``.

.. code-block:: python

	# __init__.py

	import os

	from pyramid.config import Configurator


	def main(global_config, **settings):
		""" This function returns a Pyramid WSGI application.
		"""
		settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]
		config = Configurator(settings=settings)
		config.include('pyramid_jinja2')
		config.include('.models')
		config.include('.routes')
		config.scan()
		return config.make_wsgi_app()

Because we should always try to keep code DRY (and prevent future confusion), remove the ``sqlalchemy.url`` keyword from ``development.ini``.

If we invoke ``pserve development.ini`` and navigate to the site in the browser, everything should show up the same.
Now, when we re-deploy to Heroku, we'll connect to whatever Postgres database they have running for our own site.


Recap
=====

Today's work focused on getting set up with our own PostgreSQL database.
We downloaded, installed, and ran Postgres, started up a database, and connected that database to our Pyramid app.
We populated the new database with some default data, and inspected the database to ensure it contained what we expected.

After ensuring that Postgres worked the way we needed, we discussed environment variables.
We found out where they're stored, how to create one, and how to persist one.
Finally, we defined the ``DATABASE_URL`` environment variable and pulled it into our Pyramid app.
With that as a part of our app, we nullified the need to define the ``sqlalchemy.url`` keyword in our ``.ini`` config file(s).

Tonight's work on the Learning Journal will be far lighter than previous nights.
Your job is simply to add the ``DATABASE_URL`` environment variable, connect to PostgreSQL, and re-deploy to Heroku.
Ensure that the app is complete up to this point, with thorough tests for your code.

Our next hit of Pyramid will introduce a more efficient way of handling forms.
We'll also add User registration, authentication and authorization to our web apps.