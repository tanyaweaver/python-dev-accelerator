===============================
Python Learning Journal: Step 4
===============================

We haven't been able to truly persist our Learning Journals on our Heroku deployment.
Let's change that today.

Tasks
=====

Create a new branch (``step4``) for today's work. 
Do your work on this branch.

Using what you learned today, both in class and in your readings, accomplish the following tasks for your learning journal along with your partner:

* Add the `PostgreSQL service <https://www.heroku.com/postgres>`_ to your Heroku deployment.
* Clean up the styling and structure of your app.

Your code should be *thoroughly* tested. 
Write unit tests of the view functions themselves, unit tests for your models, and *functional* tests that show the configured system works properly.

You are working with a partner to complete this application.

When all of the above work is completed, update your deployment to Heroku. 
Make sure to include the URL to your Heroku deployment in your ``README.md`` file. 
Update your ``README.md`` to include the coverage output of your tests for Python 2 **and** Python 3 for this branch.
You should have coverage reports for steps 1, 2, and 3 in your ``README.md``.

Submitting Your work
====================

When your work is done and your site is deployed, push all of your work to your GitHub repo. 
Merge your ``step4`` branch to master to prepare for your next steps.

Finally, for your submission, a special pull request.

On your development machine, check out the last commit you made to the learning-journal repository prior to starting work on step one of the learning journal project
(This is probably your initial commit of the repo).
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