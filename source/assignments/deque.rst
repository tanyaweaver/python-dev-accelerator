.. slideconf::
    :autoslides: False

***************************
Implement a Deque in Python
***************************

.. slide:: Implement a Deque in Python
    :level: 1

    This document contains no slides.

Begin by reading about the `Deque data structure <https://en.wikipedia.org/wiki/Double-ended_deque>`_.

Tasks
=====

When you're done, create a new branch in your data structures repository.
On that branch, write tests for and then implement a deque with the following features:

* **append(val)**: adds value to the end of the deque
* **appendleft(val)**: adds a value to the front of the deque
* **pop()**: removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
* **popleft()**: removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
* **peek()**: returns the next value that would be returned by ``pop`` but leaves the value in the deque (returns None if the deque is empty)
* **peekleft()**: returns the next value that would be returned by ``popleft`` but leaves the value in the deque (returns None if the deque is empty)
* **size()**: returns the count of items in the queue (returns 0 if the queue is empty)

As with the linked list and stack assignments before this, you may not use any existing Python implementation to create your deque.

You should update the repository README with information about the deque you implemented, including any resources or collaborations you used.

Submitting Your Work
====================

When your tasks are complete and all tests are passing, submit a pull request from your deque branch back to master.
Copy the URL for that pull request and submit it.
After you submit your assignment, you may merge your deque branch back to master.

Use the comment feature in Canvas to submit questions, comments and reflections.
