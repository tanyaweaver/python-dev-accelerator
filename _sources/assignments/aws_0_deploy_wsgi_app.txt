.. slideconf::
    :autoslides: False

************************
Deploy a WSGI app to AWS
************************

.. slide:: Deploy a WSGI app to AWS
    :level: 1

    This document contains no slides.

There are a number of moving parts in a full-stack web application.
In order to get accustomed to them, deploy a simple WSGI application to AWS.

Tasks
=====

1. Create and configure an AWS EC2 Instance for a web server

     a) ensure that the server accepts incoming connections over ssh and HTTP
     b) use a `t2.micro` instance to avoid incurring costs

2. Install and configure `nginx` as the HTTP front-end

     a) ensure that you use the appropriate server name, given the public DNS of your EC2 instance
     b) set up a proxy pass for the root location

3. Install `gunicorn <http://docs.gunicorn.org/en/stable/index.html>`_ or `waitress <http://docs.pylonsproject.org/projects/waitress/en/latest/>`_ as your WSGI server
4. Install `git` and clone the `sample application <https://github.com/cewing/simple-bookapp>`_.
5. Configure `upstart <http://docs.gunicorn.org/en/stable/deploy.html#upstart>`_ to start your WSGI server, running your wsgi application.
   (note that the linked configuration for `upstart` is for gunicorn, but a simple upstart file can be created for waitress using the same ideas)


Submitting Your Work
====================

Take a couple of screen shots showing a web browser viewing the application on your EC2 instance.
Ensure that the URL of the instance is visible in the images.
Upload these screenshots and submit, along with the URL of your instance so I can verify that it is still running.

**DO NOT stop or terminate your ec2 instance until this assignment is graded.**
Having the app stay up even after you have logged out is a vital part of the assignment.
