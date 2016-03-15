:orphan:

****************************
Jinja2 Template Introduction
****************************

When you install ``pyramid_jinja2`` into your virtualenv, it brings along a
Python-based templating engine called ``Jinja2``.

In this walkthrough, you'll see some basics about how templates work, and get
to know what sorts of options they provide you for creating HTML from a Python
process.

::

    "I enjoy writing HTML in Python"

      -- nobody, ever


A good framework will provide some way of generating HTML with a templating
system. As a result, there are nearly as many templating systems as there are
frameworks. Each comes with advantages and disadvantages.

Pyramid provides add-ons to use a number of different templating systems,
including `chameleon`_, `mako`_, and `Jinja2`_. Of these, Jinja2 is arguably
the easiest to learn, and has the advantage of strongly resembling the Django
templating language. We'll learn it first.

.. _Jinja2: http://jinja.pocoo.org
.. _mako: http://www.makotemplates.org
.. _chameleon: https://chameleon.readthedocs.org/en/latest/


Jinja2 Template Basics
======================

Let's start with the absolute basics. Begin by activating your learning-journal
virtualenv:

.. code-block:: bash

    $ workon learning-journal
    (learning-journal)$

Next, install the ``Jinja2`` template language package using ``pip``:

.. code-block:: bash

    (learning-journal)$ pip install jinja2
    Collecting jinja2
      ...
    Successfully installed jinja2-2.7.3 markupsafe-0.23
    (learning-journal)$

Then, fire up a Python interpreter, with your learning-journal virtualenv
active:

.. code-block:: bash

    (learning-journal)$ python

.. code-block:: pycon

    >>> from jinja2 import Template

For the next steps, you'll play around a bit with the basic concepts of Jinja2
templating.  Feel free to explore a bit, try things out, go beyond what's
suggested and learn from your mistakes.

A template starts life as a simple string:

.. code-block:: pycon

    >>> t1 = Template("Hello {{ name }}, how are you?")
    >>>

But it has a bit more to it than that. You can call the ``render`` method of a
template object, providing some *context*:

.. code-block:: pycon

    >>> t1.render(name="Freddy")
    u'Hello Freddy, how are you?'
    >>> t1.render({'name': "Roberto"})
    u'Hello Roberto, how are you?'
    >>>

*Context* can either be keyword arguments, or a dictionary.

Simple Python values passed in as context will be resolved in the template by
the *key* they are assigned to in the *context*.  These keys are arbitrary.
*Placeholders* like ``{{ name }}`` in this example will be replaced by the
corresponding values from the *context*.

Item and Attribute Access in Templates
--------------------------------------

Dictionaries passed in as part of the *context* can be addressed with *either*
subscript or dotted notation:

.. code-block:: pycon

    >>> person = {'first_name': 'Frank',
    ...           'last_name': 'Herbert'}
    >>> t2 = Template("{{ person.last_name }}, {{ person['first_name'] }}")
    >>> t2.render(person=person)
    u'Herbert, Frank'

* Jinja2 will try the *correct* way first (attr for dotted, item for
  subscript).
* If nothing is found, it will try the opposite.
* If nothing is found, it will return an *undefined* object.

The exact same is true of objects passed in as part of *context*:

.. code-block:: pycon

    >>> t3 = Template("{{ obj.x }} + {{ obj['y'] }} = Fun!")
    >>> class Game(object):
    ...   x = 'babies'
    ...   y = 'bubbles'
    ...
    >>> bathtime = Game()
    >>> t3.render(obj=bathtime)
    u'babies + bubbles = Fun!'

This means your templates can be a bit agnostic as to the nature of the things
passed in via *context*

`Read more about variables in Jinja2 templates`_.

.. _Read more about variables in Jinja2 templates: http://jinja.pocoo.org/docs/templates/#variables


Filtering values in Templates
-----------------------------

You can apply *filters* to the data passed in *context* with the pipe ('|')
operator:

.. code-block:: pycon

    t4 = Template("shouted: {{ phrase|upper }}")
    >>> t4.render(phrase="this is very important")
    u'shouted: THIS IS VERY IMPORTANT'

You can also chain filters together:

.. code-block:: python

    t5 = Template("confusing: {{ phrase|upper|reverse }}")
    >>> t5.render(phrase="howdy doody")
    u'confusing: YDOOD YDWOH'

There are `a large number of filters`_ available to use in ``jinja2``.

.. _a large number of filters: http://jinja.pocoo.org/docs/templates/#builtin-filters



Control Flow
------------

``Jinja2`` provides all the expected control structures of a featureful
programming language:

.. code-block:: pycon

    tmpl = """
    ... {% for item in list %}{{ item }}, {% endfor %}
    ... """
    >>> t6 = Template(tmpl)
    >>> t6.render(list=[1,2,3,4,5,6])
    u'\n1, 2, 3, 4, 5, 6, '

Any control structure introduced in a template **must** be paired with an
explicit closing tag ({% for %}...{% endfor %})

You can `learn more about control structures`_ by reading the documentation.

.. _learn more about control structures: http://jinja.pocoo.org/docs/templates/#list-of-control-structures


Conditionals in Templates
-------------------------

There are a number of specialized *tests* available for use with the
``if...elif...else`` control structure:

.. code-block:: pycon

    >>> tmpl = """
    ... {% if phrase is upper %}
    ...   {{ phrase|lower }}
    ... {% elif phrase is lower %}
    ...   {{ phrase|upper }}
    ... {% else %}{{ phrase }}{% endif %}"""
    >>> t7 = Template(tmpl)
    >>> t7.render(phrase="FOO")
    u'\n\n  foo\n'
    >>> t7.render(phrase="bar")
    u'\n\n  BAR\n'
    >>> t7.render(phrase="This should print as-is")
    u'\nThis should print as-is'

`Here's a list`_ of all the built-in tests in the ``jinja2`` template language.

.. _Here's a list: http://jinja.pocoo.org/docs/templates/#builtin-tests

Python Expressions in Templates
-------------------------------

You can also use basic Python-like expressions in ``jinja2`` templates. There
are some syntactic differences, though.

.. code-block:: pycon

    tmpl = """
    ... {% set sum = 0 %}
    ... {% for val in values %}
    ... {{ val }}: {{ sum + val }}
    ...   {% set sum = sum + val %}
    ... {% endfor %}
    ... """
    >>> t8 = Template(tmpl)
    >>> t8.render(values=range(1,11))
    u'\n\n\n1: 1\n  \n\n2: 3\n  \n\n3: 6\n  \n\n4: 10\n
      \n\n5: 15\n  \n\n6: 21\n  \n\n7: 28\n  \n\n8: 36\n
      \n\n9: 45\n  \n\n10: 55\n  \n'

`Learn all about expressions`_, including `assignments`_  in the documentation.

.. _Learn all about expressions: http://jinja.pocoo.org/docs/templates/#expressions
.. _assignments: http://jinja.pocoo.org/docs/templates/#assignments


Jinja2 Templates in Frameworks
==============================

The Jinja2 template engine has a concept it calls an *Environment*. The
environment for the template engine is used to:

* Figure out where to look for templates
* Set configuration for the templating system
* Add some commonly used functionality to the template *context*

In Pyramid, this environment is set up automatically when you include the
pyramid_jinja2 configuration. By default, templates will be searched for
*relative* to the file in which they are called. Paths you use to reference
templates will begin there unless you use `another referencing system`_.

.. _another referencing system: http://docs.pylonsproject.org/projects/pyramid-jinja2/en/latest/#template-lookup-mechanisms

Once configured, you can use any file ending in ``.jinja2`` as a Pyramid
*renderer*.  Needless to say, the file extension used is `also configurable`_.

.. _also configurable: http://docs.pylonsproject.org/projects/pyramid-jinja2/en/latest/#adding-or-overriding-a-renderer

.. code-block:: python

    from pyramid.config import view_config
    @view_config(renderer="templates/hello_world.jinja2")

In this case, Pyramid would expect to find a file called ``hello_world.jinja2``
in a directory called ``templates`` adjacent to the file where this code
appeared.

Let's look at what a template file like that might look like:

.. code-block:: jinja

    {% extends "layout.jinja2" %}
    {% block body %}
      <h2>Hello World!</h2>
    {% endblock %}

That's not much to look at.  Where's the rest of the HTML that makes up a page?

Template Inheritance
--------------------

``Jinja2`` templates allow for *inheritance*.  This means that you can create
shared structure in base templates, and then override or fill in named parts of
that structure in *sub-templates*.

In the above case, the ``hello_world.jinja2`` sub-template *extends* the
``layout.jinja2`` template. What does that file look like?

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
      <head>
        <title>Hello World!</title>
      </head>
      <body>
        <h1>A simple page</h1>
        <div class="content">
        {% block body %}{% endblock %}
        </div>
      </body>
    </html>

You can see here that the ``body`` block is defined in ``layout.jinja2`` and then
that block is filled by the templating in ``hello_world.jinja2``.

Inheritance can work the other way, as well. In addition to filling blocks in a
larger structure, you can pull in smaller blocks using the ``include`` template
tag.  For example, all the pages on your site might include a common footer
which is defined in ``footer.jinja2``:

.. code-block:: jinja

    <div id="footer">
      I am the footer, seen on all pages.
    </div>

Then, we can include this structure in our ``layout.jinja2`` file:

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
      <head>
        <title>Hello World!</title>
      </head>
      <body>
        <h1>A simple page.</h1>
        <div class="content">
        {% block body %}{% endblock %}
        </div>
        {% include "footer.jinja2" %}
      </body>
    </html>

Finally, you can also *import* template macros from templates where you define
them. This can be a convenient way to create libraries of shareable template
structures for repetetive elements like form inputs:

.. code-block:: jinja

    {% macro input(name, value='', type='text') -%}
        <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
    {%- endmacro %}

    {%- macro textarea(name, value='', rows=10, cols=40) -%}
        <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
            }}">{{ value|e }}</textarea>
    {%- endmacro %}

Once such a library is established, say in a file called ``forms.jinja2``, the
macros it contains can be used in other templates:

.. code-block:: jinja

    {% import 'forms.jinja2' as forms %}
    <dl>
        <dt>Username</dt>
        <dd>{{ forms.input('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ forms.input('password', type='password') }}</dd>
    </dl>
    <p>{{ forms.textarea('comment') }}</p>

There's more to learn about `inheritance`_ and `importing`_ than we can cover
here, so read up.

.. _inheritance: http://jinja.pocoo.org/docs/templates/#template-inheritance
.. _importing: http://jinja.pocoo.org/docs/templates/#import


Common Pyramid Context
----------------------

Keyword arguments you pass to ``render_template`` become the *context* passed
to the template for rendering.

Pyramid will :ref:`add values <pyramid:renderer_system_values>` to the *context* for jinja2 templates, including the
``request`` object. Within pyramid, the request object is a single location
where you can access other important information like:

* **settings**: ``request.registry.settings`` contains all settings for your
  app.
* **session**: if sessions are configured, ``request.session`` will hold
  session data.
* **route_url**: you can easily *reverse* urls from within your templates with
  ``request.route_url``.

and much much more. The Pyramid ``request`` supports an :ref:`entire ecosystem <pyramid:request_module>` of
properties and methods that can come in useful.


Much, Much More
===============

Make sure that you bookmark the `Jinja2 documentation <http://jinja.pocoo.org/docs/templates/>`_ for later use.
