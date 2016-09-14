***************************
Unsupervised Classification
***************************

Real-world data rarely comes in labeled.
However, data tends to naturally cluster around like-things.
Consider the following data about stars and galaxies.

.. ipython::

    In [1]: import pandas as pd

    In [2]: data = pd.read_csv("source/downloads/lean_stars_and_galaxies.csv")

    In [3]: print(data[:10])

If I were to visualize this data, I would see that although there's a ton of it that might wash out clumpy structure there are still some natural clusters in the data.

.. ipython::

    In [3]: import matplotlib.pyplot as plt

    In [4]: plt.scatter(data.col12, data.w3, s=1, edgecolor="None", c='k', alpha=0.1)

    In [5]: plt.xlim(-0.5, 2); plt.ylim(14, 5); plt.minorticks_on()

    @savefig unsupervised_1.png width=8in
    In [6]: plt.xlabel("Infrared Color"); plt.ylabel("Brightness")

An unsupervised classification algorithm would allow me to pick out these clusters.
Although it wouldn't be able to tell me anything about the data (as it doesn't know anything aside from the numbers it receives), it would give me a starting point for further study.

With this example my algorithm may decide that a good simple classification boundary is "Infrared Color = 0.6".
This would separate my data into left (IR color < 0.6) and right (IR color > 0.6).
From there I can investigate further and study this data to see what might be the cause for this clear separation.

Here are examples of some unsupervised classification algorithms that are used to find clusters in data:

* **K-Means Clustering**
* Gaussian Mixture Models
* Mean Shift
* Hierarchical Clustering
* Neural Networks