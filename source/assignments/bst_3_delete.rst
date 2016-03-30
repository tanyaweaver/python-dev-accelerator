.. slideconf::
    :autoslides: False

**********************************
Binary Search Tree: Deleting Nodes
**********************************

.. slide:: Binary Search Tree: Deleting Nodes
    :level: 1

    This document contains no slides.

Further extend the BST implementation you've been adding this week.
Add the ability to delete nodes from anywhere in the tree.

Tasks
=====

The API method you will add should have the following signature:

* **delete(self, val)**: remove val from the tree if present, if not present this method is a no-op.
  Return None in all cases.

Remember that there are three cases to be considered when deleting a node:

* The node is a leaf (has no descendants)
* The node has one descendant (either left or right)
* The node has two descendants (both left and right)

Your delete method should choose the appropriate course of action in the third case to keep the tree as well balanced as possible.

You will need to write some additional methods to support this delete method.
Make these methods "private" by prepending their names with an underscore.

Write tests that demonstrate the correct functioning of your delete method under a variety of cases.
Be as thorough as you can.

Add documentation of your new method to your README file.
Include any sources or collaborations.

Ensure that your repository is connected to Travis CI and that you are displaying a travis badge on your README.

Submitting Your Work
====================

Do your work on a branch.
When your work is complete, and all your tests are passing, make a pull request to master from your working branch.
Submit the URL for that pull request.
After submitting, you may merge your pull request, but do not delete the branch or the PR until your work has been evaluated.

Use the comments for your submission to add any questions that you have which come up in implementing this feature.
