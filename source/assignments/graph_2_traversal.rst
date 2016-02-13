.. slideconf::
    :autoslides: False

***********************
Build a Simple WSGI App
***********************

.. slide:: Build a Simple WSGI App
    :level: 1

    This document contains no slides.

Read a bit about `graph traversal <http://en.wikipedia.org/wiki/Graph_traversal>`_, `depth-first search <http://en.wikipedia.org/wiki/Depth-first_search>`_ and `breadth-first search <http://en.wikipedia.org/wiki/Breadth-first_search>`_.

Tasks
=====

When you've got an idea of how these work, create a new branch in your data_structures repository.
On that branch, add a pair of new methods to your graph implementation.

* **g.depth_first_traversal(start)**: Perform a full depth-first traversal of the graph beginning at start.
  Return the full visited path when traversal is complete.
* **g.breadth_first_traversal(start)**: Perform a full breadth-first traversal of the graph, beginning at start.
  Return the full visited path when traversal is complete.

In addition, write some demonstration code in an ``if __name__ == '__main__':`` block at the end of your file that shows how the two methods of traversal compare to each other when performed on the same graph.
See if you can demonstrate the performance characteristics of the two methods over a variety of graph structures.

If your graph is cyclic, each method should avoid getting trapped in loops.

Write tests that prove that your methods work for both cyclic and non-cyclic graphs, etc.

Update your README with information about your implementations, as well as any references or collaborations you used in completing the work.

Submitting Your Work
====================

When you are finished with your work and the tests are passing, create a Pull request from your new branch back to master.
Copy the URL and submit it.
You may then merge your branch back to master.

As usual, add any, questions, concerns or reflections on this work using the comment feature in Canvas.
