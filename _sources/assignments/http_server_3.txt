.. slideconf::
    :autoslides: False

**************************
Socket HTTP Server, Step 3
**************************

.. slide:: Socket HTTP Server, Step 3
    :level: 1

    This document contains no slides.

You will complete your simple HTTP server.
Create a new branch called ``step3``.
Use this branch to do your work.

Tasks
=====

Ensure that your HTTP server is aware of a "root directory", in which it will find any assets requested by clients.
Consider the security of your implementation of this feature.
In what ways could it be exploited by a hostile request?
How can you prevent those exploits?

Implement a function called ``resolve_uri`` that will take as an argument the URI parsed from a request.
It will return a body for a response and an indication of the type of content contained in the body (as a tuple).

* If the resource identified by the URI is a directory, return a simple HTML listing of that directory as the body.
* If the resource identified by the URI is a file, return the contents of the file as the body.
* The content type value should be related to the type of file.
* If the requested resource cannot be found, raise an appropriate Python exception.

Ensure that the body of the requested resource is returned in a "200 OK" response.

* The response should include the appropriate header to indicate the type of resource being returned.
* The response should also include the appropriate header to indicate the amount of content being returned.
* The response should include any other valid HTTP headers you wish to add.

You will update your ``response_ok`` function to accomplish this task.

Any Python exceptions raised should be appropriately handled and returned to the client as meaningful HTTP error responses.

Write tests for each goal before you write the code to achieve it.

Update your ``README.md`` file with an expanded description of the server you're building.
Include any sources or collaborations you used.

Here is a :download:`directory <../downloads/webroot.tgz>` you can use as a web home directory.

Submitting Your Work
====================

When you are done and your tests are all passing, push your work to GitHub and submit a pull request from the ``step3`` branch back to ``master``.
Copy the URL of the pull request.
After you've created the pull request you may merge the ``step3`` branch back to ``master``.

Submit the URL of your pull request.

As with every primary submission, use the Comments feature for this submission to add questions, comments and reflections on the work you have done so far.