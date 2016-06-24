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
        return Response("Hello World!" % request.matchdict)

    if __name__ == '__main__':
        config = Configurator()
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 8000, app)
        server.serve_forever()

Save that file and run the following from the command line:

.. code-block::

    (pyramid_test) bash-3.2$ python app.py

Notice how the shell returns nothing. That means that the server you've set up through Pyramid is up and listening for requests.

Finally, open http://localhost:8000/ in your browser. This will simply connect you to the port that Pyramid is listening to.

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

If you inspect ``setup.py`` you'll see that this app requires pyramid, jinja, SQLAlchemy, and a few other packages to work. It also comes packed ready to install some packages for tests. Let's modify it so that it runs with ``tox``:

.. code-block:: python

    # in setup.py 

    ...
    tests_require = [
        'WebTest >= 1.3.1',  # py3 compat
        'pytest',  # includes virtualenv
        'pytest-cov',
        'tox',
    ]
    ...

Don't forget to fill in the appropriate information about ``author``, ``author_email``, etc. Now, let's install it in editing mode so that the changes we make to this project will be implemented in the installed version.

.. code-block::

    (pyramid_test) bash-3.2$ pip install -e .

Let's see what this scaffold has provided us using the ``pserve`` command on the project's configuration file.

.. code-block::

    (pyramid-test) bash-3.2$ pserve development.ini --reload

Open up the browser at http://localhost:6543/ and investigate.



The vast majority of the changes we'll be making will take place in the project directory within ``testapp`` that is also called  ``testapp``. Within this one you'll find directories for "models", "views", and "templates" among other things.









