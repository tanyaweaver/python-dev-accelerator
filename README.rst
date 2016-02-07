**********************************
CodeFellows Python 401 Course Docs
**********************************

Find here the lectures, assignments and code for the Code Fellows 401 Python
course.


Building the Documentation
==========================

Begin by cloning this repository to your local machine:

.. code-block:: bash

    $ git clone https://github.com/codefellows/python-dev-accelerator.git

Change directories into the cloned repository:

.. code-block:: bash

    $ cd python-dev-accelerator

This documentation will build either in a Python 2.7 or a Python 3.4+
environment. For best results, you will want to create a virtualenv in which to
install the requirements.

If you are using Python 2.7, then install `virtualenv`_.  If you are using
Python 3.4 or greater, then the `venv`_ module should come pre-installed in
Python.

Once you have virtualenv ready to use, you can set up a virtualenv in which to
build the documentation (using Python 2.7):

.. code-block:: bash

    $ virtualenv ./

or with Python 3.4+

.. code-block:: bash

    $ python3 -m venv ./

.. _venv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://virtualenv.readthedocs.org/en/latest/

Once you have a virtualenv installed, activate it.

.. code-block:: bash

    $ . bin/activate
    (python-dev-accelerator)$

Now, you can install the required dependencies:

.. code-block:: bash

    (python-dev-accelerator)$ pip install -r requirements.pip

Once this is complete, you should be able to build the documentation using the
Makefile:

.. code-block:: bash

    (cf-pyda)$ make html slides

License
=======

Copyright 2014 Cris Ewing.

Documentation
-------------

The documentation in this work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License. To view a copy of this
license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter
to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California,
94041, USA.

A copy of this license in text format is included in this package under the
``docs`` directory

Code Examples
-------------

Code in this work is licensed under the MIT License.  A copy of this license in
text format is included in this package under the ``docs`` directory.
