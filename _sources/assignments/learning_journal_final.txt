.. slideconf::
    :autoslides: False

**********************************
Learning Journal, Final Submission
**********************************

.. slide:: Learning Journal, Final Submission
    :level: 1

    This document contains no slides.

Tasks
=====

In this step you will finish up the last bits of your learning journal work.
Once you have completed all the work in steps 1-3, make sure you have merged all your shared work to master and have both deployed to heroku.
Make sure you have good test coverage of your work and that everything is working well.
Attach a domain name to your running Heroku app so that you can visit your learning journal at a real domain rather than the generated app URL from heroku.

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

To submit this assignment, use the text box to add two links.
One will be the link to your pull request in github.
The other will be the link to your deployed learning journal on Heroku.
**Please ensure** that you have DNS set up so that the link is not a Heroku app link, but your own domain name.

After Submitting
================

Once you have submitted the final learning journal assignment there is one more step to take.
Your work on this assignment with your partner is finished.
You will each proceed from here alone.

First, fork the repository for the learning journal from the account where it lives into the other partner's account.
Once this is finished, each partner will have a separate copy of the journal (though they are still officially connected by github).
Each of you should spend the rest of the day (and the weekend) updating the templates for your copy of the journal to use the HTML mockups :doc:`you've been working on </assignments/learning_journal_mockup>`.
Take pride in your accomplishment.
Make sure it looks nice and works well.
From now on, deploy updates to heroku from your own fork.
