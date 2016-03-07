.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 5
******************************

.. slide:: Introduction To Python: Part 5
    :level: 1

    .. rst-class:: center

    In which we learn the very basics of working with Python classes

In this lecture, we will establish the basics of Object Oriented programming, working with classes in Python.

Object Oriented programming has been the dominant model for the past couple decades.
You will certainly need to use it during your career.
First, because it's a good way to solve a lot of problems.
Second, because you will need to use other libraries that are Object Oriented.
Even a fair bit of the Python standard library is Object Oriented.

.. slide:: OO Programming
    :level: 3

    It's been dominant for several decades

    .. rst-class:: build
    .. container::

        You will need to use it:

        - It's a good idea for a lot of problems

        - You'll need to work with OO packages

        (Even a fair bit of the standard library is Object Oriented)


Definitions
===========

There are a few terms that are common in object oriented programming.
We'll need to understand these terms in order to work well together.

class
  A category of objects: particular data and behavior: A "circle" (same as a type in python)

instance
  A particular object of a class: a specific circle

object
  The general case of a instance -- really any value (in Python anyway)

attribute
  Something that belongs to an object (or class): generally thought of as a variable, or single object, as opposed to a ...

method
  A function that belongs to a class

.. slide:: Definitions
    :level: 3

    .. rst-class:: build

    class
      A category of objects: particular data and behavior: A "circle" (same as a
      type in python)

    instance
      A particular object of a class: a specific circle

    object
      The general case of a instance -- really any value (in Python anyway)

    attribute
      Something that belongs to an object (or class): generally thought of as a
      variable, or single object, as opposed to a ...

    method
      A function that belongs to a class

The distinction between these last two is a *bit* fuzzy.
Since functions are first-class objects in Python, a method really *is* an attribute.
But the distinction is useful since it allows us to separate *actions* an object can perform from *data* an object contains.

.. slide:: Note
    :level: 3

    .. rst-class:: center large

        Note that in python, functions are first class objects, so a method *is* an attribute

Python Classes
==============

In Python, we build a class using the :keyword:`class <python2:class>` statement (:py:class:`py3 <class>`).
Evaluating the statement creates a new type object.
So classes are *types*, interesting!

The class object is created when the statement is evaluated, much like ``def``.
The name of the class is bound as a symbol to the class object in the namespace where it is defined.
For compatibility, you should *always* subclass from ``object`` as shown below.
We'll discuss why at a later time.

.. code-block:: ipython

    In [4]: class C(object):
       ...:     pass
       ...:
    In [5]: type(C)
    Out[5]: type

.. slide:: Python Classes
    :level: 3

    .. rst-class:: left
    .. container::

        The ``class``  statement

        .. rst-class:: build
        .. container::

            ``class``  creates a new type object:

            .. code-block:: ipython

                In [4]: class C(object):
                   ...:     pass
                   ...:
                In [5]: type(C)
                Out[5]: type

            A class is a type -- interesting!

            It is created when the statement is run -- much like ``def``

            You don't *have* to subclass from ``object``, but you *should*

            (note on "new style" classes)

Here's a sample class, just about the simplest class you can write.
In this case, our class has an ``x`` and ``y`` *class attribute*.
These attributes are available on the class object itself, or on instances of the object via the dot operator.

.. code-block:: python

    >>> class Point(object):
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

.. slide:: Class Attributes
    :level: 3

    Any attribute defined at class scope is a *class attribute*

    .. rst-class:: build
    .. container::

        .. code-block:: python

            >>> class Point(object):
            ...     x = 1
            ...     y = 2
            >>> Point
            <class __main__.Point at 0x2bf928>
            >>> Point.x
            1
            >>> p = Point()
            >>> p
            <__main__.Point instance at 0x2de918>
            >>> p.x
            1

        ``x`` and ``y`` accessible from class object via dot operator


The basic structure of a real class might look more like this.
In this case, the ``x`` and ``y`` attributes are *instance attributes*.
They are attached to ``self``.

.. code-block:: python

    class Point(object):
        # everything defined in here is in the class namespace

        def __init__(self, x, y):
            # everything attached to self is in the instance namespace
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print("p.x is:", p.x)
    print("p.y is:", p.y)

.. slide:: Instance Attributes
    :level: 3

    .. code-block:: python

        class Point(object):
            # everything defined in here is in the class namespace

            def __init__(self, x, y):
                # everything attached to self is in the instance namespace
                self.x = x
                self.y = y

        ## create an instance of the class
        p = Point(3,4)

        ## access the attributes
        print("p.x is:", p.x)
        print("p.y is:", p.y)

    .. rst-class:: build
    .. container::

        ``x`` and ``y`` are *instance attributes*

        They can also be accessed via the dot operator.

The Initializer
---------------

The ``__init__``  special method is called when a new instance of a class is created.
You can use it to do any set-up for your instance that you need.

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It is passed the arguments you provide when you *call* the class object:

.. code-block:: python

    Point(x, y)

But there's a *third* parameter in the declaration of that ``__init__`` method.
What is that ``self`` thing?

.. slide:: Initializer
    :level: 3

    ``__init__`` special method sets up new instances

    .. rst-class:: build
    .. container::

        .. code-block:: python

            class Point(object):
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

        passed the arguments provided when *calling* the class object.

        .. code-block:: python

            Point(5, 6)

        But there is a third argument, what is it?

``self``
--------

For every method of a class, the *instance* of the class on which the method is invoked is passed as the first parameter.
Calling the instance ``self`` in the parameters list is only a convention.
But this convention is one that you **do** want to use.
Anything else would be immensely confusing to any experience Python programmer.

.. slide:: ``self``
    :level: 3

    Every class method requires ``self`` as first parameter

    .. rst-class:: build
    .. container::

        Calling it ``self`` is convention, but do it

        It's a reference to the instance itself

Classes & Methods
-----------------

Most classes will need an ``__init__`` special method.
Other methods may also be required.
Methods of the class will take some parameters and use them to manipulate the attributes of ``self``.
The method may or may not return some useful value, it's not required that they do so.

.. code-block:: python

    class Circle(object):
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def grow(self, factor=2):
            self.diameter = self.diameter * factor

.. slide:: Classes & Methods
    :level: 3

    .. code-block:: python

        class Circle(object):
            color = "red"

            def __init__(self, diameter):
                self.diameter = diameter

            def grow(self, factor=2):
                self.diameter = self.diameter * factor

    .. rst-class:: build
    .. container::

        Most classes need ``__init__``

        Some also require other methods

        Methods take some parameters and manipulate attributes of ``self``

        Methods may (or may not) return useful values

Be careful when calling methods on an instance.
You may be greeted with the following ``TypeError``:

.. code-block:: ipython

    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

You'll think to yourself "Huh?  But I only gave two arguments!".

.. slide:: Gotcha
    :level: 3

    A method takes two arguments:

    .. code-block:: python

        def grow(self, factor=2):
            self.diameter = self.diameter * factor

    .. rst-class:: build
    .. container::

        Call it with two arguments:

        .. code-block:: ipython

            In [205]: C = Circle(5)
            In [206]: C.grow(2,3)

            TypeError: grow() takes at most 2 arguments (3 given)

The trick is that ``self`` is *implicitly passed* by Python when you invoke a method on an instance.
This is automatic.
Methods of a class are called ``bound`` when invoked on an instance.
They are ``unbound`` if they are invoked on the class object itself.
When unbound, an instance must be explicitly passed as the first argument.

.. code-block:: ipython

    In [2]: c1 = Circle(5)

    In [3]: c1.grow
    Out[3]: <bound method Circle.grow of <__main__.Circle object at 0x103ceae80>>

    In [4]: c1.grow(3)

    In [5]: c1.diameter
    Out[5]: 15

    In [6]: Circle.grow
    Out[6]: <function __main__.Circle.grow>

    In [7]: Circle.grow(c1, 2)

    In [8]: c1.diameter
    Out[8]: 30

.. slide:: Implicit ``self``
    :level: 3

    ``self`` passed *implicitly* when methods invoked on instances

    .. rst-class:: build
    .. container::

        methods on instances are called ``bound``

        methods can also be invoked on class object (``unbound``)

        when used unbound, an object instance *must* be passed explicitly

        [demo]

        see `here <http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html>`_ for the rationale


The requirement to explicitly specify ``self``, and then have it implicitly passed seems confusing at first.
But like most of Python's quirks, there is a strong rationale behind it.
The BDFL has made the decision that ``self`` is here to stay, and even `written extensively <http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html>`_ about why.

Namespaces and Classes
----------------------

For the following examples, consider this class definition of a point with color and size.

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

Anything assigned to a ``self.<xyz>``  attribute is kept in the *instance* name space.
Remember that ``self`` *is* the instance.
The ``x`` and ``y`` attributes of our example ``Point`` class are *instance* attributes, found in the instance namespace.

Anything that is assigned in the class scope is a class attribute.
These attributes are kept in the class namespace.
Every *instance* of the class shares **the same class namespace**.

.. slide:: Namespaces and Classes
    :level: 3

    .. code-block:: python

        class Point(object):
            size = 4
            color= "red"
            def __init__(self, x, y):
                self.x = x
                self.y = y

    .. rst-class:: build
    .. container::

        Instances have a private namespace (``x``, ``y``)

        Classes have a shared namespace (``size``, ``color``)

        Anything defined in class scope is in class namespace

        All instances share this namespace

.. note:: methods defined by ``def`` are class attributes as well.

The class has one namespace, the instance has another.
When you ask an instance for an attribute that is defined in the class namespace, it is also found.
This means that you can use ``self`` to get at attributes that belong to the class namespace.

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        ...
        def get_color():
            return self.color

    p3 = Point(5, 6)
    p3.get_color()
    'red'

Under the covers, Python looks for the name first in the instance namespace, and then in the class namespace.
If it isn't found in either place, then an ``AttributeError`` is raised.

.. slide:: Name Resolution
    :level: 3

    .. code-block:: python

        class Point(object):
            size = 4
            color= "red"
            ...
            def get_color():
                return self.color

        p3 = Point(5, 6)
        p3.get_color()
        'red'

    .. rst-class:: build
    .. container::

        The dot operator gets values in namespaces

        When used on an instance will look first in *instance* namespace

        If not found, will look in *class* namespace

        If not found there, ``AttributeError``

Wrap Up
=======

In this lesson, we've learned the basics of programming classes in Python.
We learned a few terms that we will use to describe the objects we work with.
We learned about the initializer method you can use to set up new instances.
We learned about the different namespaces available in Python classes.
And we learned a bit about the ``self`` parameter and how it works.

This should help you to get started using Python classes to build your data structures.

.. slide:: Summary
    :level: 3

    .. rst-class:: build

    * Python supports object oriented programming
    * We have a specific vocabulary we will use to talk about classes
    * Classes can have an ``__init__`` special method for set-up
    * Classes and instances both have namespaces
    * The ``self`` argument is used to refer to specific instances from within class methods