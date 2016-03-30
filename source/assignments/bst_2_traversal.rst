.. slideconf::
    :autoslides: False

******************************
Binary Search Tree: Traversals
******************************

.. slide:: Binary Search Tree: Traversals
    :level: 1

    This document contains no slides.

Trees can be traversed in four ways.
There are three depth first traversals: in-order, pre-order and post-order
There is one breadth first traversal.

Tasks
=====

In your data-structures repository, add methods that implement each of these four traversal patterns to the BST that you implemented previously:

* **in_order(self)**: will return a generator that will return the values in the tree using in-order traversal, one at a time.
* **pre_order(self)**: will return a generator that will return the values in the tree using pre-order traversal, one at a time.
* **post_order(self)**: will return a generator that will return the values in the tree using post_order traversal, one at a time.
* **breadth_first(self)**: will return a generator that will return the values in the tree using breadth-first traversal, one at a time.

Your work should include unit tests that fully demonstrate each of the four methods you've added.
Make sure to cover expected and edge cases.

Add documentation of your new methods to your README file.
Include any sources or collaborations.

Ensure that your tests are properly connected to Travis CI and that you have a travis badge displayed on your README.

Submission
==========

Do your work on a branch.
When you are finished and all your tests are passing, create a new pull request back to master from your branch and submit the URL for that pull request.
When you've made your submission, you may merge the branch, but do not delete it until your assignment has been graded.

As usual, use the comment function to submit questions, comments and reflections on the work you've done here.