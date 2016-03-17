.. slideconf::
    :autoslides: False

***************************************
Python Learning Journal: AJAX & Twitter
***************************************

.. slide:: Python Learning Journal: AJAX & Twitter
    :level: 1

    This document contains no slides.

This weeks learning journal assignments should be done on your own.
You may consult with your classmates, but do the work in your own fork of the journal project.
Each partner should submit a different pull request URL.

Tasks
=====

Your client for the Learning Journal project wants to improve the experience of
editing and sharing existing entries in the journal. A quick discovery phase
leads to the following user stories:

* As an author I want to submit my new and edited entries via AJAX so I don't have to wait for a page reload.
* As an author, I want my existing editing to stay functional so that I can work from a browser without javascript.
* As an author I want to be able to tweet the title of a post and a link to that post by pressing a button so that I can share what I've learned with my followers.

Create a Milestone in GitHub to represent this improvement.
Break these improvements down into tasks, create an issue for each task and assign the tasks to the milestone.

Create a branch for this improvement and do your work in the branch.
Make sure that master remains deployable at all times.

.. note:: For testing AJAX functionality, please be aware that the standard WebTest app will not execute javascript.
          This functionality cannot be tested using that setup.
          For this reason you are not required to test the AJAX functionality beyond a manual click-test.
          However, if you find yourself completing this assignment ahead of time and wish to take on a challenge, please read about pytest-splinter and automated browser testing with a real browser.
          There are significant challenges associated with this, but it can be accomplished with the knowledge you've learned so far.

Continue documenting the features of your journal in a README.md file.
Include references--and if applicable, links--to sources or collaborations you used in completing your tasks.

Submitting Your Work
====================

When your new improvement is complete and all tests are passing, create a pull request to master and copy the URL of that request.
Then merge your changes to master and deploy to production on Heroku.

Use the text box to submit two urls.
The first should be a link to your pull request in GitHub.
The second should be a link to a tweet you made from your journal.

As always, use the comment feature in Canvas to submit any questions, comments or reflections on this work.
