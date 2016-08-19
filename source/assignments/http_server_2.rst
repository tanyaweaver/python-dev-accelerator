.. slideconf::
    :autoslides: False

**************************
Socket HTTP Server, Step 2
**************************

.. slide:: Socket HTTP Server, Step 2
    :level: 1

    This document contains no slides.

Leveraging what you have learned about the HTTP protocol, you will improve the functionality of your simple HTTP server.
Create a new branch in your http-server repository called ``step2`` in which to do your work.

Tasks
=====


Implement a function called ``parse_request``

* The function should take a single argument which is the request from the client.
* The function should only accept GET requests.
  Any other request method should raise an appropriate Python exception.
* The function should only accept HTTP/1.1 requests.
  A request of any other HTTP version should raise an appropriate Python exception.
* The function should validate that a proper Host header was included in the request and if not, raise an appropriate Python exception.
* The function should validate that the request is well-formed.
  If the request is malformed in some way, it should raise an appropriate Python exception.
* If none of the conditions above arise, the function should return the URI from the request.

Update your ``response_error`` function to parameterize the error code and reason phrase.
The return value should still be a well-formed HTTP error response, built using the provided error code and reason phrase.

Update the server loop you built for step one:

* pass the request you accumulate into your new parse_request function
* handle any Python exceptions raised by building a meaningful HTTP error response
* if no errors are raised, build an HTTP 200 OK response.
* return the response you built to the client

Write tests for each goal before you write the code to achieve it.
Make sure you have both unit tests to cover the functions you write, and functional tests that ensure that the server loop operates as expected.

Update your ``README.md`` file with an expanded description of the server you're building.
Include any sources or collaborations you used.

Submitting Your Work
====================

When you are done and your tests are all passing, push your work to GitHub and submit a pull request from the ``step2`` branch back to ``master``.
Copy the URL of the pull request.
After you've created the pull request you may merge the ``step2`` branch back to ``master``.

Submit the URL of your pull request.

As with every primary submission, use the Comments feature for this submission to add questions, comments and reflections on the work you have done so far.
