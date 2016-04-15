.. slideconf::
    :autoslides: False

************************
Implement Insertion Sort
************************

.. slide:: Implement Insertion Sort
    :level: 1

    This document contains no slides.

In this assignment series we will explore a number of sorting algorithms.
Your goal is to understand both the implementation of the algorithm, and the circumstances under which it is a good choice.

Tasks
=====

Read about the `Insertion Sort <http://en.wikipedia.org/wiki/Insertion_sort>`_

When you're ready, create a new branch for your data-structures repository and add a module to implement the sorting algorithm.

Include an "if __name__ == '__main__':" block at the end of your module that demonstrates the performance characteristics of this sort. 
Cover a variety of lengths of input in both the best and worst-case scenarios.
Executing your module should print informative output about the performance of your sort to the terminal:

.. code-block:: bash

    $ python bogosort.py

    The bogosort randomly shuffles the items in a list until the list is sorted.
    It performs best for very short lists

    Input: [2, 1]
        number of runs: 500
        average time: 2.0e-4 seconds

    Input: [randint(0, 1000000) for i in range(10000)]
        number of runs: 500
        average time: 2345.6 seconds

Add tests to demonstrate that the sorting algorithm works in both Python 2 and 3

Add information about your implementation to the README.md in your package, including any sources and collaborations you used in creating it.

Submitting Your Work
====================

When your work is complete and your tests are passing, create a pull request from your working branch back to master.
Submit the URL of your pull request.
When you've done this, you may merge your pull request, but do not delete your branch until your work has been graded.

Use the comment feature to add any questions, comments or reflections on your work.