.. slideconf::
    :autoslides: False

************************************
Implement a Priority Queue in Python
************************************

.. slide:: Implement a Priority Queue in Python
    :level: 1

    This document contains no slides.

Tasks
=====

A `Priority Queue <http://en.wikipedia.org/wiki/Priority_queue>`_ is similar to
a queue, except that in addition to a value, each item in the queue has a
"priority".  When you pop an item off of the queue, you always get the highest
priority item.

Create a new branch of your data structures repository.  Call it priorityq. Add
a new Python module to the repository and implement a priority queue.  Your
implementation should support the following methods:

* **.insert(item)**: inserts an item into the queue.
* **.pop()**: removes the most important item from the queue.
* **.peek()**: returns the most important item without removing it from the queue.

For each feature of your new structure, begin by implementing a test to
demonstrate that feature.  Then implement the code to make the test pass.

You may not use existing implementations of this data structure from the Python
standard library or existing packages.

Submitting Your Work
====================

When you have finished work and all your tests pass, create a new pull request
from your priorityq branch to master.  Copy the URL of your pull request and
submit it using the URL input.  When you are done submitting, you may merge
your branch back to master.

As usual, use the comment feature in Canvas to add questions, comments or
reflections on the work you did for this assignment.
