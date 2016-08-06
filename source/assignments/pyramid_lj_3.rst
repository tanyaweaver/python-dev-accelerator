===============================
Python Learning Journal: Step 3
===============================

We've moved on from our basic Pyramid template to something including SQL persistence.
The walk-through is intended to get you to a working application as quickly as possible.
There will be many questions left unanswered as we proceed.
Fear not.
The answers will come as this course progresses.
For now, simply focus on the process and getting to a working application.

Tasks
=====

Create a new branch (``step3``) for today's work.
Do your work on this branch.

Using what you learned today, both in class and in your readings,
accomplish the following tasks for your learning journal along with your partner:

* Clear out the views, models, templates, routes, tests, and database provided by the scaffold/made in class.
* Bring over your views, templates, routes, and tests from yesterday's basic scaffold.
* Ensure that everything is rewired as it needs to be (taking the new directory structure into account).
* Create the data model for your Learning Journal Entries. They should have at least these attributes:

    - id
    - title
    - body
    - creation date

* Your list of current learning journal entries (the ``ENTRIES`` global from yesterday) should now be put into your database as model instances.

.. note:: Heroku will not persist your data across different deployments using sqlite3!
          To circumvent this, you should have your Entries populate your database upon creation of the database in ``learning_journal/scripts/initializedb.py``

* Modify all of your views so that they call on the database (e.g. your ``list`` view performs a query to get all of the journal entries).
* The ``create`` view should take the data from the user's input and use it to create a new model instance.
  When a new entry is created, the user should be redirected to the home page.
* The ``update`` view should only post the edited data to the page.
  It should not yet update the data in the database.

Your code should be *thoroughly* tested.
Write unit tests of the view functions themselves, unit tests for your models, and *functional* tests that show the configured system works properly.

You are working with a partner to complete this application.

When all of the above work is completed, update your deployment to Heroku.
Make sure to include the URL to your Heroku deployment in your ``README.md`` file.
Update your ``README.md`` to include the coverage output of your tests for Python 2 **and** Python 3 for this branch.
You should have coverage reports for both the ``step2`` branch and the ``step3`` branch in your ``README.md``.

Submitting Your work
====================

When your work is done and your site is deployed, push all of your work to your GitHub repo.
Open a new pull request from the ``step3`` branch to ``master``.
Submit the URL of that pull request to Canvas.

Finally, merge your pull request to prepare for the work in `Python Learning Journal: Step 4 <pyramid_lj_4.html>`_

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging
