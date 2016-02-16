.. slideconf::
    :autoslides: False

********************************************
Learning Journal Enhancement: AJAX & Twitter
********************************************

.. slide:: Learning Journal Enhancement: AJAX & Twitter
    :level: 1

    This document contains no slides.

Tasks
=====

Your client for the Learning Journal project wants to improve the experience of
editing and sharing existing entries in the journal. A quick discovery phase
leads to the following user stories:

* As an author I want to submit my new and edited entries via AJAX so I don't have to wait for a page reload.
* As an author, I want my existing editing to stay functional so that I can work from a browser without javascript.
* As an author I want to be able to tweet the title of a post and a link to that post by pressing a button so that I can share what I've learned with my followers.

Create a Milestone in GitHub to represent this improvement.

Break these improvements down into tasks, create an issue for each task and
assign the tasks to the milestone.

Create a branch for this improvement and do your work in the branch.  Make sure
that master remains deployable at all times.

For each task, write a test first. You may decide for yourselves which would be
more appropriate, a BDD or unit test. Then implement the functionality that
makes that test pass. As you make commits in working on a task, use commit
message references to connect your commits to your GitHub issues.

.. note:: For testing AJAX functionality, please be aware that the standard WebTest app will not execute javascript.
          This functionality cannot be tested using that setup.
          For this reason you are not required to test the AJAX functionality beyond a manual click-test.
          However, if you find yourself completing this assignment ahead of time and wish to take on a challenge, please read about pytest-splinter and automated browser testing with a real browser.
          There are significant challenges associated with this, but it can be accomplished with the knowledge you've learned so far.

Continue documenting the features of your journal in a README.md file.  Include
references--and if applicable, links--to sources or collaborations you used in
completing your tasks.

Submitting Your Work
====================

When your new improvement is complete and all tests are passing, create a pull
request to master and copy the URL of that request. Then merge your changes to
master and deploy to production on Heroku.

Use the text box to submit two urls.  The first should be a link to your pull
request in GitHub.  The second will be a link to your online journal where we
should be able to see at least one entry demonstrating the new formatted text
and code syntax highlighting features of your journal.

As always, use the comment feature in Canvas to submit any questions, comments
or reflections on this work.
