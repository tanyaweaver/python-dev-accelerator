.. slideconf::
    :autoslides: False

********************************
Walk Through the Django Tutorial
********************************

.. slide:: Walk Through the Django Tutorial
    :level: 1

    This document contains no slides.

In this series of assignments you will build a simple image management website using Django.

Tasks
=====

Create a new repository named django-imager in github.
Set it up with a Python .gitignore file and a good license (MIT, most likely).

On your machine, create a new virtualenv project to work on this new repository.
Install Django 1.9 into the new virtualenv and clone your project.
Set up a requirements.txt file and a basic README and commit these changes to master.
Then make a branch called 'models' to start your work.

Once the branch is created, start a new Django project using django-admin.
Call the project "imagersite".
Add the structure created by Django to your repository and commit the changes to your models branch.

You'll be creating the data model for a simple photo management application.

User Profile
------------

We will begin with users.
Django has a full-featured user system, but we want a few more bits of data about our users.
Users of our application will have a profile that captures information about each user not directly related to authentication.
The Django way is to organize individual units of functionality in a website into "apps".
Our user profile is just such a unit.

Create a new app by changing directories into the "imagersite" folder you created above.
You should be in a folder with a file called "manage.py".
Build a new app using that management command file and call it "imager_profile".
The model for our user profile will be contained in this app.

We will discuss in class the specifications for this model.
Implement the specifications as described as an ImagerProfile model.
In addition to what we discuss in class, your model must support the following API:

* **ImagerProfile.active**: provides full query functionality limited to profiles for users who are active (allowed to log in)
* **profile.is_active**: a property which returns a boolean value indicating whether the user associated with the given profile is active

Ensure that each of your models has a visual representation that appropriately displays it when using the Django shell.
Use Django's provided systems to ensure that this representation is compatible both with Python 2 and Python 3.

You must ensure that every standard Django user object created automatically gets an ImagerProfile.

You must also ensure that if a user is deleted from the database, the ImagerProfile associated with that user is also deleted.

Image Management
----------------

The main functionality of our application will be oriented around uploading and organizing images.
Our second Django app will encompass the models and views associated with this work.

From the root of your project, where the "manage.py" file is located, create a second app called "imager_images".

You'll need to create two models in this new app, the Photo and the Album.

Photo represents an individual picture uploaded by a user.
It will contain the image file itself, plus metadata about that file.
Photos are owned by a single Imager user.
Meta-data should include a title and a description, a date_uploaded, date_modified and date_published field.
You should also have a 'published' field which takes one of several possible values ('private', 'shared', 'public')

Album contains Photos and provide meta-data about the collection of photos they contain.
Albums are owned by Users
Any album can contain many Photos and any Photo may be in more than one Album.
Meta-data should include a title and a description.
Also a date created, date modified and date published as well as a published field containing the same options described for Photos.
Users should be able to designate one contained photo as the 'cover' for the album.
The albums created by a user may contain only Photos created by that same user.

Create migrations to support installing your new app.

Create a default app configuration to handle configuring a few global settings for the app.

Finally, you will implement tests that demonstrate the API you have implemented.
Use Django's built-in testing systems and the Test Case classes it provides.
These tests should be unit or integration tests.
Ensure that the tests demonstrate all aspects of the functionality, including access control.
As demonstrated in class, use FactoryBoy to create any required objects your tests need to run properly.

Submitting Your Work
====================

When you are done and all your tests are passing, open a pull request from your 'models' branch to master in GitHub.
Submit the URL to your pull request.
Once you have submitted the URL, please merge your pull request back to master in preparation for the next stage of your development.

Use the commenting feature in canvas to submit questions or comments about the work you've done.