.. slideconf::
    :autoslides: False

****************************************
Implement a Doubly-Linked List in Python
****************************************

.. slide:: Implement a Doubly-Linked List in Python
    :level: 1

    This document contains no slides.

Read a bit about the `Doubly-Linked List`_

Tasks
=====

Make a new branch of your data structures repository.  Call it ``dll`` On that
branch implement a doubly-linked list.  Your implementation should have the
following methods:

* **insert(val)** will insert the value 'val' at the head of the list
* **append(val)** will append the value 'val' at the tail of the list
* **pop()** will pop the first value off the head of the list and return it.
* **shift()** will remove the last value from the tail of the list and return
  it.
* **remove(val)** will remove the first instance of 'val' found in the list,
  starting from the head. If 'val' is not present, it will raise an appropriate
  Python exception.

Be sure to write tests to cover your new data structure.  For each feature of
your list, write the test that demonstrates it first, then implement the
feature.

Update the README to include this new structure.  In particular, add a
paragraph explaining different use-cases where the singly or doubly-linked list
might be more appropriate.

Submitting Your Work
====================

When you are done working and all your tests are passing, create a pull request
from the dll branch to master. Copy the URL of the pull request and submit that
using the URL input.  After this is done, you may merge your branch back to
master.

As usual, use the comment feature to submit questions, comments and reflections
on the work you did for this assignment.

.. _Doubly-Linked List: http://en.wikipedia.org/wiki/Doubly_linked_list