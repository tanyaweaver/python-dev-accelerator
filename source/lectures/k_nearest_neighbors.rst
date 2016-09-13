******************************
K-Nearest Neighbors Classifier
******************************

Another classifier, the K-Nearest Neighbors algorithm seeks to categorize new data based on the labels of the K closest data points.
"Closeness" is determined by the distance between test point :math:`p` with characteristics :math:`(p_1, p_2,..., p_N)` and another point :math:`q` with characteristics :math:`(q_1, q_2,..., q_N)`.

The distance between any two points can be calculated as

.. math::

    d = \sqrt{(p_1 - q_1)^2 + (p_2 - q_2)^2 + ... (p_N - q_N)^2}

Assuming that :math:`p` and :math:`q` are NumPy arrays, the function for measuring distance is:

.. code-block:: python

    import numpy as np

    def distance(p, q):
        return np.sqrt(np.sum((p - q)**2))

.. image:: http://cfile5.uf.tistory.com/image/2256FB4D5111B6FA0DA64B
    :width: 400px
    :alt: K-Nearest Neighbors example

.. image:: http://scikit-learn.org/stable/_images/plot_classification_002.png
    :width: 400px
    :alt: Visualization of the results of a K-Nearest Neighbors fitting function


The Algorithm
=============

1. Use characteristics of interest to calculate the distances between point :math:`p` and all other points

2. Sort points in order of distance from :math:`p`

3. Keep the first :math:`K` points

4. Tally the number of points in each class

5. If the tally is tied between classes, reduce K by 1 and count again

6. Assign to :math:`p` the class with the highest total


Advantages
==========

* The cost of the learning process is zero
* Often successful when labeled data is well-mixed or data boundaries are irregular.

Disadvantages
=============

* Very inefficient for large data sets 
* There's no real model to interpret
* Performance depends on the number of dimensions
* Inconsistent results when there's ties in votes

Attributes
==========

* **neighbors**: the number of nearby points from which to inherit a label

Operations
==========

* **clf.predict(full_data, test_data)**: given some full data set, predict the classifications on a new data set of one or many points.

