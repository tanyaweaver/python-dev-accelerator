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
    :alt: A visualization of the classification regions

The Algorithm
=============

For every step in the tree:

1. There is data :math:`D`, with each row having characteristics (:math:`x_1`, :math:`x_2`, ..., :math:`x_N`) and label :math:`y`

2. Within one characteristic :math:`x_j`, :math:`D` will be divided along a decision boundary :math:`t`. The data will be split into :math:`D_{left}` and :math:`D_{right}`.

.. math::

    D_{left} = D[\text{where } x_j \le t]

    D_{right} = D[\text{where } x_j > t]

3. The best decision boundary will be where the following function is at a minimum:

.. math::
    
    G(D) = \frac{n_{left}}{N_D} \cdot H(D_{left}) + \frac{n_{right}}{N_D} \cdot H(D_{right})

where...

.. math::

    H(D) =  p(1) \cdot (1 - p(1)) + p(2) \cdot (1 - p(2))

is the measurement of impurity (i.e. this region is dominated by one class or a mix of multiple classes), and

.. math::

    p(k) = \frac{n_D(\text{class} = k)}{N_D}

is the fraction of data in the region in class `k`.

4. Split the data at the best available decision boundary, and for each portion (left and right) return to step 1.

5. Iterate on steps 1-4 until you hit you hit your minimum "leaf" size, your maximum tree depth, or :math:`N_D = 1`.


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

* **max_depth**: the maximum number of decisions any branch can take
* **min_leaf_size**: the minimum number of data points acceptable before stopping iteration

Operations
==========

* **clf.fit(training_data)**: construct the tree and build up the decision chains. Returns nothing.
* **clf.predict(test_data)** -> test_data + classification: predict the classification of new data given the decision chains built already built. Returns the data given, as well as the labels output by the tree.

