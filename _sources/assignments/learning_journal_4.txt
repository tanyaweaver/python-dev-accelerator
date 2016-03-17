.. slideconf::
    :autoslides: False

*******************************
Python Learning Journal: Step 4
*******************************

.. slide:: Python Learning Journal: Step 4
    :level: 1

    This document contains no slides.

You've been writing your nightly journal entries in a group journal.
It's time you had one of your own.

Tasks
=====

Clean up the work you've done so far for your learning journal.
Ensure that your tests are working properly and that the entire app functions equally well in Python 2 and Python 3.
Use ``pytest-cov`` to calculate the coverage of your project code.
Strive to get at least 90% coverage.

Submitting Your Work
====================

Finally, for your submission, a special pull request.

On your development machine, check out the last commit you made to the learning-journal repository prior to starting work on step one of the learning journal tutorial.
You can do so by providing the commit hash as the argument to ``git checkout``:

.. code-block:: bash

    $ git checkout 1a39dc40

Once you've made that checkout, you will see that you are in "detached HEAD" state.
From here create a new branch called start:

.. code-block:: bash

    $ git checkout -b start

Then, push this branch up to your repository in github:

.. code-block:: bash

    $ git push -u origin start

Finally, make a pull request in github from your master branch to the new start branch.
This will result in a pull request containing all the code you've written during the tutorial.
**Do not merge this pull request**.

To submit this assignment, submit the link to this special "reverse pull request".

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging

After Submitting
================

Once you have submitted this end-of-week learning journal assignment there is one more step to take.
Your work on this assignment with your partner is finished.
You will each proceed from here alone.

First, fork the repository for the learning journal from the account where it lives into the other partner's account.
Once this is finished, each partner will have a separate copy of the journal (though they are still officially connected by github).
Each of you should spend the rest of the day (and the weekend) updating the templates for your copy of the journal to use the HTML mockups :doc:`you've been working on </assignments/learning_journal_mockup>`.
Take pride in your accomplishment.
Make sure it looks nice and works well.