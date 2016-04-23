.. slideconf::
    :autoslides: False

**************************************
Automate Deploying Imager with Ansible
**************************************

.. slide:: Automate Deploying Imager with Ansible
    :level: 1

    This document contains no slides.


Repeat the deployment of your Django Imager website using the Ansible Configuration Management System.

Tasks
=====

Begin by forking my `sample Ansible repository <https://github.com/cewing/codefellows-ansible-example>`_ into your own github account.
Then clone the repository to your local machine, and make the required extensions and adjustments to deploy your own imager project.
You'll need to pip install both Ansible and Boto into your system Python in order for this to work properly.
Unfortunately, Ansible just does not play nicely with Virtualenv.

Along the way, you'll need to use the ansible-galaxy command to install the `jdauphant.nginx role <https://galaxy.ansible.com/list#/roles/466>`_ from the `Ansible Galaxy roles collection <https://galaxy.ansible.com/>`_.

You will want to spend a fair amount of time looking over the `Ansible documentation <http://docs.ansible.com/>`_, which is pretty well organized.

Remember, the basic form of the command to run an ansible playbook is:

$ cd <ansible_repo>
$ ansible-playbook -i plugins/inventory/ <name_of_playbook>.yml

Submitting Your Work
====================

Please use the text box in Canvas to submit the following items:

* A URL pointing to your running Django Instance on AWS
* The URL of your Ansible Repository in GitHub
* A Screenshot of the final screen of your terminal session where the ansible playbook was run.
  This should show the steps run, which were OK, which were changed, etc.
  (You should be able to embed this screenshot in the text entry box using the little broccoli button in the editor bar.)

Part of our evaluation of this submission will be our ability to sign up for the service, add and edit photos and albums, and use the API to get to our photos.
Please ensure that all of this works on AWS.