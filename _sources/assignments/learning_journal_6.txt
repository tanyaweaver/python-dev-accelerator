.. slideconf::
    :autoslides: False

****************************************
Python Learning Journal: CSRF Protection
****************************************

.. slide:: Python Learning Journal: CSRF Protection
    :level: 1

    This document contains no slides.

This weeks learning journal assignments should be done on your own.
You may consult with your classmates, but do the work in your own fork of the journal project.
Each partner should submit a different pull request URL..

Tasks
=====

Continue your work today in the ``security`` branch you created previously.

You've completed the basic functionality for your learning journal.
You've also secured the journal so that it is safer to use in the open.

But there is still a critical flaw in the security of your Journal.
It is open to CSRF attacks.

As described in class, ensure that both the ``create`` and ``edit`` forms for your journal are protected from CSRF attacks.
Ensure that all sensitive data needed by your app is being extracted from environmental variables.
Set those variables in Heroku.
Redeploy your application

Submitting Your Work
====================

When your work is complete and all your tests are passing, push your work to your fork of the repository in GitHub.
Open a pull request from the ``security`` branch to ``master``.
Submit the URL for that pull request.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging