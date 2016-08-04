.. slideconf::
    :autoslides: False

****************************************
Implement a Singly-Linked List in Python
****************************************

.. slide:: Implement a Singly-Linked List in Python
    :level: 1

    This document contains no slides.

Think back on our discussion of the linked list in class, and then read
`this article in wikipedia`_ about linked lists.

 .. _this article in wikipedia: https://en.wikipedia.org/wiki/linked_list

Armed with this knowledge, implement a singly-linked list in Python:

Tasks
=====

Create a GitHub repository, call it ``data-structures``.

Add to the repository a ``README.md`` that explains that it will hold sample code for
a number of classic data structures implemented in Python. Be sure to include a
section of the ``README.md`` to list resources or collaborations you used in
completing your data structures assignments.

When this preliminary work is finished, commit your changes and make a new
branch in your repository called ``linked_list``.

Check out your new branch. Add a Python module called ``linked_list.py``

In that module, write the required Python class(es) to implement a linked list.
The list class should be named LinkedList.  Your list implementation should
support the following methods:

* **insert(val)** will insert the value 'val' at the head of the list
* **pop()** will pop the first value off the head of the list and return it.
* **size()** will return the length of the list
* **search(val)** will return the node containing 'val' in the list, if present, else None
* **remove(node)** will remove the given node from the list, wherever it might be (node must be an item in the list)
* **display()** will print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')"

The constructor for your LinkedList class should allow optionally passing an
iterable of values. which will result in a linked list instance containing the
values in the iterable. The head of the list should be the last item in the
iterable::

    LinkedList([1, 2, 3]) => (3)->(2)->(1)

**You must not use the Python list type to solve this problem.**

Include pytest unit tests for your linked list class in a file called
test_linked_list.py. Use Test Driven Development principles. For each method of
your class, including the constructor, first implement a test that would verify
that the method works, run the tests to show that it fails, then implement the
code needed to make it pass. Be thorough in your testing.  Ensure that you
cover failure modes and possible edge-cases. The tests you write are as much a
part of this assignment as the linked list itself.

Submitting Your Work
====================

When you have finished your work and all your tests are passing, create a new
Pull Request from your ``linked_list`` branch back to your ``master`` branch.
For your submission, provide a link to that pull request.

Once you have submitted the assignment, you may merge the pull request back to
master. I’ll still be able to interact with it properly.
