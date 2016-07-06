===============================
Python Learning Journal: Step 2
===============================

You’ve been creating your learning journal entries so far using a shared journal I have created for you. It’s time now to make your own version.

Tasks
=====

If you do not already have one, create a ``learning-journal`` repository in GitHub. Add the application skeleton created in class to this repository. Ensure that the repository also contains a good Python .gitignore file and an appropriate OSS license.

Once the basics are in place, create a new branch (``step1``) for today's work. Do your work on this branch.

Using what you learned today, both in class and in your readings, accomplish the following tasks for your learning journal:

* Move your HTML mockups into the ``templates`` directory and your CSS stylesheet into the ``static`` directory.
* Write today's learning journal entry in pure HTML and stick it in your ``templates`` directory, following the same style rules as the mockup for your HTML detail page.
* Remove the existing views from your ``views.py`` file.
* Create the following view callables: 
    - ``list`` view: for the list of journal entries
    - ``detail`` view: for a single journal entry
    - ``create`` view: for creating a new view
    - ``update`` view: for updating an existing view
* Connect each of the above views to the following routes, with descriptive but concise route names:
    - ``/``
    - ``/journal/{id:\d+}``
    - ``/journal/new-entry``
    - ``/journal/edit-entry``
* Your ``list`` view will serve up your home page mockup, with today's journal entry being the top on. The title for each entry on the list must be a link.
* Your ``detail`` view will serve up today's journal entry.
* Your ``create`` view will serve up the mockup for creating a new entry (should be a form page).
* Your ``update`` view will serve up the mockup for editing entries.
* Ensure that each page has a "Home" button visible that returns the viewer to the home page.
* Ensure that the home page has a "New Entry" button that allows the user to create new entries.

When all of the above work is completed, deploy your site to Heroku. Make sure to include the URL to your Heroku deployment in your ``README.md`` file. Also make sure that your ``README.md`` documents the routes and views used and that any function you write is appropriately documented.

Submitting Your work
====================

When your work is done and your site is deployed, push all your work to your GitHub repo. Open a new pull request from the ``step1`` branch to ``master``. Submit the URL of that pull request to Canvas.

Finally, merge your pull request to prepare for the work in `Python Learning Journal: Step 2 <pyramid_lj_2.html>`_

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging