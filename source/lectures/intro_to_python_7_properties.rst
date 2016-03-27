*************************************
A Python Class Miscellany: Properties
*************************************

.. ifslides::

    .. rst-class:: centered

    In which we meet another odd beasty from the Python class programming zoo

.. ifnotslides::

    In this lesson we will discuss some of the available features of Class programming in Python.
    We'll be exploring the :func:`property <python2:property>` function (:py:func:`py3 <property>`).
    We'll see how this function can help us to create attributes of our classes that are more dynamic.

Properties
==========

.. rst-class:: left
.. container::

    .. ifslides::

        Python is uncluttered.

        Attributes are simple and concise:

    .. ifnotslides::

        One of Python's greatest strengths is the clarity of the syntax.
        Attribute access is simple and concise, and not too verbose:

    .. code-block:: ipython

        In [5]: class C(object):
                def __init__(self):
                        self.x = 5
        In [6]: c = C()
        In [7]: c.x
        Out[7]: 5
        In [8]: c.x = 8
        In [9]: c.x
        Out[9]: 8


Getter and Setters?
-------------------

.. ifnotslides::

    Sometimes, though, it would be nice to be able to do more that just set and fetch plain values.
    You might want to do some calculation using supplied values.
    You might want to check that the data supplied is valid before setting an attribute.
    You might want to keep two separate attributes synchronized.

.. ifslides::

    But what if you need to add behavior later?

    .. rst-class:: build

    * do some calculation
    * check data validity
    * keep things in sync


.. nextslide::

.. ifnotslides::

    One possible approach is to define what are called ``getters`` and ``setters``.
    These allow you to access an attribute through a method.
    But this approach is decidedly unpythonic:

.. ifslides::

    getters and setters are decidedly unpythonic:

.. code-block:: ipython

    In [5]: class C(object):
       ...:     def __init__(self):
       ...:         self.x = 5
       ...:     def get_x(self):
       ...:         return self.x
       ...:     def set_x(self, x):
       ...:         self.x = x
       ...:
    In [6]: c = C()
    In [7]: c.get_x()
    Out[7]: 5
    In [8]: c.set_x(8)
    In [9]: c.get_x()
    Out[9]: 8

.. ifnotslides::

    Python programmers consider such an approach to be ugly and verbose.
    It's widely used by other languages, particularly Java.
    But you don't see it in Python written in the last decade.

.. ifslides::

    ugly and verbose -- Looks like Java

Properties
----------

.. ifnotslides::

    Luckily, Python provides a way to have our cake and eat it too.
    We can use the ``property`` function to combine a series of up to three functions into a single attribute.
    The three functions allow us to get, set and delete a property.
    The fourth argument is the docstring that will be attached to the resulting attribute.

    This approach allows us to retain the simple attribute access to ``C.x``.
    But the functions are invoked on access.

.. ifslides::

    Use the ``property`` function when you need this type of thing:

.. code-block:: python

    class C(object):
        def __init__(self, x=5):
            self._x = x
        def _getx(self):
            return self._x
        def _setx(self, value):
            self._x = value
        def _delx(self):
            del self._x
        x = property(_getx, _setx, _delx, doc="docstring")

.. ifslides::

    Interface is still simple attribute access!

    [demo]


.. nextslide:: "Read Only" Attributes

.. ifnotslides::

    There are three possible function arguments to ``property``.
    They provide functionality to ``get``, ``set``, and ``delete`` the resulting attribute.
    But only the first of the three is required.
    This can allow us to do interesting things like creating "read only" attributes:

.. ifslides::

    Only the ``getter`` argument is required.

    Create attributes that are "read only":

.. code-block:: ipython

    In [11]: class D(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     def getx(self):
       ....:         return self._x
       ....:     x = property(getx, doc="I am read only")
       ....:
    In [12]: d = D()
    In [13]: d.x
    Out[13]: 5
    In [14]: d.x = 6
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-14-c83386d97be3> in <module>()
    ----> 1 d.x = 6
    AttributeError: can't set attribute


.. nextslide:: Syntactic Sugar

.. ifnotslides::

    We've seen similar function calls inside a class definition before.
    The ``staticmethod`` and ``classmethod`` functions work in a similar fashion.
    We declare a method, and then bind a name to the result of calling the function with that method as an argument.

    We call this usage *imperative* because we are explicitly telling the code exactly what to do.
    The *imperative* style of adding a ``property`` to you class is clear, but it's still a little verbose.
    And what is worse, it also has the effect of leaving all those defined method objects laying around where they litter the API of your class:

.. ifslides::

    Usage is similar to ``staticmethod`` and ``classmethod``

    This *imperative* usage is verbose, sloppy

    Worse, it leaves us with access to the original methods

.. code-block:: ipython

    In [19]: d.x
    Out[19]: 5
    In [20]: d.getx
    Out[20]: <bound method D.getx of <__main__.D object at 0x1043a4a10>>
    In [21]: d.getx()
    Out[21]: 5

.. nextslide::

.. ifnotslides::

    Python provides us with a way to solve both these issues at once.
    We've seen it with both the ``staticmethod`` and ``classmethod`` functions too.
    We can also use ``property`` as a **decorator**, in a *declarative* style:

.. ifslides::

    Solve both issues at once

    Use property as a decorator, declaratively:

.. code-block:: ipython

    In [22]: class E(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = x
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.setter
       ....:     def x(self, value):
       ....:         self._x = value
       ....:
    In [23]: e = E()
    In [24]: e.x
    Out[24]: 5
    In [25]: e.x = 6
    In [26]: e.x
    Out[26]: 6

.. ifnotslides::

    Consider the case of a class representing a Circle.
    Circles have several properties we might be interested in knowing about.
    They have a radius and a diameter.
    A circumference and an area, too.

    We can use properties to tie these all together:

    .. code-block:: python
    
        In [9]: class Circle(object):
           ...:     def __init__(self, radius):
           ...:         self.radius = radius
           ...:     @property
           ...:     def diameter(self):
           ...:         return self.radius * 2
           ...:     @diameter.setter
           ...:     def diameter(self, diameter):
           ...:         self.radius = diameter / 2.0
           ...:     @property
           ...:     def circumference(self):
           ...:         return 2 * pi * self.radius
           ...:     @property
           ...:     def area(self):
           ...:         return pi * self.radius ** 2
           ...:

    And now, we can see how we retain a clean, Pythonic interface, but get the behavior we expect:

    .. code-block:: ipython
    
        In [10]: c1 = Circle(1)

        In [11]: c1.diameter
        Out[11]: 2

        In [12]: c1.circumference
        Out[12]: 6.283185307179586

        In [13]: c1.area
        Out[13]: 3.141592653589793

        In [14]: c1.diameter = 4

        In [15]: c1.radius
        Out[15]: 2.0

        In [16]: c1.circumference
        Out[16]: 12.566370614359172

        In [17]: c1.area
        Out[17]: 12.566370614359172

        In [18]: c1.radius = 4

        In [19]: c1.area
        Out[19]: 50.26548245743669

        In [20]: c1.circumference
        Out[20]: 25.132741228718345