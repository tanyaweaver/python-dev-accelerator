.. slideconf::
    :autoslides: False

*****************************************
Learning Journal Enhancement: Add Editing
*****************************************

.. slide:: Learning Journal Enhancement: Add Editing
    :level: 1

    This document contains no slides.

Your client for the Learning Journal project wants to be able to edit existing
entries in the journal. A quick discovery phase leads to the following user
stories:

* As an author I want to have a permalink for each journal entry where I can
  view it in detail.
* As an author I want to edit my journal entries so I can fix errors.
* As an author I want to use MarkDown to create and edit my entries so that I
  can format them nicely.
* As an author I want to see colorized code samples in my journal entries so
  that I can more easily understand them.

For this assignment you will be working with a partner, but each of you will
commit changes to your own repository.  I expect that each member of the
partnership will have the same solution to each problem, committed in different
repositories. You may submit one pull request as your work sample.

Tasks
=====

Create a Milestone in GitHub to represent this improvement.

Break these improvements down into tasks, create an issue for each task and
take each issue one at a time.  Note that you can make references to issues in
github from git commit messages, like so::

    $ git commit -m "Create a detail view that displays a single entry at a permanent URL.  refs #1"

Create a branch for this improvement and do your work in the branch.

For each task, begin by writing a BDD test first (as described in class). Then
implement the functionality that makes that test pass. Don't forget to also
write unit tests to ensure that you cover the code you write for each task.

As you make commits in working on a task, use commit message references to
connect your commits to your GitHub issues.

Start documenting the features of your journal in a README.md file.  Include
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
