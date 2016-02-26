.. slideconf::
    :autoslides: False

****************
Testing With Tox
****************

.. slide:: Testing With Tox
    :level: 1

    .. rst-class:: center

    In which we learn to test with multiple versions of Python.

One of our goals for this course is to become comfortable with the practice of writing Python that is *cross-compatible*.
This means we want to consistently write programs that will run equally well under Python 2 and Python 3.
The foundation of such programming rests on testing.
Without solid tests, you can never be sure that your code actually works.
Or, as we have seen before:

.. epigraph::

   Untested code is broken by design

   -- Surely Somebody

.. slide:: Justification
    :level: 2

    .. rst-class:: left
    .. container::

        We want to write *cross-compatible* code

        .. rst-class:: build
        .. container::

            It should run both in Python 2 and Python 3

            We have to have tests to ensure this

            After all "Untested code is broken by design"

            And we have to run our tests in *every Python we support*

But it isn't enough just to test our code in one version of Python.
Just because something works when run in Python 2 is no guarantee that it will work in Python 3.
We really need to run our tests consistently in both environments.

But this requirement introduces once again a complication that can make the distance between development and testing larger.
We want to keep that distance as small as possible.
That will help to prevent us from falling back to the old habits of writing tests last, if ever.
To help close the gap, `tox <https://tox.readthedocs.org>`_ allows us to run tests in any number of different Python environments.

Tox is based on ``virtualenv``.
It allows us to configure a project to run in a number of different environments.
When we execute the ``tox`` command, it builds a virtualenv for each of the configured environments and executes our tests in each.
It reports the results as they happen, so we can see quickly the fruits of our labor.

.. slide:: Testing with Tox
    :level: 3

    But testing in every environment is **hard**, right?

    .. rst-class:: build
    .. container::

        One more factor distancing development work from testing

        Keep that distance *small*!

        ``Tox`` closes the gap, automates testing across envs

        Uses ``virtualenv``, so it works with our toolchain

Installation
============

We are going to work today on setting up tox to test our Ackermann Function project in both Python 2.7 and Python 3.5.
By the end of the exercise, we'll be able to assert with confidence that our code is compatible across both versions of Python.

We'll begin by returning to the directory where we first created our Ackermann project.
Then we will activate the virtualenv we've been working in this week:

.. code-block:: bash

    Banks:~ cewing$ cd path/to/tdd-play
    Banks:tdd-play cewing$ source bin/activate
    [tdd-play]
    Banks:tdd-play cewing$

Our next step is to install the ``tox`` package.
We could do this directly with ``pip``.
But as we learned yesterday, it's better for us to declare the dependencies of our packages in ``setup.py``.
That way, we can allow python packaging tools to install them for us.

Our package is certainly not going to depend on ``tox`` just to be installed.
Really, ``tox`` is a dependency for our tests.
Remember, we can add *optional* dependencies using the concept of *setuptools extras*.
And we have alread created a ``test`` extra so we could depend on ``pytest`` and ``pytest-xdist``.
Let's add ``tox`` as a new testing dependency for our distribution:

.. code-block:: python

    # in setup.py

    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},

Now that we've updated the requirements for our ``test`` extra, let's re-install our distribution with ``pip`` and allow it to resolve the new dependency:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install -e .[test]
    Obtaining file:///Users/cewing/projects/training/codefellows/tests/tdd-play
    ...
    Successfully installed ackermann-0.1 pluggy-0.3.1 tox-2.3.1 virtualenv-14.0.6
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Installation
    :level: 3

    Move to our Ackermann project and activate the virtualenv:

    .. code-block:: bash

        Banks:~ cewing$ cd path/to/tdd-play
        Banks:tdd-play cewing$ source bin/activate

    .. rst-class:: build
    .. container::

        .. container::

            Add ``tox`` to the list of dependencies for ``[test]``:

            .. code-block:: python

                # in setup.py
                extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},

        .. container::

            re-install our distribution:

            .. code-block:: bash

                [tdd-play]
                Banks:tdd-play cewing$ pip install -e .[test]
                Obtaining file:///Users/cewing/projects/training/codefellows/tests/tdd-play
                ...
                Successfully installed ackermann-0.1 pluggy-0.3.1 tox-2.3.1 virtualenv-14.0.6

Great!
Now we are ready to begin configuring our project to use ``tox``.

Configuration
=============

``Tox`` uses `ini-style <https://en.wikipedia.org/wiki/INI_file>`_ configuration files to manage settings for testing.
In Python, support for reading ``.ini`` files is provided by the :py:mod:`configparser` module (in Python 2, it's called :mod:`ConfigParser <python2:ConfigParser>`).
The format supports *settings* specified in ``name = value`` pairs, one to a line.
The settings may be organized in *sections*, which are delineated by ``[sectionname]`` in square brackets.

In order to configure our project to use tox, we must create a file called ``tox.ini`` at the top level of our project, adjacent to our ``setup.py`` file:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ touch tox.ini

.. slide:: Configuration
    :level: 3

    Tox uses ``ini-style`` configuration (``configparser`` module)

    .. rst-class:: build
    .. container::
    
        .. code-block:: ini
        
            [section]
            setting1 = value1
            setting2 = value2, value3

            [section2]
            setting3 = value4

        Create a ``tox.ini`` file in our project directory

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ touch tox.ini

Global Configuration
--------------------

Our first step in configuring ``tox`` is to tell it which versions of Python we will want to test.
Tox can run tests in any version of Python 2 starting with 2.6, any version of Python 3 starting with 3.2, in jython (java-based Python interpreter) and pypy (python written in python).
We want to use Python 2.7 and Python 3.5, so we add the following to our ``tox.ini`` file:

.. code-block:: ini

    [tox]
    envlist = py27, py35

In order for tox to function correctly when we do so, we must have access to Python executables for each named version.
By default tox will look for executables named ``python2.7``, ``python3.5`` etc., but we can control that with the `per-environment configuration settings <tox-config-perenv>` described below.


Settings the ``[tox]`` section of ``tox.ini`` are *global* settings.
They control the over-all operation of tox within our project.
There are `a number of other global settings <https://tox.readthedocs.org/en/latest/config.html>`_ available.
But that will get us started for today.

.. slide:: Global Configuration
    :level: 3

    Applies to the running of ``tox`` itself

    .. rst-class:: build
    .. container::
    
        We can use it to configure

        .. rst-class:: build

        * where to build environments
        * how to build environments
        * which environments to build
        * ...
        
        Add the following to ``tox.ini``:

        .. code-block:: ini

            [tox]
            envlist = py27, py35

        Available: ``py26, py27, py32, py33, py34, py35, pypy...``

        You must have the right executable installed

.. _tox-config-perenv:

Per-Environment Configuration
-----------------------------

We must also set up configuration for the testing environments that will be built to run our tests.
Configuration that applies to all testing environments listed in ``envlist`` goes in the ``[testenv]`` section.
If you have any configuration that applies only to one of the environments, you can place it in a section called ``[testenv:<envname>]``.
The ``<envname>`` must match one of the environment names listed in ``envlist``.

Our needs for this project are pretty simple.
We don't need anything particularly complex or different per environment.
Let's add the following to our ``tox.ini`` file:

.. code-block:: ini

    [testenv]
    commands = py.test
    deps =
        pytest

The ``commands`` setting allows us to specify exactly the command we want to use to run our tests.
The ``deps`` setting allows us to specify dependencies our tests will require.
It is essentially the same as our ``[test]`` extra, but we don't need to provide tox (because tox is running the tests) or pytest-xdist (since we are not doing TDD here).

Another potentially useful configuration setting for testing environments is ``basepython``.
This setting takes a name (which must be available in ``$PATH``) or an absolute path to the Python executable which will be used for the specified environment.
This setting should not be used in the ``[testenv]`` shared configuration section, but only in a ``[testenv:<envname>]`` section.

.. slide:: Per-Env Configuration
    :level: 3

    Configures how each environment operates

    .. rst-class:: build
    .. container::
    
        Can use it to specify:

        .. rst-class:: build

        * what python executable to use
        * which dependencies to install
        * what commands to run
        * where to run the commands
        * ...
        
        Add the following to ``tox.ini``:

        .. code-block:: ini
        
            [testenv]
            commands = py.test
            deps =
                pytest

There are `plenty more options <https://tox.readthedocs.org/en/latest/config.html#virtualenv-test-environment-settings>`_ available to use per testing environment, but these will get us started today.

The full ``tox.ini`` file for our project:

.. code-block:: ini

    [tox]
    envlist = py27, py35

    [testenv]
    commands = py.test
    deps =
        pytest

.. slide:: Complete Configuration
    :level: 3

    The full ``tox.ini`` file for our project:

    .. code-block:: ini

        [tox]
        envlist = py27, py35

        [testenv]
        commands = py.test
        deps =
            pytest

Execution
=========

Now that everything is set with our configuration, we can go ahead and run our tests.
To do so, invoke the ``tox`` command, which should be available in our virtualenv.
You will see significant output as tox builds the virtual environments for each testenv, installs requirements, and then runs the tests and reports the outcomes:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ tox
    GLOB sdist-make: /Users/cewing/projects/training/codefellows/tests/tdd-play/setup.py
    py27 create: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/py27
    py27 installdeps: pytest
    py27 inst: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/dist/ackermann-0.1.zip
    py27 installed: ackermann==0.1,py==1.4.31,pytest==2.8.7,wheel==0.29.0
    py27 runtests: PYTHONHASHSEED='3870038194'
    py27 runtests: commands[0] | py.test
    ======================================== test session starts ========================================
    platform darwin -- Python 2.7.11, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    collected 21 items

    src/test_ack.py .....................

    ===================================== 21 passed in 0.19 seconds =====================================
    py35 create: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/py35
    py35 installdeps: pytest
    py35 inst: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/dist/ackermann-0.1.zip
    py35 installed: ackermann==0.1,py==1.4.31,pytest==2.8.7,wheel==0.29.0
    py35 runtests: PYTHONHASHSEED='3870038194'
    py35 runtests: commands[0] | py.test
    ======================================== test session starts ========================================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    collected 21 items

    src/test_ack.py .....................

    ===================================== 21 passed in 0.20 seconds =====================================
    ______________________________________________ summary ______________________________________________
      py27: commands succeeded
      py35: commands succeeded
      congratulations :)
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Run The Tests
    :level: 3

    .. code-block:: bash
    
        [tdd-play]
        Banks:tdd-play cewing$ tox

    .. rst-class:: build
    .. code-block:: text
    
        GLOB sdist-make: /Users/cewing/projects/training/codefellows/tests/tdd-play/setup.py
        py27 create: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/py27
        ...
        ======================================== test session starts ========================================
        platform darwin -- Python 2.7.11, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
        ...
        src/test_ack.py .....................

        ===================================== 21 passed in 0.19 seconds =====================================
        py35 create: /Users/cewing/projects/training/codefellows/tests/tdd-play/.tox/py35
        ...
        ======================================== test session starts ========================================
        platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
        ...
        src/test_ack.py .....................

        ===================================== 21 passed in 0.20 seconds =====================================
        ______________________________________________ summary ______________________________________________
          py27: commands succeeded
          py35: commands succeeded
          congratulations :)

Make sure we see something like that in your terminal.
If we see test failures in either version, we return to our package and update our code.
We will use the TDD principles we established earlier in this module.
Then we can re-run the tests with tox once we believe the fix to have been made.
When all our tests are passing in all the environments we have specified, we can check our code in to GitHub and go home!

.. slide:: Workflow
    :level: 3

    Use TDD in primary Python version (3) to write code and tests

    .. rst-class:: build
    .. container::
    
        When finished, run tox

        Fix errors using TDD

        Re-run tox

        When all environments are passing, check in to GitHub

Caching
-------

Tox saves time on running tests by creating a working directory where it keeps the virtualenvs it creates for running tests.
This amounts to a simple cache of the packages installed for each environment.
If you suspect that things are out-of-whack with the installed environments you can force them to be re-built using the ``--rebuild`` (or ``-r``) argument to ``tox``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ tox -r

.. slide:: Caching
    :level: 3

    Tox keeps built virtualenvs in .tox directory

    .. rst-class:: build
    .. container::
    
        Make sure to keep this out of GitHub (.gitignore)

        It's a cache of built packages

        If you have odd problems, force envs to rebuild:

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ tox -r

Wrap-Up
=======

We've learned a lot here.

* We know how to install tox as a test dependency for our packages.
* We know how to configure tox to run tests in multiple Python environments.
* We know how to configure specific environments individually.
* We know now to run our tests and to force a rebuilding of the test environments.

That's about enough for now.
You'll be required to use this knowledge in your homework tonight (and going forward from here).

.. slide:: Summary
    :level: 3

    .. rst-class:: build

    * Install tox as a testing dependency
    * Configure tox to run multiple environments
    * Configure environments to run tests
    * Run tox to see test results in all environments
    * Force environment rebuild with ``tox -r``
