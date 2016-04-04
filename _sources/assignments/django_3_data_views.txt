.. slideconf::
    :autoslides: False

*************************
Django Imager: Data Views
*************************

.. slide:: Django Imager: Data Views
    :level: 1

    This document contains no slides.

In this series of assignments you will build a simple image management website using Django.
In this second step you will implement the user-specific views for the application.
You will create a profile page, where a user can see their own profile information.
You will add a library page, where a user can see all the albums they've created and the photos they've uploaded.
And you will set up views for individual photos and albums.

Tasks
=====

Do your work for this assignment on a branch called ``front-end-2``.
Be sure that the branch contains your work for the registration and login assignment.

Profile Page
------------

This page should provide quickly readable, clear information to the user about their own profile.
Also show the user some helpful information about their own usage of the application.
Give them a count of how many images they have uploaded and how many albums they've created.

This page should also provide easy navigation links to the library page (or perhaps that should be a globally available navigation link).

Once this page exists, you should reconfigure your system so that this page is where a user lands when they log in to your site.
You should also make the displayed name in the top right corner of the site a link that leads back to this page.

The url for this page should be ``/profile/``

Library Page
------------

This page should provide a quick, thumbnail view for all the albums a user has created and all the photos they've uploaded.
For albums, display a thumbnail of the 'cover' image selected for the album.
If no cover image has been selected, display a default image (from site static resources).
For all items the title should be displayed.
You should save space by displaying small images (thumbnails) in a grid format.

To best accomplish this task, you'll install another Django add-on application, `sorl-thumbnail <http://sorl-thumbnail.readthedocs.org/en/latest/>`_. (You can also try out `easy-thumbnail <http://easy-thumbnails.readthedocs.org/en/latest/index.html>`_, but I haven't used that one myself)
The add-on will allow you to easily designate dimensions for thumbnails and will handle creating appropriately sized copies of uploaded images for you.
You **may use the database cache store** when configuring this application.
Redis or memcached are much faster, but a lot more work to get going locally.

For an extra challenge (not required) find and install a javascript add-on that will allow you to click on any image and view a full-sized version in a "lightbox" overlay.
(I've used and enjoyed ``fancybox``)

The URL for this page should be ``/images/library/``

Album and Photo Views
---------------------

Provide simple views for photos and albums.
The Photo view should display an appropriately sized rendering of the photo, perhaps with a lightbox feature to show the full-sized image.
It should also display any metadata available about the photo.
The album view should display all the photos in the album in a grid format (you might re-use the layout you created for the library view above).
Each photo in the album should be displayed.
If you get frisky, you might look into jquery-based gallery plugins like ``galleria`` to see if you can render the entire album as a gallery.

The URLs for these views should be ``/images/album/<album_id>/`` and ``/images/photos/<photo_id>/``.

Tests
-----

You must write tests for your views.
Be especially thorough in testing access-related functionality.
Ensure that no user may view information that he or she should not be allowed to see.

If you wish to test the javascript functionality of your lightbox add-on, you will need to work with a browser testing framework like splinter.

Submitting Your Work
--------------------

When you are done working, and your tests are passing, create a Pull Request from the "front-end-2" branch to master.
Submit the URL for that pull request.
When you have done so, you may merge the pull request back to master in preparation for stage 3 of your work.