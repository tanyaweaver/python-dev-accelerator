*******************************************
A Python Miscellany: Iterators & Generators
*******************************************

.. ifslides::

    .. rst-class:: large center

    In which we meet more cool creatures from the Python zoo

.. ifnotslides::

    In this lesson we will discuss a few more features of programming in Python.
    We'll be exploring the idea and implementation of iterators and generators.
    Understanding these topics will allow you to make your own classes and functions operate more Pythonically.


Iterators
=========

.. rst-class:: left
.. container::

    .. ifnotslides::

        Iterators are one of the main reasons Python code is so readable:

    .. ifslides::

        Iterators make Python readable:

    .. code-block:: python

        for x in just_about_anything:
            do_stuff(x)

    .. ifnotslides::

        What's fun is that ``just_about_anything`` does not have to be a "sequence".
        Rather, you can loop through anything that satisfies the :ref:`iterator protocol <python2:typeiter>` (:py:ref:`py3 <typeiter>`).

    .. ifslides::

        .. rst-class:: build
        .. container::

            ``just_about_anything``: lists, tuples, dicts, strings

            can also be *any object* that supports the "iterator protocol"


The Iterator Protocol
---------------------

An iterator must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

.. ifnotslides::

    The :meth:`__iter__ <python2:iterator.__iter__>` special method (:py:meth:`py3 <iterator.__iter__>`) returns the iterator object itself.
    The return value might be ``self``, or it might be an object constructed that can be iterated over.
    This is required to allow both containers and iterators to be used with the ``for`` and ``in`` statements.

.. ifslides::

    ``__iter__`` returns an iterator object (might be self, might not)

.. code-block:: python

    # python 2
    an_iterator.next()

    # python 3
    an_iterator.__next__()

.. ifnotslides::

    The :meth:`next <python2:iterator.next>` method (in python 3 it is :py:meth:`__next__ <iterator.__next__>`) returns the next item from the container.
    If there are no further items, this method must raise a ``StopIteration`` exception.

.. ifslides::

    ``next`` returns the next item in line.

    It must raise ``StopIteration`` when done.

.. ifnotslides::

    This change in interface leads to some compatibility problems.
    In order to write iterators that are compatible with both Python 2 and Python 3, use one of the `compatible idioms <http://python-future.org/compatible_idioms.html#custom-iterators>`_ from python-future.

.. nextslide:: Iterable Iterators

.. ifnotslides::

    In Python, data types like lists, tuples, sets, an dicts are sometimes referred to as "iterables".
    They too implement the iterator interface, and you can get at the "iterator" directly if you like:

.. ifslides::

    "Iterables": lists, tuples, sets, dicts

.. code-block:: ipython

    In [10]: a_list = [1,2,3]
    In [11]: list_iter = a_list.__iter__()
    In [12]: next(list_iter)
    Out[12]: 1
    In [13]: next(list_iter)
    Out[13]: 2
    In [14]: next(list_iter)
    Out[14]: 3
    In [15]: next(list_iter)
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 next(list_iter)
    StopIteration:

.. nextslide:: ``iter()``

.. ifnotslides::

    It's not really polite (or proper) to access *special methods* of objects directly like that, though.
    Instead, you should use the Python function that utilizes those methods.
    In this case, that is the :func:`iter() <python2:iter>` function (:py:func:`py3 <iter>`).

.. ifslides::

    We shouldn't directly use special methods.

    Use ``iter()`` instead.

.. code-block:: ipython

    In [20]: iter([2,3,4])
    Out[20]: <listiterator at 0x101e01350>

    In [21]: iter(u"a string")
    Out[21]: <iterator at 0x101e01090>

    In [22]: iter( (u'a', u'tuple') )
    Out[22]: <tupleiterator at 0x101e01710>

.. ifnotslides::

    For arbitrary objects, ``iter()`` calls the ``__iter__`` special method.
    But it can also handle objects (``str``, for instance) that don't have a ``__iter__`` method.

.. ifslides::

    It calls ``__iter__`` when present.

    But can also handle some objects without that method (like ``str``)


Making an Iterator
------------------

.. ifnotslides::

    Understanding the iterator protocol allows us to build iterators of our own.
    Let's try this out by building a simple iterator that will operate a bit like the Python 2 ``xrange``:

.. ifslides::

    We can make classes that are iterators

    For example, something a bit like ``xrange``:

.. code-block:: python

    class IterateMe_1(object):
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def next(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration

.. nextslide:: Fake For

.. ifnotslides::

    We can even use the protocol to build a function that emulates the Python ``for`` loop:

.. ifslides::

    Emulate the Python ``for`` loop:

.. code-block:: python

    def my_for(an_iterable, func):
        """
        Emulation of a for loop.
        func() will be called with each item in an_iterable
        """
        # equiv of "for i in l:"
        iterator = iter(an_iterable)
        while True:
            try:
                i = iterator.next()
            except StopIteration:
                break
            func(i)


.. ifnotslides::

    :mod:`itertools <python2:itertools>` (:py:mod:`py3 <itertools>`) is a collection of utilities that make it easy to build an iterator that iterates over sequences in various common ways.
    The utilities it contains work with any object that supports the iterator protocol.
    And the iterators they return can be used with any Python functions that expect iterators as arguments.
    Things like ``sum``, ``tuple``, ``sorted``, and ``list``, for example.


Generators
==========

.. rst-class:: left
.. container::

    .. ifnotslides::

        A generator object is a bit like an iterator, except that it is itself the iterator.
        Another difference is that with a generator you have no access to the data that is being returned, if it even exists.

        Conceptually, an iterator allows you to loop over data that exists.
        Generators, on the other hand, *generate* their data on the fly.
        Practically speaking, you can use them interchangeably, and generators are in fact a special case of iterators.
        Generators just handle some of the internal book-keeping for you.

    .. ifslides::

        .. rst-class:: build
        .. container::

            Generators are like iterators

            Except they are themselves the iterator object

            Also, you have no access to the data they return until it is returned

            Conceptually:
              Iterators loop over data, generators generate the data on the fly

            Practically:
              You can use either (a generator *is* a special iterator)

              Generators do some of the book-keeping for you.

``yield``
---------

.. code-block:: python

    def a_generator_function(params):
        some_stuff
        yield something

.. ifnotslides::

    The :keyword:`yield <python2:yield>` statement (:py:keyword:`py3 <yield>`) can be used to create generators.
    Using the ``yield`` statement in a function causes the function to become a ``generator function``.
    The function can then ``yield`` values instead of returning them.
    And the state of the names and values inside the function is preserved between ``yield`` statements.

.. ifslides::

    .. rst-class:: build
    .. container::

        Using ``yield`` makes a ``generator function``

        Generator functions "yield" a value, not return it

        State is preserved in between yields.

.. nextslide::

.. ifnotslides::

    When you write a function with ``yield``  in it, it becomes a "factory" for a ``generator object``.
    Calling the function returns a ``generator object``.
    And every time you call it, a *new* and *independent* generator object is returned.
    Each independent instance keeps track of its own internal state.

.. code-block:: python

    gen_a = a_generator_function()
    gen_b = a_generator_function()

.. ifslides::

    .. rst-class:: build
    .. container::

        Generator functions are factories for generator objects

        Calling one creates a new generator

        Each call is a new generator, independent of others

        Each instance keeps its own state.

.. nextslide:: Example

.. ifnotslides::

    One possible example of a simple generator function might be again to emulate the ``xrange`` object from Python 2:

.. code-block:: python

    def y_xrange(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

.. ifnotslides::

    It is most common to write generator functions to return a series of values like this.
    And as we have noted, generators are in fact just a special case of iterators.
    But notice that we do not use ``StopIteration`` to signal when a generator function is complete.
    In fact, calling ``return`` inside a generator function (or simply allowing an implicit return to happen *at the end*) causes ``StopIteration`` to be raised.
    You don't need to do it explicitly.

.. ifslides::

    Generators are Iterators

    But notice the lack of ``StopIteration``

    A ``return`` (explicit or implicit) from a generator function does this automatically.

.. nextslide::

.. ifnotslides::

    A final note on writing generator functions.
    Any callable can be a generator if it uses ``yield`` instead of ``return``.
    This means, of course, that methods on classes can also be generators.
    And even classes themselves, if they have a ``__call__`` method that uses yield, can be generators.

.. ifslides::

    .. rst-class:: centered

    Generators can also be methods on classes.

Generator Comprehensions
------------------------

.. ifnotslides::

    There is one last way to create a generator.
    It turns out that if you use ``()`` instead of ``[]`` when writing a comprehension, the result is a generator.
    It behaves exactly like the equivalent *list comprehension*, except that it only generates the values one at a time.
    This can be especially powerful if the item the comprehension is iterating over is itself a generator.
    The result can be extremely efficient processing of massive amounts of data.

.. ifslides::

    yet another way to make a generator:

.. code-block:: python

    >>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print(n)
    ... 2 4 6

.. ifslides::

    .. rst-class:: build
    .. container::

        Just like a list comprehension, except one-at-a-time

        Especially powerful when iterating over other generators

        Efficient handling of very large data sets

Wrap Up
=======

.. ifnotslides::

    In this lecture, we've learned a bit about two powerful concepts in Python.
    Using the *iterator protocol*, we learned to create iterators.
    We can thus create classes that can work natively with Python's looping structures and the ``itertools`` library.
    Generators, as we learned, are objects that ``yield`` values one-at-a-time, preserving their internal state.
    We learned that we can create them using ``yield`` inside functions or methods.
    And we learned that there are also *generator comprehensions*.
    That's enough to be going on.

.. ifslides::

    Iterators are objects that support the *iterator protocol*

    .. rst-class:: build
    .. container::

        We can create custom classes that do the same

        Those classes can work natively with itertools &c.

        Generators ``yield`` values, and preserve state

        Create them using ``yield`` statement.

        Or with *generator comprehensions*.

        Very efficient for memory.
