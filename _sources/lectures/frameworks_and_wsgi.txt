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

    Compare the ease of routing in ``Pyramid`` with the way you solved the same
    problem for the book database.

    Think about how *general* the route system is in ``Flask`` and how
    *specific* your solution for the book database.

.. nextslide::

In writing a web app with WSGI, what were your pain points? Which bits do you
wish you didn't have to think about?

.. rst-class:: build
.. container::

    How about in the case of your Pyramid app?

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

You began with the most flexible of all the frameworks, **Pyramid**.

.. rst-class:: build
.. container::

    Next you'll be working with the champion of the full-stack framework class,
    **Django**

    You'll also be asked to follow a tutorial on the king of the microframework
    class, ``Flask`` a bit later on. **Pyramid**

Frameworks and WSGI
===================

.. rst-class:: left
.. container::

    But quickly, before we move on to ``Django``, a word on WSGI and web
    frameworks.

    Modern Python web frameworks nearly all work as *wsgi apps*.

    This means that like your bookdb, you can serve them using a *wsgi server*.

    How exactly does that work?

Django and WSGI
---------------

Running a Django site in production is no different than any other framework.
Your site is run using a *wsgi server*, which calls the *wsgi application*
Django builds for you. For a peek behind the curtain, open ``wsgi.py``:

.. code-block:: python

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imager.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

.. nextslide:: Django's wsgi implementation

Let's follow this down a ways and see what we find.  What does
``get_wsgi_application`` look like?

.. code-block:: python

    def get_wsgi_application():
        """
        The public interface to Django's WSGI support. Should return a WSGI
        callable.

        Allows us to avoid making django.core.handlers.WSGIHandler public API, in
        case the internal WSGI implementation changes or moves in the future.

        """
        django.setup()
        return WSGIHandler()

.. nextslide:: The Django WSGIHandler

One level further down. Let's review ``django.core.handlers.wsgi.WSGIHandler``:

.. code-block:: python

    class WSGIHandler(base.BaseHandler):
        initLock = Lock()
        request_class = WSGIRequest

        def __call__(self, environ, start_response):
            # Set up middleware if needed. We couldn't do this earlier, because
            # settings weren't available.
            if self._request_middleware is None:
                with self.initLock:
                    try:
                        # Check that middleware is still uninitialized.
                        if self._request_middleware is None:
                            self.load_middleware()
                    except:
                        # Unload whatever middleware we got
                        self._request_middleware = None
                        raise

            set_script_prefix(get_script_name(environ))
            signals.request_started.send(sender=self.__class__)
            try:
                request = self.request_class(environ)
            except UnicodeDecodeError:
                logger.warning('Bad Request (UnicodeDecodeError)',
                    exc_info=sys.exc_info(),
                    extra={
                        'status_code': 400,
                    }
                )
                response = http.HttpResponseBadRequest()
            else:
                response = self.get_response(request)

            response._handler_class = self.__class__

            status = '%s %s' % (response.status_code, response.reason_phrase)
            response_headers = [(str(k), str(v)) for k, v in response.items()]
            for c in response.cookies.values():
                response_headers.append((str('Set-Cookie'), str(c.output(header=''))))
            start_response(force_str(status), response_headers)
            return response

Given your previous experience creating WSGI apps, this should look pretty
familiar to you.

.. nextslide:: Commonalities

All Python web frameworks that operate under the WSGI spec will do this same
sort of thing.

.. rst-class:: build
.. container::

    They have to do it.

    And these layers of abstraction allow you, the developer to focus only on
    the thing that really matters to you.

    Getting input from a request, and returning a response.
