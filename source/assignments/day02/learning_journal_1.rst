*******************************
Python Learning Journal: Step 1
*******************************

In this walk-through we will begin the process of creating an online learning
journal using Python and the Flask web framework.

The walk-through is intended to get you to a working application as quickly as
possible. There will be many questions left unanswered as we proceed. Fear not.
The answers will come as this course progresses. For now, simply focus on the
process and getting to a working application.

Prerequisites
=============

In order to follow this tutorial, you will need to have several tools in place
before you begin.

1. `Python 2.7.x`_
2. `Virtualenv and Virtualenvwrapper`_ installed and properly configured.
3. The `PostgreSQL Database Engine`_ installed and properly configured.
4. A c compiler and Python development headers.
5. An account with `GitHub`_

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
  A lightweight Flask web journal.

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
    :width: 25%

There are two versions of this URL, one for HTTPS and the other for SSH.

If you have `set up public key authentication`_ for your GitHub account, you
will want to copy the SSH version of the URL.  Otherwise, you'll need to copy
the HTTPS version.

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

    ./learning_journal/   # <- Your project directory
    ├── learning_journal  # <- Your repository root
    │   ├── LICENSE       # <- Initial files from GitHub
    │   ├── README.md
    │   ├── .gitignore


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
    192:learning_journal cewing$ pip install flask psycopg2 pytest
    Downloading/unpacking flask
    ...
    Successfully installed flask psycopg2 Werkzeug Jinja2 itsdangerous markupsafe pytest py
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

We'll start our learning journal by building the data layer.  This layer of the
application will be responsible for persisting entries to and retrieving
entries from the database you just created.
