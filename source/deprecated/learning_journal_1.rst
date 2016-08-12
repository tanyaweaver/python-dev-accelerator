.. slideconf::
    :autoslides: False

*******************************
Python Learning Journal: Step 1
*******************************

.. slide:: Python Learning Journal: Step 1
    :level: 1

    This document contains no slides.

You've been writing your nightly journal entries in a group journal.
It's time you had one of your own.

Tasks
=====

If you do not already have one, create a ``learning-journal`` repository in github.
Add the application skeleton created in class to this repository.
Ensure that the repository also contains a good Python ``.gitignore`` file and an appropriate OSS license.

Once the basics are in place, create a new branch (``step1``) for today's work.
Do your work on this branch.

Using what you learned today, both in class and in your readings, accomplish the following tasks for your learning journal:

* Remove the existing ``MyModel`` class from your ``models.py`` module.
* Create an ``Entry`` model in the ``models.py`` file.
  Your model must have the following attributes:

  - An integer *primary key* field called ``id``
  - A ``title`` field which is required, must be unique, and is at most 128 characters in length
    (the title should explicitly accept unicode characters)
  - A ``text`` field which is required and is of unlimited length
    (the text should explicitly accept unicode characters)
  - A ``created`` field which represents the date and time at which an entry was created
    (the date should default to the current date and time, and should be stored in UTC, not local time)

* Update the ``initalize_db`` script in your application (in the ``scripts`` directory) so that it does not create any new objects by default.
* Update the name of the entry point for the ``initialize_db`` script to something sane, perhaps ``initialize_db``.
* Enhance the ``pshell`` command to allow you immediate access in an interactive session to your Entry model and a database session.

For all the tasks having to do with your ``Entry`` model, ensure that you have tests in place that demonstrate that the model works as expected.

Submitting Your Work
====================

When you are done and all your tests are passing both in Python 2.7 and 3.5, push your work to GitHub and submit a pull request from the step1 branch back to master.
Copy the URL of the pull request and submit it to Canvas.
After you've created the pull request you may merge the step1 branch back to master.

Use the comment feature in Canvas to add the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging
