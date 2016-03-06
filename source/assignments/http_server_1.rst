.. slideconf::
    :autoslides: False

**************************
Socket HTTP Server, Step 1
**************************

.. slide:: Socket HTTP Server, Step 1
    :level: 1

    This document contains no slides.

Building on the foundation of your Echo Server, you will begin to implement a
simple HTTP server.

Tasks
=====

Use your 'http-server' repository in GitHub for this work.
Make a branch "step1" from master to do your work for this assignment.

* Implement a function called response_ok that will return a well formed HTTP
  "200 OK" response as a byte string suitable for transmission through a
  socket. This method should accept no arguments and return a fully-formed
  proper response.
* Implement a function called response_error that will return a well formed
  HTTP "500 Internal Server Error" response.
* Update the server loop you built for the echo server so that it:

  - accumulates an incoming request into a variable
  - "logs" that request by printing it to stdout
  - returns a well-formed HTTP 200 response to the client.

As usual, write unit tests demonstrating each function you write before you
implement the code to achieve it.  When you've finished the server loop, write
a functional test that demonstrates that it works correctly.

Include a solid README file with a description of the server you're building.
Include any sources or collaborations you used.

Submitting Your Work
====================

When you are done and your tests are all passing, push your work to GitHub and
submit a pull request from the step1 branch back to master.  Copy the URL of
the pull request.  After you've created the pull request you may merge the
step1 branch back to master.

Submit the URL of your pull request.

As with every primary submission, use the Comments feature for this submission
to add questions, comments and reflections on the work you have done so far.
