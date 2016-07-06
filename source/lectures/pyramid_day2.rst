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

The **one required argument** to ``request.static_path`` is a *path* to an asset. Note that because any package *might* define a static view, we have to specify which package we want to look in. That's why we have ``learning_journal:static/style.css`` in our call.

Create a very basic style for your learning journal and add it to ``learning_journal/static``. Then, restart your web server and see what a difference a little style makes.

Front-End Testing
=================



===================
TO DO
===================

Test the Front End

Recap
=====

