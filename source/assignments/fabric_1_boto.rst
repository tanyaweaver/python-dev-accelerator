.. slideconf::
    :autoslides: False

******************************************************
Managing AWS: Use Boto to Create And Destroy Instances
******************************************************

.. slide:: Managing AWS: Use Boto to Create And Destroy Instances
    :level: 1

    This document contains no slides.

Today in class you learned about `boto`_, the official Python wrapper for the
Amazon AWS Services SDK.

.. _boto: https://boto.readthedocs.org/en/latest/index.html

Tasks
=====

Using what you learned today in our class demo, take the following steps:

* Create a virtualenv and project for learning Amazon Web Services deployment.
  Call it awsenv (or something like that)
* Once the environment is generated, use pip to install the Python AWS SDK
  package boto3.
* Once boto is installed, read `this <https://boto3.readthedocs.org/en/latest/guide/quickstart.html#configuration>`_
  for information on safely configuring boto to use your Access Key ID and
  Secret Access Key credentials
* Find a reasonable ami to use in creating your instance.  May I suggest the
  ubuntu instance finder on `this page <http://cloud-images.ubuntu.com/locator/ec2/>`_
  to get an excellent generic Ubuntu image?
* Then, walk through the steps in `this introduction <http://boto.readthedocs.org/en/latest/ec2_tut.html>`_
  to practice creating and destroying EC2 Instances

Submitting Your Work
====================

To submit this assignment, take a screen shot of your AWS EC2 console showing
an instance you've created via the command line in a running state.

As usual, use the comment feature to add any questions, concerns or reflections
you may have on what you did here.

Please keep in mind that to stay in the Free Usage Tier for Amazon AWS, you may
only create t1.micro or t2.micro instances, and you may only have one running
at a time.