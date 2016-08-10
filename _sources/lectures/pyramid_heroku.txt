***************************
Deploying Pyramid to Heroku
***************************

In which we learn how to make a simple Pyramid application run in the Heroku environment.

Heroku's Environment
====================

Heroku is a great system for getting web applicatons up and running fast.
But to work with it, you have to make sure that your application meets with Heroku's expectations.
Let's take a moment to walk through setting up a simple Pyramid application to run on Heroku.

Assumptions
-----------

This quick tutorial assumes that you have:

* Created an account with Heroku
* Installed the `Heroku Toolbelt <https://toolbelt.heroku.com/>`_
* Authenticated the toolbelt via `heroku login` or similar

Create a Simple App
===================

Let's begin by creating a simple Pyramid application.

First, make a project directory then create and activate a virtual environment in that directory:

.. code-block:: bash

    $ mkdir pyramid_starter
    $ cd pyramid_starter
    $ python3 -m venv ./
    $ . bin/activate
    (pyramid_starter)$ pip install -U pip setuptools

Next, install pyramid:

.. code-block:: bash

    (pyramid-heroku-demo)$ pip install pyramid
    ...
    Successfully installed PasteDeploy-1.5.2 WebOb-1.6.1 pyramid-1.7 repoze.lru-0.6
      translationstring-1.3 venusian-1.0 zope.deprecation-4.1.2 zope.interface-4.2.0

Use the ``pcreate`` command to create a simple application using the ``starter`` scaffold:

.. code-block:: bash

    (pyramid-heroku-demo)$ pcreate -s starter demoapp
    ...
    Welcome to Pyramid.  Sorry for the convenience.

Install the new application so that you can test that it works:

.. code-block:: bash

    (pyramid_starter)$ pip install -e .
    Obtaining file:///Users/cewing/Desktop/pyramid_starter/demoapp
    ...
    Successfully installed Chameleon-2.24 Mako-1.0.4 MarkupSafe-0.23 Pygments-2.1.3
      demoapp pyramid-chameleon-0.3 pyramid-debugtoolbar-3.0.4 pyramid-mako-1.0.2 waitress-0.9.0

Now, test the application by starting it up and loading http://localhost:6543

.. code-block:: bash

    (pyramid_starter)$ pserve development.ini
    Starting server in PID 6795.
    serving on http://127.0.0.1:6543

If you see the nice, cranberry-colored front page of the starter app, you're all set so far.
Go ahead and quit the pyramid server.

Put it in Git
=============

The application deployment story for Heroku is tightly coupled to git.
It is **not** tightly coupled to github.
We'll use github here because it is familiar.
But the same process will work for gitlab, bitbucket, or whatever.

Start by initializing a new git repository in your application root:

.. code-block:: bash

    (pyramid_starter)$ git init
    Initialized empty Git repository in /Users/cewing/Desktop/pyramid_starter/demoapp/.git/

Set up a .gitignore file to ignore whatever you don't want:

.. code-block:: bash

    (pyramid_starter)$ touch .gitignore
    (pyramid_starter)$ echo "*.py[cod]" > .gitignore
    (pyramid_starter)$ echo "__pycache__" >> .gitignore
    (pyramid_starter)$ echo "*.egg-info" >> .gitignore
    (pyramid_starter)$ more .gitignore
    *.py[cod]
    __pycache__
    *.egg-info

Now, add the .gitignore file and then the rest of your files to your git repository:

.. code-block:: bash

    (pyramid_starter)$ git add .
    (pyramid_starter)$ git commit -m "adding a simple starter app for demo purposes"

At this point, your application is a git repository.
It isn't connected to any remote repository, like GitHub, GitLab, or BitBucket.
But that doesn't really matter for this demo.  Let's go on.

Build Heroku Needs
==================

Now that we have an application in a git repository, we are ready to integrate Heroku.

Tell Heroku This is Python
--------------------------

Heroku uses a series of heuristics to determine what type of application you have.
The primary heuristic for a Python app is the presence of a `requirements.txt` file
Let's create that file and add it to our repository:

.. code-block:: bash

    (pyramid_starter)$ pip freeze > requirements.txt

The file that was created will contain a reference to your ``demoapp``.
However, you don't actually want to install this with pip when on heroku.
So edit the ``requirements.txt`` file to remove these lines::

    ## !! Could not determine repository location
    demoapp==0.0

Add that file to your git repository and commit:

.. code-block:: bash

    (pyramid_starter)$ git add requirements.txt
    (pyramid_starter)$ git commit -m "adds requirements file so Heroku knows it is a Python app"

Tell Heroku How to Run Your App
-------------------------------

Heroku requires a plain text file called `Procfile` (spelling and capitalization count).
This file tells Heroku what to do to run your application.
Add this file to your repository, containing the text ``web: ./run``:

.. code-block:: bash

    (pyramid_starter)$ echo ``web: ./run`` > Procfile
    (pyramid_starter)$ git add Procfile
    (pyramid_starter)$ git commit -m "Tells Heroku how to run my app"

Now Heroku is going to look for an executable script by the name ``run`` in our application's root directory.
We need to make that file.
We'd like it to install our application and then start up a server to serve it.

Create the file ``run`` in the ``demoapp`` directory.
Then type the following text into it:

.. code-block:: bash

    #!/bin/bash
    set -e
    python setup.py develop
    python runapp.py

This script tells the Heroku server to use the ``bash`` shell (``#!/bin/bash``).
It says that if any part of the script returns an error, it should exit the script (``set -e``).
It then installs our application in develop mode (equivalent to running ``pip install -e .``).
Finally, it executes a Python module called ``runnapp.py``.

This file needs to be executable, so that Heroku can run it.
We can use the ``chmod`` command to fix that:

.. code-block:: bash

    (pyramid_starter)$ chmod u+x run

Now, add the file to your repository and commit it:

.. code-block:: bash

    (pyramid_starter)$ git add run
    (pyramid_starter)$ git commit -m "adds a shell script to start my app"

Create the ``runapp.py`` module
-------------------------------

Finally, we need to actually write the Python module that will run our application.
Create a file ``runapp.py`` and type the following Python code into it:

.. code-block:: python
    :linenos:

    import os

    from paste.deploy import loadapp
    from waitress import serve

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app = loadapp('config:production.ini', relative_to='.')

        serve(app, host='0.0.0.0', port=port)

In line 6, we use a "main" block to make this module a Python script.
The code in this block will only be executed when the script is run.

In line 7, we read the "PORT" variable from the operating system environment.
Heroku uses environmental variables to pass information to applications.
This allows you to separate configuration from code and is a good pattern.
Notice that we default to port 5000 if no 'PORT' has been set in the environment.

In line 8, we create an application, using the ``production.ini`` file that is located adjacent to this Python module.

Finally, in line 10, we serve our application, setting it up to listen on any available IP address.

Add this file to our git repository and commit your changes:

.. code-block:: bash

    (pyramid_starter)$ git add runapp.py
    (pyramid_starter)$ git commit -m "adds a python script to run our application"

Set Up Heroku and Deploy
========================

Okay, with that, we've got all we need to get our app running on Heroku.
Next, we'll use the Heroku toolbelt to create a new app:

.. code-block:: bash

    (pyramid_starter)$ $ heroku create
    Creating app... done, ⬢ safe-scrubland-24595
    https://safe-scrubland-24595.herokuapp.com/ | https://git.heroku.com/safe-scrubland-24595.git

Finally, we push our app to heroku:

.. code-block:: bash

    (pyramid_starter)$ git push heroku master
    ...
    remote: Verifying deploy... done.

And once that is finished, you can view your app in a browser:

.. code-block:: bash

    (pyramid_starter)$ heroku open

Cleaning Up the Edges
=====================

There's one last problem here.
Heroku defaults to serving our application over ``https``.
This is desireable.

But our Pyramid application has no idea that it is being served securely.
When it generates the URLs for css files, it uses ``http``.
Our browsers will not appreciate this.

We can fix it using configuration.

Open the file ``production.ini`` from your application root directory in your text editor.
First, find the first section header at the top that contains this ``[app:main]``.
Change that to read ``[app:demoapp]``

Next, find the section of the file that looks like this:

.. code-block:: ini

    ###
    # wsgi server configuration
    ###

    [server:main]
    use = egg:waitress#main
    host = 0.0.0.0
    port = 6543

**Before** this section, add the following configuration:

.. code-block:: ini
    :linenos:

    [filter:paste_prefix]
    use = egg:PasteDeploy#prefix

    [pipeline:main]
    pipeline =
        paste_prefix
        demoapp

Lines 1-2 create a wsgi middleware filter that will detect the ``https`` scheme and make that information available to our Pyramid app.

Lines 4-7 set up a wsgi pipeline which puts this filter before our new app (remember, we changed the app name above to ``demoapp``).

Save these changes, add them to the stage, and commit them to your repository.
Then you can re-deploy your application using ``git push``:

.. code-block:: bash

    (pyramid_starter)$ git add production.ini
    (pyramid_starter)$ git commit -m "enables pyramid to properly render https urls for static resources"
    (pyramid_starter)$ git push heroku master

And that finishes us up.
We now have a small, functional Pyramid application running on Heroku, serving resources over https.
Tonight, you'll repeat this process with your own Pyramid app.

