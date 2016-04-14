.. slideconf::
    :autoslides: False

****************************
Deploy the Imager app to AWS
****************************

.. slide:: Deploy the Imager app to AWS
    :level: 1

    This document contains no slides.


Deploy your imager application to AWS, using manual means.

Tasks
=====

Here are the things you must incorporate to get it all working:

* Create an EC2 instance
* Install and configure nginx to proxy to Django, and to serve static and media files without proxying these requests to Django.
* Set up `gunicorn` or `waitress` serving your Django app as an upstart process (see the gunicorn deployment docs for examples of how to do this).

  * Install GUnicorn or some equivalent wsgi server
  * Install your application code
  * Create an upstart conf file that includes required system environment variables to get everything working correctly.

* Create an RDS instance and connect to it from Django.
* Use a gmail account to send email.
  Be very careful about setting up an appropriate setting for DEFAULT_FROM_EMAIL.
  If this is not set to the address that belongs to the gmail account (or an alias registered with the account) google will refuse to send the email.


For a basic walkthrough of this process, `see this lecture <http://uwpce-pythoncert.github.io/training.python_web/html/presentations/session10.html>`_.
You may wish to add `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_ and `django-configurations <http://django-configurations.readthedocs.org/en/latest/>`_ to your setup to simplify the job of using environment variables to manage sensitive configuration.

You will absolutely want to read the `Django Deployment Checklist <https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/>`_ in order to get your Django configuration squared away for public deployment.

Please read `this blog post <http://bruno.im/2013/may/18/django-stop-writing-settings-files/>`_ for another approach to controlling settings across environments (an alternative to django-configurations).

Submittin Your Work
===================

When you have the deployment working, and I can register myself for the site and upload some pictures, submit the URL for your running site.