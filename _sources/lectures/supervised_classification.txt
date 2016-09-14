*************************
Supervised Classification
*************************

Consider an average e-mail inbox.
This inbox receives any number of messages from various sources many times per day.
Some of those sources aren't folks that you want to hear from, so you manually filter them away.
Most emails you get with "Special Offer Guarantee!" in the body can go straight to spam. 
Some are marked "important!", typically ones from emails ending in "@mycompany.com". 
Others still are just regular emails that you may look into at some point in the future.

If you're fortunate, your e-mail client will start to learn from what you've been doing with your messages and try to emulate that activity.
It'll look at all the things you've labeled as "spam" or "trash" and infer what constitutes a message to be labeled as such from the patterns within.
Similarly, "important" messages will likely have certain similarities that would identify them ahead of time, without you having to mark it yousrelf.

If your email client has any sort of message-filtering built in it's making use of a **Supervised Classification** algorithm, using data that you DO know about to infer labels for data that you DON'T know about.

Common `supervised classification algorithms <http://scikit-learn.org/stable/supervised_learning.html>`_ include:

* Regression algorithms
* Support Vector Machines
* **K-Nearest Neighbors**
* Gaussian Processes
* Neural Networks
* Naive Bayes
* **Decision Trees**

We'll talk about the ones in bold here.
You're encouraged to explore the rest on your own.


The Look of Labeled Data
========================

What constitutes a label, or a *class*, is entirely dependent upon the question being asked.
Consider this data about survivors of the Titanic:

.. code-block:: ipython

    In [1]: import pandas as pd

    In [2]: data = pd.read_csv("../downloads/titanic_data.csv")

    In [3]: print(data)
       PassengerId  Survived  Pclass                                                Name     Sex   Age  SibSp Parch            Ticket     Fare Cabin Embarked 
    0            1         0       3                             Braund, Mr. Owen Harris    male  22.0      1     0         A/5 21171   7.2500   NaN        S 
    1            2         1       1   Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1     0          PC 17599  71.2833   C85        C  
    2            3         1       3                              Heikkinen, Miss. Laina  female  26.0      0     0  STON/O2. 3101282   7.9250   NaN        S  
    3            4         1       1        Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1     0            113803  53.1000  C123        S 
    4            5         0       3                            Allen, Mr. William Henry    male  35.0      0     0            373450   8.0500   NaN        S 
    5            6         0       3                                    Moran, Mr. James    male   NaN      0     0            330877   8.4583   NaN        Q  
    6            7         0       1                             McCarthy, Mr. Timothy J    male  54.0      0     0             17463  51.8625   E46        S
    7            8         0       3                      Palsson, Master. Gosta Leonard    male   2.0      3     1            349909  21.0750   NaN        S
    8            9         1       3   Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female  27.0      0     2            347742  11.1333   NaN        S
    9           10         1       2                 Nasser, Mrs. Nicholas (Adele Achem)  female  14.0      1     0            237736  30.0708   NaN        C
    ...   

If my question were "Who lived and who died on the Titanic?" then clearly the class would be "Survived", and I would write an algorithm that most efficiently predicted survival.
However, if my question had been, "What's the best determinant of where a passenger embarked from?" my classes would be entirely different and would pull from the "Embarked" column.

When writing your own machine learning algorithms, you can tailor them to interpret along the classes given in your data.
This means your classes can be "1, 2, 3" or "A, B, C" or "fruit, vegetable, meat", or whatever.
However, if you were to use the algorithms present in Python's `scikit-learn <http://scikit-learn.org/>`_ package for Data Science and Machine Learning, you'd have to translate the classes to numerical information.
