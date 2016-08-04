=====
Queue
=====

Definition
==========

Unlike a **Stack**, a *Queue* is a data structure that inserts elements at the tail (enqueue) and accesses/removes elements at the head (dequeue).

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png
    :width: 400px
    :alt: An example of a data Queue. Source: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

Motivation
==========

* Sequential
* Limited access
* First-In First-Out (FIFO) access
* **When might I actually use this?**
    - Building a task manager
    - Modeling traffic patterns
    - Printing a document (or several documents) in proper order


Attributes
==========

* head
* is_empty
* size


Operations
==========

* enqueue()
* dequeue()
* clear()
