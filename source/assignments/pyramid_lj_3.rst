===============================
Python Learning Journal: Step 3
===============================

.. This is currently just a direct copy of day 2's assignment.

Thus far the basic structure and style of your learning journals has been planned out. Now we want to take a bit more advantage of Pyramid to make for a more dynamic site.

Tasks
=====

Create a new branch (``step2``) for today's work. Do your work on this branch.

Using what you learned today, both in class and in your readings, accomplish the following tasks for your learning journal along with your partner:

* Convert your HTML mockups into Jinja2 templates, and keep them DRY with template inheritance.
* Create a list of learning journal entries in ``views.py``, containing today's entry, yesterday's entry, and at least the three days prior to that. Each entry should have attributes of "id", "title", "creation_date", and "body".
* Wire your views to your app using ``view_config``, choosing the appropriate ``route_name`` and ``renderer`` for each view.
* The home page should contain a list of entries, starting with the most recent. For each listed entry there should be an obvious link (e.g. clickable title, a "more" button, etc.) from the home page to the detail view showing the content of that specific entry.
* The ``detail`` view for each entry should contain a link to a form to edit that entry.
* When submitted, the ``create`` and ``update`` views for each entry should return the form data to the same page.

Your views should be *thoroughly* tested. Write both *unit* tests of the view functions themselves, and *functional* tests that show the configured system works properly.

You are working with a partner to complete this application.

When all of the above work is completed, update your deployment to Heroku. Make sure to include the URL to your Heroku deployment in your ``README.md`` file. Update your ``README.md`` to include the coverage output of your tests for Python 2 **and** Python 3.

Submitting Your work
====================

When your work is done and your site is deployed, push all of your work to your GitHub repo. Open a new pull request from the ``step2`` branch to ``master``. Submit the URL of that pull request to Canvas.

Finally, merge your pull request to prepare for the work in `Python Learning Journal: Step 2 <pyramid_lj_3.html>`_

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging