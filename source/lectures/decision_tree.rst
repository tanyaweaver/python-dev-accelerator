****************************
The Decision Tree Classifier
****************************

A decision tree classifier is an algorithm that uses branches of divisions in parameter space to classify data.
Training data is used to construct the tree, and any new data that the tree is applied to is classified based on what was set by the training data.
Divisions occur one characteristic at a time, so classification ends up following a human-understandable sequence boolean decisions (e.g. class A people are shorter than 5 foot 3, and class B people are taller).

.. image:: http://mines.humanoriented.com/classes/2010/fall/csci568/portfolio_exports/lguo/image/decisionTree/decisionTree.jpg
    :width: 400px
    :alt: A visualization of a decision tree

.. image:: http://perclass.com/doc/guide/images/clas_sdtree_2.png
    :width: 400px
    :alt: A visualization of the classification

Advantages
==========

* Requires very little data preparation/manipulation
* Prediction on test data is O(log n)
* Can work on numerical and categorical data

Disadvantages
=============

* This does not generalize data well, and is *very* prone to overfitting, especially as life sizes decrease.
* Cannot handle data with missing values

Attributes
==========

* max_depth: the maximum number of decisions any branch can take
* min_leaf_size: the minimum number of data points acceptable before stopping iteration

Operations
==========

* tree.fit(``training_data``): construct the tree and build up the decision chains. Returns nothing.
* tree.predict(``test_data``) -> test_data + classification: predict the classification of new data given the decision chains built already built.
Returns the data given, as well as the labels output by the tree.

