.. slideconf::
    :autoslides: False

***************************
Mail Room Madness: Building
***************************

.. slide:: Mail Room Madness: Building
    :level: 1

    This document contains no slides.

.. include:: mailroom_madness_1_planning.rst
    :start-line: 34
    :end-line: 70


Tasks
=====

Using all you've learned so far, complete your mailroom program.
For guidance, use the pseudocode and flow chart you created previously.

* use dicts where appropriate
* see if you can use a dict to switch between the users selections
* Try to use a dict and the .format() method to do the letter as one big template -- rather than building up a big string in parts.
* For extra fun, see if you can use a file to preserve the donation list and changes made to it while the program is running.

Begin by creating a new repository called ``mailroom`` in GitHub.
Create the repository with a Python ``.gitignore`` file and a reasonable license (MIT is good).
Clone that repository locally.
Once you have it cloned, immediately create a branch called ``implementation``.
Do your work on that branch.

Add a ``setup.py`` file that defines your program as a distribution.
This file will allow you to install your program.
Make sure that code you want to distribute to end users is included in the distribution.

optional:
  Use :ref:`a console script entry point <python_packaging_cli_python>` to register your main program entry point.
  If your program is installed, a user should be able to execute it at the command line:

  .. code-block:: bash

      $ mailroom

Add a ``tox.ini`` file that runs your tests in both Python 2.7 and Python 3.5
Make sure your tests pass in both Python environments.
To run your tests, you should be able simply to run tox:

.. code-block:: bash

    $ tox

Create whatever functions you require in order to accomplish your tasks.
Organize the code in a way that makes the most sense to you.
If you want to work entirely in one module, that's fine.
If you'd prefer to create a package with multiple modules, that is also fine.

For each and every function you write, use TDD methods to ensure that you have well-tested code.
If you have functions with branching logic, you *will need* to have more than one test for that function.
Remember, each test should be only as complex as it needs to be to test *one thing*.
Your tests are as much a part of this assignment as the code itself.
Do not neglect them.

The only exceptions to the testing requirements are functions which require user input.
Remember `the video you watched <https://www.youtube.com/watch?v=DJtef410XaM>`_ and the lessons it taught about clean architecture.

As you work, commit early and often.
Write commit messages that are clear, concise and meaningful.
In your code pairings, switch the driver and navigator roles often.

Submitting Your Work
====================

When you are done implementing the entire program and all your tests are passing push your code to github.
Open a pull request from your ``implementation`` branch to the ``master`` branch (which should only contain the README, the ``.gitignore`` and the license)
Copy the URL of that pull request and submit it in Canvas.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging