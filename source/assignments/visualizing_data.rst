******************
Analyze a Data Set
******************

Today we've learned about how to use ``Numpy``, ``Matplotlib``, and ``Jupyter Notebook`` to read and present data.
Now let's use it with an actual data set.
:download:`Here </downloads/boston_housing_data.csv>`_ is a link to a data set compiling data on home values in suburbs in Boston from 1993.
You can read more about it `here <https://archive.ics.uci.edu/ml/datasets/Housing>`_, where there is a description of the columns.

Tasks
=====

If you haven't already, start a new virtual environment and create a repository named ``machine_learning``.
Within that repository start a branch called ``analyze``.

Open a new Jupyter Notebook entitled **Analyze a Data Set**.
Beneath that title, put the date and your name.

Download the above data set and read it into your Jupyter Notebook.
Briefly describe the data in a cell above all your code.
Then, from this data set, find:

* The median and average home values across all Boston Suburbs in dollars.
* The median home value of the suburb with the newest houses.

Visualize the following appropriately (as either points or lines):

* The relationship between per-capita crime rate and the pupil-teacher ratio. Differentiate between whether or not the suburb is bounded by the Charles River.
* The relationship between the proportion of black citizens and the distance to employment centers in Boston.
* The relationship between median value of owner-occuped homes and nitric oxide concentration along with median home value and the proportion of non-retail business (on the same plot).

In text, describe the figures you create and any conclusions that you may draw from your visualizations.
Make sure that all your figures have axis labels, as well as titles for each plot.

Finally, come up with a question of your own about this data set.
Try to use the data to answer that question.
Write both the question and your data-driven answer to that question in your Jupyter Notebook.

Submitting Your Work
====================

Once you're done with the above questions, reset your Notebook and run all of the cells from top to bottom.
When it's done, your cells should start with ``[1]`` and every sequent cell should have numbering ``[N + 1]``.

When your Notebook is clean of unnecessary comments and is well organized from top to bottom, push your Notebook **and only your Notebook** (not the ``.ipynb-checkpoints`` directory or your data) to GitHub and open a pull request to your ``master`` branch.
Submit the link to that pull request to Canvas.
When you're done, merge your ``analyze`` branch to ``master``.


