====================================
Pyramid Routes, Views, and Templates
====================================

Last time we discussed the **model** part of the *MVC* application design pattern. We set up a project using the Pyramid web framework and the SQLAlchemy library for persisting our data to a database. We looked at how to define a simple model by investigating the demo model created on our behalf.

Finally, we briefly covered how we can interact with this model at the command line with ``pshell`` to make sure we've got it right. Now we move forward toward displaying the data that we save to the database.

The MVC Controller
==================

Let's go back to thinking for a bit about the *Model-View-Controller* pattern.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
    :width: 275px
    :alt: By Alan Evangelista (Own work) [CCo]
    :align: center

    By Alan Evangelista (Own work) [CCo], via Wikimedia Commons

Today we'll dig into *controllers* and *views*, or as we will know them in Pyramid: *views* and *renderers*.

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

Most web frameworks now call the *path* a **route**, and provide a way of matching *routes* to the code that will be run to handle requests. In our Pyramid scaffold, routes are handled as *configuration* and are included in the *main* function in ``__init__.py``:

.. code-block:: python

    # __init__.py
    def main(global_config, **settings):
        # ...
        config.include('.routes')
        # ...

That ``config.include`` function will look in the ``routes.py`` module in the same directory for a function called ``includeme``, which tells Pyramid what routes to add (amongst other things):

.. code-block:: python

    # routes.py
    def includeme(config):
        # ...
        config.add_route('home', '/')

Our Pyramid scaffold created a sample route for us, using the ``add_route`` method of the Configurator class. The ``add_route`` method has two required arguments: a **name** and a **pattern**. In our sample route, the *name* is ``'home'``, and the *pattern* is ``'/'``.

When a request comes in to a Pyramid application, the framework looks at all the *routes* that have been configured. One by one, in order, it tries to match the path of the incoming request against the *pattern* of the route. As soon as a *pattern* matches the *path* from the incoming request, that route is used and no further matching is performed. If no route is found that matches, then the request will automatically get a **404 Not Found** error response.

In our sample app, we have one sample *route* named ``'home'``, with a pattern of ``'/'``. This means that any request that comes in for ``/`` will be matched to this route, and any other request will be **404**.

In a very real sense, the *routes* defined in an application *are* the public API. Any route that is present represents something the user can do. Any route that is not present is something the user cannot do.

You can use the proper definition of routes to help conceptualize what your app will do. What routes might we want for a learning journal application? What will our application do?

Adding Routes
~~~~~~~~~~~~~

Let's add routes for our application. Open ``learning_journal/routes.py``.

For our list page, the existing ``home`` route will do fine, so leave it as is. Add the following two routes:

.. code-block:: python

    # in learning_journal/routes.py

    config.add_route('home', '/') # already there
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('action', '/journal/{action}')

* The ``detail`` route will serve a single journal entry, identified by the provided ``id``.
* The ``action`` route will serve ``create`` and ``edit`` actions, which will be encapsulated in views, depending on the ``action`` specified.

In both cases, we want to capture a portion of the matched path to use information it provides. In a pattern, you can capture a *path segment replacement marker*, a valid Python symbol surrounded by curly braces:

.. code-block:: python

    /home/{foo}/

If you want to match a particular pattern, add a *regular expression*. In the following example, we specify that we want digits only with ``\d+``:

.. code-block:: python

    /journal/{id:\d+}

Matched path segments are captured in a ``matchdict``:

.. code-block:: python

    # pattern           # actual url    # matchdict
    /journal/{id:\d+}   /journal/27     {'id': '27'}

The ``matchdict`` is made available as an attribute of the *request object*. More on that soon.

Views in Pyramid

In Pyramid, a *route* is connected by configuration to a *view*. In our app, two sample views have been created for us in ``views/default.py`` and ``views/notfound.py``. Let's inspect the former:

.. code-block:: python

    # in learning_journal/views/default.py
    # ...
    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def my_view(request):
        # ...

**THE ORDER IN WHICH ROUTES ARE CONFIGURED IS IMPORTANT**, so that must be done with some mindfulness in ``learning_journal/routes.py``. The order in which views are connected to routes *is not important*, so the *declarative* ``@view_config`` decorator can be used. When ``config.scan`` is called in ``learning_journal/__init__.py``, all files in our application are searched for such *declarative configuration* and it is added.

The Pyramid View
----------------

Let's imagine that a *request* has come to our application for the path ``'/'``. The framework made a match of that path to a *route* with the pattern ``'/'``. Configuration connected that route to a *view* in our application. Now, the view that was connected will be *called*, which brings us to the nature of *views*.

.. note:: A Pyramid View is a callable that takes `request` as an argument.

The view can then use information from that request to build appropriate data, perhaps using the application's *models*. Then, it returns the data it assembled, passing it to a `renderer <http://docs.pylonsproject.org/projects/pyramid/en/1.7-branch/narr/renderers.html>`_. Which *renderer* to use is determined, again, by configuration:

.. code-block:: python

    # in learning_journal/views/default.py
    # ...
    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def my_view(request):
        # ...

More about this in a moment.

The *view* stands at the intersection of *input data*, the application *model* and *renderers* that offer rendering of the results. **Pyramid Views are the Controllers in our MVC application**.

Let's add a few of our own. Comment out the default ``my_view`` function along with its ``@view_config`` decorator and add temporary views to our application in ``learning_journal/views/default.py``.

.. code-block:: python

    @view_config(route_name='home', renderer='string')
    def index_page(request):
        return 'list page'

    @view_config(route_name='detail', renderer='string')
    def view(request):
        return 'detail page'

    @view_config(route_name='action', match_param='action=create', renderer='string')
    def create(request):
        return 'create page'

    @view_config(route_name='action', match_param='action=edit', renderer='string')
    def update(request):
        return 'edit page'

Let's verify that our view configuration has worked. Make sure your ``virtualenv`` is properly activated and start the web server with ``pserve``:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini
    Starting server in PID 46797.
    serving on http://127.0.0.1:6543

Now try viewing some of the expected application urls (remember your available routes!):

* http://localhost:6543/
* http://localhost:6543/journal/1
* http://localhost:6543/journal/create
* http://localhost:6543/journal/edit

Note what happens if you visit a URL that isn't specified in our routes.

Now that we've got temporary views that work, we can fix them to get the information from our database. We'll begin with the list view, which will list our individual Learning Journal entries. We need some code that will fetch all the journal entries we've written, in reverse order (newest at the top), and hand that collection back for rendering.

.. code-block:: python

    # in learning_journal/views/default.py
    # ...

    from ..models import (
        Entry, # <- Add this import. It should be the new model you made last night
    )

    # and update this view function
    @view_config(route_name='home', renderer='string')
    def index_page(request):
        entries = request.dbsession.query(Entry).all()
        return {'entries': entries}

Next, we want to write the view for a single entry. We'll need to use the ``id`` value of our route captured in ``request.matchdict``. Remember that ``matchdict`` is an attribute of the ``request`` object. We'll get the ``id`` from there, and use it to query for the correct entry.

.. code-block:: python

    # still in learning_journal/views/default.py
    # add this next import at the top
    from pyramid.httpexceptions import HTTPNotFound

    # ...
    # and update this view function
    @view_config(route_name='detail', renderer='string')
    def view(request):
        this_id = request.matchdict.get('id', -1)
        entry = request.dbsession.query(Entry).get(this_id)
        if not entry:
            return HTTPNotFound()

        return {'entry': entry}

We can now verify that these views work correctly. Start the web server back up.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini
    Starting server in PID 46797.
    serving on http://127.0.0.1:6543

Then try viewing the list page and the entry page.

* http://localhost:6543/
* http://localhost:6543/journal/1

What happens when you request an entry with an id that isn't in the database?

* http://localhost:6543/journal/100

The MVC View
============

Again, back to the *Model-View-Controller* pattern. We've built a *model* and we've created some *controllers* that use it. In Pyramid, we call *controllers* **views** and they are callables that take *request* as an argument. Let's turn to the last piece of the *MVC* pattern, the *view*.

Presenting Data
---------------

The job of the *view* in the *MVC* pattern is to present data in a format that is readable to the user of the system. There are many ways to present data. Some are readable by humans (e.g. tables, charts, graphs, HTML pages, text files), while others are more for machines (e.g. xml files, csv, json). Which of these formats is the *right one* depends on your purpose. What is the purpose of our learning journal?

Pyramid Renderers
-----------------

In Pyramid, the job of presenting data is performed by a *renderer*. So we can consider the Pyramid **renderer** to be the *view* in our *MVC* app.

We've already seen how we can connect a *renderer* (MVC view) to a Pyramid *view* (MVC controller) with configuration. In fact, we've already done so, using a built-in renderer called ``'string'``. This renderer converts the return value of its *view* to a string and sends that back to the client as an HTTP response. But the result doesn't look all that nice.

The *built-in renderers* (``'string'``, ``'json'``, ``'jsonp'``) in Pyramid are not the only ones available. There are add-ons to Pyramid that support using various *template languages* as renderers. In fact, one of these was installed by default when you created the scaffold for this project.

.. code-block:: python

    # in setup.py
    requires = [
        # ...
        'pyramid_jinja2',
        # ...
    ]

    # in learning_journal/__init__.py
    def main(global_config, **settings):
        # ...
        config.include('pyramid_jinja2')
        # ...

The ``pyramid_jinja2`` package supports using the *Jinja2* template language. Let's learn a bit about how `Jinja2 templates <http://jinja.pocoo.org/docs/templates/>`_ work.

Jinja2 Template Basics
----------------------

We'll start with the absolute basics. Fire up an iPython interpreter in your virtual environment.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ ipython
    ...
    In [1]:

Then import the `Template` class from the `jinja2` package:

.. code-block:: ipython

    In [1]: from jinja2 import Template

A template is constructed with a simple string:

.. code-block:: ipython

    In [2]: t1 = Template("Hello {{ name }}, how are you")

Here, we've simple typed the string directly, but it is more common to build a template from the contents of a *file*.

Notice that our string has some odd stuff in it: ``{{name}}``. This is called a *placeholder*, and when the template is *rendered* it is replaced. We can see that if we call ``t1``'s ``render`` method, providing *context* for ``{{name}}``:

.. code-block:: ipython

    In [3]: t1.render(name="Freddy")
    Out[3]: 'Hello Freddy, how are you'

    In [4]: t1.render(name="Gloria")
    Out[4]: 'Hello Gloria, how are you'

*Context* can either be keyword arguments, or a dictionary. Note the resemblance to the string formatting we've seen before:

.. code-block:: ipython

    In [5]: "This is {owner}'s string".format(owner="Cris")
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

Our Templates
-------------

There's more that Jinja2 templates can do, but it will be easier to introduce you to that in the context of a working template. So let's make some.

We have a Pyramid ``view`` that returns a single entry. Let's create a template to show it. In ``learning_journal/templates/`` create a new file ``detail.jinja2``:

.. code-block:: html

    <article>
        <h1>{{ entry.title }}</h1>
        <hr/>
        <p>{{ entry.body }}</p>
        <hr/>
        <p>Created <strong title="{{ entry.created }}">{{entry.created}}</strong></p>
    </article>

Then wire it up to the detail view in ``learning_journal/views/default.py``:

.. code-block:: python

    # views.py
    @view_config(route_name='detail', renderer='../templates/detail.jinja2')
    def view(request):
        #...

Now we should be able to see some rendered HTML for our journal entry details. Start up your server:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini
    Starting server in PID 53587.
    serving on http://127.0.0.1:6543

Then try viewing an individual journal entry: http://localhost:6543/journal/1

Let's now create a template such that our index shows a list of journal entries. In ``learning_journal/templates/`` create a new file ``list.jinja2``:

.. code-block:: python

    {% if entries %}
    <h2>Journal Entries</h2>
    <ul>
      {% for entry in entries %}
        <li>
        <a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a>
        </li>
      {% endfor %}
    </ul>
    {% else %}
    <p>This journal is empty</p>
    {% endif %}

It's worth taking a look at a few specifics of this template.

.. code-block:: python

    {% for entry in entries %}
    ...
    {% endfor %}

Jinja2 templates are rendered with a *context*. A Pyramid *view* returns a dictionary, which is passed to the renderer as part of that *context*. This means we can access values we return from our *view* in the *renderer* using the names we assigned to them.

Let's look at another aspect of the same template.

.. code-block:: python

    <a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a>

The *request* object is also placed in the context by Pyramid. ``request`` has a method ``route_url`` that will create a URL for a named route. This allows you to include URLs in your template without needing to know exactly what they will be. This process is called *reversing*, since it's a bit like a reverse phone book lookup.

Finally, you'll need to connect this new renderer to your listing view:

.. code-block:: python

    @view_config(route_name='home', renderer='../templates/list.jinja2')
    def index_page(request):
        #...

We can now see our list page too. Let's try starting the server:

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pserve development.ini
    Starting server in PID 53587.
    serving on http://127.0.0.1:6543

Then try viewing the home page of your journal at http://localhost:6543/. Click on the link to an entry, and it should route you to that entry.

These views are reasonable, if quite plain. It'd be nice to put them into something that looks more like a website.

Jinja2 allows you to combine templates using something called `template inheritance <http://jinja.pocoo.org/docs/dev/templates/#template-inheritance>`_. You can create a basic page structure, and then *inherit* that structure in other templates.

Let's make a template for the basic outer structure of our pages. The following code will serve as our page template, and will go into a file called ``layout.jinja2``. Save that file to your templates directory. Here's the code:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Python Learning Journal</title>
        <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
      </head>
      <body>
        <header>
          <nav><ul><li><a href="{{ request.route_url('home') }}">Home</a></li></ul></nav>
        </header>
        <main>
          <h1>My Python Journal</h1>
          <section id="content">{% block body %}{% endblock %}</section>
        </main>
        <footer><p>Created in the Code Fellows 401 Python Program</p></footer>
      </body>
    </html>

The important part here is the ``{% block body %}...{% endblock %}`` expression. This is a template **block** and it is a kind of placeholder. Other templates can inherit from this one, and fill that block with additional HTML.

Let's update our detail and list templates:

.. code-block:: html+jinja

    {% extends "layout.jinja2" %}
    {% block body %}
    <!-- everything else that was already here goes here -->
    {% endblock %}

Start the server so we can see the result.

.. code-block:: bash

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
        config.include('.models')
        config.include('.routes')
        # add this next line
        config.add_static_view(name='static', path='learning_journal:static')
        config.scan()
        return config.make_wsgi_app()

* The first argument to ``add_static_view`` is a name that will need to appear in the path of URLs requesting assets.
* The second argument is a *path* that is relative to the package being configured. Assets referenced by the *name* in a URL will be searched for in the location defined by the *path*.
* Additional keyword arguments control other aspects of how the view works.

Once you have a static view configured, you can use assets in that location in templates. The *request* object in Pyramid provides a ``static_path`` method that will render an appropriate asset path for us.

Add the following to our ``layout.jinja2`` template:

.. code-block:: html+jinja

    <head>
      <!-- ... -->
      <link href="{{ request.static_path('learning_journal:static/style.css') }}" rel="stylesheet">
    </head>

The **one required argument** to ``request.static_path`` is a *path* to an asset. Note that because any package *might* define a static view, we have to specify which package we want to look in. That's why we have ``learning_journal:static/style.css`` in our call.

Create a very basic style for your learning journal and add it to ``learning_journal/static``. Then, restart your web server and see what a difference a little style makes.

Getting Interactive
===================

We have a site that allows us to view a list of journal entries. We can also view details of a single entry. However, as yet, we don't really have any *interaction* in our site yet. *We can't create new entries.* Let's add that functionality next.

User Input
----------

In HTML websites, the traditional way of getting input from users is via `HTML forms <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms>`_. Forms use *input elements* to allow users to enter data, pick from drop-down lists, or choose items via checkbox or radio button.

It is possible to create plain HTML forms in templates and use them with Pyramid. It's a lot easier, however, to work with a *form library* to create forms, render them in templates, and interact with data sent by a client.

We'll be using a form library called `WTForms <http://wtforms.readthedocs.org/en/latest/>`_ in our project. The first step to working with this library is to install it. Start by including the library as a *dependency* of our package by adding it to the *requires* list in ``setup.py``:

.. code-block:: python

    requires = [
        #...
        'wtforms', # <- add this to the list
    ]

Then, in the root directory for this project, re-install our package to download and install the new dependency.

.. code-block:: bash

    (pyramid_lj) bash-3.2$ pip install -e .

Using WTForms
-------------

We'll want a form to allow a user to create a new Journal Entry.

Add a new file called ``forms.py`` to our learning_journal package in ``learning_journal/models``:

.. code-block:: python

    from wtforms import Form, StringField, TextAreaField, validators

    strip_filter = lambda x: x.strip() if x else None

    class EntryCreateForm(Form):
        title = StringField(
            'Entry title',
            [validators.Length(min=1, max=255)],
            filters=[strip_filter]
        )
        body = TextAreaField(
            'Entry body',
            [validators.Length(min=1)],
            filters=[strip_filter]
        )

Just like we imported our ``Entry`` model into ``learning_journal/models/__init__.py``, we have to give our app access to our ``EntryCreateForm`` form model. So add the following line to ``__init__.py``, right under where you import your ``Entry`` model.

.. code-block:: python

    # in learning_journal/models/__init__.py
    # ...
    from .entries import Entry
    from .forms import EntryCreateForm
    # ...

Next, we need to add a new view that users this form to create a new entry. Add this to ``learning_journal/views/default.py``:

.. code-block:: python

    # add these imports
    from pyramid.httpexceptions import HTTPFound
    from ..models import (
        Entry,
        EntryCreateForm,
    )

    import transaction # <-- allows us to commit our changes to the database
    # ...

    # and update this view function
    def create(request):
        entry = Entry()
        form = EntryCreateForm(request.POST)
        if request.method == "POST" and form.validate():
            entry = Entry(title=form.title.data, body=form.body.data)
            request.dbsession.add(entry)
            transaction.commit()
            return HTTPFound(location=request.route_url('home'))

        return {'form': form, 'action': request.matchdict.get('action')}

We already have a route that connects here. Let's test it. Start your server and try connecting to the ``action`` route at http://localhost:6543/journal/create. You should see something like this:

.. code-block:: python

    {'form': <learning_journal.models.forms.EntryCreateForm object at 0x104ded2e8>, 'action': 'create'}

Finally, we need to create a template that will render our form. Add a new template called ``edit.jinja2`` in ``learning_journal/templates/``

.. code-block:: python

    {% extends "templates/layout.jinja2" %}
    {% block body %}
    <form action="" method="POST">
    {% for field in form %}
      {% if field.errors %}
        <ul>
        {% for error in field.errors %}
            <li>{{ error }}</li>
        {% endfor %}
        </ul>
      {% endif %}
        <p>{{ field.label }}: {{ field }}</p>
    {% endfor %}
        <p><input type="submit" name="submit" value="Submit" /></p>
    </form>
    {% endblock %}

You need to update the ``view_config`` for the ``create`` view to use this new renderer. Update the configuration in ``learning_journal/views/default.py``

.. code-block:: python

    # ...
    @view_config(route_name='action', match_param='action=create', renderer='../templates/edit.jinja2')
    def create(request):
        # ...

Now restart your server and look at the results, at http://localhost:6543/journal/create

Great! Now you can add new entries to your journal. But in order to do so, you have to hand-enter the URL. You should add a new link in the UI somewhere that helps you get there more easily. Add the following to ``list.jinja2``:

.. code-block:: html+jinja

    {% extends "layout.jinja2" %}
    {% block body %}
    {% if entries %}
    ...
    {% else %}
    ...
    {% endif %}
    <!-- Add This Link -->
    <p><a href="{{ request.route_url('action', action='create') }}">New Entry</a></p>
    {% endblock %}

That way, you can get to your post-creation view from the front page!



