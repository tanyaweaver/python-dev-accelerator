.. slideconf::
    :autoslides: False

******************
Socket Echo Server
******************

.. slide:: Socket Echo Server
    :level: 1

    This document contains no slides.

In this assignment you will build an echo server using Python sockets.

Tasks
=====

Create a new repository called ``http-server`` in GitHub for this work.
Make sure it contains an appropriate license and ``.gitignore`` file.
Make a branch ``echo`` from ``master`` to do your work for this assignment.

Create two new python modules in your repository, ``client.py`` and ``server.py``.
In addition, create a ``test_servers.py`` file to contain your tests.

Add a ``setup.py`` file so you can install your package.
And a ``tox.ini`` file so you can run your tests in both Python 2.7 and Python 3.5

The Client
----------

In your ``client.py`` file, create a function ``client`` which takes one required parameter, ``message``.
When called, the ``client`` function should open a socket connection to the server.
It should send the message passed as an argument to the server through the socket.
It should accumulate any reply sent by the server into a string.
Once the full reply is received, it should close the socket and return the message.

This file should contain an ``if __name__ == "__main__":`` block so it can be run as a script.
This script should be called from the command line with a single argument which is the message to send.
The script should print the reply from the server to the terminal where the script was run:

.. code-block:: bash

    $ python client.py "this is the message to send"
    this is the reply received.

The Server
----------

In your ``server.py`` file, create a function ``server`` which takes no arguments.
When run, this function should start a server running.
The server should continue running, sending responses for any messages it receives.
When the user presses ``ctrl-d`` (the keyboard interrupt), the server should cleanly exit.
All open sockets should be closed.

The server should accept incoming connections.
It should receive messages sent from those connections and *echo them back* exactly as received.
Once an entire message has been received and echoed, the connection to the client should be closed.

The server *must remain running and accepting connections*.

Testing
-------

The tests you write for this work may be considered *functional* tests, as opposed to *unit* tests.
They will test the system, rather than either individual function.
Your tests should use the ``client`` function from ``client.py`` to send test messages and return the replies sent by the server.
They should assert that the message sent is identical to the reply received.

The following conditions should be tested:

* messages shorter than one *buffer* in length
* messages longer than several buffers in length
* messages that are an exact multiple of one buffer in length
* messages containing non-ascii characters

Submitting Your Work
====================

When you are finished implementing your server and client and all your tests are passing both in Python 2 and Python 3, push your changes to the ``echo`` branch to github.
Open a pull request from the ``echo`` branch to your master.
Paste the URL of this pull request as your submission.

As with every primary submission, use the Comments feature for this submission
to add questions, comments and reflections on the work you have done so far.

Once you have submitted your assignment, you may merge your ``echo`` branch back to master in preparation for the next step in this assignment series.
