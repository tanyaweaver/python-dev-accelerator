.. slideconf::
    :autoslides: False

*********************************
Implement a Binary Heap in Python
*********************************

.. slide:: Implement a Binary Heap in Python
    :level: 1

    This document contains no slides.

Read about the `Binary Heap <http://en.wikipedia.org/wiki/Binary_heap>`_.

Tasks
=====

Create a new branch in your data structures repository.  Call it binheap.
You'll do your work for this assignment in the new branch.

Add a new Python module to your repository.  In that file, implement a Binary
Heap.  You may use the Python list type as a storage unit for your
implementation.

You may choose for yourself whether you want to implement a min-heap or a
max-heap.

For an additional challenge, implement a heap that can be either and allow the
choice to be made at initialization time.

Your heap should support the following public operations:

* **.push()**: puts a new value into the heap, maintaining the heap property.
* **.pop()**: removes the "top" value in the heap, maintaining the heap property.

You will need to implement some private api in order to support those
operations.

The constructor for your heap should default to creating an empty heap, but
allow for creating a populated given an iterable as an input.

For each feature of your heap, start by writing tests to demonstrate that
feature.  Then implement the code to pass the tests.

Update your README with information about your implementation of the Binary
Heap data type.  Include all references and collaborations.

Submitting Your Work
====================

When you are finished with your implementation and all tests are passing,
create a Pull request from your binheap branch to master. Copy the URL of the
new pull request.  Submit that URL using the URL input.  After you have
completed this task, you may merge your branch back to master.

As usual, use the comment feature to submit questions, comments and reflections
on the work you did for this assignment.
