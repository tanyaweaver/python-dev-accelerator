.. slideconf::
    :autoslides: False

******************************************
Python Classes: Inheritance v. Composition
******************************************

.. slide:: Inheritance v. Composition
    :level: 1

    .. rst-class:: center

    In which we learn to build things from other things

In this lesson we will talk about how to build classes based on existing classes.
There are two approaches to doing this, :ref:`inheritance <inheritance_description>` and composition.
Each has its strengths and weaknesses.
We'll look at each here.

.. _inheritance_description:

Inheritance
===========

In object-oriented programming (OOP), inheritance is a way to reuse code of existing objects.
It's good when you want to establish a subtype from an existing object.
Objects are defined by classes, classes can inherit attributes and behavior from pre-existing classes.
The resulting classes are known as `derived classes or subclasses <http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29>`_.

A subclass "inherits" all the attributes (methods, etc) of the parent class.
We can create new attributes or methods to *add* to the behavior of the parent
We can change ("override") some or all of the attributes or methods to *change* the behavior.
We can also *extend* the behavior of the parent by using the original methods and adding a bit more.

We indicate that a new class should inherit from an existing class by placing the name of the existing class in the list of base classes.
The class(es) named in the list of base classes must be in the current namespace when the class statement is evaluated.
For compatibility across Python 2 and 3, any new classes we create wil always inherit from *at least* ``object``.
This basic class sits at the top of the Python data model, and is in the ``__builtin__`` namespace.

This is a pseudocode model for the simplest subclass in Python:

.. code-block:: python

    class Subclass(Superclass):
        pass

``Subclass``  now has exactly the same behavior as ``Superclass``

.. note:: When we put ``object`` in the base class list, it means we are inheriting from object -- getting the core functionality of all objects.

.. slide:: Inheritance
    :level: 3

    An OOP Technique

    .. rst-class:: build
    .. container::

        Useful for re-using code (be careful of thinking *taxonomy*)

        In Python, provide the name of the parent class in the *base class list*:

        .. code-block:: python

            class Subclass(Superclass):
                pass

        ``Subclass`` now does *everything* that ``Superclass`` does

        From here, we can *add*, *override*, or *extend* the parent's attributes

        Adding is trivial, we'll skip talking about it

Overriding attributes
---------------------

One of the core purposes of a subclass is to *change* the behavior of the parent class in some useful way.
We call this *overriding* the inherited behavior.
Overriding attributes of a parent class in Python is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle(object):
        color = "red"

    class NewCircle(Circle):
        color = "blue"

    nc = NewCircle
    print(nc.color)
    blue


Any instances of the new class will have the ``blue`` color.
Instances of the original class will have the ``red`` color.

.. slide:: Overriding Attributes
    :level: 3

    We can *override* attributes by making an attribute on the subclass with the same name

    .. rst-class:: build
    .. container::

        .. code-block:: python

            class Circle(object):
                color = "red"

            class NewCircle(Circle):
                color = "blue"

            nc = NewCircle
            print(nc.color)
            blue

        Instances of ``Circle`` are red

        Instances of ``NewCircle`` are blue

Overriding methods
------------------

Overriding methods works in exactly the same way (remember, a method *is* an attribute in python).

.. code-block:: python

    class Circle(object):
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)

Instances of the new circle class will have the new behavior for the ``grow`` method.
Instances of the existing class will continue to have the old behavior.

.. slide:: Overriding Methods
    :level: 3

    Remember, methods *are* just attributes

    .. rst-class:: build
    .. container::

        Overriding them works the same way:

        .. code-block:: python

            class Circle(object):
            ...
                def grow(self, factor=2):
                    """grows the circle's diameter by factor"""
                    self.diameter = self.diameter * factor
            ...
            class NewCircle(Circle):
            ...
                def grow(self, factor=2):
                    """grows the area by factor..."""
                    self.diameter = self.diameter * math.sqrt(factor)

        ``NewCircle`` instances also can grow, but differently

When overriding behavior for a subclass, remember that in good OO programming a subclass should be substantially similar to its parents.
If you have a system which uses the parent class, you should be able to use the subclass in all the same places, and in all the same ways.
This is known as the "Liskov Substitution Principle".
The authors of ``Think Python`` put it this way::

    whenever you override a method, the interface of the new method should be
    the same as the old.  It should take the same parameters, return the same
    type, and obey the same preconditions and postconditions.

    If you obey this rule, you will find that any function designed to work
    with an instance of a superclass, like a Deck, will also work with
    instances of subclasses like a Hand or PokerHand.  If you violate this
    rule, your code will collapse like (sorry) a house of cards.

    -- [ThinkPython 18.10]

.. slide:: Liskov Substitution Principle
    :level: 3

    Any subclass should be able to be used *in place of* its parent

    .. rst-class:: build
    .. container::

        Should share all the same methods, with the same parameters

        Should return the same number of values, of the same type

        Should not break expectations of the parent

        Consider this carefully

Extending Methods
-----------------

Wanting or needing to override ``__init__`` is very common.
After all, we are trying to modify how the parent class works.
However, we often also want to do some or all of the things that the parent class does with ``__init__``.
We really want to *extend* the functionality of the parent class ``__init__``.
Think "do everything my parent does, plus this other stuff".

.. code-block:: python

    class Circle(object):
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...
    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)

.. slide:: Extending
    :level: 3

    Often want to do everything the parent does

    .. rst-class:: build
    .. container::
    
        But do it a bit differently

        Or add a bit more to it

        .. code-block:: python

            class Circle(object):
                color = "red"
                def __init__(self, diameter):
                    self.diameter = diameter
            ...
            class CircleR(Circle):
                def __init__(self, radius):
                    diameter = radius*2
                    Circle.__init__(self, diameter)

        Both circles are initialized by a number

        The ``CircleR`` uses radius but uses the parent for the actual work

You can do the same thing with the any methods of the parent class.
There isn't anything special about the ``__init__`` method (except that it is called automatically).

.. code-block:: python

    class Circle(object):
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

Attribute resolution order
--------------------------

We have discussed how Python looks up attributes of a class instance.
It starts in the namespace of the instance, and then looks in the namespace of the class.
What happens when your class is a subclass?
If the name is not found in the namespace of our instance, or in the class, then the search continues in the parent class, and so on.

* Is it an instance attribute?
* Is it a class attribute?
* Is it a superclass attribute?
* Is it a super-superclass attribute?
* ...

.. slide:: Attribute Resolution
    :level: 3

    For simple classes, names are found first in instance namespace

    .. rst-class:: build
    .. container::
    
        Then sought in namespace of the class

        When a parent class is involved that is checked next

        And so on...

        Python supports multiple inheritance

        What if the hierarchy isn't strictly linear?

        New algorithm (``C3``) added in Python 2.3

        Use ``ClassObject.mro()`` to see the order

The process of looking up attributes of a class in an inheritance hierarchy seems relatively straightforward.
But Python also supports multiple inheritance (two or more names in the base class list).
What happens then?

In Python 2.3 a new algorithm was added to Python to clarify this question.
The clearest documentation of it can be found in `the release notes for 2.3 <https://www.python.org/download/releases/2.3/mro/>`_
and in a blog post on the `History of Python blog <http://python-history.blogspot.com/2010/06/method-resolution-order.html>`_.

For our purposes, it is enough to say that if you have any questions, you can use the ``Class.mro()`` method of any new-style class to get the ordered list of its parent classes:

.. code-block:: ipython

    In [37]: class A(object): x = 'A'
       ....:
    In [38]: class B(object): x = 'B'
       ....:
    In [39]: class C(A): pass
       ....:
    In [40]: class D(C, B): pass
       ....:
    In [41]: D.mro()
    Out[41]: [__main__.D, __main__.C, __main__.A, __main__.B, object]
    In [42]: D.x
    Out[42]: 'A'
    In [43]: class E(B, C): pass
       ....:
    In [44]: E.mro()
    Out[44]: [__main__.E, __main__.B, __main__.C, __main__.A, object]
    In [45]: E.x
    Out[45]: 'B'

.. slide:: ``ClassObject.mro()``
    :level: 3

    .. rst-class:: build
    .. container::
    
        Says *method*, but means any *attribute*, actually

        .. code-block:: ipython

            In [37]: class A(object): x = 'A'
               ....:
            In [38]: class B(object): x = 'B'
               ....:
            In [39]: class C(A): pass
               ....:
            In [40]: class D(C, B): pass
               ....:
            In [41]: D.mro()
            Out[41]: [__main__.D, __main__.C, __main__.A, __main__.B, object]
            In [42]: D.x
            Out[42]: 'A'
            In [43]: class E(B, C): pass
               ....:
            In [44]: E.mro()
            Out[44]: [__main__.E, __main__.B, __main__.C, __main__.A, object]
            In [45]: E.x
            Out[45]: 'B'

The acronym ``MRO`` stands for ``Method Resolution Order``.
Clearly, though, it applies to *all* attributes of a class, not just to methods.

One final note, regarding the use of ``object`` in the base class list for a class.
In Python 2, this is the way that we distinguish *new-style* classes from *old-style* classes.
Old-style classes had a different way of dealing with attribute resolution.
It faired poorly when used with multiple inheritance.
New-style classes did better with this, especially after Python 2.3
But old-style classes were still around.

In Python 3, there is no such thing as old-style classes.
*All* classes inherit from ``object`` whether specified or not.
We provide the ``object`` base class to maintain compatibility between Python 2 and Python 3.

.. slide:: Inherit from ``object``
    :level: 3

    Original Python classes also had multiple inheritance

    .. rst-class:: build
    .. container::
    
        But the resolution order was very different

        Caused problems with multiple inheritance

        Python 2.2 added ``new-style`` classes

        Must inherit from ``object``

        This is default in Python 3 (no old-style classes anymore)

        Still, inherit from ``object`` for compatibility

When to Subclass
----------------

Remember that we have stated previously that inheritance should be used primarily to promote code re-use.
It's really meant to be used when the thing you want to build *is a* variation on the parent class.

If you want to be able to use your new class in all the places and in all the ways that you can use the parent, then it should inherit from the parent.
But this is not the only possible choice.

Composition
===========

Let's imagine that we have a class that needs to accumulate an arbitrary number of objects.
A list can do that, so we should subclass list, right?

The thing is, that in addition to being able to accumulate objects, lists support a number of other operations.
We can iterate over the objects they contain.
We can sort and reverse them.

Does our new class need to do all those things?
If the answer is no, then our new class might be better served by *containing* a list, rather than inheriting from it.

Composition is another Object Oriented programming approach.
We use it when we want to use some aspect of another class without promising *all* of the features of that other class.

.. slide:: Composition
    :level: 3

    Another, alternative OO Programming approach

    .. rst-class:: build
    .. container::
    
        Used when you only want *some* of the functionality of the other class

        Involves *containing* the other, instead of *inheriting* it

        .. code-block:: ipython

            In [46]: class Accumulator(object):
               ....:     def __init__(self):
               ....:         self._container = []
               ....:     def accumulate(self, obj):
               ....:         self._container.append(obj)
               ....:     def stuff(self):
               ....:         return self._container[:]
               ....:

Think about our example.
Maybe accumulating objects is all we want this new class to do.
No other functionality from a list is required.
We can build our class to contain a list:

.. code-block:: ipython

    In [46]: class Accumulator(object):
       ....:     def __init__(self):
       ....:         self._container = []
       ....:     def accumulate(self, obj):
       ....:         self._container.append(obj)
       ....:     def stuff(self):
       ....:         return self._container[:]
       ....:

Now, we can build an instance of our ``Accumulator`` class and start accumulating stuff:

.. code-block:: ipython

    In [47]: junk_drawer = Accumulator()
    In [48]: junk_drawer.accumulate('spatula')
    In [49]: junk_drawer.accumulate('cork screw')
    In [50]: junk_drawer.accumulate('old rubber band')

And every so often, we can even ask to see what's in the junk drawer (though like any good junk drawer you can't actually take anything out):

.. code-block:: ipython

    In [51]: junk_drawer.stuff()
    Out[51]: ['spatula', 'cork screw', 'old rubber band']

    In [52]: junk_drawer.stuff().pop()
    Out[52]: 'old rubber band'

    In [53]: junk_drawer.stuff()
    Out[53]: ['spatula', 'cork screw', 'old rubber band']

.. slide:: Composition
    :level: 3

    Now, we can put stuff into our accumulator:

    .. rst-class:: build
    .. container::
    
        .. code-block:: ipython

            In [47]: junk_drawer = Accumulator()
            In [48]: junk_drawer.accumulate('spatula')
            In [49]: junk_drawer.accumulate('cork screw')
            In [50]: junk_drawer.accumulate('old rubber band')

        And we can view, but can't remove things:

        .. code-block:: ipython

            In [51]: junk_drawer.stuff()
            Out[51]: ['spatula', 'cork screw', 'old rubber band']
            In [52]: junk_drawer.stuff().pop()
            Out[52]: 'old rubber band'
            In [53]: junk_drawer.stuff()
            Out[53]: ['spatula', 'cork screw', 'old rubber band']

Type-Based Dispatch
===================

One final word for this lesson about classes.
We'll occasionally see code that looks like this:

.. code-block:: python

    if isinstance(other, SomeClass):
        Do_something_with_other
    else:
        Do_something_else

In general, it's usually better to use "duck typing" (polymorphism).
After all, if ``other`` has the right methods or attributes, then why would we care if it *is* an instance of ``SomeClass``?
But when it's called for, you can use ``isinstance``, or its cousin ``issubclass``:

.. code-block:: ipython

    In [54]: isinstance(junk_drawer, Accumulator)
    Out[54]: True

    In [55]: isinstance(junk_drawer, object)
    Out[55]: True

    In [56]: issubclass(Accumulator, object)
    Out[56]: True

    In [57]: issubclass(object, Accumulator)
    Out[57]: False

.. slide:: Type-Based Dispatch
    :level: 3

    .. code-block:: python

        if isinstance(other, SomeClass):
            do_something_with_other()
        else:
            do_something_else()

    .. rst-class:: build
    .. container::

        Making a choice based on the type of thing we have

        Usually better to use Duck-Typing (polymorphism)

        If you need it, use ``isinstance`` or ``issubclass``:

        .. code-block:: ipython

            In [54]: isinstance(junk_drawer, Accumulator)
            Out[54]: True
            In [55]: isinstance(junk_drawer, object)
            Out[55]: True
            In [56]: issubclass(Accumulator, object)
            Out[56]: True
            In [57]: issubclass(object, Accumulator)
            Out[57]: False

Wrap Up
=======

In this lecture we learned about subclassing and composition, two approaches to OO programming.
We learned how to make a subclass in Python.
We learned about the method resolution order and how attributes are looked up when inheritance is in play.
We also learned about the difference between old- and new-style classes and how to maintain compatibility in Python 3.
Finally, we learned how to use composition to gain access to some of the powers of another class without needing to inherit it all.

As you work on your Data Structures assignments, consider how these new tools can help you.

.. slide:: Summary
    :level: 3

    .. rst-class:: build

    * Subclassing is an OO approach
    * Use it for sharing code
    * How to make subclasses in Python
    * How to determine where an attribute will be found
    * Old vs. New-style classes
    * Composition as an alternate approach