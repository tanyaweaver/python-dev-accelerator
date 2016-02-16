****************************
Distributing Python Packages
****************************

.. rst-class:: left
.. container::

    Over the past weeks, you've been creating python code and putting it into
    repositories.

    At the same time, you've been installing code created by other people using
    ``pip``.

    Wouldn't it be nice to be able to install your own code?

    Or for that matter, to share code you've written with others so that they can
    install it?

    This brings us to the ideas of Packages and Distribution.

Python Packages
===============

.. rst-class:: left
.. container::

    The code we've written so far has been pretty simple in structure.

    We've limited ourselves to single Python files (``modules``) which provide
    symbols.

    We've seen how we can make ``modules`` *runnable* by adding ``__main__``
    blocks, and how we can use these to protect code we do not want to execute
    when we import one of our modules.

    We've also seen how we can import symbols from the modules we write into a
    Python interpreter, or even into other Python modules we write.

    But what happens when our code gets more complex?

    What happens when we have a number of ``modules`` all of which are related?

    We create packages.

Anatomy of a Package
--------------------

A package is any folder that contains a file with the special name
``__init__.py``::

    portlets/
    ├── __init__.py
    ├── ad.py
    ├── collection.py
    ├── events.py
    ├── support.py
    ├── thisweekshighlights.py
    └── yellowpurple.py

The presence of a file called ``__init__.py`` in the directory called "portlets"
above turns the directory into a Python package.

Your First Package
------------------

Let's create a "package" here in class.

Fire up a terminal and create a folder called ``mypackage``.  In it, create
three files.  When you're done, your directory structure should look like this::

    mypackage/
    ├── __init__.py
    ├── module1.py
    └── module2.py

In each of the three files starting with ``module``, add the following function
(substitute the name of the Python file for ``<modulename>``):

.. code-block:: python

    def whoami():
        print "I am <modulename>"

.. nextslide::

Now, once you've saved all that, fire up a Python interpreter in the directory
that contains the ``mypackage`` directory.

.. code-block:: pycon

    >>> import mypackage
    >>> dir()
    ['__builtins__', '__doc__', '__name__', '__package__', 'mypackage']
    >>> dir(mypackage)
    ['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'module1']
    >>> import mypackage.module1
    >>> dir(mypackage.module1)
    ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'whoami']
    >>> mypackage.module1.whoami()
    I am module1
    >>> import mypackage.module2
    >>> mypackage.module2.whoami()
    I am module2

The modules and functions within the package are available to us via the
*package namespace*


Turn Data-Structures Into a Package
-----------------------------------

You've been building a collection of data-structure implementations in Python.

Let's use that repository as a gateway to learning Python packaging and
distribution.

Our first step is to turn the collection of Python modules we have into a
``package``.

.. nextslide::

At the moment, your data-structures repository should look something like this:

.. code-block:: bash

    heffalump:packaging cewing$ cd data-structures
    heffalump:data-structures cewing$ tree .
    .
    ├── README.md
    ├── hasher.py
    ├── linked_list.py
    ├── test_linked_list.py
    ├── ll_stack.py
    ├── queue.py
    ├── test_queue.py
    ├── requirements.txt
    └── test_stack.py

.. nextslide::

To turn this collection of modules into a Python ``package``, all we have to do
is add an ``__init__.py`` file to the repository.

However, it's worth thinking for a moment about the larger issue of
``distributing`` our package before we do so.

When you want to share your code with others, there are two basic ways to do
so:

.. rst-class:: build

1. Point them to your repository and say "go to it".
2. Provide them with a ``distribution`` of your code that they can install.

.. rst-class:: build
.. container::

    Clearly, #2 is the more friendly of the two.

    But when you do this, it's not great to have all your program code *and*
    all your tests all mashed together in one big blob.

.. nextslide:: Cleaning House

So, let's fix that for our package by separating the two.  We'll create a pair
of ``packages`` in our repository, one to hold the program code, and one to
hold the tests.  Then we'll move all the program code to the first, and all the
tests to the second:

.. code-block:: bash

    heffalump:data-structures cewing$ mkdir data_structures
    heffalump:data-structures cewing$ mkdir tests
    heffalump:data-structures cewing$ git add data_structures tests
    ...
    heffalump:data-structures cewing$ git commit -m "coverting to package"
    ...
    heffalump:data-structures cewing$ git mv test*.py tests/
    heffalump:data-structures cewing$ git mv *.py data_structures/

.. nextslide:: After the Cleanup

Your directory structure should look something like this:

.. code-block:: bash

    heffalump:data-structures cewing$ tree .
    .
    ├── README.md
    ├── data_structures
    │   ├── linked_list.py
    │   ├── ll_stack.py
    │   └── queue.py
    ├── requirements.txt
    └── tests
        ├── test_linked_list.py
        ├── test_queue.py
        └── test_stack.py

.. nextslide:: Creating Python Packages

Then, add an ``__init__.py`` file to each of our new sub-directories, turning
them into Python ``packages``:

.. code-block:: bash

    heffalump:data-structures cewing$ touch data_structures/__init__py tests/__init__.py
    heffalump:data-structures cewing$ tree .
    .
    ├── README.md
    ├── data_structures
    │   ├── __init__.py
    │   ├── linked_list.py
    │   ├── ll_stack.py
    │   └── queue.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        ├── test_linked_list.py
        ├── test_queue.py
        └── test_stack.py

.. nextslide:: Broken Imports

So now we have two ``packages``, but the issue that we have created is that the
code in our tests no longer has correct imports to get at the program code it
is designed to test.  Try it:

.. code-block:: bash

    heffalump:data-structures cewing$ py.test
    ...
    __________________ ERROR collecting tests/test_linked_list.py __________________
    tests/test_linked_list.py:1: in <module>
    >   import linked_list as LL
    E   ImportError: No module named linked_list
    ...
    heffalump:data-structures cewing$

The answer to our problem is to turn this set of ``packages`` into a
``distribution``.


Python Distributions
====================

.. rst-class:: left
.. container::

    Packaging and distribution in Python is a contentious issue. Debates rage
    over *the right way*. More than one strong-hearted developer has been
    broken on the rocks of trying to establish a standard that works.

    Luckily, there is now `a standard`_ that points to the future.

    .. _a standard: http://python-packaging-user-guide.readthedocs.org

    You can just follow it to ensure that you are doing "the right thing™".

Distutils and Setuptools
------------------------

A ``distribution`` is defined by the `packaging glossary`_ as::

    A Python distribution is a versioned archive file that contains Python
    packages, modules, and other resource files that are used to distribute a
    Release. The distribution file is what an end-user will download from the
    internet and install.

.. _packaging glossary: http://python-packaging-user-guide.readthedocs.org/en/latest/glossary.html#term-distribution

.. nextslide::

Distribution of Python packages was first established via a standard library
module called `distutils`_ However, as packaging needs grew more complex, the
limitations of that code led to the creation of a new library to extend it,
`setuptools`_.

.. _distutils: http://docs.python.org/2/distutils/
.. _setuptools: http://pythonhosted.org/setuptools/

Both of these libraries work off of the idea of a file called ``setup.py``,
which is responsible for establishing a set of *metadata* about a distribution
and the code it contains.

This file contains two main Python statements, an import statement that pulls
the ``setup`` function into the module namespace, and a call of that function,
which builds package metadata.

Creating a Distribution
-----------------------

Let's add such a file to our project code base:

.. code-block:: bash

    heffalump:data-structures cewing$ touch setup.py
    heffalump:data-structures cewing$ ls -1
    README.md
    requirements.txt
    tests
    data_structures
    setup.py

.. nextslide:: Setting Up

Then open the ``setup.py`` file in your editor and add the following code:

.. code-block:: python

    from setuptools import setup

    long_description = """
    This is a package that provides some basic data structures implemented in
    Python.
    """

.. nextslide::

Continue adding this to the same ``setup.py`` file:

.. code-block:: python

    setup(
        name="data-structures",
        version="0.1-dev",
        description="Basic Data Structures",
        long_description=long_description,
        # The project URL.
        url='http://github.com/<yourname>/data-structures',
        # Author details
        author='<Your Name>',
        author_email='<your.email@domain.com',
        # Choose your license
        #   and remember to include the license text in a 'docs' directory.
        # license='MIT',
        packages=['data_structures'],
        install_requires=['setuptools', ]
    )


Installing
----------

This will turn our data-structures repository into an installable distribution.
The distribution will provide one Python package called ``data_structures``

Let's install our package into a virtualenv and try it out.

First we build the virtualenv and install ``pytest``:

.. code-block:: bash

    heffalump:data-structures cewing$ mkvirtualenv dsenv
    New python executable in dsenv/bin/python
    Installing setuptools, pip...done.
    [dsenv]
    heffalump:data-structures cewing$ pip install pytest
    ...
    [dsenv]
    heffalump:data-structures cewing$

.. nextslide::

Then we execute the ``setup.py`` script with the ``install`` subcommand:

.. code-block:: bash

    [dsenv]
    heffalump:data-structures cewing$ python setup.py install
    running install
    ...
    Using /Users/cewing/virtualenvs/dsenv/lib/python2.7/site-packages
    Finished processing dependencies for data-structures==0.1-dev
    [dsenv]
    heffalump:data-structures cewing$

Finally, we can fire up Python and import from our installed pacakge:

.. code-block:: pycon

    >>> import data_structures
    >>> from data_structures.linked_list import LinkedList
    >>> 

.. nextslide:: Fixing Imports

However, we still can't run our tests:

.. code-block:: bash

    [dsenv]
    heffalump:data-structures cewing$ py.test
    ...
    __________________ ERROR collecting tests/test_linked_list.py __________________
    tests/test_linked_list.py:1: in <module>
    >   import linked_list as LL
    E   ImportError: No module named linked_list
    ...
    [dsenv]
    heffalump:data-structures

The reason for this has to do with the format of our import. We are trying to
import the ``linked_list.py`` module as if it were at the top level of our
package, but it isn't. It's actually an attribute in the namespace of the
``data_structures`` package.

.. nextslide:: Fixing Imports

Now we can fix that in our ``test_linked_list.py`` file.  Edit that file so that we
import our symbols from the right place:

.. code-block:: python

    
    from data_structures import linked_list as LL

    def test_init_LinkedList():
        """Assert that a LinkedList object is instantiated."""
        linked_list = LL.LinkedList()
        assert type(linked_list) == LL.LinkedList

.. nextslide:: Working Tests

And now, our tests work:

.. code-block:: bash

    heffalump:data-structures cewing$ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    collected 12 items

    tests/test_linked_list.py ............
    ...
    ===================== 0 failed, 12 passed in 0.15 seconds ======================


Developing
----------

Installing a package with ``python setup.py install`` is great when you are
working with a finished product.

But your code here is not finished.

Installing makes copies of your code in
``$VIRTUAL_ENV/lib/python2.x/site-packages``

If you make changes to the code in your project directory, they won't get
picked up.

Setuptools provides a fix for this by allowing you to ``develop`` packages.

.. nextslide::

To do so, simply run the ``setup.py`` file with a different subcommand,
``develop``:

.. code-block:: bash

    [dsenv]
    $ python setup.py develop

This will create a *link* to your code in ``site-packages``, but leave the code
in place.

You can continue working and be sure that what you are importing is the latest.


