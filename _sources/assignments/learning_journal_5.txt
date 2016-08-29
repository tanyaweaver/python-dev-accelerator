.. slideconf::
    :autoslides: False

*********************************
Python Learning Journal: Security
*********************************

.. slide:: Python Learning Journal: Security
    :level: 1

    This document contains no slides.

This weeks learning journal assignments should be done on your own.
You may consult with your classmates, but do the work in your own fork of the journal project.
Each partner should submit a different pull request URL.

Tasks
=====

Begin by opening a new branch ``security`` for the work in this assignment.

For this part of the assignment you will implement the security layer of your learning journal.
Create an ``ACL`` that grants the ``view`` permission to any visitor and the ``edit`` and ``create`` permissions only to authenticated users.
Configure an authentication system that will allow a single user to log in to the site if they provide a password.
Do not store the password anywhere in plain text.

Next, add two views that provide login/logout functionality

* The ``login`` view will display a form with inputs for username and password
  When the form is submitted, the view will validate the provided credentials and if validation passes, authenticate the user.
* The ``logout`` view will remove all authentication data, returning the viewer to an anonymous state.

Now that you have authentication and authorization, use it protect those parts of your application that are sensitive.
Using the ``create`` and ``edit`` permissions, ensure that no buttons leading to the creating or editing of entries are visible to anonymous users.
Also ensure that the views themselves are not accessible.

Add tests or update your existing tests to cover this new functionality.
Ensure that the access controls you have implemented work.
Be sure that you cannot see or access the pages for adding or editing entries unless you have logged in.

Submitting Your Work
====================

When your work is complete and all your tests are passing, push your work to your fork of the repository in GitHub.
Open a pull request from the ``security`` branch to ``master``.
Submit the URL for that pull request.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging
