.. slideconf::
    :autoslides: False

***************************
Implement a Stack in Python
***************************

.. slide:: Implement a Stack in Python
    :level: 1

    This document contains no slides.

For this assignment, you will add the implementation of a `stack`_ to your
``data-structures`` repository.

.. _stack: http://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Tasks
=====

The Stack class should be in a file called ``stack.py`` and the class should be
called Stack.  This class should implement two methods:

* **push(value)** - Adds a value to the stack. The parameter is the value to
  be added to the stack.
* **pop()** - Removes a value from the stack and returns that value.  If the
  stack is empty, attempts to call pop should raise an appropriate Python
  exception class.

Your class implementation should include a constructor that optionally accepts
an iterable of values.  When an iterable is passed, the result should be a
stack which contains the values in the iterable.

Your implementation is not allowed to use the built-in Python list, tuple or
dictionary.  Nor are you allowed to use any of the native implementations of
stack/queue/dequeue from the queue python standard library module.

Your implementation must include pytest unit tests.  For each method on your
stack class, including the constructor, write your tests first, then implement
the methods that will support them. Be thorough in your tests, test failure
modes as well as successes. Tests are as much a part of this assignment as the
stack itself.

Update the repository ``README.md`` with information about the Stack you implemented,
including any resources or collaborations you used.

Submitting Your Work
====================

Work on a branch in your GitHub repository.  When you are done, and all tests
are passing, open a pull request from your ``stack`` branch back to the ``master``
branch of your repository.  Submit the URL for that pull request.

Once you have submitted the assignment, you may merge the pull request back to
``master``.  I'll still be able to interact with it properly.

Use the comment feature to add any questions or comments you come up with while
working on this assignment.
