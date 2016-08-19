*********************************
Working with Virtual Environments
*********************************

.. epigraph::

   For every non-standard package installed in a system Python, the gods kill a kitten

   -- me


Why Virtual Environments?
=========================

.. ifslides::

    .. rst-class:: build

    * You will need to install packages that aren't in the Python standard library
    * You often need to install *different* versions of the *same* library for different projects
    * Version conflicts cause long-term nightmares
    * Use a :py:mod:`venv <venv>` ...
    * **Always**

.. ifnotslides::

    As a professional developer, your projects will often require packages that are not part of Python's standard library.
    And as the number of projects you work on increases, so does the likelihood that you require *different* versions of the *same* library in different projects.
    Version conflicts are the stuff of which nightmares are made.
    Therefore, it is considered best practice to *always* isolate your projects using a *virtual environment*.

    There are a number of different approaches to solving this problem.
    I'll list some others later, but for this course we will focus on using the :py:mod:`venv module <venv>` module.


Installing Virtual Environments
===============================

.. ifnotslides::

    As of Python 3.3, it is no longer required to install an additional package to create a virtual environment.
    The :py:mod:`venv module <venv>` ships with Python as a part of the standard library.

    Some linux distributions (notably Ubuntu) have taken steps to *un-bundle* the module for some reason.
    If you are using linux, be aware that the following examples may not work at first.
    If they do not, then you will have to install an additional package using your system package manager.
    For Ubuntu 16.04, that package is ``python3-venv``.

.. ifslides::

    .. rst-class:: build

    * The :py:mod:`venv module <venv>` is shipped with Python 3.3 and above
    * Ubuntu *un-bundles* the module for some reason
    * On Ubuntu 16.04, you'll ``apt-get install python3-venv`` to get it.


Using Virtual Environments
==========================

.. ifnotslides::

    To create a new virtual environment, you can use the following command:

.. ifslides::

    Create a virtual environment like so:

.. code-block:: bash

    $ python3 -m venv demoenv

.. ifnotslides::

    That command invokes your Python 3 executable (``python3``).
    It is used to run the ``venv`` module (``-m venv``).
    The module is asked to create a named virtual environment (``demoenv``).

    The result of this command is to create a folder called ``demoenv`` in your current working directory:

.. ifslides::

    This creates a ``demoenv`` directory where you are.

.. code-block:: bash

    $ ls .
    demoenv

.. ifnotslides::

    In general, the form of this command is as follows.
    ``<ENV>`` is the name of the environment you want to create.
    If you are already in a folder and want to create an environment there, use ``./``.
    The available options are :py:mod:`well documented <venv>`.
    You can use the ``-h`` option to get some help at the command line.

.. code-block:: bash

    $ virtualenv [options] <ENV>

.. ifslides::

    .. rst-class:: build

    * this the general form
    * use ``./`` as <ENV> to create an environment *here*
    * options are documented, use ``-h`` to get help

What Happened?
--------------

.. ifnotslides::

    When you ran that command, a couple of things took place:

    * A new directory with your requested name was created.
    * A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows).
    * The new Python was cloned from your Python 3.
    * The new Python was isolated from any libraries installed in the original Python.
    * ``Pip`` and ``setuptools`` were installed so you can install additional packages.

    You can take a peek to see the resulting structure of the ``demoenv`` directory:

.. ifslides::

    See what we got:

::

    demoenv/
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── easy_install
    │   ├── easy_install-3.5
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.5
    │   ├── python -> python3
    │   └── python3 -> /usr/bin/python3
    ├── include
    ├── lib
    │   └── python3.5
    ├── lib64 -> lib
    ├── pyvenv.cfg
    └── share
        └── python-wheels

Activation
----------

.. ifnotslides::

    The virtual environment you just created, ``demoenv`` contains an executable Python command.
    If you do a quick check to see which Python executable is found by your terminal, you'll see that it is not the new one:

.. ifslides::

    * you have a virtual environment.
    * but your Python command is still the old one:

.. code-block:: bash

    $ which python
    /usr/bin/python

You can execute the new Python by explicitly pointing to it:

.. code-block:: bash

    $ ./demoenv/bin/python -V
    Python 3.5.2

.. nextslide::

.. ifnotslides::

    That's tedious and hard to remember.
    Instead, you can ``activate`` your virtualenv using the bash ``source`` command:

.. ifslides::

    * difficult to remember
    * ``activate`` your env instead:

.. code-block:: bash

    $ source demoenv/bin/activate
    (demoenv)$ which python
    /Users/cewing/demoenv/bin/python

.. ifnotslides::

    There.
    That's better.
    Now whenever you run the ``python`` command, the executable that will be used will be the new one in your ``demoenv``.

    Notice also that the your shell prompt has changed.
    It indicates which ``virtualenv`` is currently active.
    Little clues like that really help you to keep things straight when you've got a lot of projects going on.
    It's nice the makers of virtualenv thought of it.

.. ifslides::

    .. rst-class:: build

    * ``python`` is the one in your ``demoenv``
    * shell prompt changes, indicates an active virtual environment

Installing Packages
-------------------

.. ifnotslides::

    With an active virtual environment, you also have ``pip`` and ``easy_install``.
    These Python packaging tools allow you to install packages *in your virtual environment*.
    The installed packages will not be available in your wider Python installation.
    They are isolated and safe.

.. ifslides::

    * active virtual env has ``pip`` and ``easy_install``
    * install packages *into your virtual environment*
    * isolated from other Python installations

.. code-block:: bash

    (demoenv)$ which pip
    /Users/cewing/demoenv/bin/pip
    (demoenv)$ which easy_install
    /Users/cewing/demoenv/bin/easy_install

.. nextslide::

.. ifnotslides::

    Let's see this in action.
    We'll install a package called ``docutils``.
    It provides support for converting ReStructuredText documents into other formats.
    This document you are reading is built using tools from that package.

.. ifslides::

    * let's test this
    * install ``docutils`` using ``pip``
    * it's not in the standard library

.. code-block:: bash

    (demoenv)$ pip install docutils
    Downloading/unpacking docutils
      Downloading docutils-0.11.tar.gz (1.6MB): 1.6MB downloaded
      Running setup.py (path:/Users/cewing/demoenv/build/docutils/setup.py) egg_info for package docutils
        ...
        changing mode of /Users/cewing/demoenv/bin/rst2xml.py to 755
        changing mode of /Users/cewing/demoenv/bin/rstpep2html.py to 755
    Successfully installed docutils
    Cleaning up...

.. nextslide::

.. ifnotslides::

    And now, when we fire up our Python interpreter, the docutils package is available to us:

.. ifslides::

    Now ``docutils`` is installed, and we can import it:

.. code-block:: pycon

    (demoenv)$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import docutils
    >>> docutils.__path__
    ['/Users/cewing/demoenv/lib/python2.7/site-packages/docutils']
    >>> ^d
    (demoenv)$

.. ifnotslides::

    There's one other interesting side-effect of installing software with ``venv``.
    The ``docutils`` package provides a number of executable scripts when it is installed: ``rst2html.py``, ``rst2latex.py`` and so on.
    You can see them in the ``bin`` directory inside your ``demoenv``.
    These scripts are set up to execute using the Python with which they were built.
    What this means is that running these scripts will use the Python executable in your virtualenv, *even if that virtualenv is not active*!

Deactivation
------------

.. ifnotslides::

    So you've got a virtual environment created.
    And you've activated it so that you can install packages and use them.
    Eventually you'll need to move on to some other project.
    This likely means that you'll need to stop working with this ``demoenv`` and switch to another.
    It's a good idea to keep a separate virtual environment for every project you work on.

    When a ``venv`` is active, you use the ``deactivate`` command to turn it off:

.. ifslides::

    * you should create fresh virtual environments for each project you work on.
    * how do you change from one virtual environment to another?
    * use the ``deactivate`` command to turn off the currently active env:

.. code-block:: bash

    (demoenv)$ deactivate
    $ which python
    /usr/bin/python

.. ifnotslides::

    Note that your shell prompt returns to normal.
    The executable Python found when you check ``which python`` is the system one again.

.. ifslides::

    .. rst-class:: build

    * your shell prompt returns to normal
    * your executable python is again the system one

Cleaning Up
-----------

.. ifnotslides::

    There is one more great advantage that ``venv`` confers on you as a developer.
    The ability to easily remove a batch of installed Python software from your system.
    Consider a situation where you installed a library that breaks your Python (it happens).
    If you are working in your system Python, you now have to figure out what that package installed, where, and go clean it out manually.
    With ``venv`` the process is as simple as removing the directory that was created when you started out.

    Let's do that with our ``demoenv``:

.. ifslides::

    .. rst-class:: build

    * sometimes installed code breaks
    * cleanup should not be difficult
    * remove the folder ``venv`` created:

.. rst-class:: build
.. code-block:: bash

    $ rm -rf demoenv

.. ifnotslides::

    And that's it.
    The entire environment and all the packages you installed into it are now gone.
    There's no traces left to pollute your world.




Other Options
=============

.. ifnotslides::

    The ``venv`` module is part of the Python standard library starting with Python 3.3.
    But what if you are forced to use Python 2?
    What if you are on a system where ``venv`` is un-bundled and hopelessly borked?
    There are other options available.

    The `virtualenv <https://virtualenv.pypa.io>`_ package is one such option.
    It works for Python 2.x (and for Python 3 as well).
    In fact, it is the predecessor of the ``venv`` module.

    The ``virtualenv`` package can be supplemented by `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_.
    It provides a number of command-line tools that can really add power to your workflow with ``virtualenv``.

    Another option is the `conda <http://conda.pydata.org/docs/get-started.html>`_ packaging system.
    Conda is part of the `Anaconda <https://docs.continuum.io/anaconda/>`_ Python distribution.
    It is widely used in the data science and scientific computing communities.
    We will not use it in this class.
    **Do Not** install it on your machine for the duration of class, as it has side effects that can break our working patterns.

    **Managing Multiple Pythons**

    Sometimes you find yourself needing to install many different versions of Python.
    The more versions you have, the more challenging it can be to keep them cleanly managed.
    The `pyenv <https://github.com/yyuu/pyenv>`_ project provides tools that can help.

    You can identify different Python installations available in your system.
    You can choose which of them to treat as your *global* Python.
    You can change global versions at will.
    You can set different versions to be active in different directories.
    And much more.

    It's well beyond the scope of this course to dive into this tool.
    It is mentioned here as a reference, in case you find it useful at some point in your future career.

.. ifslides::

    There are other ways to do virtual environments in Python

    .. rst-class:: build

    * ``virtualenv`` is for Python 2
    * ``virtualenvwrapper`` works with ``virtualenv`` to provide power workflow tools
    * ``conda`` is used widely by data science and scientific computing folks (NOT IN THIS CLASS)
    * ``pyenv`` can make it easier to manage multiple Python installations (but is not itself a virtualization tool)

A Note
======

.. ifnotslides::

    It can be easy to confuse the virtual environments provided by the ``venv`` module with OS virtualization (like virtualbox or vagrant).
    Be aware that ``venv`` **only** isolates Python and Python packages.
    It is not responsible for isolating any system packages.
    Packages like ``openssl``, ``apache``, ``nginx`` and so on are never managed by ``venv``.

.. ifslides::

    .. rst-class:: build

    * ``venv`` is a *Python* virtual environment system
    * do not confuse it with ``vagrant`` or ``virtualbox``
    * OS virtualization is a completely different thing
    * only Python packages are managed by ``venv``

Wrap-Up
=======

In this lecture we've:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * learned why we might want to use a virtual environment in Python
    * learned to use the ``venv`` module in Python 3 to create such an environment
    * learned how to activate and deactive a virtual environment
    * learned how to install packages in a virtual environment using ``pip``
    * learned that virtual environments can be disposed of

    That's enough for now.

