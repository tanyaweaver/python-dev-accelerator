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

.. code-block::
    
    http://www.codefellows.org/courses/code-401/advanced-software-development-in-python

Let's break that up into its constituent parts:

`http://`:
    This part is the *protocol*, it determines how the request will be sent.

`www.codefellows.org`:
    This is a *domain name*. It's the human-facing address for a server somewhere.

`/courses/code-401/advanced-software-development-in-python`:
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

Our Pyramid scaffold created a sample route for us, using the ``add_route`` method of the Configurator class. The ``add_route`` method has two required arguments: a **name** and a **pattern**. In our sample route, the *name* is `'home'`, and the *pattern* is `'/'`. 

When a request comes in to a Pyramid application, the framework looks at all the *routes* that have been configured. One by one, in order, it tries to match the path of the incoming request against the *pattern* of the route. As soon as a *pattern* matches the *path* from the incoming request, that route is used and no further matching is performed. If no route is found that matches, then the request will automatically get a **404 Not Found** error response.

In our sample app, we have one sample *route* named `'home'`, with a pattern of `'/'`. This means that any request that comes in for `/` will be matched to this route, and any other request will be **404**.

In a very real sense, the *routes* defined in an application *are* the public API. Any route that is present represents something the user can do. Any route that is not present is something the user cannot do. 

You can use the proper definition of routes to help conceptualize what your app will do. What routes might we want for a learning journal application? What will our application do?

Adding Routes
~~~~~~~~~~~~~

Let's add routes for our application. Open `learning_journal/routes.py`.

For our list page, the existing `home` route will do fine, so leave it as is. Add the following two routes:

.. code-block:: python 

    # in learning_journal/routes.py

    config.add_route('home', '/') # already there
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('action', '/journal/{action}')

* The `detail` route will serve a single journal entry, identified by the provided `id`. 
* The `action` route will serve `create` and `edit` actions, which will be encapsulated in views, depending on the `action` specified.

In both cases, we want to capture a portion of the matched path to use information it provides. In a pattern, you can capture a *path segment replacement marker*, a valid Python symbol surrounded by curly braces:

.. code-block:: python
    
    /home/{foo}/

If you want to match a particular pattern, add a *regular expression*. In the following example, we specify that we want digits only with `\d+`:

.. code-block:: python

    /journal/{id:\d+}

Matched path segments are captured in a `matchdict`:

.. code-block:: python 

    # pattern           # actual url    # matchdict
    /journal/{id:\d+}   /journal/27     {'id': '27'}

The `matchdict` is made available as an attribute of the *request object*. More on that soon.

Views in Pyramid

In Pyramid, a *route* is connected by configuration to a *view*. In our app, two sample views have been created for us in `views/default.py` and `views/notfound.py`. Let's inspect the former:

.. code-block:: python

    # in learning_journal/views/default.py
    # ...
    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def my_view(request):
        # ...

**THE ORDER IN WHICH ROUTES ARE CONFIGURED IS IMPORTANT**, so that must be done with some mindfulness in `learning_journal/routes.py`. The order in which views are connected to routes *is not important*, so the *declarative* `@view_config` decorator can be used. When `config.scan` is called in `learning_journal/__init__.py`, all files in our application are searched for such *declarative configuration* and it is added.

The Pyramid View
----------------

Let's imagine that a *request* has come to our application for the path `'/'`. The framework made a match of that path to a *route* with the pattern `'/'`. Configuration connected that route to a *view* in our application. Now, the view that was connected will be *called*, which brings us to the nature of *views*.

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

Let's add a few of our own. Comment out the default `my_view` function along with its `@view_config` decorator and add temporary views to our application in `learning_journal/views/default.py`.

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

Let's verify that our view configuration has worked. Make sure your `virtualenv` is properly activated and start the web server with `pserve`:

.. code-block::

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
        MyModel,
        Entry, # <- Add this import. It should be the new model you made last night
    )

    # and update this view function
    @view_config(route_name='home', renderer='string')
    def index_page(request):
        entries = Entry.all()
        return {'entries': entries}

Next, we want to write the view for a single entry. We'll need to use the `id` value of our route captured in `request.matchdict`. Remember that `matchdict` is an attribute of the `request` object. We'll get the `id` from there, and use it to query for the correct entry.

.. code-block:: python

    # still in learning_journal/views/default.py
    # add this next import at the top
    from pyramid.httpexceptions import HTTPNotFound

    # ...
    # and update this view function
    @view_config(route_name='detail', renderer='string')
    def view(request):
        this_id = request.matchdict.get('id', -1)
        entry = Entry.by_id(this_id)
        if not entry:
            return HTTPNotFound()

        return {'entry': entry}

We can now verify that these views work correctly. Start the web server back up.

.. code-block::

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









