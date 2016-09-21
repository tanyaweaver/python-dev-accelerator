********************************************
Implement the K-Means Classifier
********************************************

Tasks
=====

Create a new branch in your data structures repository called ``kmeans``.
You'll use this branch to do your work for this assignment.
Add a new file to your data-structures repository called ``k_means.py``.
In this file, implement a K-Means Classifier object.

On initialization, your K-Means Classifier should take semi-optional parameters ``max_iter`` and ``min_step``.
If one is specified you don't need the other.

Your classifier should have the following public methods:

* clf.fit(self, data, k): Generates `k` centroids with which to classify the given data. **Does not return anything**
* clf.predict(self, data): Returns classes for some data if ``clf.fit`` has already been called. This should be able to take in an iterable of data records (either a tuple of records, or a list of records, or Pandas DataFrame). If ``clf.fit`` has not yet been called, raise an appropriate error.

The classifier should default to 2 centroids.
We'll also only work with two characteristics for this, though you can generalize your classifier if you want.
Appropriately handle the case where ``k`` is provided with an invalid input (e.g. -1, or ``k > len(data)``)

Your implementation must include tests.
The tests must run in both Python 2 and Python 3.
Ensure that your tests are properly connected to Travis CI and that you have a Travis badge displayed on your ``README.md``.
Expand your ``README.md`` to include notes about your classifier.
Include any external sources used in its creation.

:download:`Click here </downloads/flowers_data.csv>`_ for a data file of classified flowers which you may use to test your classifier.
You can either use the column named "target" or "class_name" as your class label.
They each map directly to each other.

You can also use the :download:`lean_stars_and_galaxies.csv </downloads/lean_stars_and_galaxies.csv>`_ data shown in the notes.
If you do, ask for help.


Stretch Goal
-----------

Enable your classifier to use as many characteristics as you provide.
For example, if your input data from ``flowers_data.csv`` looks like (petal_length, petal_width, sepal_length, sepal_width), your classifier should be using the total distance between points.
If unclear, ask.


Submitting Your Work
====================

When you've completed your work and all your tests are passing, submit a pull request from the ``kmeans`` branch back to ``master``.
Copy the URL for that pull request and submit it using the URL input on Canvas.
Once submitted you may merge your branch back to ``master``.

Use the comment function to submit quests, comments, and reflections on the work you've done.