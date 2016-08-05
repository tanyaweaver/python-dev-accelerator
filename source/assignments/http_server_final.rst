.. slideconf::
    :autoslides: False

*************************
Socket HTTP Server, Final
*************************

.. slide:: Socket HTTP Server, Final
    :level: 1

    This document contains no slides.

In parts one, two, and three of this assignment, you implemented a simple HTTP server using standard Python network sockets.

In class we've discussed the problems this server will face when it comes to higher traffic.
Let's improve our model so that it can handle a heavier traffic load.

Tasks
=====

Create a new branch in your network tools repository.
Call it ``concurrency``.
You'll do your work in this branch.

Use pip to install `gevent`_ into your http project virtual environment.

.. _gevent: http://www.gevent.org/

Add a new file that will hold your concurrent HTTP server script.
In it you will re-write your server loop appropriately as a handler for the gevent StreamServer.

You should be able to import most of the required functionality from your original HTTP server without need for repeating yourself.

The functionality of the server should not change.
You should be able to maintain the test suite you created for the original server.

Submitting Your Work
====================

When you are done and all your tests are passing, submit a pull request from the ``concurrency`` branch back to master.
Copy the URL and submit it.
When you are done you may merge concurrency to master on your own.

As with every primary submission, use the Comments feature to add questions, comments and reflections on your assignment.