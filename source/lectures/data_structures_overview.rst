.. slideconf::
    :autoslides: False

.. slide:: Data Structures: An Overview
    :level: 1

    .. rst-class:: center

    Things to think about and concepts to expect in data structures of Code 401

.. slide:: History
    :level: 2

    .. rst-class:: build

    * Charles Babbage and the Difference Machine 
    * Ada Lovelace and the first algorithm
    * Storing and retrieving data
    * Groups of Bits (GOBs)

.. slide:: Storying and Fetching Data
    :level: 2

    .. rst-class:: build

    * The Analytical Engine only used fixed point arithmetic (column width of 50).
    * Data Structures improve the storing and/or fetching of GOBS.
    * Data Structures organize GOBs

.. slide:: Types of Data Structures
    :level: 2

    GOBs are organized into data structures. These are then grouped into data types:

    .. rst-class:: build

    * Primitive
    * Composite
    * Abstract Data Types 

.. slide:: Primitive Data Types
    :level: 3

    .. rst-class:: left

    Primitive data types are basically built-in types like integers and booleans. 

    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | Type                            | Values                                                                            | Python Implementation     |
    +=================================+===================================================================================+===========================+
    | Boolean                         | True or False                                                                     | ``bool``                  |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | Character                       | `grapheme <https://en.wikipedia.org/wiki/Grapheme>`_ or unicode point             | ``s[n]`` or ``ord(s[n])`` |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | Floating Point                  | single-precision real numbers (±1.18 x 10\ :sup:`-38`\  to ±3.4 x 10\ :sup:`38`\) | n/a                       |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | Double-precision Floating Point | wider float (±2.23 x 10\ :sup:`-308`\  to ±1.80 x 10\ :sup:`308`\)                | ``float``                 |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | Integer                         | fixed-precision values (ex: ...-3, -2, -1, 0, 1, 2, 3...)                         | ``int``                   |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
    | NoneType                        | empty variable without meaningful value                                           | ``None``                  |
    +---------------------------------+-----------------------------------------------------------------------------------+---------------------------+

.. slide:: Composite Data Types
    :level: 3

    .. rst-class:: left

    Data types composed of two or more other data types. Here are *some*:

    +--------+--------------------------------------------+-----------------------+
    | Type   | Values                                     | Python Implementation |
    +========+============================================+=======================+
    | Array  | Mutable object containing other values     | ``list`` or ``[]``    |
    +--------+--------------------------------------------+-----------------------+
    | Record | Immutable object containing other values   | ``tuple`` or ``()``   |
    +--------+--------------------------------------------+-----------------------+
    | Union  | Contains values that can be multiple types | ``dict`` or ``{}``    |
    +--------+--------------------------------------------+-----------------------+

.. slide:: Abstract Data Types
    :level: 3

    .. rst-class:: left

    A set of data values and operations that are precisely specified independent of any particular implementation.

    .. rst-class:: build

    * List (singly- and doubly-linked)
    * Stack
    * Queue
    * Deque (Double-ended queue)
    * Priority queue
    * Associative array
    * Multimap
    * Multiset
    * Set
    * Tree
    * Graph

.. slide:: For This Class...
    :level: 4

    .. rst-class:: left

    We will *consume* primitive and composite data types.

    * These are encapsulated quite nicely by Python.
    * We care about what they do and what they allow us to do

    We will *implement* abstract data types

    * We care about performance
    * We look at their attributes and operations.


.. slide:: Common Attributes of Abstract Data Types
    :level: 2

    .. rst-class:: build

    * index, key
    * node
    * edge
    * length, size
    * value, cargo, information
    * next
    * previous
    * leaf
    * head, root
    * tail

.. slide:: Common Operations of Abstract Data Types
    :level: 2

    .. rst-class:: left

    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | Operation              | Definition                                                                                                                                                                                                                                                                                                                             | Also Known As...        |
    +========================+========================================================================================================================================================================================================================================================================================================================================+=========================+
    | ``search(S, k)``       | Given a structure ``S`` and a key ``k``, returns the value that ``S`` points to at position ``k``                                                                                                                                                                                                                                      | traverse, walk, find    |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``insert(S, x[, k])``  | A modifying operation for mutable types. Adds the element assigned to ``x`` to the structure ``S``. We usually assume that any attributes in element ``x`` needed by the structure implementation have already been initialized.  Sometimes takes an optional argument ``k`` specifying exactly where in the structure to insert ``x`` | push, append            |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``delete(S, x)``       | A modifying operation for mutable types. Removes the element assigned to ``x`` from the structure ``S``.                                                                                                                                                                                                                               | remove, pop             |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``minimum(S)``         | A query on an ordered structure that returns the element of ``S`` with the smallest value.                                                                                                                                                                                                                                             | min                     |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``maximum(S)``         | Similar to above, returns the element of ``S`` with the largest value.                                                                                                                                                                                                                                                                 | max                     |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``successor(S, x)``    | A query on an ordered structure ``S`` that returns the next value after element ``x`` if one exists.                                                                                                                                                                                                                                   | next, child             |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
    | ``predecessor(S, x)``  | Similar to above, returning the value before element ``x`` if one exists                                                                                                                                                                                                                                                               | previous, prior, parent |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+



============================
Data Structures: An Overview
============================

Read This
=========

Getting Real Chapter 2: `What's Your Problem <https://gettingreal.37signals.com/ch02_Whats_Your_Problem.php>`_

History
=======

`Charles Babbage <https://en.wikipedia.org/wiki/Charles_Babbage>`_ (1791 - 1871) designed the Difference Machine: https://www.youtube.com/watch?v=be1EM3gQkAY to build error-free mathmatical tables. He automated the process by creating printing plates, thereby reducing the typesetting errors of the time.

He then generalized the Difference Machine to the first (if it had been built) Turing-complete computer. It has an arithmetic logic, memory, and control flow (branching & loops).

`Ada Lovelace <https://en.wikipedia.org/wiki/Ada_Lovelace>`_ (1815 - 1852) wrote the first algorithm to compute the Bernoulli (Kowa) sequence for the Babbage Analytical Engine.

    “As soon as an Analytical Engine exists, it will necessarily guide the future course of the science. Whenever any result is sought by its aid, the question will then arise—By what course of calculation can these results be arrived at by the machine in the shortest time?”

    ~ Charles Babbage - Passages from the Life of a Philosopher

Babbage’s design was revolutionary in that the computer could store and then retrieve data. Then it was “pegs in a barrel” –like a music box. Today it’s groups of bits (GOBs).

Storing and Fetching Data
=========================

* The Analytical Engine only used fixed point arithmetic (column width of 50).
* Data Structures improve the storing and/or fetching of GOBS.
* Data Structures organize GOBs

Types of Data Structures
========================

GOBs are organized into data structures. These are then grouped into data types:

* Primitive
* Composite
* Abstract Data Types 

Primitive Data Types
--------------------

Primitive data types are basically built-in types like integers and booleans. 

+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| Type                            | Values                                                                            | Python Implementation     |
+=================================+===================================================================================+===========================+
| Boolean                         | True or False                                                                     | ``bool``                  |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| Character                       | `grapheme <https://en.wikipedia.org/wiki/Grapheme>`_ or unicode point             | ``s[n]`` or ``ord(s[n])`` |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| Floating Point                  | single-precision real numbers (±1.18 x 10\ :sup:`-38`\  to ±3.4 x 10\ :sup:`38`\) | n/a                       |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| Double-precision Floating Point | wider float (±2.23 x 10\ :sup:`-308`\  to ±1.80 x 10\ :sup:`308`\)                | ``float``                 |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| Integer                         | fixed-precision values (ex: ...-3, -2, -1, 0, 1, 2, 3...)                         | ``int``                   |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+
| NoneType                        | empty variable without meaningful value                                           | ``None``                  |
+---------------------------------+-----------------------------------------------------------------------------------+---------------------------+

Composite Data Types
--------------------

Data types composed of two or more other data types. Here are *some*:

+--------+--------------------------------------------+-----------------------+
| Type   | Values                                     | Python Implementation |
+========+============================================+=======================+
| Array  | Mutable object containing other values     | ``list`` or ``[]``    |
+--------+--------------------------------------------+-----------------------+
| Record | Immutable object containing other values   | ``tuple`` or ``()``   |
+--------+--------------------------------------------+-----------------------+
| Union  | Contains values that can be multiple types | ``dict`` or ``{}``    |
+--------+--------------------------------------------+-----------------------+

Abstract Data Types
-------------------

An abstract data type is a set of data values and associated operations that are precisely specified independent of any particular implementation. The implementation is up to the problem trying to be solved and the programmer solving it.

Note: Since the data values and operations are defined with mathematical precision, rather than as an implementation in a computer language, we may reason about effects of the operations, relations to other abstract data types, whether a program implements the data type, etc.

Abstract data types follow some mathmatical model of a data structure. A developer implements the data structure, and a user expects certain behaviors from the implementation characteristic of the data type. Here are a few:

* List (singly- and doubly-linked)
* Stack
* Queue
* Deque (Double-ended queue)
* Priority queue
* Associative array
* Multimap
* Multiset
* Set
* Tree
* Graph

For this class
~~~~~~~~~~~~~~

We will *consume* primitive and composite data types.

* These are encapsulated quite nicely by Python.
* We care about what they do and what they allow us to do

We will *implement* abstract data types

* We care about performance
* We look at their attributes and operations.

Common Attributes of Abstract Data Types
========================================

* index, key
* node
* edge
* length, size
* value, cargo, information
* next
* previous
* leaf
* head, root
* tail

Common Operations of Abstract Data Types
========================================

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| Operation              | Definition                                                                                                                                                                                                                                                                                                                             | Also Known As...        |
+========================+========================================================================================================================================================================================================================================================================================================================================+=========================+
| ``search(S, k)``       | Given a structure ``S`` and a key ``k``, returns the value that ``S`` points to at position ``k``                                                                                                                                                                                                                                      | traverse, walk, find    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``insert(S, x[, k])``  | A modifying operation for mutable types. Adds the element assigned to ``x`` to the structure ``S``. We usually assume that any attributes in element ``x`` needed by the structure implementation have already been initialized.  Sometimes takes an optional argument ``k`` specifying exactly where in the structure to insert ``x`` | push, append            |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``delete(S, x)``       | A modifying operation for mutable types. Removes the element assigned to ``x`` from the structure ``S``.                                                                                                                                                                                                                               | remove, pop             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``minimum(S)``         | A query on an ordered structure that returns the element of ``S`` with the smallest value.                                                                                                                                                                                                                                             | min                     |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``maximum(S)``         | Similar to above, returns the element of ``S`` with the largest value.                                                                                                                                                                                                                                                                 | max                     |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``successor(S, x)``    | A query on an ordered structure ``S`` that returns the next value after element ``x`` if one exists.                                                                                                                                                                                                                                   | next, child             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
| ``predecessor(S, x)``  | Similar to above, returning the value before element ``x`` if one exists                                                                                                                                                                                                                                                               | previous, prior, parent |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+

For operations like ``size``, ``maximum``, and ``minimum``, do what you can to make them compatible with python built-in functions like ``len()``, ``max()``, and ``min()``.