.. slideconf::
    :autoslides: False

**********************************
Learning Journal, Final Submission
**********************************

.. slide:: Learning Journal, Final Submission
    :level: 1

    This document contains no slides.

Take the time to complete the work of building your learning journal.
Incorporate the mockups you've been working on.
Update the adding of entries so that you use a separate page, rather than the form in the list page from the tutorial.

Do your work on a branch, ensuring that your master branch is kept safe.
Write tests for new views you create, and adjust existing tests to match your mockups.
Make a pull request back to your master branch when you are finished and deploy your completed work to Heroku.

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
Please ensure that you have DNS set up so that the link is not a Heroku app link, but your own domain name.
