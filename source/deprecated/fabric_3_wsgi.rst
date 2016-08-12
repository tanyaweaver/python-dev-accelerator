.. slideconf::
    :autoslides: False

********************************
Manage AWS: Deploying a WSGI App
********************************

.. slide:: Manage AWS: Deploying a WSGI App
    :level: 1

    This document contains no slides.

In class we walked through a `manual deployment <../lectures/simple_wsgi_deployment>`_
of a simple WSGI application.

Your task is to automate the process, adding fabric tasks that will allow you
to upload an application, configure nginx to proxy that application, and
restart nginx.  Use your simple book database application as the app you
upload.

Read about `fabric.contrib.project <http://docs.fabfile.org/en/latest/api/contrib/project.html>`_ and
`fabric.contrib.files <http://docs.fabfile.org/en/latest/api/contrib/files.html>`_
for some helpful fabric tools.

One challenge in this assignment is to figure out how to start your wsgi server
running and keep it running even though you are not continuously logged in to
the AWS instance.

One possible solution to this is to apt-get install `supervisord <http://supervisord.org/>`_.
You can then use the supervisorctl process to start a "program".  A very simple
configuration might look like this:

.. code-block:: ini

    source

    [program:bookapp]
    command: /usr/bin/python -m bookapp
    directory: /home/ubuntu
    autostart: true

Another possibility (one which is a bit easier though eventually a bit less
flexible) is to use the Linux process manager Upstart to
`run your app <http://docs.gunicorn.org/en/latest/deploy.html#upstart>`_.

Your goal should be to have a single command you can run which deploys your
latest application code to a running server on AWS. Something like this:

.. code-block:: bash

    $ fab deploy

Submitting Your Work
====================

To submit the assignment, upload your fabfile.py and any configuration
templates you create. Also upload screenshots of the bookdb app running on your
AWS Server.

Use the comments feature to add any questions, comments or reflections on your
work.
