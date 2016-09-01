********************************
Introduction to Machine Learning
********************************

Machine Learning is tightly coupled with Data Science, and is for the most part a data-driven field. 
It's chiefly concerned with taking some initial data set as a starting point and using it to predict the properties of unknown data.
As such, Machine Learning problems tend to come in two flavors: Classification and Regression

Classification
==============

.. image:: http://scikit-learn.org/stable/_images/plot_classification_0012.png
    :width: 400px
    :alt: K-Nearest Neighbors Classification Example. Source: http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
  
*The main statement*: Data from the same population should share similar characteristics that differentiate them from other populations. 
Thus given some data, we should be able to adequately categorize some new data.

For example:

- Teenagers tend to have fewer financial assets and know fewer people than thirty-somethings.
- Sea water near the equator has higher temperatures and lower mineral content than water near the poles.
- Public schools tend to have larger class sizes, lower test scores, and less funding than private schools.


Regression
==========

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/2000px-Linear_regression.svg.png
    :width: 400px
    :alt: Linear Regression Example. Source: https://en.wikipedia.org/wiki/Linear_regression

*The main statement*: While it may not be simple, the world acts in a predictable, regular manner.
So, given data on the way that a certain thing has been behaving thus far, I can predict how it will behave in the future.

For example:

- Stock market (or Bitcoin) prices with time
- The average width of a tree's leaf given the height of the tree
- Activity on Twitter given the hour of the day


Whether attacking an issue of classification or regression, a Machine Learning problem will require data to make decisions.
Python's scientific and numerical tools allow us to read, write, visualize, and otherwise work with this data in an efficient and organized manner.
Typically those tools are wrapped together and included in the Anaconda distribution of Python. 
**DO NOT DOWNLOAD THIS DISTRIBUTION. IT WILL WRECK YOUR WORK WITH ENVIRONMENTS**.

Instead follow these steps:

.. code-block:: shell

    bash-3.2$ mkdir machine_learning
    bash-3.2$ cd machine_learning
    bash-3.2$ python3 -m venv .
    bash-3.2$ source bin/activate

Download the tools in the requirements file :download:`here </downloads/data_science_requirements.txt>`_ to your new ``machine_learning`` directory.
Then, ``pip install`` the requirements file:

.. code-block:: shell

    (machine_learning) bash-3.2$ pip install -r data_science_requirements.txt --upgrade


Jupyter Notebook
================

Thus far we've written all of our Python code either in scripts or on the command line using the Python interpreter.
Jupyter notebooks combine the convenience and code-persistence of the iPython interpreter with the editability and thought-persistence of a script.
The file extensions for Jupyter notebooks are ``.ipynb`` since they inherit from what used to be iPython notebooks.
Let's create one!

.. code-block:: shell

    (machine_learning) bash-3.2$ jupyter notebook
    [I 17:24:55.837 NotebookApp] Serving notebooks from local directory: /Users/Nick/Documents/codefellows/courses/code401_python/machine_learning
    [I 17:24:55.838 NotebookApp] 0 active kernels 
    [I 17:24:55.838 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 17:24:55.838 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

Unless told otherwise (or there's another instance of Jupyter Notebook already running), Jupyter Notebook will always serve on port 8888.
Jupyter Notebook will pop open a tab in your browser at the address ``http://localhost:8888/tree`` where you will see your current working directory.
In it will be all the files you currently have access to.

We can create a new notebook using the menu on the left side of the screen.
Click the "New" button to get a dropdown menu and ``Python 3`` to open a new Python 3 Jupyter Notebook.
If your environment also included Python 2, you'd have the option to open a notebook in Python 2.

When you open a new notebook you're started off with an empty cell.
Within this cell you will write code as you would either in a script file or in the command line.
The code that you write will automatically have syntax highlighting for your convenience.
You execute the code within a cell by holding ``Shift`` and pressing ``Enter``.

.. code-block:: ipython

    In [1]: print("Hello World")
    Hello World

If the line of code that you write prints to stdout, that output will appear below the cell.
If instead you declare a variable, import anything, or declare a function or a class, nothing will appear.
You can of course write multiple lines of code, because otherwise it'd just be silly.

You can write code in your notebook as you would in any script file. 
If you try to write code blocks, it will auto-indent for you.
Some of the same commands for applying comments or indentations in Sublime (or Atom) are present here.

If you need to check the documentation of an object or method, type the following

.. code-block:: ipython

    In [2]: ? object_or_method

Jupyter Notebook will pop up a mini-window from the bottom of your screen containing the top-level documentation for that object or method.
You can also get more detailed documentation by typing

.. code-block:: ipython

    In [3]: help(object_or_method)

Jupyter will print the detailed documentation for you below that cell in a scrollable field.

One important difference between Jupyter Notebook and iPython is that the order in which code is executed can change and is extremely important.
Consider the line numbers on the left side. 
The higher the number, the more recently that cell has been executed.
If you re-bind a name to a different value in a previous cell, any code executed after that will use the new value even though it appears earlier on in the notebook. 
This allows for experimentation with your code without having to re-run an entire script.
It can however be dangerous if you don't maintain an understanding of how your code is working.

If you've been experimenting with code in your notebook and want to refresh and run all the cells from top-to-bottom, click on ``Kernel`` in the menu at the top.
``Restart & Run All`` will wipe all of your output, restart the kernel upon which this particular notebook is running, and execute every cell in order from top to bottom.
If any exceptions are thrown along the way that execution will stop at the offending cell, and the stack trace will print into the notebook.

Because these notebooks were modeled after how scientists write and think in their own notebooks, you have the option of being able to write text and/or Markdown in cells amongst your code.
This is accomplished via the dropdown menu at the top currently entitled ``Code``.
Select a cell, click on that menu, and change the cell's format to ``Markdown``.
Then you can write code in Markdown as you please, and render that Markdown when you execute the cell.
This is very handy for writing down thoughts as you try out code.

As you write more code and text, your notebook will no doubt become cluttered.
Keep a clear mind by keeping a clean notebook. If you're not using a cell, delete it.
To delete a cell, select that cell and navigate to the ``Cell`` menu at the top.
Select ``Delete Cells`` and poof, the cell is gone.
You can accomplish this faster with keyboard commands.
Selecting a cell (without the cursor blinking inside the cell) and hitting the ``D`` key twice will delete a cell.
Alternatively, you can add a new cell by hitting the ``A`` key once.
All of these keyboard commands and more are available in the ``Help`` menu at the top under ``Keyboard Shortcuts``.

Finally, save your notebook!
You can use your normal keystroke for saving files here if you'd like, or you can navigate to the ``File`` menu and select ``Save and Checkpoint``.
A checkpoint acts sort of like a Git commit, allowing you access to a previous state for your code.
If you go too long without saving, Jupyter Notebook will autosave (though not that frequently, so save often!).

You'll notice that when you save, you don't get the option to change the name of your notebook.
You can do that by clicking on "Untitled" at the top, and changing it there.
This will change the filename itself on the file system.

If you want to shutdown this individual notebook, navigate back to ``https://localhost:8888/tree`` and select the checkbox next to the name of your notebook.
The click on the ``Shutdown`` button at the top.
To exit out of Jupyter Notebook entirely, return to your command line and hit ``Control-C``.
You'll be asked to confirm the shutdown of the server that the Notebook, and if you take too long it'll assume you made a mistake and resume operations.
When you confirm shutdown of the server, it'll also shutdown any currently-running notebooks being served from that port.

Numpy
=====

Pandas
======

Matplotlib
==========

