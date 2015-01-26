**********************************
CodeFellows Python Dev Accelerator
**********************************

Find here the lectures, assignments and code for the Code Fellows Python Dev
Accelerator program.


Building the Documentation
==========================

Create a virtual environment in which to build the documentation:

.. code-block:: bash

    $ mkvirtualenv cf-pyda
    (cf-pyda)$

Clone the repository:

.. code-block:: bash

    (cf-pyda)$ git clone https://github.com/codefellows/python-dev-accelerator.git

Change directories into the cloned repository:

.. code-block:: bash

    (cf-pyda)$ cd python-dev-accelerator

Install the required dependencies:

.. code-block:: bash

    (cf-pyda)$ pip install -r requirements.txt

Also install the `hidden_code_block`_ sphinx extension (used to hide sample
code in walk-through assignments):

.. _hidden_code_block: http://scopatz.github.io/hiddencode/

.. code-block:: bash

    (cf-pyda)$ wget -P $VIRTUAL_ENV/lib/python2.7/site-packages/ https://raw.githubusercontent.com/scopatz/hiddencode/master/hidden_code_block.py

Once this is complete, you should be able to build the documentation using the
Makefile:

.. code-block:: bash

    (cf-pyda)$ make html slides

License
=======

Copyright 2014 Cris Ewing.

The documentation in this work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License. To view a copy of this
license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter
to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California,
94041, USA.

A copy of this license in text format is included in this package under the
``docs`` directory

Code in this work is licensed under the MIT License.  A copy of this license in
text format is included in this package under the ``docs`` directory.
