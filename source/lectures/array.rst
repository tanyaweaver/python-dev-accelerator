======
Arrays
======

.. ifslides::

    A Basic Data Type in Action

Motivation
==========

.. rst-class:: left
.. container::

    * Take advantage of contiguous memory to organize fixed-width groups of bits (data) in a list.
    * In the most basic version, it cannot be changed (immutable). A number of memory slots are allocated and filled with data
    * Arrays are used to represent matrices, vectors (tuples in Python).
    * Random access to data

Base Definition and Operations
==============================

.. ifnotslides::

    Ignoring size, an array may be seen as a data type with the following operations

.. ifslides::

    .. rst-class:: left
    .. container::

        Has the following operations:

.. rst-class:: left
.. container::

    * ``new(N)``: create a new array of length ``N``
    * ``set(A, i, v)``: in array ``A`` set the value at index ``i`` to ``v``
    * ``get(A, i)``: get the value of the ``i``th element of array ``A``
    * ``size(A)``: return the size/length of the array
    * ``remove(A, i)``: removes a value from the array, maintaining array size

.. ifnotslides::

    where ``i`` is a numeric index, ``v`` is a value, and ``A`` is an array.

.. ifslides::

    .. rst-class:: left
    .. container::

        ``i``: index, ``v``: value, ``A``: the array

Attributes
==========

.. rst-class:: left
.. container::

    * index: a position in the array
    * value: an element in the array

Implementation
==============

We will implement the array with a container (node) for one item, and an array class to hold all the items.

Implementing the Node
---------------------

First, a container for one item:

.. code-block:: python

    class Node(object):
        def __init__(self, value):
            """The keeper of individual data"""
            self.value = value

        def __repr__(self):
            """Display the data in this node"""
            return str(self.value)

Implementing the Array
----------------------

Then, initialize the arrray class:

.. code-block:: python

    class Array(object):
        def __init__(self, length):
            """Create a new Array object, ready for filling!"""
            container = [None] * length
            self._container = container

.. nextslide::

Get, set, and remove values by index:

.. code-block:: python

        def get(self, index):
            """Get the value of the item at the given index"""
            if hasattr(self._container[index], "value"):
                return self._container[index].value
            return "None"

        def set(self, index, value):
            """Set the item at the given index to the given value"""
            if value:
                new_node = Node(value)
                self._container[index] = new_node
            else:
                self._container[index] = None

        def remove(self, index):
            """Remove the value at the given index"""
            self.set(index, None)

.. nextslide::

Query size and represent the array:

.. code-block:: python

        def __repr__(self):
            """Display the current state of the array"""
            return str([node.value if hasattr(node, "value") else None for node in self._container])

        def __len__(self):
            """Return the size of the array"""
            return len(self._container)

Using Our Array
===============

new(``N``)
----------

Create a new empty array of length ``N``.

.. code-block:: ipython

    In [1]: my_array = Array(10)

    In [2]: my_array
    Out[2]: [None, None, None, None, None, None, None, None, None, None]


set(``A, i, v``)
----------------

.. code-block:: ipython

    In [3]: my_array.set(5, "kidney beans")

    In [4]: my_array
    Out[4]: [None, None, None, None, None, 'kidney beans', None, None, None, None]


get(``A, i``)
-------------

.. code-block:: ipython

    In [5]: my_array.get(5)
    Out[5]: 'kidney beans'


size(``A``)
-----------

.. code-block:: ipython

    In [6]: len(my_array)
    Out[6]: 10


remove(``A, i``)
----------------

.. code-block:: ipython

    In [7]: my_array.remove(5)

    In [8]: my_array
    Out[8]: [None, None, None, None, None, None, None, None, None, None]
