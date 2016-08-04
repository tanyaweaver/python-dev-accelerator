.. slideconf::
    :autoslides: False

***************************
Implement a Queue in Python
***************************

.. slide:: Implement a Queue in Python
    :level: 1

    This document contains no slides.

Begin by reading about the `Queue data structure`_.

.. _Queue data structure: http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html

Tasks
=====

When you're done, create a new branch in your data structures repository.  On
that branch, write tests for and then implement a queue with the following
features:

* **enqueue(value)**: adds value to the queue
* **dequeue()**: removes the correct item from the queue and returns its value
  (should raise an error if the queue is empty)
* **peek()**: returns the next value in the queue without dequeueing it. If the
  queue is empty, returns None
* **size()**: return the size of the queue.  Should return 0 if the queue is
  empty.

As with the linked list and stack assignments before this, you may not use any
existing Python implementation to create your queue.

You should update the repository ``README.md`` with information about the Queue you
implemented, including any resources or collaborations you used.

Submitting Your Work
====================


When your tasks are complete and all tests are passing, submit a pull request
from your queue branch back to ``master``.  Copy the URL for that pull request and
submit it.  After you submit your assignment, you may merge your queue branch
back to ``master``.

Use the comment feature in Canvas to submit questions, comments and
reflections.
