.. slideconf::
    :autoslides: False

***********************************
An Introduction to Python Packaging
***********************************

.. slide:: Intro to Python Packaging
    :level: 1

    .. rst-class:: center

    In which we learn to share with others.


We've created a small project that implemented the Ackermann function.
In building it, we used Test Driven Development.
This means that we have a well-tested function that could be of use to another developer.

We've also used code that others have written for us.
Our tests make use of the ``pytest`` module.
And our TDD set up uses the pytest plugin ``pytest-watch``.
Both of these packages were written by other developers, but are available for us to install and use.

How does that work?

These packages are also "distributions".

And you can make your code into distributions as well.

.. slide:: Distributions
    :level: 2

    .. rst-class:: left
    .. container::

        We built a small project

        .. rst-class:: build
        .. container::

            Implemented the Ackermann Function

            Our tests make use of the ``pytest`` module

            Our TDD set up uses the ``pytest-watch`` plugin

            How does it work that we can install that code?

            .. rst-class:: center

            **Distributions**

Python Distributions - A History
================================

Packaging and distribution in Python is a contentious issue.
Debates rage over *the right way*.
More than one strong-hearted developer has been broken on the rocks of trying to establish a standard.

Luckily, there is now `a standard <http://python-packaging-user-guide.readthedocs.org>`_ that points to the future.
You can follow it to ensure that you are doing "the right thing™".

.. slide:: The Packaging Bible
    :level: 3

    There's a lot of conflicting information

    Skip it all and go to the sole authority

    The `Python Packaging Users Guide <http://python-packaging-user-guide.readthedocs.org>`_

    Canonical information updated as needed by the PyPA

Distutils and Setuptools
------------------------

A ``distribution`` is defined by the `packaging glossary <http://python-packaging-user-guide.readthedocs.org/en/latest/glossary.html#term-distribution>`_ as::

    A Python distribution is a versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release.
    The distribution file is what an end-user will download from the internet and install.

In the early days of Python, there was no such thing as a distrubution.
If you wanted to install someone else's code, you had to download and build the code manually and move it into your PYTHONPATH yourself.
This was not particularly simple or convenient.

In 1998 a group of Python developers organized a discussion of this problem.
The came up with the idea of a special file you could add to your package code, called ``setup.py``.
Through this file you could issue commands that would allow you to do a number of useful things.
You could create a compressed archive of your package to send to other developers.
You could install such an archive automatically into your PYTHONPATH.
And you could even compile C extensions to your code to make binaries that can be shared wtih others.

This work became the :ref:`distutils library <python2:distutils-index>` (:ref:`py3 <distutils-index>`).
It was added to the Python standard library in 2000 in version 1.6.

In 2002, Richard Jones began working on an online catalog of available Python distributions.
By 2003, the index was up and running as the Python Package Index (PyPI), also known as the "cheeseshop" after the well known comedy sketch.
This index allowed developers to find packages online.
Then they could download the packages and use the included ``setup.py`` file to install them.

Providing support for this type of discovery allowed developers to create packages with more and more dependencies.
Eventually, the pressure of dependency management led to a need to be able to install a package *and all its dependencies*.

In 2004 Phillip Eby started to work on a set of extensions to ``distutils`` he called `setuptools <https://pythonhosted.org/setuptools/>`_.
The ``setuptools`` library provided complex dependency management, automated recognition of version precedence, and an automatic installation tool called ``easy_install``.
Though it has never landed in the standard library, ``setuptools`` has become the primary means for creating and distributing Python packages.

.. note:: Much of this history is derived from `this blog post <http://blog.startifact.com/posts/older/a-history-of-python-packaging.html>`_ from 2009.
          It isn't a complete history, but it's good.
          There are also several other posts on that blog well worth reading.

.. slide:: History
    :level: 3

    Early Python had no packaging

    .. rst-class:: build
    .. container::

        In 1998 a group of developers began to discuss this problem

        Their idea: ``setup.py`` file to control installation of code

        The ``distutils`` module was added to Python 1.6 (2000) (Greg Ward)

        The ``cheeseshop`` added a web archive of packages in 2003 (Richard Jones)

        In 2004, Phillip Eby started ``setuptools`` to enhance ``distutils``

        In 2008, Ian Bicking created ``pip`` to overcome problems in ``easy_install``

Creating a Python Distribution
==============================

Both of these libraries work off of the idea of a file called ``setup.py``.
This file is responsible for establishing a set of *metadata* about a distribution and the code it contains.

A ``setup.py`` file contains two main Python statements.
The first is an import statement that pulls the ``setup`` function into the module namespace.
The second calls the function, with a series of keyword arguments that set up metadata.

.. code-block:: python

    from setuptools import setup

    setup (
        # ... metadata keyword arguments go here
    )

There are *lots* of these keyword arguments, and it's a lot easier to explore them interactively.
Let's turn our *ackermann* implementation (and its tests) into a simple python distribution.

.. slide:: Distribution Basics
    :level: 3

    Both ``distutils`` and ``setuptools`` rely on a ``setup.py`` file.

    .. rst-class:: build
    .. container::

        This file must have at least two Python statements:

        .. code-block:: python

            from setuptools import setup

            setup (
                # ... metadata keyword arguments go here
            )

        Execute the file from the command line to get functionality:

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ python setup.py --help
            Common commands: (see '--help-commands' for more)
              ...

Create ``setup.py``
-------------------

Begin, by returning to the ``tdd-tests`` folder you created earlier.

.. code-block:: bash

    Banks:~ cewing$ cd path/to/tdd-tests
    Banks:tdd-play cewing$

Then, activate our virtual environment so our work will be isolated from our system.

.. code-block:: bash

    Banks:tdd-play cewing$ source bin/activate
    [tdd-play]
    Banks:tdd-play cewing$

In this directory, create a new file called ``setup.py``.
Open that file in your text editor.
In ``setup.py`` add the following code:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from setuptools import setup

    setup()

.. slide:: Modify Ackermann
    :level: 2

    .. rst-class:: left
    .. container::

        .. code-block:: bash

            Banks:~ cewing$ cd path/to/tdd-tests
            Banks:tdd-play cewing$

        .. rst-class:: build
        .. container::

            .. code-block:: bash

                Banks:tdd-play cewing$ source bin/activate
                [tdd-play]
                Banks:tdd-play cewing$

            .. code-block:: bash

                [tdd-play]
                Banks:tdd-play cewing$ touch setup.py

            .. code-block:: python

                # -*- coding: utf-8 -*-
                from setuptools import setup

                setup()

Set Basic Metadata
------------------

This is the basic skeleton for a ``setup.py`` file.
There are a lot of different options we can use in the call to ``setup``.
Let's begin with an easy one, the *name* of our distribution.
We'll call the distribution by the same name as the module (and the function defined inside it):

.. code-block:: python

    setup(
        name="ackermann"
    )

In truth, we can use any name at all here.
This name is how other developers can refer to our distribution when they wish to install it.
As is, our distribution could be installed with ``pip install ackermann``.
Perhaps we want to be more explicit that this is a Python implementation.
We could change the name to ``py-ackermann`` or the like, without altering anything else about the code.

We can also specify a description for our package.
The description should be a single, short sentence that clarifies what our package does.
There is also a ``long_description`` argument available.
The value will be used as the text of the distribution's home page on PyPI.

.. code-block:: python

    setup(
        name="ackermann",
        description="A Python implementation of the Ackermann Function."
    )

.. slide:: Package Metadata
    :level: 3

    The arguments to ``setup`` are *metadata* about our package

    .. rst-class:: build
    .. container::

        The ``name`` argument is the name our package can be installed as

        The ``description`` provides a short, one sentence description

        ``long_description`` also available, skip it for now

        .. code-block:: python

            setup(
                name="ackermann",
                description="A Python implementation of the Ackermann Function."
            )

        Keywords, classifiers and more are also available

It's important to establish a *version number* for your source packages.
Doing so signals that your code has reached a level of completeness.
As you make changes to the code, you can increment the version number.
This is a signal to others that your package has changed and new features may be available.

Python encourages using `semantic versioning <http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#semantic-versioning-preferred>`_.
But any versioning scheme is fine so long as it is compliant with the standards of :pep:`440`.

.. code-block:: python

    setup(
        name="ackermann",
        description="A Python implementation of the Ackermann Function.",
        version=0.1
    )

.. slide:: Version Number
    :level: 3

    Set a version number with ``version``:

    .. code-block:: python

        setup(
            name="ackermann",
            description="A Python implementation of the Ackermann Function.",
            version=0.1
        )

    .. rst-class:: build
    .. container::

        There are several version *schemes*

        Use *Semantic Versioning*: ``Major.Minor.Patch``

        Versions < 1.0 are not *final*

We should probably also add a bit of metadata about ourselves.
This will allow users of the package to know who to contact in case of problems.

.. code-block:: python

    setup(
        name="ackermann",
        description="A Python implementation of the Ackermann Function.",
        version=0.1,
        author="Cris Ewing",  # use your own name, of course
        author_email="cris@crisewing.com"
    )

.. slide:: Personal Metadata
    :level: 3

    It's also important to add metadata about ourselves.

    .. rst-class:: build
    .. container::

        ``author`` allows naming an author

        ``author_email`` gives contact information for the author

        Both are strings, so you can format multiple names if needed

        .. code-block:: python

            setup(
                name="ackermann",
                description="A Python implementation of the Ackermann Function.",
                version=0.1,
                author="Cris Ewing",  # use your own name, of course
                author_email="cris@crisewing.com"
            )

        Similar options for ``maintainer`` if you take over sombody's work

If our code is licensed, then we can specify the license in ``setup`` as well.
It's important to consider the license you want to use for your open source packages.
The license allows other developers to understand how you allow your code to be re-used.
If there is no license in a package, then the code is `copyright by default <http://programmers.stackexchange.com/questions/148146/open-source-code-with-no-license-can-i-fork-it>`_.

.. code-block:: python

    setup(
        name="ackermann",
        description="A Python implementation of the Ackermann Function.",
        version=0.1,
        author="Cris Ewing",  # use your own name, of course
        author_email="cris@crisewing.com",
        license='MIT'
    )


.. slide:: License Metadata
    :level: 3

    All open source code must have a license specifying rights

    .. rst-class:: build
    .. container::

        No License == No Usage  (copyrighted)

        A good open source license allows others to use your code freely

        Specify with the ``license`` argument

        .. code-block:: python

            setup(
                name="ackermann",
                description="A Python implementation of the Ackermann Function.",
                version=0.1,
                author="Cris Ewing",  # use your own name, of course
                author_email="cris@crisewing.com",
                license='MIT'
            )

Find Source Code
----------------

Finally, we want to tell setuptools how to find the code for our distribution.
There are a few options to the ``setup`` function related to this:

``py_modules``
  Use this option to specify individual Python modules that should be part of your distribution.
  The value of the argument should be a list containing the name(s) of the module(s), without the ``.py`` extension.

``packages``
  Use this option to specify entire packages of code that should be part of your source.
  When a package is included, any modules or packages inside it will also be part of the distribution
  The value should be a list containing the name(s) of filesystem folder(s).
  The named folders are expected to contain an ``__init__.py`` file.

``package_dir``
  The value of this option is a dictionary rather than a list.
  Use it when your source code is *not* located directly in the same folder as ``setup.py``.
  The values you provide here will affect the way the values in the two previous arguments are used.

In our case, we have no packages in our distribution.
So we won't need that argument.

We do have a module.
It's called ``ackermann.py``, so the name ``ackermann`` must be in our ``py_modules`` list.
We also have a ``test_ack.py`` module, but we don't want that to be included in our distribution.
We can leave the name out of our ``py_modules`` list.

And in our case, our module is not located at the root of the package.
Instead it lives in a ``src`` directory.
We'll need to use the ``package_dir`` argument to point ``setuptools`` in the right direction.
We use a key of an empty string to indicate that the directory we are pointing to should be considered the root.
Then the value is ``src``, telling ``setuptools`` to use that directory as the root of our source.

.. code-block:: python

    setup(
        name="ackermann",
        description="A Python implementation of the Ackermann Function.",
        version=0.1,
        author="Cris Ewing",  # use your own name, of course
        author_email="cris@crisewing.com",
        license='MIT',
        py_modules=['ackermann'],
        package_dir={'': 'src'}
    )

And that's all we require to make our ``ackermann`` package into a distribution.

.. slide:: Source Metadata
    :level: 3

    We can control which files are included

    .. rst-class:: build
    .. container::

        ``packages`` includes listed python packages (must have ``__init__.py``)

        ``py_modules`` includes listed Python modules

        ``package_dir`` determines where to look for the two above

        (and how to name it)

        .. code-block:: python

            setup(
                name="ackermann",
                description="A Python implementation of the Ackermann Function.",
                version=0.1,
                author="Cris Ewing",  # use your own name, of course
                author_email="cris@crisewing.com",
                license='MIT',
                py_modules=['ackermann'],
                package_dir={'': 'src'}
            )

Installing a Distribution
=========================

One of the benefits of using ``setup.py`` is that it allows us to install a distribution.
We do so by *running* the ``setup.py``, with the ``install`` argument.

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ python setup.py install

We can do the same thing by using pip and pointing it at our current directory:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install .

Once this is done, then your distribution has been installed into the Python in our current virtual environment.
We can now start up python and use the code we wrote yesterday:

.. code-block:: python

    >>> import ackermann
    >>> dir(ackermann)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
     '__name__', '__package__', '__spec__', 'ackermann']
    >>> ackermann.ackermann(3, 4)
    125

That's wonderful!

.. slide:: Installing a Distro
    :level: 3

    Now our package can be installed

    .. rst-class:: build
    .. container::

        .. container::

            The traditional way is to run the ``setup.py`` file:

            .. code-block:: bash

                [tdd-play]
                Banks:tdd-play cewing$ python setup.py install

        .. container::

            You can also use ``pip``:

            .. code-block:: bash

                [tdd-play]
                Banks:tdd-play cewing$ pip install .

        .. code-block:: python

            >>> import ackermann
            >>> dir(ackermann)
            ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
             '__name__', '__package__', '__spec__', 'ackermann']
            >>> ackermann.ackermann(3, 4)
            125

Developing Distribution Code
----------------------------

Installing a distribution is great.
It makes the code we've written available to be imported and used anywhere.
However, it does so by placing copies of that code into the ``site-packages`` directory for the active Python.
If we make changes to our code, those changes are *not* reflected in that copied code.

There's a better way.

.. slide:: Problems
    :level: 3

    When you install a package, code is written to ``site-packages``

    .. rst-class:: build
    .. container::

        Python looks there as part of ``PYTHONPATH``

        But if we change code, installed code stays the same

        We must reinstall

        But there is a better way

We can install our code using the ``develop`` argument to ``setup.py``.
Then Python will *link* our code into the ``site-packages`` directory.
And changes we make will be available immediately.

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ python setup.py develop

The same may be accomplished with the ``pip`` *editable* flag (``-e``):

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install -e .

Now if we make changes to our source code, we can see them in our python interpreter.

Open ``ackermann.py`` in your editor and make the following change:

.. code-block:: python

    # add this import
    from __future__ import print_function

    def ackermann(m, n):
        print("hello") # and add this line of code
        if m == 0:
            return n + 1
        # ...

Now, restart python and re-import ackermann to see the changes in action:

.. code-block:: python

    >>> from ackermann import ackermann
    >>> ackermann(1, 4)
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    6
    >>>

.. slide:: Develop Mode
    :level: 3

    .. code-block:: bash

        [tdd-play]
        Banks:tdd-play cewing$ python setup.py develop

    .. rst-class:: build
    .. container::

        This makes *a link* to your package code in ``site-packages``

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install -e .

        When you make changes, they are seen

        .. code-block:: python

            # add this to ackermann.py
            from __future__ import print_function

            def ackermann(m, n):
                print("hello") # and add this line of code
                if m == 0:
                    return n + 1
                # ...

Specifying Dependencies
=======================

If the code we write uses any Python packages that are not in the standard library, that package is a dependency.
In order for our code to run, we must *also* install that package.
The ``setup`` function allows for this, providing an argument that lists dependencies by name.
For example, if we require a package named ``foo``, we could add it to our ``setup.py``.
Then installing our package would cause the ``foo`` package also to be installed:

.. code-block:: python

    setup(
        # ...
        install_requires=['foo']
    )

.. slide:: Dependency Management
    :level: 3

    Sometimes you need code not in the standard library

    .. rst-class:: build
    .. container::

        This code is a *dependency*

        Manage dependencies with ``setup`` argument ``install_requires``

        If you require ``foo``, ``bar`` and ``baz``:

        .. code-block:: python

            setup(
                # ...
                install_requires=['foo', 'bar', 'baz']
            )

        On install, ``setuptools`` or ``pip`` will find and install them


Our package does not require any dependencies to run.
But we do use the ``pytest`` and ``pytest-watch`` packages when testing.
The ``setup`` function also allows for this, with the ``extras_require`` argument.
The argument takes a dict as an argument.
The keys of the dict are the names of "extras" (installation options for our package).
The values are lists of packages that are required in order for that functionality to be available.

Let's add a ``test`` extra that will automatically install the packages our tests require.
In our ``setup.py``, add the following:

.. code-block:: python

    setup(
        # ...
        install_requires=[],
        extras_require={'test': ['pytest', 'pytest-watch']},
    )

.. slide:: Extras
    :level: 3

    Sometimes, dependencies are need for optional code

    .. rst-class:: build
    .. container::

        Our package depends on ``pytest``, ``pytest-watch``

        But **only** for tests

        Declare an *extra* in ``setup``:

        .. code-block:: python

            setup(
                # ...
                install_requires=[],
                extras_require={'test': ['pytest', 'pytest-watch']},
            )

        Install the *extra* (from where ``setup.py`` is):

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install -e .[test]

To prove that this works, we'll destroy our current virtualenv and then start over.

First, deactivate the current virtualenv.
Then, from the ``tdd-play`` directory, remove everything **except** ``setup.py`` and the ``src`` directory:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ deactivate
    Banks:tdd-play cewing$ rm -r bin include lib *.json *.egg-info

Next, make a new virtualenv.
Update pip and setuptools, just in case.
Finally, install our package *with the test extra*:

.. code-block:: bash

    Banks:tdd-play cewing$ python3 -m venv ./
    ...
    Banks:tdd-play cewing$ source bin/activate
    [tdd-play]
    Banks:tdd-play cewing$ pip install -U pip setuptools
    ...
    [tdd-play]
    Banks:tdd-play cewing$ pip install -e .[test]
    ...
    Successfully installed ackermann apipkg-1.4 execnet-1.4.1 py-1.4.31 pytest-2.8.7 pytest-watch-4.1.0
    [tdd-play]
    Banks:tdd-play cewing$

And now, we should be able to run our tests, just as before:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ py.test
    ======================= test session starts ========================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    plugins: xdist-1.14
    collected 21 items

    src/test_ack.py .....................

    ==================== 21 passed in 0.28 seconds =====================
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Proof of Success
    :level: 3

    .. code-block:: bash

        [tdd-play]
        Banks:tdd-play cewing$ deactivate
        Banks:tdd-play cewing$ rm -r bin include lib *.json *.egg-info

    .. rst-class:: build
    .. container::

        .. code-block:: bash

            Banks:tdd-play cewing$ python3 -m venv ./
            ...
            Banks:tdd-play cewing$ source bin/activate
            [tdd-play]
            Banks:tdd-play cewing$ pip install -U pip setuptools

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install -e .[test]
            ...
            Successfully installed ackermann apipkg-1.4 execnet-1.4.1 py-1.4.31 pytest-2.8.7 pytest-watch-4.1.0

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ py.test


.. _python_packaging_cli_python:

Command-Line Python
===================

Sometimes, we might want to allow users to use our code outside a Python interpreter.
Perhaps our code provides a utility that would be of use on the command line.
We can tell ``setup.py`` to provide access to that code as a ``console script``.

In computer science, we refer to the functions in our that users interact with directly as *entry points*.
They are the doorways that provide access to our code.
In ``setup.py`` we can specify entry points to our code.
The argument is called ``entry_points``, and the value is a dict.
The keys of the dict are different categories of entry point.
The values of the dict are lists of "entry point specifiers" that belong in that category.
For our purposes, we can just use the ``console_scripts`` category.
Entry points in this category will be built into executable scripts when our package is installed.

.. slide:: Command Line Python
    :level: 3

    You can write useful tools with Python

    .. rst-class:: build
    .. container::

        You can expose these tools to the command line

        Runnable code is referred to as an **entry point**

        ``setup`` allows ``entry_points`` argument

        Value is a dict of categories and lists of specifiers

        Specifiers: ``executable_name = python_module.path:function_name``

        One category is ``console_scripts``

        These are turned into executable code on installation

Add the following to our ``setup.py`` file:

.. code-block:: python

    setup(
        # ...
        entry_points={
            'console_scripts': [
                "ackermann = ackermann:main"
            ]
        }
    )

Let's look at the "entry point specifier" we just added.
Specifiers take the following form::

    executable_name = python_module.path:function_name

The ``executable_name`` is the name that will be used on the command line.
You can make it anything you like.
The ``python_module.path`` is the import path that leads to the module in which your code is defined.
The ``function`` is the name of the actual executable function that will run when the ``executable_name`` is invoked from the command line.

.. slide:: In ``setup.py``
    :level: 3

    Add the following code:

    .. code-block:: python

        setup(
            # ...
            entry_points={
                'console_scripts': [
                    "ackermann = ackermann:main"
                ]
            }
        )

    .. rst-class:: build
    .. container::

        executable will point to ``main`` function in ``ackermann`` module

        Eeeeeeek!

Our ackermann module does not contain a ``main`` function.
Let's add one.

We'd like to be able to specify the two values to use on the command line.
We can use the Python ``sys.argv`` to get these values.
Then we can call our ackermann function, pass in the values from sys.argv and print the result.

If an error happens, we can handle it by telling the user to try a different pair of values.
If the user provides fewer (or more) than two values, we can print a usage message to help them out.

.. code-block:: python

    import sys

    # other, existing code ...

    USAGE = """
    Usage: ackermann m n

        where m and n are required and should be integers

    """

    def main():
        if len(sys.argv) != 3:
            print(USAGE)
            sys.exit(1)

        try:
            result = ackermann(int(sys.argv[1]), int(sys.argv[2]))
        except RuntimeError:
            print("We can't calculate the result, try using m < 3 and n < 4")
            sys.exit(1)

        print(result)
        sys.exit(0)

.. slide:: In ``ackermann.py``
    :level: 3

    .. code-block:: python

        import sys
        # other, existing code ...
        USAGE = """
        Usage: ackermann m n
            where m and n are required and should be integers
        """
        def main():
            if len(sys.argv) != 3:
                print(USAGE)
                sys.exit(1)

            try:
                result = ackermann(int(sys.argv[1]), int(sys.argv[2]))
            except RuntimeError:
                print("We can't calculate the result, try using m < 3 and n < 4")
                sys.exit(1)

            print(result)
            sys.exit(0)

Now, we have a ``main`` function that will use arguments the user passes on the command line to run our ``ackermann`` function.
And we've specified an entry point in our ``setup.py`` file.
Our last step is to make that script available as a console script.
To do this, our package metadata (which has changed) must be re-read.

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install -e .

Check in the ``bin`` directory, you should see a new executable named ``ackermann``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ ls bin
    ackermann           pip3
    activate            pip3.5
    activate.csh        py.test
    activate.fish       py.test-2.7
    activate_this.py    python
    easy_install        python3
    easy_install-3.5    python3.5
    pip
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Changing Metadata
    :level: 3

    We have updated ``setup.py``

    .. rst-class:: build
    .. container::

        Our package metadata has changed

        We must re-install to pick up the changes

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install -e .

        Now we can see the new executable:

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ ls bin
            ackermann <===      pip3
            activate            pip3.5

And we can use it:

.. code-block:: text

    [tdd-play]
    Banks:tdd-play cewing$ ackermann 3 4
    125
    [tdd-play]
    Banks:tdd-play cewing$ ackermann

    Usage: ackermann m n

        where m and n are required and should be integers


    [tdd-play]
    Banks:tdd-play cewing$ ackermann 4 4
    We can't calculate the result, try using m < 3 and n < 4
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Using the New Toy
    :level: 3

    .. code-block:: text

        [tdd-play]
        Banks:tdd-play cewing$ ackermann 3 4
        125
        [tdd-play]
        Banks:tdd-play cewing$

    .. rst-class:: build
    .. container::

        .. code-block:: text

            [tdd-play]
            Banks:tdd-play cewing$ ackermann
            Usage: ackermann m n
                where m and n are required and should be integers
            [tdd-play]
            Banks:tdd-play cewing$

        .. code-block:: text

            [tdd-play]
            Banks:tdd-play cewing$ ackermann 4 4
            We can't calculate the result, try using m < 3 and n < 4
            [tdd-play]
            Banks:tdd-play cewing$

Wrap Up
=======

We've learned a lot here today.

* a bit of the history of Python packaging and distribution
* how to create a simple distribution using ``setup.py``
* how to install our distribution, both permanently, and for further development
* how to specify the dependencies of our distribution
* how to manage dependencies for testing separately from those needed for installation
* how to make certain code available on the command line as a console script

You'll use these tools over the next few days in your homework.


.. slide:: Summary
    :level: 3

    How can we share code with others

    .. rst-class:: build
    .. container::

        History of packaging and distribution

        Create a simple distribution using ``setup.py``

        Install distributions permanently and for development

        Specify dependencies

        Optional installs with *extras*

        Make executable scripts with *entry points*
