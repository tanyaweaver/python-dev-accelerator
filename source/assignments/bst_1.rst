.. slideconf::
    :autoslides: False

****************************************
Implement a Binary Search Tree in Python
****************************************

.. slide:: Implement a Binary Search Tree in Python
    :level: 1

    This document contains no slides.

Tasks
=====

Create a new branch for your data structures repository.
Call it "bst".
You will use this branch to do your work for this assignment.

Add a new file to your data-structures repository.
Call it bst.py.

In this file, implement a Binary Search Tree as a Python class (or classes).
Your tree should have the following methods:

* **insert(self, val)**: will insert the value val into the BST.
  If val is already present, it will be ignored.
* **contains(self, val)**: will return ``True`` if val is in the BST, ``False`` if not.
* **size(self)**: will return the integer size of the BST (equal to the total number of values stored in the tree).
  It will return 0 if the tree is empty.
* **depth(self)**: will return an integer representing the total number of levels in the tree.
  If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
* **balance(self)**: will return an integer, positive or negative that represents how well balanced the tree is.
  Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value.
  An ideally-balanced tree should return 0.


In implementing your tree you may find it helpful to be able to visualize the structure.
You can do so by adding a method that will return the structure of the tree `in DOT notation <https://en.wikipedia.org/wiki/DOT_(graph_description_language)>`_.
The return value of such a method could be written to a file which can then be processed by a tool like `graphviz <http://www.graphviz.org/>`_ into an image.
Some sample code for such a method is included below.
(If not immediately obvious, these methods are quite tied to implementation details of your tree. You will need to significantly update them in order to get them to work):

.. code-block:: python

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.data is None else (
            "\t%s;\n%s\n" % (
                self.data,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)


Your BST implementation must include tests.
The tests, as usual for our data structures, must run both in Python 2.7 and Python 3.5.

Beyond unit testing for the methods you implement, include as an "if __name__ == '__main__' block that document the best-case and worst-case performance of searching the tree for a given value.

Expand your README to include notes about the BST you've constructed. Include any sources or collaborations.

Submitting Your Work
====================

When you've completed your work and all your tests are passing, submit a pull request from the bst branch back to master.
Copy the URL for that pull request and submit it using the URL input.
When that is done, you may merge your branch back to master.
However, do not delete your working branch until your assignment has been graded.

As usual, use the comment function to submit questions, comments and reflections on the work you've done here.