******************************
Manage AWS Resources with Boto
******************************

.. ifslides::

    | Using the AWS
    | (*Amazon Web Services*) API
    | to manage cloud resources


AWS API
=======

.. ifnotslides::

    Amazon Web Services provides an API for interacting directly with cloud
    resources from the command line. Using this API allows you to automate
    deployment tasks.

    Automated tasks are easy.

    Easy tasks get done more often.

    Therefore, using the API means you can and will perform deployment tasks
    like setting up and running a testing environment with a much higher
    frequency. This will improve the quality of your work.

.. ifslides::

    .. rst-class:: left build

    * AWS provides an API to manage cloud resources
    * This allows common tasks to be automated
    * Automated tasks are easy to do
    * Easy things are done more often than hard things
    * Therefore you will do things that should be done more often if you
      automate them


AWS in Python
-------------

.. ifnotslides::

    `Boto`_ is the Python binding of the AWS API. It's a solid, well-built
    package that provides control over most of the available services in AWS.

    In this lesson, we'll spend some time learning a basic interaction with AWS
    EC2 (*Elastic Compute Cluster*) using boto.

.. ifslides::

    .. rst-class:: build

    * `Boto`_ is the Python binding of the AWS API
    * Solid, well-built, reliable and secure.
    * Provides control over most AWS services

.. _Boto: http://boto.readthedocs.org/

.. nextslide:: Practice Safe Development

To get started, install boto in a virtual environment:

.. code-block:: pycon

    $ mkproject bototests
    New python executable in bototests/bin/python
    Installing setuptools, pip...done.
    ...
    [bototests]
    heffalump:bototests cewing$ pip install boto
    Downloading/unpacking boto
      ...
    Successfully installed boto
    Cleaning up...
    [bototests]
    heffalump:bototests cewing$ pwd
    /Users/cewing/projects/bototests
    [bototests]
    heffalump:bototests cewing$

Configuration
-------------

.. ifnotslides::

    Next, we want to configure boto so that it has access to the security
    credentials it needs.

    Boto will look for configuration in a configuration file in your home
    directory.  This file is called ``.boto``. Create it, if it doesn't exist:

.. ifslides::

    .. rst-class:: build

    * Boto requires access to your security credentials
    * It will look for configuration in your home directory
    * You must create a .boto file there

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ ls ~/.b*
        /Users/cewing/.bash_history

        /Users/cewing/.buildout:
        default.cfg downloads   eggs        extends

        /Users/cewing/.bundler:
        tmp

    .. ifnotslides::

        Since that file does not exist in my home directory, I create it:

    .. code-block:: bash

        [bototests]
        heffalump:bototests cewing$ touch ~/.boto

.. nextslide::

Open this file in your text editor and add the following lines:


.. rst-class:: build
.. container::

    .. code-block:: ini

        [Credentials]
        aws_access_key_id = YOURACCESSKEY
        aws_secret_access_key = YOURSECRETKEY

    Use the credentials you set up for your IAM user when you registered for
    AWS.

    .. ifnotslides::

        .. warning:: 

            You should never use root AWS credentials for anything other than
            managing IAM users.  Always set up an IAM user and grant the
            required privileges to that user.  If that account is compromised
            you can delete it. You cannot delete your root account without
            losing all your AWS resources.

    You will want to secure that file from easy access by making it readable
    and writable only by yourself:

    .. code-block:: bash

        [bototests]
        heffalump:bototests cewing$ chmod 600 ~/.boto


Create Your First EC2 Instance
==============================

.. rst-class:: left

You are ready now to create your first instance.

Getting Connected
-----------------

.. ifnotslides::

    First, we are going to make a connection to the EC2 service.  When we do
    so, we have to designate the AWS region to which we are connecting.  All
    AWS resources are tied to a region in some fashion.

    We'll set up stream logging so that we can see more information about what
    is happening:

.. ifslides::

    .. rst-class:: build

    * We'll make a connection to the EC2 service.
    * We must designate the *AWS region* we will connect to.
    * We'll set up *stream logging* so we can see what's happening.

.. rst-class:: build
.. code-block:: pycon

    [bototests]
    heffalump:bototests cewing$ python
    ...
    >>> import boto
    >>> boto.set_stream_logger('boto')
    >>> import boto.ec2
    >>> ec2 = boto.ec2.connect_to_region('us-west-2')
    2014-02-14 17:32:56,641 boto [DEBUG]:Using access key found in config file.
    2014-02-14 17:32:56,641 boto [DEBUG]:Using secret key found in config file.
    >>> ec2
    EC2Connection:ec2.us-west-1.amazonaws.com
    >>> 

Configuring an Instance
-----------------------

Next we must set up some configuration values for our server-to-be.

.. ifnotslides::

    The first step is to find an AMI that you want to use. AMIs are machine
    images that Amazon uses in order to create a cloud server of a particular
    type.

    I generally use Ubuntu Linux when creating cloud servers with AWS, and I
    like to choose images from `Alestic`_, which is sort of the 'official' face
    of Ubuntu in EC2.

    At the top right of the Alestic homepage is a tool for finding AMI ids in a
    given AWS region.  We've connected to us-west-2, so we need one for that
    region. We also need to choose the virtualization type, ``PV``
    (paravirtualization) or ``HVM`` (hardware virtual machine). The tool
    reports that an EBS-store image using PV for Ubuntu 14.04
    Utopic is 'ami-b5471c85'. Let's use that.

.. ifslides::

    .. rst-class:: build

    * We need an *AMI* (*Amazon Machine Image*) for our server

      * This determines what OS and pre-installed software our server will
        have.

    * I use Ubuntu Linux for cloud servers.
    * You can choose bare-bones images from `Alestic`_.
    * At the top right of the Alestic homepage is a tool to choose AMIs
    * Select the **us-west-2** region
    * Find an image for Ubuntu Utopic 14.04
    * Use an EBS store (the OS disk is persisted when you *stop* your instance)
    * Use PV (paravirtualization) for now.

.. rst-class:: build
.. code-block:: pycon

    >>> image_id = 'ami-b5471c85'

.. _Alestic: http://alestic.com

.. nextslide::

.. ifnotslides::

    We also need to designate a key pair name and the name of a security group. Use
    the key pair name and security group you created as part of the assignment to
    get an AWS account. If you followed the instructions explicitly, these should
    be ``pk-aws`` and ``ssh-access``.

.. ifslides::

    .. rst-class:: build

    * We must also provide a public/private keypair.
    * And a security group, which determines firewall rules (access via ports).
    * You created these when you signed up for AWS.
    * If you followed the instructions, they are called ``pk-aws`` and
      ``ssh-access``.

.. rst-class:: build
.. code-block:: pycon

    >>> key_pair = 'pk-aws'
    >>> security_group = 'ssh-access'

.. nextslide::

.. ifnotslides::

    Finally, we need to designate exactly what type of instance to create. AWS
    instances come in all shapes and sizes, but the only ones that are in the
    free usage tier are the ``t1.micro`` and ``t2.micro`` types.  We'll begin
    with the older ``t2.micro`` type.

.. ifslides::

    .. rst-class:: build

    * Finally, we pick an instance type
    * These control how much CPU power, RAM and disk space you have
    * We'll start out with a ``t2.micro`` instance
    * If you use only one of these, they are on the **free usage tier**

.. rst-class:: build
.. code-block:: pycon

    >>> instance_type = 't2.micro'

Starting an Instance
--------------------

Finally we are ready to run an instance. Using your open ec2 connection object,
run the following command:

.. rst-class:: build
.. code-block:: pycon

    >>> reservations = ec2.run_instances(
    ...     image_id,
    ...     key_name=key_pair,
    ...     instance_type=instance_type,
    ...     security_groups=[security_group])
    >>>


.. nextslide::

When the command returns, ``reservations`` will hold a list of all the
instances we have just created (there should be only one).

.. code-block:: pycon

    >>> reservations
    Reservation:r-9f78c096
    >>> reservations.instances
    [Instance:i-d0d558d9]
    >>> len(reservations.instances)
    1


.. nextslide::

We can pull that instance out and check its status:

.. code-block:: pycon

    >>> instance = reservations.instances[0]
    >>> instance
    Instance:i-d0d558d9>>> instance.id
    u'i-d0d558d9'
    >>> instance.state
    u'pending'
    >>> instance.update()
    2014-02-14 22:14:00,660 boto [DEBUG]:Method: POST
    ...
    >>> instance.state
    u'running'


.. nextslide::

You may need to update a couple of times until you see the state change to
``running``. Once it does, you can get the public DNS name of the instance:

.. code-block:: pycon

    >>> instance.public_dns_name
    u'ec2-54-203-88-113.us-west-2.compute.amazonaws.com'


SSH Into the New Instance
-------------------------

You can use that DNS name to ssh into the running instance.

**In another terminal**, run the following command:

.. ifnotslides::

    .. code-block:: text

        $ ssh -i ~/.ssh/pk-aws.pem ubuntu@ec2-your.dns.name.amazonaws.com
        The authenticity of host 'ec2-54-203-88-113.us-west-2.compute.amazonaws.com (54.203.88.113)' can't be established.
        RSA key fingerprint is 56:3e:9c:b3:75:96:4f:11:44:e9:2b:14:3a:02:f8:f2.
        Are you sure you want to continue connecting (yes/no)? yes
        Warning: Permanently added 'ec2-54-203-88-113.us-west-2.compute.amazonaws.com,54.203.88.113' (RSA) to the list of known hosts.
        ...
        (user "root"), use "sudo <command>".
        See "man sudo_root" for details.

        ubuntu@ip-10-235-47-92:~$

.. ifslides::

    .. code-block:: bash

        $ ssh -i ~/.ssh/pk-aws.pem ubuntu@ec2-your.dns.name.amazonaws.com
        ...
        Are you sure you want to continue connecting (yes/no)? yes
        ...
        To run a command as administrator (user "root"), use "sudo <command>".
        See "man sudo_root" for details.

        ubuntu@ip-10-235-47-92:~$

.. rst-class:: build
.. container::

    You are now working in a shell *on the server you just created*!

    Run a few simple shell commands and look around a bit.

    Disconnect by typing the ``exit`` command and return to your Python
    interpreter.


Stop the Instance
-----------------

Okay, that's enough for now. It's time to clean up our toys. Let's begin by
requesting that our instance be stopped:

.. code-block:: pycon

    >>> instance.stop()
    2014-02-14 22:25:25,012 boto [DEBUG]:Method: POST
    ... 
    >>> instance.state
    u'stopping'
    >>> instance.update()
    2014-02-14 22:28:55,768 boto [DEBUG]:Method: POST
    ... 
    >>> instance.state
    u'stopped'

.. nextslide:: Termination

Once the instance is cleanly stopped, we can terminate it, which will
completely destroy it and leave us ready to play again another day:

.. code-block:: pycon

    >>> instance.terminate()
    2014-02-14 22:31:06,801 boto [DEBUG]:Method: POST
    ... 
    >>> instance.state
    u'terminated'
    >>>


Wrap-up
=======

.. ifnotslides::

    Boto, the Python wrapper for the AWS API allows us to automate the
    management of cloud resources. This type of automation makes the typical
    tasks of creating deployments (whether to production, staging or testing)
    easy and quick. This in turn lowers the bar to doing what we should all be
    doing, deploying consistently and often.

.. ifslides::

    .. rst-class:: build left

    * Boto allows us to automate the management of cloud resources.
    * This makes the tasks of deployment easier and faster.
    * That lowers the bar to doing such tasks frequently.
    * Which increases the velocity with which we can make updates to projects.

.. rst-class:: build left
.. container::

    There's much more to learn about AWS and boto, but that's all we have time
    for now.

    Please read more in the `boto documentation`_.

.. _boto documentation: http://boto.readthedocs.org/

