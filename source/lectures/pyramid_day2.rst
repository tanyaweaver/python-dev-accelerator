===============================================
Pyramid Views, Templates, and Front-end Testing
===============================================

Last time, we got started with a Pyramid app with the intention to display learning journal entries online. Toward this end, we created basic views that read raw HTML files and provided them to the browser as an HTTP response. That worked, but it's a really crappy way to use Pyramid and doesn't even begin to take advantage of its capabilities. Today we'll learn about better ways to connect views to the HTML they serve, and how to use templates to display our information.

The MVC View
============

We return again to the *Model-View-Controller* pattern. We've built our *controller* using Pyramid's **view** callables that take *HTTP requests* as arguments. We've also created the beginnings of our MVC *view* using our HTTP files. Let's dig into both of these some more.

Presenting Data 
===============

The job of the *view* in the *MVC* pattern is to present data in a format that is readable to the user of the system. There are many ways to present data. Some are readable by humans (e.g. tables, charts, graphs, HTML pages, text files), while others are more for machines (e.g. xml files, csv, json). Which of these formats is the *right one* depends on your purpose. What is the purpose of our learning journal?

Pyramid Renderers and ``view_config``
-------------------------------------

In Pyramid, the job of presenting data is performed by a *renderer*, which can come in a variety of types. Pyramid has two `renderers <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/renderers.html>`_ built-in: string, json. These renderers will take a *non-response* object and return it as an HTTP response in the given format. They are attached to a view using the ``@view_config`` decorator:

.. code-block:: python

    # views.py
    # ...
    from pyramid.view import view_config

    # ...
    @view_config(renderer='string')
    def detail_view(request):
        return "This was transformed into an HTTP response"

    # ...

If we want to see the result of this code, we of course have to connect this view to a route. Since we're using this **declarative style** of defining a view, we can add in the ``route_name`` as a parameter to ``view_config``:

.. code-block:: python

    @view_config(route_name='detail', renderer='string')

Finally, since we're now connecting our view to our route with this decorator (and we will forever onward), we'll need to start refactoring our code...

* We no longer need to import or use ``Response`` from ``pyramid.response``
* Decorate each of our views with a ``view_config`` where the ``renderer`` is ``string`` and ``route_name`` is the appropriate route name for that view
* We don't need the ``includeme`` function as ``view_config`` ensures that the decorated view is automatically included.
* In ``__init__.py`` we don't have to use ``config.include('.views')`` for the same reason as above.

After refactoring, our code should look *something* like this:

.. code-block:: python

    # __init__.py
    from pyramid.config import Configurator


    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

.. code-block:: python

    # views.py

    from pyramid.view import view_config

    @view_config(route_name='home', renderer='string')
    def list_view(request):
        return "Home!"

    @view_config(route_name='detail', renderer='string')
    def detail_view(request):
        return {"content" : "This was transformed into an HTTP response"}

    @view_config(route_name='create', renderer='string')
    def create_view(request):
        return ["A", "list", "of", "values"]

    @view_config(route_name='edit', renderer='string')
    def update_view(request):
        return ("This is", "a tuple")

Note that for each of the above views, *anything* that was in the ``return`` statement was printed to the browser as a string, without having to have it wrapped in an HTTP response object. 

We can attach external renderers to our views as well. We have in fact included one in ``__init__.py`` with the ``pyramid_jinja2`` package. Recall:

.. code-block:: python

    # __init__.py
    config.include('pyramid_jinja2')

The ``pyramid_jinja2`` package supports using the *Jinja2* template language. Let's learn a bit about how `Jinja2 templates <http://jinja.pocoo.org/docs/templates/>`_ work.

Jinja2 Template Basics
----------------------

We'll start with the absolute basics. Fire up an iPython interpreter in your virtual environment and import the ``Template`` class from the ``jinja2`` package:

.. code-block::
    
    (pyramid_lj) bash-3.2$ ipython 
    ...
    In [1]: from jinja2 import Template

A template is constructed with a simple string:

.. code-block:: ipython

    In [2]: t1 = Template("Hello {{ name }}, how are you")

Here, we've simply typed the string directly, but it is more common to build a template from the contents of a *file*. 

Notice that our string has some odd stuff in it: ``{{name}}``. This is called a *placeholder*, and when the template is *rendered* it is replaced. We can see that if we call ``t1``'s ``render`` method, providing *context* for ``{{name}}``:

.. code-block:: ipython

    In [3]: t1.render(name="Freddy")
    Out[3]: 'Hello Freddy, how are you'

    In [4]: t1.render(name="Gloria")
    Out[4]: 'Hello Gloria, how are you'

*Context* can either be keyword arguments, or a dictionary. Note the resemblance to the string formatting we've seen before:

.. code-block:: ipython

    In [5]: "This is {owner}'s string".format(owner="Cris") # <-- this is straight Python, NOT Jinja2
    Out[5]: 'This is Cris's string'

Dictionaries passed in as part of the *context* can be addressed with either subscription or dotted notation:

.. code-block:: ipython

    In [6]: person = {'first_name': 'Frank',
       ...:           'last_name': 'Herbert'}
    In [7]: t2 = Template("{{ person.last_name }}, {{ person['first_name'] }}")
    In [8]: t2.render(person=person)
    Out[8]: 'Herbert, Frank'    

* Jinja2 will try the *correct* way first (attr for dotted, item for subscript).
* If nothing is found, it will try the opposite.
* If still nothing, it will return an *undefined* object.

The exact same is true of objects passed in as part of *context*:

.. code-block:: ipython

    In [9]: t3 = Template("{{ obj.first_attr }} + {{ obj['second_attr'] }} = Fun!")
    In [10]: class Game(object):
       ...:     first_attr = 'babies'
       ...:     second_attr = 'bubbles'
       ...:
    In [11]: bathtime = Game()
    In [12]: t3.render(obj=bathtime)
    Out[12]: 'babies + bubbles = Fun!'

This means your templates can be agnostic as to the nature of the things found in *context*.

You can apply `filters <http://jinja.pocoo.org/docs/dev/templates/#filters>`_ to the data passed in *context* with the pip ('|') operator:

.. code-block:: ipython

    In [13]: t4 = Template("shouted: {{ phrase|upper }}")
    In [14]: t4.render(phrase="this is very important")
    Out[14]: 'shouted: THIS IS VERY IMPORTANT'

You can also chain filters together:

.. code-block:: ipython

    In [15]: t5 = Template("confusing: {{ phrase|upper|reverse }}")
    In [16]: t5.render(phrase="howdy doody")
    Out[16]: 'confusing: YDOOD YDWOH'

Logical `control structures <http://jinja.pocoo.org/docs/dev/templates/#list-of-control-structures>`_ are also available:

.. code-block:: ipython

    In [17]: tmpl = """
       ....: {% for item in list %}{{ item}}, {% endfor %}
       ....: """
    In [18]: t6 = Template(tmpl)
    In [19]: t6.render(list=['a', 'b', 'c', 'd', 'e'])
    Out[19]: '\na, b, c, d, e, '

Any control structure introduced in a template **must** be paired with an explicit closing tag (``{% for %} ... {% endfor %}``, ``{% if %} ... {% elif %} ... {% else %} ... {% endif %}``). 

Remember, although template tags like ``{% for %}`` or ``{% if %}`` look a lot like Python, *they are not*. The syntax is specific and must be followed correctly.

There are a number of specialized *tests* available for use with the ``if...elif...else`` control structure:

.. code-block:: ipython

    In [20]: tmpl = """
       ....: {% if phrase is upper %}
       ....:   {{ phrase|lower }}
       ....: {% elif phrase is lower %}
       ....:   {{ phrase|upper }}
       ....: {% else %}{{ phrase }}{% endif %}"""
    In [21]: t7 = Template(tmpl)
    In [22]: t7.render(phrase="FOO")
    Out[22]: '\n\n  foo\n'
    In [23]: t7.render(phrase='bar')
    Out[23]: '\n\n  BAR\n'
    In [24]: t7.render(phrase='This should print as-is')
    Out[24]: '\nThis should print as-is'

Basic `Python-like expressions <http://jinja.pocoo.org/docs/dev/templates/#expressions>`_ are also supported:

.. code-block:: ipython

    In [25]: tmpl = """
       ....: {% set sum = 0 %}
       ....: {% for val in values %}
       ....: {{ val }}: {{ sum + val }}
       ....:   {% set sum = sum + val %}
       ....: {% endfor %}
       ....: """
    In [26]: t8 = Template(tmpl)
    In [27]: t8.render(values=range(1, 11))
    Out[27]: '\n\n\n1: 1\n  \n\n2: 3\n  \n\n3: 6\n  \n\n4: 10\n
              \n\n5: 15\n  \n\n6: 21\n  \n\n7: 28\n  \n\n8: 36\n
              \n\n9: 45\n  \n\n10: 55\n  \n\n'

Templates Applied
=================

There's more that Jinja2 templates can do, but it will be easier to introduce you to that in the context of a working template. So let's make some.

We have a Pyramid ``view`` that'll return the content of a single entry. Let's create a template to show it. In ``learning_journal/templates/`` create a new file ``detail.jinja2``:

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <article>
                <h1>LJ - Day 12</h1>
                <hr />
                <p>Created <strong>Aug 23, 2016</strong></p>
                <hr />
                <p>Sample body text.</p>
            </article>
        </body>
    </html>

We're going to hold on replacing names with keywords. First, let's just serve up this HTML. Notice that the file type is ``.jinja2``, not ``.html``. 

Wire up our new detail template to the detail view in ``learning_journal/views.py``:

    # views.py
    @view_config(route_name='detail', renderer='templates/detail.jinja2')
    def view(request):
        #...

Now we should be able to see some rendered HTML for our journal entry details. Start up your server:

.. code-block::

    (pyramid_lj) bash-3.2$ pserve development.ini 
    Starting server in PID 53587.
    serving on http://127.0.0.1:6543

Then try viewing an individual journal entry: `http://localhost:6543/journal/1`_

The HTML in our Jinja2 template comes up just as we've structured it! However there's a problem. If we were to continue on like this we'd still have to create an individual template for *every* journal entry. If we just wanted to write static HTML this way, why would we ever use a template? 

Jinja2 templates are rendered with a *context*. A Pyramid *view* returns a dictionary, which is passed to the renderer as part of that *context*. This means we can access values we return from our *view* in the *renderer* using the names we assigned to them. 

Just like we did in the command line, we can use placeholders and feed data to those placeholders through the ``return`` statement of our ``detail_view``:

.. code-block:: python

    # templates/detail.jinja2
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <article>
                <h1>{{ title }}</h1>
                <hr />
                <p>Created <strong>{{ creation_date }}</strong></p>
                <hr />
                <p>{{ body }}</p>
            </article>
        </body>
    </html>

.. code-block:: python

    # views.py
    def detail_view(request):
        return {
            "title": "LJ - Day 12",
            "creation_date": "Aug 23, 2016",
            "body": "Sample body text."
        }

The *request* object is also placed in the context by Pyramid *by default*. ``request`` has a method ``route_url`` that will create a URL for a named route and an attribute ``url`` that will create a URL for the current page. This allows you to include URLs in your template without needing to know exactly what they will be. This process is called *reversing*, since it's a bit like a reverse phone book lookup.

.. code-block:: python

    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <article>
                <h1><a href="{{ request.url }}">{{ title }}</a></h1> # this is new
                <hr />
                <p>Created <strong>{{ creation_date }}</strong></p>
                <hr />
                <p>{{ body }}</p>
            </article>
            <footer><a href="{{ request.route_url('home') }}">Home</a></footer> # this is also new
        </body>
    </html>

Let's now create a template such that our index shows a list of journal entries, showing only the title and the date of creation. In ``learning_journal/templates/`` create a new file ``list.jinja2``:

.. code-block:: python

    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <h1>Home Page</h1>
            {% if entries %}
                {% for entry in entries %}
                    <article>
                        <h2><a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a></h2>
                        <hr />
                        <p>Created <strong>{{ entry.creation_date }}</strong></p>
                    </article>
                {% endfor %}
            {% else %}
                <p>This journal is empty</p>
            {% endif %}
            <footer><a href="{{ request.route_url('home') }}">Home</a></footer>
        </body>
    </html>

It's worth taking a look at a few specifics of this template.

.. code-block:: python

    {% for entry in entries %}
    ... # stuff here
    {% endfor %}

Pyramid has *control structures* just like Python, however every ``for`` loop and ``if`` block in Pyramid must end with an ``endfor``/``endif``. As with looping in Python, as long as the variable being referenced by the loop is an iterable, you can alias the individual items within the iterable and use those items in your code.

Let's look at another aspect of the same template.

.. code-block:: python

    <a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a>

Before we saw ``request.route_url`` used to...request the url of the route named ``home``. Now we're seeing it used to get the url for the ``detail`` route, but note in ``routes.py`` that the ``detail`` route takes the keyword ``id``. Up to now we've been bypassing this by just providing a number that would fit the bill. In this case, we have to provide any keywords we want to reference in the url as an argument to ``request.route_url``.

Finally, you'll need to connect this new renderer to your listing view. Since we need to display data on the page, we have to feed it data to be displayed. Let's alter views.py:

.. code-block:: python

    # ...
    ENTRIES = [
        {"title": "LJ - Day 10", "creation_date": "Aug 19, 2016", "id": 10, "body": "Sample body text."},
        {"title": "LJ - Day 11", "creation_date": "Aug 22, 2016", "id": 11, "body": "Sample body text."},
        {"title": "LJ - Day 12", "creation_date": "Aug 23, 2016", "id": 12, "body": "Sample body text."},
    ]

    @view_config(route_name='home', renderer='templates/list.jinja2')
    def list_view(request):
        return {"entries": ENTRIES}

    #...

``ENTRIES`` here is a rare global variable because you're going to want to use this for your ``detail`` view tonight. When we discuss models tomorrow, we'll dispose of this entirely.

We can now see our list page in all its glory. Let's try starting the server:

.. code-block::

    (pyramid_lj) bash-3.2$ pserve development.ini 
    Starting server in PID 53587.
    serving on http://127.0.0.1:6543

View the home page of your journal at http://localhost:6543/. Click on the link to an entry, and it should route you to the detail view.

These views are reasonable, if quite plain. There's also code between them that's repeated **heavily**, and we want to do our best to keep code DRY. Let's put our templates into something that looks more like a website.

Template Inheritance
--------------------

Jinja2 allows you to combine templates using something called `template inheritance <http://jinja.pocoo.org/docs/dev/templates/#template-inheritance>`_. You can create a basic page structure, and then *inherit* that structure in other templates.

Let's make a template for the basic outer structure of our pages. The following code will serve as our page template, and will go into a file called ``layout.jinja2``. Save that file to your ``templates`` directory. Here's the code:

.. code-block:: python

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Python Learning Journal</title>
            <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
        </head>
    <body>
    <header>
        <nav>
            <ul>
                <li>
                    <a href="{{ request.route_url('home') }}">Home</a>
                </li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>My Python Journal</h1>
        <section id="content">
            {% block body %}{% endblock %}
        </section>
    </main>
    </body>
    <footer>
        <p>Created in the Code Fellows 401 Python Program</p>
    </footer>
    </html>

The important part here is the ``{% block body %}...{% endblock %}`` expression. This is a template **block** and it is a kind of placeholder. Other templates can inherit from this one, and fill that block with additional HTML.

Let's update our ``detail`` and ``list`` templates:

.. code-block:: python

    {% extends "layout.jinja2" %}
    {% block body %}
    <!-- the meat for each page goes here -->
    {% endblock %}

Start the server so we can see the result.

.. code-block::

    (pyramid_lj) bash-3.2$ pserve development.ini 
    Starting server in PID 53587.
    serving on http://127.0.0.1:6543

Start at the home page, click on an entry, and it should still work. Now, you've shared page structure that is in both.

Static Assets
-------------

Although we have a shared structure, it isn't particularly nice to look at. Aspects of how a website looks are controlled by CSS (*Cascading Style Sheets*). Stylesheets are one of what we generally speak of as *static assets*.

Other static assets include *images* that are part of the site's design (logos, button images, etc) and *JavaScript* files that add client-side dynamic behavior.

Serving static assets in Pyramid requires adding a *static view* to configuration. Luckily, it's a simple addition for us to get and serve these assets.

.. code-block:: python

    # in learning_journal/__init__.py
    # ...
    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.routes')
        # add this next line
        config.add_static_view(name='static', path='learning_journal:static')
        config.scan()
        return config.make_wsgi_app()

* The first argument to ``add_static_view`` is a name that will need to appear in the path of URLs requesting assets.
* The second argument is a *path* that is relative to the package being configured. Assets referenced by the *name* in a URL will be searched for in the location defined by the *path*.
* Additional keyword arguments control other aspects of how the view works.

Once you have a static view configured, you can use assets in that location in templates. The *request* object in Pyramid provides a ``static_path`` method that will render an appropriate asset path for us.

Add the following to your ``layout.jinja2`` template:

.. code-block:: python

    <head>
      # stuff that was here before
      <link href="{{ request.static_path('learning_journal:static/style.css') }}" rel="stylesheet">
    </head>
    # everything else

The **one required argument** to ``request.static_path`` is a *path* to an asset. Note that because any package *might* define a static view with the directory name ``static``, we have to specify which package we want to look in. That's why we have ``learning_journal:static/style.css`` in our call.

Create a very basic style for your learning journal and add it to ``learning_journal/static``. Then, restart your web server and see what a difference a little style makes.

Testing Your Pyramid App
========================

Thus far we have written tons of code for handling HTTP routing and filling templates with data, but we haven't yet written any tests of our own to make sure that things work the way that we need them to work. We can fortunately do this with a combination of Pyramid's own ``testing`` module, as well as the ``unittest`` package from ``pytest``. When it comes to testing your Pyramid app, you need to not only do unit tests for individual pieces of functionality. You need to test for how things perform when in practice. For example, if your app sends an email, you need to check that the email is actually sent.

Setting Up a Test for a View
----------------------------

Our scaffold provided for us a ``tests.py`` file. Let's inspect it.

.. code-block:: python

    # tests.py
    import unittest

    from pyramid import testing


    class ViewTests(unittest.TestCase):
        def setUp(self):
            self.config = testing.setUp()

        def tearDown(self):
            testing.tearDown()

        def test_my_view(self):
            from .views import my_view
            request = testing.DummyRequest()
            info = my_view(request)
            self.assertEqual(info['project'], 'learning_journal')


    class FunctionalTests(unittest.TestCase):
        def setUp(self):
            from learning_journal import main
            app = main({})
            from webtest import TestApp
            self.testapp = TestApp(app)

        def test_root(self):
            res = self.testapp.get('/', status=200)
            self.assertTrue(b'Pyramid' in res.body)

We use the ``unittest`` package provided by ``pytest``, which was specified in our ``setup.py`` file in the ``tests_require`` list.

``unittest`` comes with a ``TestCase`` object that we can inherit from and modify. When we inherit from ``TestCase``, we get access to a ton of ``asserts``, such as the ``assertEqual`` and ``assertTrue`` seen here, as well as functionality for setting up a testing environment (``setUp``) and tearing it down (``tearDown``). This is not Pyramid-specific, but available whenever we import ``unittest``. 

As part of the setup, we have pyramid's own ``testing`` object, which allows us to set up the configuration we need to run our app and have access to the ``request`` and ``response`` objects that we need to test our views. Recall that our views can only run when taking a ``request`` object as an argument. So, we provide a ``request`` with ``testing.DummyRequest``.

Let's comment out ``FunctionalTests`` bit for now (I'm removing it entirely) and for the moment just focus on ``ViewTests``. Let's also replace ``my_view`` with ``detail_view``. Finally, recall that our ``detail_view`` returns a dictionary, with the "title", "creation_date", and "body" of a sample learning journal entry. Let's make our test reflect that, checking that "title" is an attribute of our ``detail_view``'s return statement. For now, we'll be working with this:

.. code-block:: python

    # tests.py
    import unittest

    from pyramid import testing


    class ViewTests(unittest.TestCase):
        def setUp(self):
            self.config = testing.setUp()

        def tearDown(self):
            testing.tearDown()

        def test_detail_view(self):
            from .views import detail_view
            request = testing.DummyRequest()
            info = detail_view(request)
            self.assertIn("title", info.keys())
 

Running Pyramid Tests
---------------------

To run this test we have to first install all the things we need for testing. We defined those in our ``setup.py`` so just navigate to the project root and install like so:

.. code-block:: 

    (pyramid_lj) bash-3.2$ pip install -e ".[testing]"

In between the quotes we have ``.[testing]`` because we want to install everything in the current directory (the ``.``), but we want the extra packages that we specified for testing. If you have other extra packages you want for some other reason, you install them in this fashion.

Now that all is installed, run our test!

.. code-block:: 

    py.test learning_journal/tests.py -q

We've designed this one test to pass, so we should get a statement saying it passes. Spectacular. But we want to test across versions of Python, so we need to incorporate ``tox``. Recall that when we first set up our app via the scaffold, we added ``tox`` into ``tests_require``. When we pip-installed ``testing`` above, tox was installed along with everything else. Now we just have to construct our ``tox.ini`` configuration file so that we can run tox. Let's add a little bit more to our tox file than we usually do. We don't want to just run our tests across versions, we ultimately want to make sure that our app is well-tested across everything we've written. We want to add coverage. So, our tox file should look like the following:

.. code-block::

    [tox]
    envlist = py27, py35

    [testenv]
    commands = py.test --cov=learning_journal learning_journal/tests.py -q
    deps =
        pytest
        pytest-cov
        webtest

Now we run tox as we always have and ensure that our test passes across Python 2.7 and 3.5. On top of that, we get a report of the coverage of our tests in the console. 

.. code-block::

    ---------- coverage: platform darwin, python 3.5.1-final-0 -----------
    Name                           Stmts   Miss  Cover
    --------------------------------------------------
    learning_journal/__init__.py       7      5    29%
    learning_journal/routes.py         6      6     0%
    learning_journal/views.py         10      3    70%
    --------------------------------------------------
    TOTAL                             23     14    39%

    1 passed in 1.48 seconds

This seems trivial now because in this particular moment we're just testing that the view is returning the data that we put into it in the first place. That's OK, even trivial tests are still evidence that your code works. Tomorrow when we talk about data models and hook those up to our views, testing our views will involve several more bits.

Enter Functional Tests
----------------------

As the name implies, functional tests verify that various components of our app function together as they should. We'll use functional tests to "look" at our front-end and make sure that what's being displayed is what we expect. To set up our functional tests we again inherit from the ``unittest.TestCase`` object. We then set up a "working" version of our app and use HTTP methods on our routes. As an example (expanded from what was provided by the scaffold):

.. code-block:: python

    class FunctionalTests(unittest.TestCase):
        def setUp(self):
            from learning_journal import main
            app = main({})
            from webtest import TestApp
            self.testapp = TestApp(app)

        def test_layout_root(self):
            """Tests that our layout template is present in the rendered root"""
            response = self.testapp.get('/', status=200)
            self.assertTrue(b'Created in the Code Fellows 401 Python Program' in response.body)

        def test_root_contents(self):
            """Tests that the contents of the root page contains <article>"""
            response = self.testapp.get('/', status=200)
            self.assertTrue(b'<article>' in response.body)

Here, we set up a new WSGI app instance by providing our ``main`` function, which is already taking our base global configuration, with an empty dict for settings. ``webtest.TestApp`` wraps that app to provide some additional functionality, such as the ability to send ``GET`` requests to a given route. ``WebTest`` is a great app for testing functionality with respect to real HTTP requests, but it can do so much more (even check for cookies!). `Read the documentation <http://webtest.pythonpaste.org/en/latest/api.html#webtest.app.TestApp>`_ for more details about how ``WebTest`` can help you write robust tests for your web app.

This is great and all, however it seems somewhat silly to test for HTML elements and content using byte strings. It would be great if a package existed that specialized in collecting and picking apart the DOM.

The BeautifulSoup Interlude
---------------------------

`Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ is a Python package for reading and working with HTML as if you were traversing the DOM. Luckily for us, Pyramid installed BeautifulSoup for us when it was itself installed. ``pip freeze`` for evidence of this (and other packages you may not know you had access to). Let's fire up ``pshell`` and use it a little.

.. code-block:: ipython

    In [1]: from bs4 import BeautifulSoup

``bs4`` is the package name, and BeautifulSoup is an object that we use to wrap HTML so that we can parse it apart. Let's give it some of the HTML that we wrote for our mockups before we knew about the joys of templates.

.. code-block:: ipython

    In [2]: some_html = open("learning_journal/templates/sample.html").read()
    In [3]: print(some_html)
    <html>
        <head>
            <link rel="stylesheet" href="static/style.css" type="text/css" />
        </head>
        <body>
            <h1>This is styled HTML</h1>
            <ul>
                <li>One</li>
                <li>Two</li>
                <li>Three</li>
            </ul>
        </body>
    </html>

In order to actually interact with the HTML à la DOM traversal, we must first wrap our HTML in a ``BeautifulSoup`` instance.

.. code-block:: ipython

    In [4]: soup = BeautifulSoup(some_html, 'html.parser')

If we don't specify the parser, ``BeautifulSoup`` uses the best-available parser, and will tell you so with a nice verbose warning.

.. code-block:: ipython

    In [5]: tmp_soup = BeautifulSoup(some_html)
    /Users/Nick/Documents/codefellows/courses/code401_python/pyramid_lj/lib/python3.5/site-packages/bs4/__init__.py:166: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

    To get rid of this warning, change this:

     BeautifulSoup([your markup])

    to this:

     BeautifulSoup([your markup], "html.parser")

      markup_type=markup_type))

So, be sure to specify your parser. Note, there are other parsers that you can install. Check the docs for more info.

We've now made our ``soup`` object and it comes packed with some useful methods and attributes. One of these is ``soup.findAll('html_element')``. When given the appropriate HTML element, like say ``'li'``, it'll find every instance of that object and return it to you in a ``list``-like object.

.. code-block:: ipython

    In [6]: soup.findAll("li")
    Out[6]: [<li>One</li>, <li>Two</li>, <li>Three</li>]

    In [7]: type(soup.findAll("li"))
    Out[7]: bs4.element.ResultSet

    In [8]: these_results = soup.findAll("li")
    In [9]: len(these_results)
    Out[9]: 3

You can also inspect individual DOM elements. For example, I may want to check what's actually contained within the text of my ``<h1>`` tag. It's simple with ``BeautifulSoup``.

.. code-block:: ipython

    In [10]: h1 = soup.find("h1")
    In [11]: h1.get_text()
    Out[11]: 'This is styled HTML'

You don't just have to inspect the body of the document either. You can look at anything that was a part of that HTML document. For example, I may want to look into the ``link`` tag at the top. With ``BeautifulSoup`` I can look at the individual attributes that comprise it.

.. code-block:: ipython

    In [12]: style = soup.find("link")
    In [13]: print(style)
    <link href="static/style.css" rel="stylesheet" type="text/css"/>

    In [14]: style.attrs
    Out[14]: {'href': 'static/style.css', 'rel': ['stylesheet'], 'type': 'text/css'}

Of course this is only a cursory look, but ``BeautifulSoup`` goes deep and wide, and is entirely worth dipping into. Even though we've only scratched the surface of ``BeautifulSoup``, we can use what we've seen thus far to more thoroughly test our fledgling app.

Return of the Functional Test
-----------------------------

Recall our functional test, specifically the one that renders the home page.

.. code-block:: python

    def test_root_contents(self):
        """Tests that the contents of the root page contains <article>"""
        response = self.testapp.get('/', status=200)
        self.assertTrue(b'<article>' in response.body)

This page is supposed to put up an ``<article>`` tag for every given journal entry. That being the case, we should make sure that there are as many tags on the page as journal entries. ``BeautifulSoup`` makes that possible.

.. code-block:: python

    def test_root_contents(self):
        """Tests that the contents of the root page contains as many <article> tags as journal entries"""
        from .views import ENTRIES
        from bs4 import BeautifulSoup as Soup

        response = self.testapp.get('/', status=200)
        soup = Soup(response.body, 'html.parser')
        self.assertEqual(len(ENTRIES), len(soup.findAll("article")))

That's our new functional test for the home page. Notice that instead of simply testing for the existence of any article tag, it tests specifically that the number on the page matches the number of journal entries. This is the type of test you want, and you can keep the general form of this one the same when we incorporate data models (with some minor tweaks). Now, run ``tox`` and look at that sweet, sweet coverage:

.. code-block::

    ---------- coverage: platform darwin, python 3.5.1-final-0 -----------
    Name                                             Stmts   Miss  Cover
    --------------------------------------------------------------------
    learning_journal_basic/__init__.py                   7      0   100%
    learning_journal_basic/routes.py                     6      0   100%
    learning_journal_basic/views.py                     10      2    80%
    --------------------------------------------------------------------
    TOTAL                                               23      2    91%

    3 passed in 1.71 seconds

Woo!


Recap
=====

Today's work involved a lot of refactoring, switching to Jinja2 templates, and finally dipping our feet into testing. Specifically, we used Pyramid's built-in ``view_config`` decorator to wire our views to the appropriate renderers, removing the need to manually include views and connect routes to those views. 

We then of course made the appropriate renderers using Jinja2 templates. Within those templates, we used placeholders with Jinja2 syntax to wire the data we wanted into the appropriate places without having to manually include them. We also saw how we could even make our front-end DRY by using template inheritance, creating a master ``layout.jinja2`` template that wrapped each page as needed.

Finally, we saw how to write unit tests for individual views, providing our view callable with a dummy HTTP request and inspecting the data that resulted from that view being called. In this process, we saw how we could use Pyramid's own ``testing`` module to set up a dummy app and send requests without having to access the browser. We then stepped into functional tests, seeing how we could validate our front-end after the data has been passed and the page has been rendered. Lastly, we saw how we could use ``BeautifulSoup`` to make our front-end tests more robust, piecing apart the rendered HTML itself and ensuring that the contents of our page match our expectations at a functional level.

Tonight you will use these to update your learning journal app with sensible DRY templates and connections between views and routes using the declarative style of ``view_config``. You will then write comprehensive tests for your individual views as well as your front end. Tomorrow, we'll stop messing about with hard-coded data and learn how we can use Pyramid models and SQL persistence for a more robust web app.