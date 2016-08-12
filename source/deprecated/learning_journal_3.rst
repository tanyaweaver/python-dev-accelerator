.. slideconf::
    :autoslides: False

*******************************
Python Learning Journal: Step 3
*******************************

.. slide:: Get an Amazon AWS Account
    :level: 1

    This document contains no slides.

You've been writing your nightly journal entries in a group journal.
It's time you had one of your own.

Tasks
=====

Begin by opening a new branch ``step3`` for the work in this assignment.

With your partner, create and configure the following views for your learning journal:

* The ``add_entry`` view will display an empty form for a new entry.
  When the form is submitted, the view will create a new entry and return the user to the detail view of that entry.
* The ``edit_entry`` view will display a form populated with the values from an existing entry.
  When the form is submitted, the view will update the existing entry with the newly submitted values.

Ensure that there is a link to your ``add_entry`` view visible on the front page of the site.
Ensure that on each detail page there is a link leading to the ``edit_entry`` view for that entry.

When adding or editing an entry ensure that you can use *markdown* to format your entry text.
You should be able to format and colorize code examples using github-style fenced code blocks with three ticks::

    ```python
    def exp(x, y):
        return x ** y
    ```

Make sure that you have both *unit* and *functional* tests that demonstrate the functionality of these views.


Submitting Your Work
====================

When your work is done and all tests are passing, push your work to GitHub.
Open a new pull request from the ``step3`` branch to your master branch.
Copy the URL for that pull request.

Submit a link to the pull request you created for the step3 branch.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging