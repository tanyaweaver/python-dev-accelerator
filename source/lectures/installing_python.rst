*****************
Installing Python
*****************

.. rst-class:: left
.. container::

    .. ifnotslides::

        Python is in an era of transition.
        Version 2 of the language is being phased out (the end-of-life is set for 2020).
        Version 3 is growing in support and usage.
        However, in your professional lives as Python programmers you are still quite likely to be working in Python 2.

        This class is focused on developing code that is compatible with both Python 2 *and* Python 3.
        The intent is to ensure that you can contribute to updating the code base in your future position.
        You'll be equipped to help break up the log-jam of older code that needs upgrading.

        You will, therefore, need to have a working version of both Python 2 and Python 3.
        This lecture is intended to help you achieve that goal.

    .. ifslides::

        .. rst-class:: build

        * Python 2 is phasing out (E.O.L. in 2020)
        * Python 3 is growing in support and use.
        * You're likely still to work primarily in Python 2
        * You can write compatible code
        * Can help to move existing code forward
        * Must install both Python 2 and 3 for this class

For OS X
========

.. rst-class:: left
.. container::

    .. ifnotslides::

        Python 2 comes pre-installed on OS X.  However, it's not the most up-to-date.
        You can use the `Homebrew <http://brew.sh/>`_ package manager to install a more recent version, and to install Python 3.
        Use that link to install the package manager, if you have not already done so.

        Once you've got ``Homebrew`` installed, you will install each version:

    .. ifslides::

        .. rst-class:: build

        * the system Python is out-of-date
        * install `Homebrew <http://brew.sh/>`_
        * use it to install Python 2 and Python 3

    .. rst-class:: build
    .. container::

        .. code-block:: bash

            $ brew install python
            ...
            $ brew install python3
            ...

For Linux
=========

.. rst-class:: left
.. container::

    .. ifnotslides::

        Depending on which distribution and version of Linux you are using, the system Python may be 2 *or* 3.
        On most recent versions of most distributions you can use the system package manager to install the other version.
        This example assumes Ubuntu linux 16.04.

        By default, the Python installed on Ubuntu 16.04 (Xenial) is version 3.5.
        To install the required extensions to Python 3, as well as what you'll need to work with Python 2, issue the following command:

    .. ifslides::

        .. rst-class:: build

        * Which version is present depends on flavor and version
        * We assume Ubuntu 16.04 (Xenial)
        * Adjust accordingly for your own flavor or version

    .. rst-class:: build
    .. container::

        .. code-block:: bash

            $ sudo apt-get update
            ...
            $ sudo apt-get install build-essential python3-dev python3-venv python python-dev

The Result
==========

.. rst-class:: left
.. container::

    When you've completed these tasks, you should be able to use either Python 2 or Python 3.

Where is Python?
----------------

.. ifnotslides::

    Use the ``which`` command to discover the location of the executable will be summoned for each version:

.. ifslides::

    ``which`` tells you where a command is located:

    .. code-block:: bash

        $ which python2
        /usr/local/bin/python2

        $ which python3
        /usr/local/bin/python3

        $ which python
        /usr/bin/python

What Versions Do I Have?
------------------------

.. ifnotslides::

    You can use the ``-V`` command-line flag to check the version of your Python executables without starting an interpreter:

.. ifslides::

    Use ``-V`` to check versions:

.. code-block:: bash

    $ python3 -V
    Python 3.5.2

    $ python2 -V
    Python 2.7.12

    $ python -V
    Python 2.7.12


