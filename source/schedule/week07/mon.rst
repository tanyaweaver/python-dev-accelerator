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

* Learn about the Hash Table data structure
* Understand the difference between (and increased utility of) class-based views from function-based views
* Get practice setting up your own Relational Database Server (RDS) on AWS

Readings
========

Django Views
------------

.. include:: /readings/django_readings.rst
    :start-line: 34
    :end-line: 54

* Hash Tables at `VisuAlgo <http://visualgo.net/hashtable>`_
* (Read *ONLY!* Do not *do* yet!) `Creating a Database Server <http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/getting-started-create-rds.html>`_
* Be aware of the `security controls for Amazon RDS <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html>`_
* In particular, learn about `RDS Security Groups <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html>`_ and controlling access between RDS and EC2

Review
======

.. * Node Deletion in the Binary Search Tree
.. * Django Models (the ``ImagerProfile``)

* Django Urls and Views
* Binary Search Tree

Concepts
========

.. toctree::
    :maxdepth: 2

    .. /lectures/django_relationships
    .. /lectures/django_files

    /lectures/django_cbv

* AWS Database Management: RDS

Demo
====

* Setting up EC2 and RDS to Communicate With Each Other
* Using django-configurations to achieve 12-factor Nirvana
* Hashing and The Hash Table

.. Managing relationships in the Django ORM

Assignments
===========

.. * :doc:`/assignments/django_2_registration`
.. * :doc:`/assignments/bst_4_balancing` (Due Wednesday)

* :doc:`/assignments/hash_table`
* :doc:`/assignments/django_3_data_views` (adding class-based views)
* :doc:`/assignments/aws_1_deploy_imager`
* :doc:`/assignments/daily_lj_entry`
