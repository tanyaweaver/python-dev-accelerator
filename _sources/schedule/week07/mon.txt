.. slideconf::
    :autoslides: False

******
Monday
******

.. slide:: Course Presentations
    :level: 1

    This document contains no slides.

Objectives
==========

* Learn about Django Views, URLs and the urlconf
* Learn about the services offered by Amazon Web Services (AWS)
* Learn to provision a web server in AWS
* Learn about AVL rotations and how to build a self-balancing Binary Search Tree

Readings
========

Django Views
------------

.. include:: /readings/django_readings.rst
    :start-line: 36
    :end-line: 56


* Read about using `Django's Authentication Systems <https://docs.djangoproject.com/es/1.10/topics/auth/default/>`_
* `Writing Views in Django <https://docs.djangoproject.com/en/1.10/topics/http/views/>`_
* (Read *ONLY!* Don't *do* this yet) `Deploying a Django App to Amazon AWS <https://ashokfernandez.wordpress.com/2014/03/11/deploying-a-django-app-to-amazon-aws-with-nginx-gunicorn-git/>`_
* (Read *ONLY!* Do not *do* yet!) `Creating a Database Server <http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/getting-started-create-rds.html>`_
* Be aware of the `security controls for Amazon RDS <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html>`_
* In particular, learn about `RDS Security Groups <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html>`_ and controlling access between RDS and EC2

Review
======

* Binary Search Tree Deletion
* Django Data Model

Concepts
========

.. toctree::
    :maxdepth: 2

    /lectures/django_views
    /lectures/simple_wsgi_deployment

* Tree Rotations and self-balancing Binary Search Trees

Demo
====

Interacting with AWS through the web, an introduction to AWS web services.

Assignments
===========

* :doc:`/assignments/aws_0_deploy_wsgi_app`
* :doc:`/assignments/daily_lj_entry`
* :doc:`/assignments/bst_4_balancing` (Due Tuesday)
