.. slideconf::
    :autoslides: False

*************************
Get an Amazon AWS Account
*************************

.. slide:: Get an Amazon AWS Account
    :level: 1

    This document contains no slides.

You've deployed one application to Heroku.  Now we'll learn another deployment
stack: `Amazon Web Services <http://aws.amazon.com/>`_.

Tasks
=====

Please sign up for an account.

To allow you a bit more freedom in your learning on AWS we've arranged with Amazon for each of you to receive AWS credits to use.
In order to receive this credit you'll need to sign up for your account.
Please use the same email address I see on your profile here in canvas.

There will be further instructions forthcoming for how to receive your credits.

**Please do pester us if your credits do not appear after a week or two**.

Once you've signed up for an account take the following actions:

* `Create an IAM user <http://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html>`_
  and **place them in a group** with ``Power User`` access.

  - Set up Security Credentials for that IAM user.
  - Save these Security Credentials in a safe place so you can use them for class.

* `Create a Keypair <http://docs.aws.amazon.com/gettingstarted/latest/wah/getting-started-create-key-pair.html>`_

  - Choose the 'US West (Oregon)' region since it's geographically closest to
    you.
  - When you download your private key, save it to ~/.ssh/pk-aws.pem
  - Make sure that the private key is secure and useable by doing the following
    command::

    $ chmod 400 ~/.ssh/pk-aws.pem

* `Create a custom security group <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`_

  - The security group should be named ``ssh-access``
  - Add one custom TCP rule::

      allow port 22
      allow addresses 0.0.0.0/0

Be sure to complete these actions before class, as you will need them.

Submitting Your Work
====================

To submit, tell me you're done.

.. warning:: If you use an email address other than the one on your profile here in Canvas,
             or if you are already signed up for AWS under a different email address
             please submit that email address.
