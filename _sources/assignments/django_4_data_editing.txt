.. slideconf::
    :autoslides: False

***************************
Django Imager: Data Editing
***************************

.. slide:: Django Imager: Data Editing
    :level: 1

    This document contains no slides.

In this series of assignments you will build a simple image management website using Django.
In this third step, you will provide users with a way to add and edit resources from the front-end of the application.
That way, you need not grant them access to the Django admin.

Tasks
=====

Do your work for this assignment on a branch called ``front-end-3``.
Be sure that the branch contains your work for the previous two parts of this work.

Creating
--------

To begin with, create views that allow creating albums and photos.
From the library page you created previously, add a prominent button that allows a user to reach each of these pages.
The page should show a form with the needed fields to create a new album or image.
The album form need not offer the ability to upload photos.
When the form is submitted, the user should be returned to the library page where they can see the newly created object.

The URLs for these pages should be ``/images/albums/add/`` and ``/images/photos/add/``.

Editing
-------

Next, create views that allow updating existing albums and photos.
On the library page, add an 'edit' button to each album and photo that will load this view when clicked.
The view that loads should show a form with the fields of the object to be edited.
The album form should offer the user the ability to choose photos from their library to add to the album.
When the form is submitted, the user should be returned to the library page.

The URLs for these pages should be ``/images/albums/<album_id>/edit/`` and ``/images/photos/<photo_id>/edit/``.

Finally, create a view that allows a user to edit their Profile.
This view should provide access not only to the data on the user's ImagerProfile, but also to fields like "email" or "first_name" and "last_name" that are defined on the User object instead.
When the form is submitted, the user should be returned to their profile page where they can see the updated information.

The URL for this page should be ``/profile/edit/``

Tests
-----

You must implement tests to ensure your views are functioning properly.
In particular ensure that no user may edit resources that do not belong to him or her.

Submitting Your Work
--------------------

When you are done working and all your tests are passing, create a Pull Request from the "front-end" branch to "master".
Submit the URL for that pull request.
When you are done, you can merge the pull request in preparation for the next stage of your work.
