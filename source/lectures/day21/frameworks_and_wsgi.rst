******************************
Introduction to Web Frameworks
******************************

.. rst-class:: left
.. container::

    We've been at this for a couple of weeks now.  We've learned a great deal:

    .. rst-class:: build

    * Sockets, the TCP/IP Stack and Basic Networking Mechanics
    * Web Protocols and the Importance of Clear Communication
    * APIs and Consuming Data from The Web
    * CGI and WSGI and Getting Information to Your Dynamic Applications
    * Building applications using a *framework*


Frameworks
==========

.. rst-class:: left
.. container::

    From Wikipedia:

        A web application framework (WAF) is a software framework that is
        designed to support the development of dynamic websites, web
        applications and web services. The framework aims to alleviate the
        overhead associated with common activities performed in Web
        development. For example, many frameworks provide libraries for
        database access, templating frameworks and session management, and they
        often promote code reuse


Abstraction
-----------

Great, but what does that really *mean*?

.. rst-class:: build
.. container::

    Well, it means that a *framework* is something you use to build an
    *application*.

    A framework allows you to build different kinds of applications.

    A framework abstracts what needs to be abstracted, and allows control of
    the rest.

Appropriate Abstractions
------------------------

Think back over the first half of class.

.. rst-class:: build
.. container::

    In particular, contrast the book db app you created using WSGI and your
    first full-scale web project.

    Compare the ease of routing in ``Flask`` with the way you solved the same
    problem for the book database.

    Think about how *general* the route system is in ``Flask`` and how
    *specific* your solution for the book database.

.. nextslide::

In writing a web app with WSGI, what were your pain points? Which bits do you
wish you didn't have to think about?

.. rst-class:: build
.. container::

    How about in the case of your Flask app?

    How about with using ``psycopg2`` directly?

    This last question is important when it comes to choosing a framework

    .. rst-class:: build

    * abstraction ∝ 1/freedom
    * The more they choose, the less you can
    * *Every* framework makes choices in what to abstract
    * *Every* framework makes *different* choices

    One important lesson to keep in mind: **Don't Fight the Framework**

.. nextslide:: Choices

There are scores of Python web frameworks (this is a partial list).

========= ======== ======== ========== ==============
Django    Grok     Pylons   TurboGears web2py
Zope      CubicWeb Enamel   Gizmo(QP)  Glashammer
Karrigell Nagare   notmm    Porcupine  QP
SkunkWeb  Spyce    Tipfy    Tornado    WebCore
web.py    Webware  Werkzeug WHIFF      XPRESS
AppWsgi   Bobo     Bo7le    CherryPy   circuits.web
Paste     PyWebLib WebStack Albatross  Aquarium
Divmod    Nevow    Flask    JOTWeb2    Python Servlet
Engine    Pyramid  Quixote  Spiked     weblayer
========= ======== ======== ========== ==============

.. nextslide:: Choices

.. ifslides::

    There are scores of Python web frameworks.

.. rst-class:: build

 * Each of them has made choices about the appropriate level of abstraction.
 * Each has made slightly different choices.
 * Picking the right one is an important choice.

Choosing a Framework
--------------------

Many folks will tell you "<XYZ> is the **best** framework".

.. rst-class:: build
.. container::

    In most cases, what they really mean is "I know how to use <XYZ>"

    In some cases, what they really mean is "<XYZ> fits my brain the best"

    What they usually forget is that everyone's brain (and everyone's use-case)
    is different.

.. nextslide::

Cris' First Law of Frameworks: **Pick the Right Tool for the Job**

.. rst-class:: build

First Corollary:
  The right tool is the tool that allows you to finish the job quickly and
  correctly.

Second Corollary:
  You can't know unless you try

.. nextslide::

You began with the current king of the micro-framework class, **Flask**.

.. rst-class:: build
.. container::

    Next you'll be working with the champion of the full-stack framework class,
    **Django**

    You'll also be asked to follow a tutorial on "the second most popular
    microframework and the second most popular full-stack framework",
    **Pyramid**

Frameworks and WSGI
===================

.. rst-class:: left
.. container::

    But quickly, before we move on to ``Django``, a word on WSGI and web
    frameworks.

    Modern Python web frameworks nearly all work as *wsgi apps*.

    This means that like your bookdb, you can serve them using a *wsgi server*.

    How exactly does that work?

Flask and WSGI
--------------

Consider the code for a simple ``hello world`` app in ``Flask``:

.. code-block:: python

    from flask import Flask
    
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()


.. nextslide:: What's Happening Here?

Flask the framework provides a Python class called `Flask`. This class
functions as a single *application* in the WSGI sense.

.. rst-class:: build
.. container::

    We know a WSGI application must be a *callable* that takes the arguments
    *environ* and *start_response*.

    It has to call the *start_response* method, providing status and headers.

    And it has to return an *iterable* that represents the HTTP response body.


    In Python, an object is a *callable* if it has a ``__call__`` method.

.. nextslide::

Take a moment to start up your ``learning_journal`` virtualenv and fire up a
Python interpreter:

.. code-block:: bash

    heffalump:~ cewing$ workon learning_journal
    [learning_journal]
    heffalump:learning_journal cewing$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Once there, import the ``flask`` package. Our ``app`` is an instance of the
``Flask`` class from this package.  Let's go look that up and see what it does:

.. code-block:: pycon

    >>> import flask
    >>> flask.__file__
    '/Users/cewing/virtualenvs/learning_journal/lib/python2.7/site-packages/flask/__init__.pyc'
    >>> 

.. nextslide::

Open that ``flask`` directory in your editor and open ``__init__.py``:

.. code-block:: python

    # -*- coding: utf-8 -*-
    """
        flask
        ~~~~~

        A microframework based on Werkzeug.  It's extensively documented
        and follows best practice patterns.
        ...
    """
    # ...
    from werkzeug.exceptions import abort
    from werkzeug.utils import redirect
    from jinja2 import Markup, escape

    from .app import Flask, Request, Response
    from .config import Config

.. nextslide:: The ``Flask.__call__`` method

On line 21 you should see that ``Flask`` is imported into the global ``flask``
namespace from ``.app``.  Open the ``app.py`` file to dig a bit further.

Here's the ``__call__`` method of the ``Flask`` class (lines 1834-36 in my
version):

.. code-block:: python

    def __call__(self, environ, start_response):
        """Shortcut for :attr:`wsgi_app`."""
        return self.wsgi_app(environ, start_response)

As you can see, it calls another method, called ``wsgi_app``.  Let's follow
this down...

.. nextslide:: The ``Flask.wsgi_app`` method

.. code-block:: python

    def wsgi_app(self, environ, start_response):
        """The actual WSGI application.  
        ...
        """
        ctx = self.request_context(environ)
        ctx.push()
        error = None
        try:
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.make_response(self.handle_exception(e))
            return response(environ, start_response)
        #...

``response`` is another WSGI app.  ``Flask`` is actually *WSGI middleware*!

.. nextslide:: The ``werkzeug.Response`` class

Following this all the way down leads to a ``Response`` class from a package
called *werkzeug*. Here's the ``__call__`` method provided by that class:

.. code-block:: python

    def __call__(self, environ, start_response):
        """Process this response as WSGI application.

        :param environ: the WSGI environment.
        :param start_response: the response callable provided by the WSGI
                               server.
        :return: an application iterator
        """
        app_iter, status, headers = self.get_wsgi_response(environ)
        start_response(status, headers)
        return app_iter

Given the amount of time you've spent in week three working on WSGI apps,
this should look pretty familiar to you.

.. nextslide:: Commonalities

All Python web frameworks that operate under the WSGI spec will do this same
sort of thing.

.. rst-class:: build
.. container::

    They have to do it.

    And these layers of abstraction allow you, the developer to focus only on
    the thing that really matters to you.

    Getting input from a request, and returning a response.

    In the case of ``Flask`` both the Request and the Response are actually
    instances of Python classes defined in the ``werkzeug`` package. These
    classes smooth over some of the complications of interacting with the raw
    WSGI ``environ``.

