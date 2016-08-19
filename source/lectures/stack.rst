=====
Stack
=====

Definition
==========

A *Stack* is a data structure where elements are inserted into and removed from the head of the container.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/391px-Data_stack.svg.png
    :width: 400px
    :alt: An example of a data stack. Source: https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues


Motivation
==========

* Sequential
* Limited access
* Last-In First-Out (LIFO) access
* Linear
* **When might I actually use this?**
    - `Towers of Hanoi puzzle <https://larc.unt.edu/ian/TowersOfHanoi/4-256.gif>`_
    - Rearranging railroad cars
    - Sorting...anything


Attributes
==========

* top
* is_empty
* size


Operations
==========

* push(item)
* pop()
