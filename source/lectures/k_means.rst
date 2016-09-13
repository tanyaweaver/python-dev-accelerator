******************
K-Means Classifier
******************

The job of the K-Means Classifier is to establish :math:`k` nodes, each one representing the "center" of a cluster of data.
For each node desired then, the algorithm positions that center (called a "centroid") at the point where the distance between it and the nearest points is on average smaller than the distance between those points and the next node.

.. image:: http://blog.mpacula.com/wp-content/uploads/2011/04/kmeans1.png
    :width: 400px
    :alt: K-Means Nodes


The Algorithm
=============

1. Within the space of your data, choose :math:`k` nodes to have random positions.

2. Calculate the distance between **every** data point and each node.

3. For each data point, assign its "class" to whichever node is closest.

4. Using these tentative classes, find the average position (i.e. the *mean*) of each class. Basically, where's the "center" of each class?

5. Move each node to the position of its class's center.

6. Repeat steps 2-5 until the nodes don't move much anymore or until you've reached some maximum number of iterations.

7. Assign the resulting classes to the data.


Advantages
==========

* Will always result in a solution.
* Generally good at picking centroids when data shows believable separations.


Disadvantages
=============

* Computationally expensive for large data sets 
* Highly dependent on how data is clustered. Also highly dependent on what data is present. Under-sampling skews results.
* Highly dependent on where centroids are initialized. Problematic when they're close to each other.
* Highly dependent on how many centroids are initialized.
* Number of centroids may not correspond to actual number of separations in data; entirely at the mercy of the programmer.
* Poor at predicting separations in irregularly shaped data (e.g. elongated clusters)


Attributes
==========

* **centroids**: the number of clusters expected from the data
* **max_iter**: the number of iterations before the algorithm stops
* **min_step**: the smallest difference in distance between an old centroid and a new centroid before the algorithm stops

Operations
==========

* **clf.fit(full_data, k)**: generate :math:`k` nodes for classifying data.
* **clf.predict(some_data)**: predict classification (i.e. if :math:`k = 2` then class 1 or 2) on data.

