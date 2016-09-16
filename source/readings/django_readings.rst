.. slideconf::
    :autoslides: False

*****************************
Suggested Readings for Django
*****************************

.. slide:: Suggested Readings for Django
    :level: 1

    This document contains no slides.

An annotated list of suggested readings for the Django Web Framework.

Django Models and Testing
=========================


These readings will support your work on the Data Model for our Django Imager website.

* `Django Models API <https://docs.djangoproject.com/en/1.10/topics/db/models/>`_

* `Django Model Managers <https://docs.djangoproject.com/en/1.10/topics/db/managers/>`_

* `Django's Signal Framework <https://docs.djangoproject.com/en/1.10/topics/signals/>`_, `Built-In Signals <https://docs.djangoproject.com/en/1.10/ref/signals>`_ and `Signal Handling <https://docs.djangoproject.com/en/1.10/topics/signals/#listening-to-signals>`_ (You'll also want to read up on using the new `App Config system <https://docs.djangoproject.com/en/1.10/ref/applications/#configuring-applications>`_ to `register signals and signal handlers <http://chriskief.com/2014/02/28/django-1-7-signals-appconfig/>`_)

* `Django Testing <https://docs.djangoproject.com/en/1.10/topics/testing/>`_ (familiarize yourself both with `writing and running tests <https://docs.djangoproject.com/en/1.10/topics/testing/overview/>`_ and with the `tools Django provides <https://docs.djangoproject.com/en/1.10/topics/testing/tools/>`_ for testing.

* Using Dynamic Test Fixtures with `Factory Boy <http://factoryboy.readthedocs.org/>`_ (in particular pay attention to `using Factory Boy with Django <http://factoryboy.readthedocs.org/en/latest/orms.html#django>`_)

* `Django Migrations <https://docs.djangoproject.com/en/1.10/topics/migrations/#data-migrations>`_


Django Views
============

For your tasks this week, you'll need to create a number of views in Django.
Please refer to the following readings for help in answering your quesitons:

* `Writing Views in Django <https://docs.djangoproject.com/en/1.10/topics/http/views/>`_

* An overview of `Django's Class-Based Views <https://docs.djangoproject.com/en/1.10/topics/class-based-views/>`_

* Full `API Documentation <https://docs.djangoproject.com/en/1.10/ref/class-based-views/>`_ for Class-Based Views

You may also wish to refer to the following materials for help in writing templates in Django:

* `An overview <https://docs.djangoproject.com/en/1.10/ref/templates/language/>`_ of the Django Template Language

* Django `Templates Configuration <https://docs.djangoproject.com/en/1.10/topics/templates/>`_ (including configuration of template lookup and engine selection)

* The `built-in template tags and filters <https://docs.djangoproject.com/en/1.10/ref/templates/builtins/>`_ in Django

* Creating your own `custom template tags and filters <https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/>`_


Django Forms
============

To support creating and editing objects in Django, you'll need to learn about Django Forms.  Here are some readings to keep in mind as you progress:

* Start by learning how to `work with forms <https://docs.djangoproject.com/en/1.10/topics/forms/>`_ in general

* Follow that up with reading about `ModelForms <https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/>`_ and what they provide

* Make sure you understand `form and field validation <https://docs.djangoproject.com/en/1.10/ref/forms/validation/>`_ so you can ensure proper data is submitted

* Particularly complex forms, or forms which require javascript or special css, will need to utilize `form assets <https://docs.djangoproject.com/en/1.10/topics/forms/media/>`_

* You'll want to keep a reference open for the `Forms API <https://docs.djangoproject.com/en/1.10/ref/forms/api/>`_

* Keep in mind that the custom form field you imagine may already have been created and check `the Forms category <https://www.djangopackages.com/grids/g/forms/>`_ on http://www.djangopackages.com
