**************************************
Implement the Decision Tree Classifier
**************************************

Tasks
=====

Create a new branch in your data structures repository called ``decision-tree``.
You'll use this branch to do your work for this assignment.
Add a new file to your data-structures repository called ``decision_tree.py``.
In this file, implement a Decision Tree Classifier object.
Your classifier should have the following public methods:

* clf.fit(self, data): construct a decision tree based on some incoming data set; returns nothing
* clf.predict(self, data): returns labels for your test data.
This should be able to take in an iterable of data records (either a tuple of records, or a list of records, or Pandas DataFrame).

The tree should take two optional parameters: ``max_depth`` and ``min_leaf_size``.

* ``max_depth`` will limit the maximum number of steps your tree can take down any decision chain.
If not specified, it'll walk down the chain until a region of parameter space has 100% of one type of class OR only 1 data point.
* ``min_leaf_size`` will limit the minimum number of data points that may exist within a region before ending a decision chain.
If not specified, it'll also walk down the chain until a region of parameter space has 100% of one type of class OR only 1 data point.

Your implementation should only work on two characteristics total.
Keep the scope narrow.
To decide which characteristics to use, try visualizing your data and figuring out where the best separation between classes lies.

Your implementation must include tests.
The tests must run in both Python 2 and Python 3.
Ensure that your tests are properly connected to Travis CI and that you have a Travis badge displayed on your ``README.md``.
Expand your ``README.md`` to include notes about your classifier.
Include any external sources used in its creation.

:download:`Click here </downloads/flowers_data.csv>`_ for a data file of classified flowers which you may use to test your tree.
You can either use the column named "target" or "class_name" as your class label.
They each map directly to each other.


Stretch Goal
-----------

Enable your classifier to use as many characteristics as you provide.
For example, if your input data from ``flowers_data.csv`` looks like (petal_length, petal_width, sepal_length, sepal_width), your tree should be able to split along any one of those characteristics.


Submitting Your Work
====================

When you've completed your work and all your tests are passing, submit a pull request from the ``decision-tree`` branch back to ``master``.
Copy the URL for that pull request and submit it using the URL input on Canvas.
Once submitted you may merge your branch back to ``master``.

Use the comment function to submit quests, comments, and reflections on the work you've done.