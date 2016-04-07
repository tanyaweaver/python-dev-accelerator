.. slideconf::
    :autoslides: False

**********************************
Binary Search Tree: Self-Balancing
**********************************

.. slide:: Binary Search Tree: Self-Balancing
    :level: 1

    This document contains no slides.

The binary search tree you have implemented has the ability to document its 'balance'.
But there is no way to ensure that it is in fact balanced (other than by seeding it with ideal data).
And as it turns out, balance is important in a binary search tree.
The better your balance, the more ideal your performance for finding values within the tree.

Tasks
=====

As a last step for your work on the tree, add the ability to balance the tree.
You *could* re-build the tree entirely each time you add or remove an item.
That's a valid solution for situations where the tree is not often updated.

But that solution isn't any fun.

Instead, I want you to add functionality to your tree that will adjust the balance automatically any time an item is inserted or removed.
There are a number of possible approaches for building a `self-balancing <http://en.wikipedia.org/wiki/Self-balancing_binary_search_tree>`_.
You should read about them, and choose one.
I have found `AVL <http://en.wikipedia.org/wiki/AVL_tree>`_ and `Red-Black <http://en.wikipedia.org/wiki/Red-black_tree>`_ to be reasonably understandable.

You might find information like this `description of AVL tree rotations in psuedocode <https://en.wikipedia.org/wiki/Tree_rotation>`_ helpful.

Submitting Your Work
====================

As usual, do your work on a branch.
When you are finished (and all tests are passing) create a new Pull Request containing only the work on balancing.
Submit the URL of your pull request.
When that is done, you may merge the pull request.

Add documentation of your changes to your README file.
Include any sources or collaborations.

Ensure that your repository is connected to Travis CI and that you have your travis badge displayed in your README.