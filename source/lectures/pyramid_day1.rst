============================
Getting Started With Pyramid
============================

Create a directory to work in. We'll be using this directory as the jumping-off point for deploying our learning journals, so call it something sensible like ``pyramid_lj``. Navigate to that directory and create (and activate) a new virtual environment. Then pip install the most recent versions of ``pip``, ``setuptools``, and ``ipython``.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -U pip setuptools
    (pyramid_lj) bash-3.2$ pip install ipython pyramid_ipython

Installation
============

In order to begin working with Pyramid, we have to install it.

.. code-block:: bash
    
    (pyramid_lj) bash-3.2$ pip install pyramid

The version that should be pulled down is the latest version, 1.7. Note the other packages that get installed along with it, as it has dependencies. For example, ``WebOb`` handles HTTP responses, and Pyramid's ``response`` object inherits from this. Many other frameworks also use this package.

Along with its dependencies, Pyramid installs for you a bunch of new shell commands (``pcreate``, ``pshell``, ``prequest``, etc), and you can see them all in the ``bin`` directory of your virtual environment.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ls bin
    activate         easy_install-3.5 ipython3         pip3             pserve           python
    activate.csh     iptest           pcreate          pip3.5           pshell           python3
    activate.fish    iptest3          pdistreport      prequest         ptweens
    easy_install     ipython          pip              proutes          pviews

Writing a "Hello World" App
===========================

Source: `trypyramid.com <http://www.trypyramid.com>`_. 

As is tradition, when using a new bit of technology we test that it works by having it print something like "Hello World". This is no different. Make a directory for your "hello world" app called ``hello_world``. Within that directory create a file named ``app.py`` and type the following:

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

Finally, open http://localhost:6543/ in your browser. This will simply connect you to the port that you told Pyramid to listen to.

This is an almost irresponsibly-simple web app for proving the concept of having a framework handle HTTP requests and responses. We'll definitely be using Pyramid for significantly more-complicated things. That being said, it's very easy to get a simple site up and running with Pyramid. For the more complex-stuff, it helps to have some structure set up beforehand.

Using the ``pcreate`` Command to Create a Scaffold
===================================================

``pcreate`` allows us to create a "scaffold" for a web app that includes the basic functionality and best practices of a Pyramid app. Before using this command, back out by one directory and invoke ``pcreate`` like so:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pcreate -s starter learning_journal_basic

This scaffold will set you up with the base files that you need to run a Pyramid app, ending with "Sorry for the convenience." **if you see this line, your scaffold was created just fine**. The entire scaffold will be encapsulated in the ``learning_journal_basic`` directory that was just created. Navigate to it and initialize a git repository.

If you use git status you'll see all of the new files that were just created in this directory. We want to make sure we don't track any ``.pyc`` files or the ``.DS_Store`` file in this directory, so create a ``.gitignore`` file and add lines to ignore those files. Add this entire directory to your repository with ``git add .``.

This project root directory will contain a bunch of files that contain metadata and operational instructions for our application:

* ``CHANGES.txt`` tracks what changes we've made to our app over time
* ``MANIFEST.in`` controls what files are actually present when we package our stuff together and upload it
* ``README.txt`` is our ``README`` file. We can add a markdown file of the same name without consequence and use that as the ``README.md`` for our eventual GitHub repos
* ``setup.py`` lets our directory become an installable python package
* ``development.ini`` discussed later 
* ``production.ini`` discussed later
* ``pytest.ini`` directs ``pytest`` as to which files to test (presuming any file ending in "``.py``")
* ``.coveragerc`` determines which directories get targeted for reports of coverage

Inspecting ``setup.py`` reveals that this app requires Pyramid, ``Chameleon`` (a templating engine), and a few other packages to work. It also comes packed ready to install some packages for tests. Let's modify it so that it runs with ``tox`` as part of its test suite, and that it uses the ``Jinja2`` templating engine (which we'll get to another time):

.. code-block:: python

    # in setup.py 
    ...
    requires = [
        'pyramid',
        'pyramid_chameleon', # <-- DELETE THIS LINE
        'pyramid_jinja2',
        ... # other package dependencies
    ]
    ...
    tests_require = [
        'WebTest >= 1.3.1',  # py3 compat
        'pytest',  # includes virtualenv
        'pytest-cov',
        'tox', # you have to add this one in
    ]
    ...
    setup(name='learning_journal_basic',
        version='0.0',
        ... # package metadata
        install_requires=requires,
        entry_points="""\ # Entry points are ways that we can run our code once it has been installed
        [paste.app_factory]
        main = learning_journal_basic:main 
        """
    )

Don't forget to fill in the appropriate information about ``author``, ``author_email``, etc. Now, let's install it in editing mode so that the changes we make to this project will be implemented in the installed version.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -e .

One of the things produced after pip installing is a ``*.egg-info`` file. Let's modify our ``.gitignore`` to exclude those.

Pyramid is Python
=================

Navigate to the ``learning_journal_basic`` directory in your project root and inspect it.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ls
    __init__.py static      templates   tests.py    views.py

In the ``__init__.py`` file you'll find a ``main`` function, which runs when you use ``pserve`` to connect your site to the localhost. We'll have to change a line here to match the templating engine we intend to use (even though we're not going to use it yet).

.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2') # <-- this is the line that gets changed.
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('home', '/')
        config.scan()
        return config.make_wsgi_app()

This looks somewhat different from the ``app.py`` file we had created earlier. The machinery here is handling some of the stuff we had hard coded before. Let's look at this in detail.

.. code-block:: python 
    
    def main(global_config, **settings):

Configuration is passed into an application after being read from the specified ``.ini`` file (e.g. ``development.ini``). The settings come in through, you guessed it, the ``**settings`` kwarg. The ``.ini`` files contain sections (e.g. ``[app:main]``) containing ``name = value`` pairs of *configuration data*. This data is parsed with the Python `ConfigParser <https://docs.python.org/2/library/configparser.html>`_ module, which reads the configuration data and returns it as a dictionary. The result appears in ``settings`` as:

.. code-block:: python

    {'pyramid.debug_notfound': 'false', 
    'pyramid.reload_templates': 'true', 
    'pyramid.default_locale_name': 'en', 
    ...
    }

Those settings get read and handled on the next line after the docstring

.. code-block:: python 

    config = Configurator(settings=settings)

where the Configurator class object is instantiated with the above settings.

We can also ``include`` configuration from other add-on packages and even other regions of the app we're inside of. That explains the next line:

.. code-block:: python

    config.include('pyramid_jinja2')

The next line down connects Pyramid to the directory holding your static files, conveniently created for you, called ``static`` (second argument; the path to the directory) and aliased here as ``static`` (first argument). 

.. code-block:: python

    config.add_static_view("static", "static", cache_max_age=3600)

The above includes things like CSS files you want to link in, local JS scripts and libraries you may be using, and any other files that contribute to the functionality and design of your site.

The last bit is

.. code-block:: python

    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()

That first line adds a path to your URL of ``<whatever your domain name is>/``. The ``.add_route()`` method adds a "route name" to your Pyramid site, that can then be used to connect HTML to that name. Here, the route name ``home`` connects to ``<whatever your domain name is>/``. If instead the second argument was ``'/new_entry'``, then ``home`` would connect to ``<whatever your domain name is>/new_entry``. More on routes shortly. 

Lastly ``config.scan()`` checks to make sure that there are no issues with how everything is wired together, and ``config.make_wsgi_app()`` returns to Pyramid all of the above configuration.

We'll return to the configuration of our application repeatedly over the next few sessions. For greater detail about configuration in Pyramid, check the `configuration chapter <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html>`_ documentation.

Routes and The MVC Controller
=============================

Let's go back to thinking for a bit about the *Model-View-Controller* pattern.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
    :width: 275px
    :alt: By Alan Evangelista (Own work) [CCo]
    :align: center

    By Alan Evangelista (Own work) [CCo], via Wikimedia Commons


HTTP Request/Response
---------------------

If you recall from the HTTP server that we built last week, internet software is driven by the HTTP Request/Response cycle. A *client* (perhaps a user with a web browser) makes a **request**. A *server* receives and handles that request and returns a **response**. The *client* receives the response and views it, perhaps making a new **request**, and so on and so forth.

An HTTP request arrives at a server through the magic of a **URL**

.. code-block:: bash
    
    http://www.codefellows.org/courses/code-401/advanced-software-development-in-python

Let's break that up into its constituent parts:

``http://``:
    This part is the *protocol*, it determines how the request will be sent.

``www.codefellows.org``:
    This is a *domain name*. It's the human-facing address for a server somewhere.

``/courses/code-401/advanced-software-development-in-python``:
    This part is the *path*. It serves as a locator for a resource *on the server*.

In a static website the *path* identifies a **physical location** in the server's file system. Some directory on the server is the *home* for the web process, and the *path* is looked up there. Whatever resource (a file, an image, whatever) is located there is returned to the user as a response. If the path leads to a location that doesn't exist, the server responds with a **404 Not Found** error.

In the golden days of yore, this was the only way content was served via HTTP. In today's world we have dynamic systems, server-side web frameworks like Pyramid. The requests that you send to a server are handled by a software process that *assembles a response* instead of looking up a physical location. But, we still have URLs, with *protocol*, *domain*, and *path*. What is the role for a path in a process that doesn't refer to a physical file system?

Routes in Pyramid
-----------------

Most web frameworks now call the *path* a **route**, and provide a way of matching *routes* to the code that will be run to handle requests. In our Pyramid scaffold, routes are handled as *configuration* and as we saw above are configured in the *main* function in ``__init__.py``:

.. code-block:: python
    
    # back inside __init__.py
    def main(global_config, **settings):
        #...
        config.add_route('home', '/')
        #...

The ``add_route`` method takes a required ``name`` argument for each route added. Everything else is, to some degree, an optional argument. Above, we also provide the ``pattern`` that gets appended to the site's root URL (in this case, "/"). Anything that we use accessing the specified ``name`` argument in our Pyramid app will be broadcast to the ``pattern`` that we provide.

When a request comes in to a Pyramid application, the framework looks at all the *routes* that have been configured. One by one, in order, it tries to match the path of the incoming request against the *pattern* of the route. As soon as a *pattern* matches the *path* from the incoming request, that route is used and no further matching is performed. If no route is found that matches, then the request will automatically get a **404 Not Found** error response.

In a very real sense, the *routes* defined in an application *are* the public API. Any route that is present represents something the user can do. Any route that is not present is something the user cannot do. 

One can imagine that if we were to build a site with many routes (as we will), it would clutter up this ``main`` function, causing it to really be handling multiple things instead of being singularly focused (as functions should be). As a completely hypothetical example:

.. code-block:: python

    # a hypothetical __init__.py; DO NOT TYPE THIS

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_static_view('special_styles', 'special_styles', cache_max_age=3600)
        config.add_static_view('misc_styles', 'misc_styles', cache_max_age=3600)
        config.add_route('home', '/')
        config.add_route('about', '/about-me')
        config.add_route('create', '/journal/new-entry')
        config.add_route('edit', '/journal/edit-entry')
        config.add_route('delete', '/journal/delete-entry')
        config.add_route('view', '/journal/{id:\d+}')
        config.add_route('contact', '/contact-me')
        config.add_route('register', '/register')
        config.add_route('login', '/login')
        config.add_route('logout', '/logout')
        config.add_route('settings', '/settings')
        config.scan()
        return config.make_wsgi_app()

Luckily, we can break out our routes and our static views into a ``routes.py`` file in the same directory, whose sole purpose will be to hold and handle all of the routing and routing configuration for our Pyramid site. We can include the routes into the configuration of ``__init__.py`` by using the ``include()`` method of the ``Configurator``:

.. code-block:: python

    # inside routes.py
    def includeme(config):
        """ This function adds routes to Pyramid's Configurator """
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('home', '/')

    # inside __init__.py
    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

We have our route, and so anything we connect to that specific route name will be shown on the home page. However, we do not yet have anything (of substance) to show on that page. We can change all that with **Views**.

The Pyramid View
----------------

Let's imagine that a *request* has come to our application for the path ``'/'``. The framework made a match of that path to a *route* with the pattern ``'/'``. Configuration connected that route to a *view* in our application. Now, the view that was connected will be *called*, which brings us to the nature of *views*.

.. note:: A Pyramid View is a callable that takes `request` as an argument.

The view can then use information from that request to build appropriate data, perhaps using the application's *models* (more on that tomorrow). Then, it simply returns the data it assembled.

If you recall our ``hello_world`` app, we defined a function named ``hello_world()``, which took a ``request`` as an argument and used Pyramid's ``Response`` object to provide an HTTP response. If we look inside of the ``views.py`` file provided by Pyramid's "starter" scaffold, you'll find a similar situation.

.. code-block:: python

    # views.py
    from pyramid.view import view_config


    @view_config(route_name='home', renderer='templates/mytemplate.pt')
    def my_view(request):
        return {'project': 'learning_journal_basic'}

Here, ``my_view`` is the function name, taking a request, and a dictionary is being returned as a response. This is great and all, but let's start simpler. Clear out the file and replace it with the following:

.. code-block:: python

    # complete code for views.py right now
    from pyramid.response import Response 

    def home_page(request):
        return Response("This is my first view!")

    def includeme(config):
        config.add_view(home_page, route_name='home')

We can connect this view to our existing ``home`` route in ``__init__.py``:

.. code-block:: python

    # __init__.py

    #...
    def main(global_config, **settings):
        # ...
        config.include('.views') <-- connects our views
        config.scan()
        return config.make_wsgi_app()

Now that we're all wired together, let's navigate back to our project route and ``pip install`` this Pyramid app. Then, we can use ``pserve development.ini`` to start up a server and investigate the fruits of our labor.

What happens if instead we try to include the text contained within another file? Let's set ourselves up for it by creating a file in the same directory called ``sample.txt``.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ echo "This is text in an external file." > sample.txt

Now modify the view that we've made to read this file into Python, and return that text in the HTTP response object.

.. code-block:: python

    # views.py
    # ...
    import os

    HERE = os.path.dirname(__file__)

    def home_page(request):
        imported_text = open(os.path.join(HERE, 'sample.txt')).read()
        return Response(imported_text)
    # ...

We don't just have to work with plain text. Let's make a new file that contains HTML instead.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ echo "<h1>This is text in an external file.</h1>" > sample.html

And now modify our view to access this new file

.. code-block:: python

    # views.py
    # ...
    import os

    HERE = os.path.dirname(__file__)

    def home_page(request):
        imported_text = open(os.path.join(HERE, 'sample.html')).read()
        return Response(imported_text)
    # ...

Re-launch the server and voila, html appears!


Recap
=====

Today we got Pyramid working and set up to run a simple "Hello World" app. We went from there to using Pyramid's ``pcreate`` command to set up a slightly more complex scaffold, complete with the base files we'd need to start work toward a larger project. Within that scaffold we learned how to capture HTTP requests and provide responses to those requests, connecting those responses to a URL via routing. 

Finally, we used view callables to take in a request and display some data on a webpage. First we used views to simply write a message onto the page. We soon saw that we could also use them to display the contents of an external file, and even display HTML within that file.

Tonight you will use views to display your own HTML, complete with whatever CSS styles your project. Tomorrow, we'll learn about a better way to use Pyramid to serve up HTML via templates, and we'll write robust tests for our Pyramid app.