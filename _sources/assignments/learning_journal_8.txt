.. slideconf::
    :autoslides: False

**************************************
Python Learning Journal: Prior Entries
**************************************

.. slide:: Python Learning Journal: Prior Entries
    :level: 1

    This document contains no slides.

This weeks learning journal assignments should be done on your own.
You may consult with your classmates, but do the work in your own fork of the journal project.
Each partner should submit a different pull request URL.

Tasks
=====

This week you've completed and deployed your own Python learning journal.
You should now be writing your nightly journal entries in your own journal deployed publicly.
However, you still have entries from the first part of class that are hidden in the shared class journal.

Begin by creating a new branch ``api-script`` in your repository.
Do your work for this assignment in the branch.

As described in lecture, the shared class journal has an API that allows you to extract your journal entries as JSON.
Write a script that will use the `requests <http://docs.python-requests.org/en/master/>`_  library to retrieve this data.
The script should then parse the JSON and insert each entry into your database.
You must protect against inserting duplicate entries so that the script can be run safely multiple times.
As final output, your script should print the number of entries inserted to the terminal.

Factor the code you write to be testable.
Write extensive tests to demonstrate that the script functions as expected.
Ensure that you test for failure modes as well, and that your database is protected against corruption.

Finally, add an entry point for your script so that it can be run from the command line.

Once you've submitted your pull request and merged (see below), deploy these changes to Heroku.
Run the script on Heroku to populate your live database with your entries from the shared class journal.

Submitting Your Work
====================

When you have finished your work and all your tests are passing, push your changes to GitHub.
Open a pull request to master and submit a link to that pull request.
Afterwards, merge your changes to master so you can deploy to Heroku.

Finally, after deploying take a screenshot showing the first entry you ever wrote in the shared learning journal as it appears now in your personal journal.
