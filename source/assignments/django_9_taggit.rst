.. slideconf::
    :autoslides: False

******************************************
Django: Implement Django Taggit for Imager
******************************************

.. slide:: Django: Implement Django Taggit for Imager
    :level: 1

    This document contains no slides.

We've seen how tags can be used to categorize models on the back-end and the front.
It's time for you to implement them yourself.

For your next assignment for the Imager app, you'll be adding tags to your images. 

Tasks
=====

* Install Django Taggit into your virtualenv.
* Make sure to update your requirements.txt file.
* Make sure to also update your installed apps and migrations.
* Add tags to your photo models.
* Modify your views and templates to reflect the addition of tagging.
* Ensure that from an individual photo's page, a user can access at least 5 other photos like the one they're currently viewing.
* Add tests that show your tagging system works the way that it should.

Feel free to use tags with other models, like the albums which house your photos.
**Make sure though that when a user goes looking for albums belonging to a given tag, they only get albums and not photos.**

Submitting Your Work
====================

Do your work for this assignment on a branch, called ``taggit``.
When you've completed the work push your branch and make a Pull Request to ``master``.
Submit the URL for that pull request.
When you've submitted the URL you may merge the PR.
