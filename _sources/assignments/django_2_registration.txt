.. slideconf::
    :autoslides: False

*******************************************
Django Imager: Registration, Login and Home
*******************************************

.. slide:: Django Imager: Registration, Login and Home
    :level: 1

    This document contains no slides.

In this series of assignments you will build a simple image management website using Django.
You began by defining a data model.
Next, you'll create a home page, and allow new users to register for an account.

Tasks
=====

You will do your work for today on a branch.
Call it "front-end-1".

Unless you have strong opinions about design, you can get a reasonably nice-looking design using a front-end framework like Bootstrap or Zurb Foundation.
There are good add-ons available for both (django-bootstrap3, django-zurb-foundation).
I have personally worked with the former, but not the latter.
In any case, put some effort into making your base.html look nice, whether you choose to use a framework for that or not.

Home Page
---------

The home page for your application should have the url '/'.
It will contain marketing text that invites users to join the site.
It will include a prominent display of an image chosen at random from all the public photos uploaded by your users.
If there are no public photos, it should show an image you pre-select (served as a static resource) instead.

In addition to the above elements the page will provide clear calls to action for logging in or joining the site.
The login call to action, when clicked, will lead to a login form.
The registration call to action will lead to the registration page.

The home page should make use of a basic HTML skeleton provided by a base.html template.
It should fill blocks in that skeleton rather than defining the entire layout of the page itself.

Login / Logout
--------------

The site will allow users to log in and out of the system without needing to go to the Django admin login page.
The urls for these views will be "/login" and "/logout".
I encourage you to use the views already provided by the django.contrib.auth package for login and logout rather than creating your own.
You can override the view template used for login to make it extend your base.html skeleton template.

Registration
------------

The site will allow new users to register themselves so as to begin using the service.
To make this work, you will install and configure a Django add-on called `django-registration <http://django-registration.readthedocs.org/en/stable/>`_.
It provides all the required functionality.
You will need to add the URLs for the application to your site urlconf.
You will also need to provide all the required templates.
You will use the HMAC registration backend which uses the following registration flow:

* Users fills out registration form and clicks 'submit'
* User ends up at a page that informs them that an email has been sent to them with a link to finish the registration.
* User clicks on the link in the email and ends up at a page that tells them that their registration has been confirmed.
* User can then log in to the site with the username and password they provided when they registered.
* Once a user logs in, they should be redirected to the home page, but they should now see their username in the top left corner of the page.

Because the registration service involves sending emails, you will have to configure `email services for Django <https://docs.djangoproject.com/en/1.9/topics/email/>`_.
However, you don't want to send real emails when developing, so make sure that you `configure the Django console email backend <https://docs.djangoproject.com/en/1.9/topics/email/#configuring-email-for-development>`_.
Then any emails you send while working will simply print to the console where Django is running.

Tests
-----

You must write tests for each view you implement, verifying that it works as expected.
Since these tests will involve rendered html you will want to read about the `Django test client <https://docs.djangoproject.com/en/1.9/topics/testing/tools/#the-test-client>`_.
To test registration you will want to be aware of how Django's `email services work in a test environment <https://docs.djangoproject.com/en/1.9/topics/testing/tools/#email-services>`_.

Submitting Your Work
--------------------

When you have completed the work for this assignment, open a pull request from the ``front-end-1`` branch back to master.
Submit the URL for that pull request.
Then, merge the pull request back to master to prepare for the next stage of your front-end development work.
