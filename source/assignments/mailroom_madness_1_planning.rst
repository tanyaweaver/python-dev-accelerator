.. slideconf::
    :autoslides: False

***************************
Mail Room Madness: Planning
***************************

.. slide:: Mail Room Madness: Planning
    :level: 1

    This document contains no slides.

This is an abstract task.
Given a list of goals for a software project, you create a plan for completing these goals.
After next session, you'll use your plan to build the described program.

To accomplish this task, you'll need to write some *pseudocode*. Like this:

.. code-block:: python

    def get_user_input(prompt, validator=None):
        """return the value input by a user prompted by `prompt`

        optionally, validate the input with a function `validator` which must
        take one argument, the input from the user and must return the input if
        valid, and None if not valid
        """
        reply = None
        while reply is None:
            reply = ask_for_input(prompt)
            if there_is_a_validator:
                validate_the_reply
        return reply

Description
===========

You work in the mail room at a local charity.
Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts.
You are tired of doing this over an over again, so you've decided to let Python help you out of a jam.

You want to write a small command-line script that can handle some of the tasks associated with this job for you.
Here's a list of the things you want to be able to do:

* The script should have a data structure that holds a list of your donors and a history of the amounts they have donated.
* When run, the script should prompt the user to choose from a menu of 2 actions: 'Send a Thank You' or 'Create a Report'.
* If the user selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Verify that the amount is in fact a number, and re-prompt if it isn't.
  * Once an amount has been given, add that amount to the donation history of the selected user.
  * Finally, use string formatting to compose an email thanking the donor for their generous donation.
    Print the email to the terminal and return to the original prompt.

**You need not persist the new donors when the script quits running.**

* If the user (you) selected 'Create a Report' Print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation amount as values in each row.
  - Using string formatting, format the output rows as nicely as possible.
    The end result should be tabular (values in each column should align with those above and below)
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return to the original prompt.
* From the original prompt, the user should be able to quit the script cleanly.

Tasks
=====

Begin by thinking of each individual step as a stand-alone operation.
What kind of function would you need to write to accomplish a single step from the above list of steps?

Write a series of *pseudocode* functions to accomplish the tasks identified by the list of steps above.

Continue by planning the *flow* of your script.
What should happen first, second?
How will you move from one step to the next?

You may find that creating a *flow chart* that shows how you expect your script to work can help you to visualize this process.

You can use a program to create a flow chart, or a free web service like `draw.io <https://www.draw.io>`_.
Or you can simply sketch something by hand.

Submitting Your Work
====================

To submit this homework, attach a file containing your pseudocode functions and a screenshot of your flow chart to the submission page in canvas.

We will discuss the implementation of this program in more detail during the next session.
Make sure you think this through so you can participate in that discussion.