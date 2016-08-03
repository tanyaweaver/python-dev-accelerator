=====
Deque
=====

Definition
==========

A *Deque* is a Queue that works at both ends. Data can be inserted at the head or tail, and retrieved from the head or the tail.

.. image:: http://www.codeproject.com/KB/recipes/669131/deque.png
    :width: 400px
    :alt: An example of a Deque. Source: http://www.codeproject.com

Motivation
==========

* Sequential 
* Limited access
* **When might I actually use this?**
    - Tracking the running minimum and maximum run times for code being tested
    - Modeling how passengers board and deboard an airplane with two entrances/exits


Attributes
==========

* head
* tail
* is_empty
* size


Operations
==========

* add_first()
* add_last()
* delete_first()
* delete_last()
* clear()

