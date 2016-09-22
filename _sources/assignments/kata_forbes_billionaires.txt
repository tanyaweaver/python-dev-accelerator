.. slideconf::
    :autoslides: False

**********************************
Python Practice: The Forbes Top 40
**********************************

.. slide:: Python Practice: The Forbes Top 40
    :level: 1

    This document contains no slides.

Tasks
=====

Download :download:`this JSON file </downloads/forbes_billionaires_2016.json>` containing the top 40 billionaires in the world. 
Each has a name, age, rank, net worth, industry that made them rich, and their country. For the curious, the data was compiled from `Forbes.com <http://www.forbes.com/billionaires/list/>`_.

Write a function that,

* returns the name, net worth, and industry of the **oldest billionaire under 80 years old** AND **the youngest billionaire** with a valid age.
* Oldest *under* 80, not *including* 80.
* You may not use a sorting function.
* You may not use any external library (you don't need it).

Stretch Goals
-------------

Write another function that takes the company owned by the oldest under 80 and youngest billionaire and scrapes the web for its current stock price.
If the company is not public, have an appropriate message. If the company is not an actual company, have an appropriate message.

Submitting Your Work
====================

Create a ``forbes`` branch in your ``code-katas`` repository. Add this/these function(s) in a script to your ``forbes`` branch.

The tests that demonstrate your code works should be in a ``test_forbes.py`` file.
Add documentation about your code in the repo's ``README.md``.
Make sure to add notes about and resources or collaborators you worked with in
solving this problem.

After you've added your code solution into GitHub, send a pull request
to your master branch.
**Submit the link to that pull request to Canvas.**

Use the comment box in Canvas to add any questions, comments or reflections on this
assignment and your approach to it.