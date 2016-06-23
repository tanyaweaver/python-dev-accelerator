============================
Getting Started With Pyramid
============================

Make a directory to work in, I'll call it ``pyramid_test``, and make a new virtual environment in that directory. Then navigate to that directory and activate the virtual environment. Then pip install the most recent versions of ``pip`` and ``setuptools``

.. code-block::

    (pyramid_test) bash-3.2$ pip install -U pip setuptools
    (pyramid_test) bash-3.2$ pip install ipython

Installation
============

In order to begin working with Pyramid, we have to install it.

.. code-block::
    
    (pyramid_test) bash-3.2$ pip install pyramid

Note the other packages that get installed along with it, as it has dependencies. For example, WebOb handles HTTP responses, and Pyramid's response object inherits from this. Many other frameworks also use this package.

Along with its dependencies, Pyramid installs for you a bunch of new shell commands (``pcreate``, ``pshell``, ``prequest``, etc), and you can see them all in the ``bin`` directory of your virtual environment.

.. code-block:: bash

    (pyramid_test) bash-3.2$ ls bin
    activate         easy_install-3.5 ipython3         pip3             pserve           python
    activate.csh     iptest           pcreate          pip3.5           pshell           python3
    activate.fish    iptest3          pdistreport      prequest         ptweens
    easy_install     ipython          pip              proutes          pviews
