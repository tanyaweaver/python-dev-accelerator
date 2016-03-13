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

* The ``edit_entry`` view will display a form populated with the values from an existing entry.
  When the form is submitted, the view will update the existing entry with the newly submitted values.
* The ``login`` view will display a form with inputs for username and password
  When the form is submitted, the view will validate the provided credentials and if validation passes, authenticate the user.
* The ``logout`` view will remove all authentication data, returning the viewer to an anonymous state.

The ``add_entry`` and ``edit_entry`` views should be configured to be visible *only* to authenticated users.
Additionally, the application should hide any links or buttons leading to these views if the user is not authenticated.

Ensure that both the ``add_entry`` and ``edit_entry`` views are protected against CSRF attacks.

Make sure that you have both *unit* and *functional* tests that demonstrate the full functionality of these three views.
In particular, ensure that the access controls you have implemented work.
Be sure that you cannot see the pages for adding or editing entries unless you have logged in.

Throughout the week you'll be working with a partner to complete this application.
However, each student must deploy their work to Heroku individually.

Submitting Your Work
====================

When your work is done and all tests are passing, push your work to GitHub.
Open a new pull request from the ``step3`` branch to your master branch.
Copy the URL for that pull request.

Then merge the pull request so that you can deploy to heroku.
Take screen shots of your app as it runs online at Heroku.
Each partner will need to deploy to Heroku separately.

Submit that screenshot and a link to the pull request you created for the step3 branch.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging