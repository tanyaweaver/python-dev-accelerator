.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 1
******************************

.. slide:: Introduction To Python: Part 1
    :level: 1

    .. rst-class:: center

    In which we establish a common understanding of our primary tool.

In this lecture, we will establish a common understanding of Python, the language you'll be spending the next ten weeks writing.

What is Python?
===============

Python is a dynamic, strongly typed, byte-compiled, interpreted language.
But what exactly does that mean?

.. slide:: What  is Python?
    :level: 2

    .. rst-class:: build left

        * Dynamic
        * Object oriented
        * Byte-compiled
        * Interpreted

Python Features
---------------

Unlike C, C++, C\#, or Java, Python is *dynamically typed*.
In this respect, it is more similar to Lisp, Perl or JavaScript.
In dynamically typed languages there are no *type declarations*.
One effect of this is that programs written in Python tend to be shorter and more flexible.
Another effect is that because there is less code, there are fewer bugs to find.

In addition, Python is *interpreted*.
This means that there is no need to compile programs into executable form.
As a result, the process of creating a program in Python is simpler.
You can test the results of your work immediately.
You can even work interactively, through the Python interpreter.

.. slide:: Python Features
    :level: 3

    .. rst-class:: build

        * Unlike C, C++, C\#, Java ... More like Ruby, Lisp, Perl, Javascript
        * **Dynamic** -- no type declarations

          - Programs are shorter
          - Programs are more flexible
          - Less code means fewer bugs
        * **Interpreted** -- no separate compile, build steps - programming
          process is simpler

What's is Dynamic Typing?
-------------------------

In a *dynamically typed* language, the *types* of individual values are not declared ahead of time.
When a program is run, each value is checked for its type.
Once its type is understood, then statements involving the value can be dispatched to appropriate functions or methods.
An example might help to clarify what we mean.
Here is a statement written in Python:

.. code-block:: ipython

    In [1]: x = a + b

Because Python is *dynamically typed*, a few questions need to be answered before this statement can be evaluated.
First, what type of value is ``a``?
Second, what type of value is ``b``?
Finally, what does it mean to apply the *addition operator* (``+``) to these two values?

There is one final aspect of a language being *dynamically typed*.
At any time, the type of a variable might change.
**Every time** an operation involving ``a`` or ``b`` occurs, these checks must happen again.

.. slide:: Dynamic Typing
    :level: 3

    Type checking and dispatch happen at run-time

    .. code-block:: ipython

        In [1]: x = a + b

    .. rst-class:: build

        * What is ``a``?
        * What is ``b``?
        * What does it mean to add them?
        * ``a`` and ``b`` can change at any time before this process

What is Strong Typing?
----------------------

In a strongly typed language, **everything** has a type.
The type of a thing determines what it is capable of.
In Python, we can use the :class:`type <python2:type>` (:py:class:`py3 <type>`) object to learn the type of anything:

.. code-block:: ipython

    In [1]: a = 5

    In [2]: type(a)
    Out[2]: int

    In [3]: b = '5'

    In [4]: type(b)
    Out[4]: str

.. slide:: Strong Typing
    :level: 3

    .. rst-class:: build

        * **everything** has a type.
        * the *type* of a thing determines what it can do.
        * the ``type`` object can be used to determine the type of anything

        .. code-block:: ipython

            In [1]: a = 5

            In [2]: type(a)
            Out[2]: int

            In [3]: b = '5'

            In [4]: type(b)
            Out[4]: str

Duck Typing
-----------

The combination of *Dynamic Typing* and *Strong Typing* is often referred to as *Duck Typing*.

.. epigraph::

   "When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck."

   -- James Whitcomb Riley

Basically, this means that if an object behaves in the expected way when a program is run, then that object is of the right type.


.. slide:: Duck Typing
    :level: 3

    .. rst-class:: center large

    "If it looks like a duck, and quacks like a duck -- it's probably a duck"


Python Versions
===============

There are two major versions of Python active at this time: Python 2 (currently at version 2.7.11) and Python 3 (currently at version 3.5.1).
Python 2 can be referred to as the "classic" version of Python.
It evolved directly from the original Python, first released publicly in 1991.

Python 3 is an updated version, the first version of which was released in 2008.
It was created because over time certain fundamental flaws had been discovered in the original design of the language.
These flaws could not be fixed without breaking backwards compatibility.
Guido Van Rossum, the creator of Python and "Benevolent Dictator for Life" (BDFL) determined that fixing the flaws was more important than maintaining 100% backward compatiblity.

.. slide:: Python Versions
    :level: 2

    .. rst-class:: build left

        Python 2.x

        .. rst-class:: build

            * "Classic" Python
            * Evolved from original

        Python 3.x ("py3k")

        .. rst-class:: build

            * Updated version
            * Removed the "warts"
            * Allowed to break code

Writing Compatible Code
-----------------------

In this class we will focus on writing code that is compatible with *both* Python 2 and Python 3.

Adoption of Python 3 is growing fast.
It is quite possible at this point to write entire projects from the start with Python 3.
There's even a nice service to `check your dependencies`_ for compatibility with Python 3.

However, a great preponderance of existing code in use today is written in Python 2.
It is highly likely that you will end up employed in a company that still uses Python 2.
If you learn how to write code that is compatible across both versions, you will be able to help contribute to breaking up the log-jam of legacy code that exists in the world.

In writing compatible code, these resources will be of great use.  Please bookmark them:

* https://wiki.python.org/moin/PortingPythonToPy3k
* http://python3porting.com (particulary the chapters on modern idioms and
  supporting Python 2 and 3)
* http://python-future.org/compatible_idioms.html

.. _check your dependencies: https://caniusepython3.com/

.. slide:: Compatible Code
    :level: 3

    We will write code that works for both Python 2 and Python 3

    .. rst-class:: build

        * Adoption of Python 3 is growing fast
        * You can write projects entirely in Python 3
        * Legacy code is still largely in Python 2
        * Learn to write compatible code and help change this

            - https://wiki.python.org/moin/PortingPythonToPy3k
            - http://python3porting.com
              (particulary the chapters on modern idioms and supporting Python 2 and 3)
            - http://python-future.org/compatible_idioms.html

Important Differences
---------------------

There are three differences between Python 2 and Python 3 that will be important from the start.
The change in handling strings that are bytes versus those that are unicode.
The change in the behavior of the division operators: ``/`` and ``//``.
The change of ``print`` from a statement to a function.

We will see each of these in action today, though we will not talk deeply about them.
There are other differences, and we'll cover about them as they come up.

.. slide:: 2 vs. 3
    :level: 3

    Three main differences we care about at first:

    .. rst-class:: build
    .. container::

        .. rst-class:: build

            * bytes vs. unicode
            * the behavior of the division operators: ``/`` and ``//``
            * the change of the ``print`` statement to a function

        We'll see all of these in action today.

        There are other differences

        We'll cover them as we meet them


Introduction to Your Environment
================================

In working with Python, you'll need three basic tools:

* Your Command Line
* Your Interpreter
* Your Editor

.. slide:: Tools of the Trade
    :level: 2

    .. rst-class:: Left
    .. container::

        There are three basic elements to your environment when working with Python:

        .. rst-class:: build

        * Your Command Line
        * Your Interpreter
        * Your Editor


Your Command Line (cli)
-----------------------

Having some facility on the command line is important.
You need to be able to move comfortably through your filesystem, create and remove files and folders, execute programs and evaluate output.
We won't cover this in class, so if you are not comfortable, please bone up.

I suggest running through the **cli** tutorial at "learn code the hard way":

`http://cli.learncodethehardway.org/book`_

.. _http://cli.learncodethehardway.org/book: http://cli.learncodethehardway.org/book

There are a few things you can do to make your command line a better place to work.
You'll do this for homework.
More about specific enhancements later.

.. slide:: The ``cli``
    :level: 3

    You need to be able to work on the command line.

    .. rst-class:: build
    .. container::

        If you are not comfortable at a command line, you must practice.

        You can use http://cli.learncodethehardway.org/book

        We'll be making enhancements to our ``cli`` environment as homework.

Your Interpreter
----------------

Python comes with a built-in interpreter.
You see it when you type ``python`` at the command line:

.. code-block:: pycon

    $ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

That last thing you see, ``>>>`` is the "Python prompt".
This is where you type code.

.. slide:: Python Interpreter
    :level: 3

    Python has a built-in interpreter

    .. rst-class:: build
    .. container::

        It start when you type ``python`` at the command line prompt.

        The ``>>>`` is the "Python prompt".

        You type Python code after it.

Try it out:

.. code-block:: pycon

    >>> print(u"hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print(u"one string" + u" plus another")
    one string plus another
    >>>

.. slide:: Type Some Python
    :level: 3

    Try using the interpreter now:

    .. code-block:: pycon

        >>> print(u"hello world!")
        hello world!
        >>> 4 + 5
        9
        >>> 2 ** 8 - 1
        255
        >>> print(u"one string" + u" plus another")
        one string plus another
        >>>

When you are in an interpreter, there are a number of tools available to you.
There is a help system:

.. code-block:: pycon

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.

You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: pycon

    >>> bob = u"this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.

.. slide:: Interpreter Tools
    :level: 3

    There are tools you can use in the interpreter

    .. rst-class:: build
    .. container::

        .. code-block:: pycon

            >>> help(str)
            Help on class str in module __builtin__:
            ...

        Type 'q' to exit the help system.

        .. code-block:: pycon

            >>> bob = u"this is a string"
            >>> dir(bob)
            ['__add__', '__class__', '__contains__', '__delattr__',
             ...
             'zfill']
            >>> help(bob.zfill)


In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

More on this soon.

.. slide:: Advanced Interpreters
    :level: 3

    Advanced interpreters have more features.

    .. rst-class:: build
    .. container::

        We'll use one called iPython in this class.

        More on that soon

Your Editor
-----------

Typing code in an interpreter is great for exploring.
But for anything "real", you'll want to save the work you are doing in a more permanent fashion.
This is where an Editor fits in.

Any good text editor will do.
MS Word is **not** a text editor.
Nor is *TextEdit* on a Mac.
``Notepad`` is a text editor -- but a crappy one.
A text editor saves only what it shows you, with no special formatting characters hidden behind the scenes.

.. slide:: Your Editor
    :level: 3

    Your Editor is where you write and save files of code.

    .. rst-class:: build
    .. container::

        MS Word is **not** a text editor.

        Nor is *TextEdit* on a Mac.

        ``Notepad`` is a text editor -- but a crappy one.


You need a real "programmers text editor".
This special tool supports a number of features that make writing code much easier.
At a minimum, your editor should support:

.. rst-class:: build

* Syntax Colorization
* Automatic Indentation
* Code linting (syntax and style validation)

In addition, great features to add include:

* Tab completion
* Jump-to-definition
* Interactive follow-along for debugging

.. slide:: Minimum Requirements
    :level: 3

    At a minimum, your editor should have:

        .. rst-class:: build

        * Syntax Colorization
        * Automatic Indentation
        * Code linting

        In addition, great features to add include:

        .. rst-class:: build

        * Tab completion
        * Jump-to-definition
        * Interactive follow-along for debugging

There are those who have religious feelings about their editors.
I am not one of them.
The best tool is the one that you are happy using.
If you already have an editor that supports these features, please use it.

If you do not already have such an editor, then may I suggest `Sublime Text`_?
It is written in Python, can be scripted, and has extensions for all the features you need.
I use version 3 and am very happy with it.

.. _Sublime Text: http://www.sublimetext.com

Why No IDE?
-----------

I am often asked this question.
An IDE does not give you much that you can't get with a good editor plus a good interpreter.
An IDE often weighs a great deal, both in memory and CPU.
Setting up IDEs to work with different projects can be challenging and time-consuming.
And finally, particularly when you are first learning, you don't want too much done for you.

If you currently use an IDE, then continue to do so.
If you really really want to use one, I suggest `PyCharm`_.
It is written for Python, is supported by a well-known company, and is very good.

.. _PyCharm: https://www.jetbrains.com/pycharm/

.. slide:: No IDE?
    :level: 3

    A common question

    .. rst-class:: build
    .. container::

        No really strong advantage to using one

        They can be resource heavy

        The can impose restrictions on project structure

        They can be a crutch that impedes learning in the early stages

        .. rst-class:: centered

            **YAGNI**

        But PyCharm is a good one

Introduction to iPython
-----------------------

As I said before, in this class we'll be using the `iPython`_ interpreter in class.
There are a number of enhancements it offers that make it easier to work in than the built-in interpreter.
There is extensive `official documentation`_ you can read to learn everything there is to know about it.
You may want to start by reading about `Using iPython for Interactive Work`_.
Today, we'll just touch the surface in order to get you started.

.. slide:: Intro to iPython
    :level: 3

    We'll be using `iPython`_ in class.

    .. rst-class:: build
    .. container::

        You can read all about it in the `official documentation`_.

        **Do** read the documentation on `Using iPython for Interactive Work`_.

        Let's learn a bit about it now.

.. _iPython: http://ipython.org
.. _official documentation: http://ipython.org/ipython-doc/stable/index.html
.. _Using iPython for Interactive Work: http://ipython.org/ipython-doc/stable/interactive/index.html


Installing iPython
******************

Earlier this class, we installed ``virtualenv`` to allow us to create sandboxes to play in.
Let's use that pattern here, to install iPython for the purposes of this class.

Begin by making a new virtualenv and then activating it:

.. code-block:: bash

    $ python3 -m venv day1
    ...
    $ source day1/bin/activate
    (day1)$

Then, we can install iPython into our new virtual environment:

.. code-block:: bash

    (day1)$ pip install ipython
    ...

.. slide:: Install iPython
    :level: 3

    .. code-block:: bash

        $ python3 -m venv day1
        ...
        $ source day1/bin/activate
        (day1)$

    .. code-block:: bash

        (day1)$ pip install ipython
        ...

The very basics of iPython
**************************

Now that it is installed, go ahead and fire it up:

.. code-block:: bash

    (day1)$ ipython
    Python 3.5.1 (default, Jan 18 2016, 14:50:30)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.1.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:

The iPython prompt looks quite a bit different from the standard Python interpreter prompt.
For starters, it shows you line numbers which count up as you work.
You can refer to these line numbers later when saving or re-running code you've already typed.
In addition, it tells you if you are viewing "input" (``In [1]:``) or "output" (``Out[1]:``).
This can be handy.
More on this later.

.. slide:: Start iPython
    :level: 3

    .. code-block:: bash

        (day1)$ ipython
        Python 3.5.1 (default, Jan 18 2016, 14:50:30)
        Type "copyright", "credits" or "license" for more information.

        IPython 4.1.1 -- An enhanced Interactive Python.
        ?         -> Introduction and overview of IPython's features.
        %quickref -> Quick reference.
        help      -> Python's own help system.
        object?   -> Details about 'object', use 'object??' for extra details.

        In [1]:

There are a few basic tricks you'll use every day.
The help system shows you information about any object::

.. code-block:: ipython

    In [2]: str?

You can use two question marks to get more detailed information.
In some cases, this will even show you the source code for the thing you are asking about.
If you are done with the help system, typing ``q`` will exit back to the iPython prompt.

.. code-block:: ipython

    In [3]: str.<tab>

You can use tab completion which works in a way very similar to that in your ``cli``.
Type a few characters of something, and use tab completion to finish it.
If there is more than one possible match, you'll be shown all of them.
You can also use tab completion to explore the APIs available on objects in the interpreter.
Type the name of an object, then a dot, and then the tab character to see all available methods and attributes.

.. code-block:: ipython

    In [4]: ls

Simple shell commands are available to you directly in the iPython interpreter.
You can use these to navigate and keep track of what is around you as you work.
With the ``!`` character, you can execute *any* available shell command:

.. code-block:: ipython

    In [5]: !touch foo.py

.. slide:: Basic Usage
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [2]: str?

        .. code-block:: ipython

            In [3]: str.<tab>

        .. code-block:: ipython

            In [4]: ls

        .. code-block:: ipython

            In [5]: !touch foo.py

You can use the ``paste`` magic command to paste the contents of your clipboard directly into an iPython session.
This preserves whitespace correctly, which makes it much easier to paste long code snippets without running into formatting problems.

.. code-block:: ipython

    In [6]: %paste

Finally, command line recall in iPython allows you to use the up and down arrows to navigate through previous commands.
If you type a bit, then using the up and down arrows will navigate through previous lines that started the same way.

The combination of these few tricks can get you quite a long way in learning Python.
There's not a lot more you'll use every day.

.. slide:: Basic Usage
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [6]: %paste

        Command line recall

        That'll get you pretty far.

Basic Python Syntax
===================

.. rst-class:: center mlarge

| Expressions, Statements,
| Values, Types, and Symbols


.. slide:: Basic Syntax
    :level: 3

    .. rst-class:: mlarge

        | Expressions, Statements,
        | Values, Types, and Symbols


Code structure
--------------

In python, every line is a piece of code.
There are three basic types of lines of code: comments, expressions, and statements.

Comments:

.. code-block:: ipython

    In [3]: # everything after a '#' is a comment

Expressions:

.. code-block:: ipython

    In [4]: # evaluating an expression results in a value

    In [5]: 3 + 4
    Out[5]: 7

Statements:

.. code-block:: ipython

    In [6]: # statements do not return a value, may contain an expression

    In [7]: print(u"this")
    this

    In [8]: line_count = 42

    In [9]:

Notice how in iPython the presence of the ``Out[N]:`` prompt can help you to spot the difference between statements and expressions.

.. slide:: Code Structure
    :level: 3

    .. rst-class:: build
    .. container::

        Comments help clarify:

        .. code-block:: ipython

            In [3]: # everything after a '#' is a comment

        Expressions result in values when evaluated:

        .. code-block:: ipython

            In [5]: 3 + 4
            Out[5]: 7

        Statements do not result in values, may contain expressions:

        .. code-block:: ipython

            In [7]: print(u"this")
            this
            In [8]: line_count = 42

Printing
--------

One of the largest differences between Python 2 and Python 3 is in printing values.
In Python 2.x, printing is a statement. In Python 3, it was changed to a function.
In order to write code compatible across both versions, include the following statement at the top of your Python code files:

.. code-block:: python

    from __future__ import print_function

Then you can use ``print`` as a function in any version of Python starting with 2.6:

.. code-block:: iPython

    In [9]: print(u'this works everywhere now')

You should use this idiom in any code you write for this class.

.. slide:: Printing
    :level: 3

    Printing was a statement in Python 2:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [10]: print u"this is Python 2"

        It is a function in Python 3:

        .. code-block:: ipython

            In [11]: print(u"this is Python 3")

        For compatibility:

        .. code-block:: ipython

            In [12]: from __future__ import print_function
            In [13]: print(u"this works in both 2 and 3")

With the print function, you can print multiple things, separated by commas:

.. code-block:: ipython

    In [3]: print(u"the value is", 5)
    the value is 5

For each call to ``print``, Python automatically adds a newline.
You can provide a different ending with ``end`` argument to the print function:

.. code-block:: ipython

    In [12]: for i in range(5):
       ....:     print(u"the value is", end=' ')
       ....:     print(i)
       ....:
    the value is 0
    the value is 1
    the value is 2
    the value is 3
    the value is 4

Any python object can be printed (though it might not be pretty...):

.. code-block:: ipython

    In [1]: class Bar(object):
       ...:     pass
       ...:

    In [2]: print(Bar)
    <class '__main__.Bar'>

.. slide:: Print Features
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            # print multiple objects
            In [11]: print(u"the value is", 5)
            the value is 5

        .. code-block:: ipython

            # control the ending character
            In [12]: for i in range(5):
               ....:     print(u"the value is", end=' ')
               ....:     print(i)
               ....:

        .. code-block:: ipython

            # print anything
            In [13]: print(str)
            <class 'str'>

Code Blocks
-----------

Python is formatted as blocks of code.
Blocks of code are delimited by a colon and indentation:

.. code-block:: python

    def a_function():
        a_new_code_block
    end_of_the_block

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    try:
        do_something_bad()
    except:
        fix_the_problem()


.. slide:: Code Blocks
    :level: 3

    Python uses colons and whitespace to delimit blocks of code:

    .. rst-class:: build
    .. container::

        .. code-block:: python

            def a_function():
                a_new_code_block
            end_of_the_block

        .. code-block:: python

            for i in range(100):
                print(i**2)

        .. code-block:: python

            try:
                do_something_bad()
            except:
                fix_the_problem()

Python uses whitespace to delineate code structure.
This means that in Python, whitespace is **significant**.
(but **ONLY** for newlines and indentation)
The standard is to indent with **4 spaces**.

.. note:: **SPACES ARE NOT TABS** and **TABS ARE NOT SPACES**

These two blocks look the same:

.. code-block:: python

    for i in range(100):
        print(i**2)

    for i in range(100):
        print(i**2)

But when you see the whitespace characters, it turns out they are not:

.. code-block:: python

    for i in range(100):
    \s\s\s\sprint(i**2)

    for i in range(100):
    \tprint(i**2)

In this class there is a hard and fast rule.

.. rst-class:: center

    **ALWAYS INDENT WITH 4 SPACES**.

You should set up your editor to use spaces only.
Ideally, it should even do so when you use the <tab> key.

.. slide:: Indent With 4 Spaces
    :level: 3

    Always use spaces to indent to avoid problems

    .. rst-class:: build
    .. container::

        .. code-block:: python

            for i in range(100):
                print(i**2)

            for i in range(100):
                print(i**2)

        With whitespace visible:

        .. code-block:: python

            for i in range(100):
            \s\s\s\sprint(i**2)

            for i in range(100):
            \tprint(i**2)

.. slide:: Class Rule
    :level: 3

    .. rst-class:: centered large

    **ALWAYS INDENT WITH 4 SPACES**


Values
------

In Python, we use the term **values** to refer to pieces of unnamed data.
Like the integer ``42``, or the unicode object ``u'Hello world!'``, or this list of five integers: ``[1, 2, 3, 4, 5]``.
You can find the type of a value by passing it as an argument to the ``type`` object:

.. code-block:: ipython

    In [21]: type(42)
    Out[21]: int

Python is fully object-oriented.
In Python, every value is an object.
You can use the :func:`dir <python2:dir>` (:py:func:`py3 <dir>`) builtin to inspect the attributes and methods supported by any value.

.. code-block:: ipython

    In [22]: dir(42)
    Out[22]:
    ['__abs__',
     '__add__',
     ...
     'real',
     'to_bytes']

.. slide:: Values
    :level: 3

    .. rst-class:: build

        * Values are pieces of unnamed data: ``42, u'Hello, world',``
        * Every value belongs to a type

          * Try ``type(42)`` - the type of a value determines what it can do

        * In Python, all values are objects

          * Try ``dir(42)``  - lots going on behind the curtain!

Object Literals
***************

In Python, values of the basic types may be constructed using *object literals*.
This is a special type of syntax that lets us create instances of these types merely by typing them.
No need for constructor functions.

For numbers you can simply type the number:

.. code-block:: python

    # an integer
    42
    # a floating point number
    3.14

For the string types, you use quotation marks to set off the characters of the string.
Single- and double-quotes are interchangeable.
If a string contains a quotation mark of the same type as used to contain the string, it must be escaped with a backslash (``\``).

.. code-block:: python

    u'This is a unicode string'
    b"This is a bytestring"
    u'Contained quotes of the same type\'ll require escaping'

You can also define multi-line strings by enclosing the string in tripled quotation marks.
Either single- or double-quotes may be used:

.. code-block:: python

    u'''This is a string that covers
    multiple lines
    '''
    u"""This string has
    more than one line in it as well
    """

The two boolean values are, in and of themselves, object literals:

.. code-block:: python

    True
    False

.. slide:: Object Literals
    :level: 3

    We can create instances of some types using *object literals*

    .. rst-class:: build

        Numbers:
          - floating point: ``3.4``
          - integers: ``456``

        Text:
          -  ``u"a bit of text"``
          -  ``u'a bit of text'``
          - (either single or double quotes work -- why?)

        Boolean values:
          -  ``True``
          -  ``False``

        And more to come...

There are more literals, but these will do for now.


Using Values
------------

Expressions are made of values and operators in combination.
When the expression is *evaluated* (like when you press enter in the interpreter), it returns a new value.

.. code-block:: ipython

    In [28]: 2 + 2
    Out[28]: 4

.. code-block:: ipython

    In [29]: u"Hip " * 2 + u"Hooray!"
    Out[29]: u"Hip Hip Hooray!"

.. slide:: Using Values
    :level: 3

    Values can be used with operators in expressions

    .. rst-class:: build
    .. container::

        evaluating expressions result in new values

        .. code-block:: ipython

            In [28]: 2 + 2
            Out[28]: 4

        .. code-block:: ipython

            In [29]: u"Hip " * 2 + u"Hooray!"
            Out[29]: u"Hip Hip Hooray!"

Symbols
*******

Python gives names to values using *symbols*.
There are rules about what makes a legal symbol.
A legal symbol **must** begin with an underscore or a letter.
After the first character, a legal symbol **may** contain any number of underscores, letters and digits.

::

    this_is_a_symbol
    this_is_2
    _AsIsThis
    1butThisIsNot
    nor-is-this

When a value has been given a name, we can refer to it by name in later lines of code.

.. slide:: Symbols
    :level: 3

    Symbols give names to values.

    .. rst-class:: build
    .. container::

        Symbols must begin with an underscore or letter

        Symbols can contain any number of underscores, letters and numbers

        .. rst-class:: build

            * this_is_a_symbol
            * this_is_2
            * _AsIsThis
            * 1butThisIsNot
            * nor-is-this

Assignment
**********

In Python, we never declare variables.
Instead, we **bind** symbols to values using the *assignment operator* (``=``):

.. code-block:: ipython

    In [24]: the_answer = 42

A symbol can never exist in Python without being bound to a value.
For this reason, Python does not have the concept of *undefined*.
Instead, attempting to refer to a symbol that has not yet been bound to any value results in a ``NameError``:

.. code-block:: ipython

    In [25]: unbound
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-25-7aafa8f1cb96> in <module>()
    ----> 1 unbound

    NameError: name 'unbound' is not defined

Any value can be bound to one symbol, many symbols, or to no symbols.
Values that have no symbols bound to them are *unreachable* and will be garbage collected.

Binding a symbol to a value is a *statement*, not an *expression*.
No value is returned.

.. slide:: Assignment
    :level: 3

    A *symbol* is **bound** to a *value* with the assignment operator: ``=``

    .. rst-class:: build

    * This attaches a name to a value
    * A value can have many names (or none!)
    * Assignment is a statement, it returns no value

When a symbol has been bound to a value, then evaluating that symbol returns the value to which it is bound:

.. code-block:: ipython

    In [26]: name = u"value"

    In [27]: name
    Out[27]: u'value'

    In [28]: an_integer = 42

    In [29]: an_integer
    Out[29]: 42

    In [30]: a_float = 3.14

    In [31]: a_float
    Out[31]: 3.14

.. slide:: Evaluating Symbols
    :level: 3

    Symbols evaluate to the values to which they are bound:

    .. code-block:: ipython

        In [26]: name = u"value"
        In [27]: name
        Out[27]: u'value'
        In [28]: an_integer = 42
        In [29]: an_integer
        Out[29]: 42
        In [30]: a_float = 3.14
        In [31]: a_float
        Out[31]: 3.14

In Python, symbols themselves do not have any type.
Evaluating the type of a *symbol* will return the type of the *value* to which it is bound.

.. code-block:: ipython

    In [19]: type(42)
    Out[19]: int

    In [20]: type(3.14)
    Out[20]: float

    In [21]: a = 42

    In [22]: b = 3.14

    In [23]: type(a)
    Out[23]: int

    In [25]: a = b

    In [26]: type(a)
    Out[26]: float

.. slide:: Symbols and Type
    :level: 3

    The type of a symbol is the type of the value to which it is bound

    .. code-block:: ipython

        In [19]: type(42)
        Out[19]: int
        In [20]: type(3.14)
        Out[20]: float
        In [21]: a = 42
        In [22]: b = 3.14
        In [23]: type(a)
        Out[23]: int
        In [25]: a = b
        In [26]: type(a)
        Out[26]: float

Python supports "in-place assignment" for a number of operators.
The in-place assignment operators are  ``+=``, ``-=``, ``*=``, ``/=``, ``**=``, and ``%=``.

.. code-block:: ipython

    In [32]: a = 1

    In [33]: a
    Out[33]: 1

    In [34]: a = a + 1

    In [35]: a
    Out[35]: 2

    In [36]: a += 1

    In [37]: a
    Out[37]: 3

.. slide:: In-Place Assignment
    :level: 3

    These are the in-place assignment operators::

        += -= *= /= **= %=

    .. code-block:: ipython

        In [32]: a = 1
        In [33]: a
        Out[33]: 1
        In [34]: a = a + 1
        In [35]: a
        Out[35]: 2
        In [36]: a += 1
        In [37]: a
        Out[37]: 3

In Python, you can also perform *multiple-assignment*.
This allows you to bind more than one symbol to an equal number of values simultaneously.
Python evaluates all the expressions on the right before doing any assignments.

.. code-block:: ipython

    In [48]: x = 2

    In [49]: y = 5

    In [50]: i, j = 2 * x, 3 ** y

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

Using this feature, we can perform a nifty Python trick.
We can swap values between two symbols in a single statement:

.. code-block:: ipython

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

    In [53]: i, j = j, i

    In [54]: i
    Out[54]: 243

    In [55]: j
    Out[55]: 4

Multiple assignment and symbol swapping can be very useful in certain contexts.

.. slide:: Multiple Assignment
    :level: 3

    Multiple assignment binds more than one symbol to an equal number of values:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [48]: x = 2
            In [49]: y = 5
            In [50]: i, j = 2 * x, 3 ** y
            In [51]: i
            Out[51]: 4
            In [52]: j
            Out[52]: 243

        This allows us to perform value juggling:

        .. code-block:: ipython

            In [53]: i, j = j, i
            In [54]: i
            Out[54]: 243
            In [55]: j
            Out[55]: 4

Unbinding
*********

You can't actually delete any values in Python.
So long as there is any symbol bound to a value, the value will be kept in memory.

You can unbind a symbol using the :keyword:`del <python2:del>` (:py:keyword:`py3 <del>`) builtin function.
When a symbol is unbound, it is no longer present, and attempting to evaluate it will raise a ``NameError``.
When there are no longer any references to a value, it becomes unreachable, and will be garbage collected.

.. code-block:: ipython

    In [56]: a = 5

    In [57]: b = a

    In [58]: del a

    In [59]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-59-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined

    In [60]: b
    Out[60]: 5

.. slide:: Unbinding
    :level: 3

    The ``del`` builtin function unbinds a symbol.

    .. code-block:: ipython

        In [56]: a = 5
        In [57]: b = a
        In [58]: del a

    .. rst-class:: build
    .. container::

        Unbinding a symbol means you cannot evalute it any longer

        .. code-block:: ipython

            In [59]: a
            ---------------------------------------------------------------------------
            ...
            NameError: name 'a' is not defined

        But other symbols pointing to the same value remain:

        .. code-block:: ipython

            In [60]: b
            Out[60]: 5

        When all references to a value are gone, then the value is garbage collected.

Identity and Equality
---------------------

Every value in Python is an object.
Every object is unique and has a unique *identity*, which you can inspect with  the :func:`id <python2:id>` (:py:func:`py3 <id>`) builtin:

.. code-block:: ipython

    In [68]: id(i)
    Out[68]: 140553647890984

    In [69]: id(j)
    Out[69]: 140553647884864

    In [70]: new_i = i

    In [71]: id(new_i)
    Out[71]: 140553647890984

You can find out if the values bound to two different symbols are the **same object** using the :keyword:`is <python2:is>` (:py:keyword:`py3 <is>`) keyword:

.. code-block:: ipython

    In [72]: count = 23

    In [73]: other_count = count

    In [74]: count is other_count
    Out[74]: True

    In [75]: count = 42

    In [76]: other_count is count
    Out[76]: False

.. slide:: Identity
    :level: 3

    Values have identity, you can see it with the ``id`` builtin:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [68]: id(i)
            Out[68]: 140553647890984
            In [69]: id(j)
            Out[69]: 140553647884864
            In [70]: new_i = i
            In [71]: id(new_i)
            Out[71]: 140553647890984

        And you can prove two symbols point at **the same value** with the ``is`` keyword:

        .. code-block:: ipython

            In [72]: count = 23
            In [73]: other_count = count
            In [74]: count is other_count
            Out[74]: True
            In [75]: count = 42
            In [76]: other_count is count
            Out[76]: False

Equality is a different concept from identity.
Certain types of values may be compared for equality, but not all.
If two values mutually support it, you can test equality with the ``==`` operator (:ref:`py2 <python2:stdcomparisons>`) (:ref:`py3 <python3:stdcomparisons>`).

.. code-block:: ipython

    In [77]: val1 = 20 + 30

    In [78]: val2 = 5 * 10

    In [79]: val1 == val2
    Out[79]: True

    In [80]: val3 = u'50'

    In [81]: val1 == val3
    Out[84]: False

.. slide:: Equality
    :level: 3

    Python values may be compared for equality using ``==``

    .. code-block:: ipython

        In [77]: val1 = 20 + 30
        In [78]: val2 = 5 * 10
        In [79]: val1 == val2
        Out[79]: True
        In [80]: val3 = u'50'
        In [81]: val1 == val3
        Out[84]: False


Operators
---------

Like other programming languages, Python uses ``operators`` to perform actions on values.
Operator Precedence determines which of the possible operations in an expression will be evaluated first.
To force statements to be evaluated out of the order set by operator precedence, use parentheses.

.. code-block:: python

    4 + 3 * 5 != (4 + 3) * 5

.. slide:: Operators
    :level: 3

    Operators perform actions

    .. rst-class:: build
    .. container::

        They have a built-in precedence

        To alter it, you use parentheses:

        .. code-block:: python

            4 + 3 * 5 != (4 + 3) * 5


Python Operator Precedence
**************************

Parentheses and Literals:
  ``(), [], {}``

  ``"", b'', u''``

Function Calls:
  ``f(args)``

Slicing and Subscription:
  ``a[x:y]``

  ``b[0], c['key']``

Attribute Reference:
  ``obj.attribute``

Exponentiation:
  ``**``

Bitwise NOT, Unary Signing:
  ``~x``

  ``+x, -x``

Multiplication, Division, Modulus:
  ``*, /, %``

Addition, Subtraction:
  ``+, -``

Bitwise operations:
  ``<<, >>,``

  ``&, ^, |``

Comparisons:
  ``<, <=, >, >=, !=, ==``

Membership and Identity:
  ``in, not in, is, is not``

Boolean operations:
  ``or, and, not``

Anonymous Functions:
  ``lambda``

.. slide:: Operator Precedence
    :level: 3

    Parentheses and Literals:
      ``(), [], {}``

      ``"", b'', u''``

    Function Calls:
      ``f(args)``

    Slicing and Subscription:
      ``a[x:y]``

      ``b[0], c['key']``

    Attribute Reference:
      ``obj.attribute``

.. slide:: Operator Precedence
    :level: 3

    Exponentiation:
      ``**``

    Bitwise NOT, Unary Signing:
      ``~x``

      ``+x, -x``

    Multiplication, Division, Modulus:
      ``*, /, //, %``

    Addition, Subtraction:
      ``+, -``

.. slide:: Operator Precedence
    :level: 3

    Bitwise operations:
      ``<<, >>,``

      ``&, ^, |``

    Comparisons:
      ``<, <=, >, >=, !=, ==``

    Membership and Identity:
      ``in, not in, is, is not``

    Boolean operations:
      ``or, and, not``

    Anonymous Functions:
      ``lambda``

Keywords
--------

Python defines a number of ``keywords``.
These are language constructs.
You *cannot* use these words as symbols.

::

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try

If you try to use any of the keywords as symbols, you will cause a
``SyntaxError``:

.. code-block:: ipython

    In [13]: del = u"this will raise an error"
      File "<ipython-input-13-c816927c2fb8>", line 1
        del = u"this will raise an error"
            ^
    SyntaxError: invalid syntax

.. code-block:: ipython

    In [14]: def a_function(else=u'something'):
       ....:     print(else)
       ....:
      File "<ipython-input-14-1dbbea504a9e>", line 1
        def a_function(else=u'something'):
                          ^
    SyntaxError: invalid syntax

.. slide:: Keywords
    :level: 3

    Keywords are reserved in Python

    .. rst-class:: build
    .. container::

        If you attempt to use any of them as symbols, you cause a ``SyntaxError``

        ::

            and       del       from      not       while
            as        elif      global    or        with
            assert    else      if        pass      yield
            break     except    import    print
            class     exec      in        raise
            continue  finally   is        return
            def       for       lambda    try

Builtins
--------

Python also has a number of pre-bound symbols, called **builtins**.
They are loaded in a namespace called ``__builtins__``.
You can see them by passing the namespace to the ``dir`` function:

.. code-block:: ipython

    In [6]: dir(__builtins__)
    Out[6]:
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BufferError',
     ...
     'unicode',
     'vars',
     'xrange',
     'zip']

You are free to rebind these symbols.
However, this is generally a **BAD IDEA**.
Your editor, when properly configured for syntax colorization, should alert you to the problem.

.. code-block:: ipython

    In [15]: type(u'a new and exciting string')
    Out[15]: unicode

    In [16]: type = u'a slightly different string'

    In [17]: type(u'type is no longer what it was')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-907616e55e2a> in <module>()
    ----> 1 type(u'type is no longer what it was')

    TypeError: 'unicode' object is not callable

.. slide:: Builtins
    :level: 3

    A number of useful values are pre-bound in Python.

    .. rst-class:: build
    .. container::

        They are contained in a namespace called ``__builtins__``

        You can list them:

        .. code-block:: ipython

            In [8]: dir(__builtins__)

        You can rebind these symbols, but it is a **BAD IDEA**

Exceptions
----------

Notice that the first batch of ``__builtins__`` are all *Exceptions*.
Exceptions are how Python tells you that something has gone wrong.
Understanding the standard exception types in Python and what can cause them is very helpful in debugging your code.

There are several exceptions that you are likely to see a lot of:

.. rst-class:: build

* ``NameError``: indicates that you have tried to use a symbol that is not bound to
  a value.
* ``TypeError``: indicates that you have tried to use the wrong kind of object for
  an operation.
* ``SyntaxError``: indicates that you have mis-typed something.
* ``AttributeError``: indicates that you have tried to access an attribute or
  method that an object does not have (this often means you have a different
  type of object than you expect)

.. slide:: Exceptions
    :level: 3

    Exceptions help us understand what went wrong in our program.

    .. rst-class:: build
    .. container::

        These exceptions are common when you first start in Python:

        .. rst-class:: build

            * ``NameError``: indicates that you have tried to use a symbol that
              is not bound to a value.
            * ``TypeError``: indicates that you have tried to use the wrong
              kind of object for an operation.
            * ``AttributeError``: indicates that you have tried to access an
              attribute or method that an object does not have (this often
              means you have a different type of object than you expect)
            * ``SyntaxError``: indicates that you have mis-typed something.

Functions
---------

A function is a self-contained chunk of code.
You write a function when you need the same code to run multiple times, or in multiple parts of the program.
We call this being DRY (for Don't Repeat Yourself).
It's also useful to keep your code clean.
Finally, writing well-scoped, single-purpose functions helps us to write tests that prove that our code works properly.

A function is created with the :keyword:`def <python2:def>` (:py:keyword:`py3 <def>`) statement.
The statement requires the ``def`` keyword, a name for the function, a list of parameters (possibly empty) and a colon, followed by an indented block of code.

.. code-block:: python

    def func_name(params, list):
        # the body contains statements and expressions
        func_body = params * list

This minimal python function actually does nothing.
The :keyword:`pass <python2:pass>` (:py:keyword:`py3 <pass>`) statement fulfills the requirement for an indented function body, but is a no-op (it does nothing).

.. code-block:: python

    def minimal():
        pass

.. slide:: Functions
    :level: 3

    Functions contain re-usable code

    .. rst-class:: build
    .. container::

        Writing functions keeps code clean, DRY and testable

        A function is created with a ``def`` statement

        .. code-block:: python

            def minimal():
                pass

When the ``def`` statement is executed it creates a *function object*.
This value is bound to a symbol, the *name* of the function.
The ``def`` statement must be executed before the function may be used.

.. code-block:: ipython

    In [23]: unbound()
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-23-3132459951e4> in <module>()
    ----> 1 unbound()

    NameError: name 'unbound' is not defined

.. code-block:: ipython

    In [18]: def simple():
       ....:     print(u"I am a simple function")
       ....:

    In [19]: simple()
    I am a simple function

.. slide:: Functions
    :level: 3

    [Function Writing Demo]


Calling Functions
*****************

You **call** a function using the ``call`` operator (parens).
When a function is called, it is executed.
The statements in the function are evaluated sequentially.
Symbols bound in the function may be used in later statements.

.. code-block:: ipython

    In [1]: def simple():
       ....:     value = 5 + 3
       ....:     print(u"I am a simple function", value)
       ....:

    In [2]: type(simple)
    Out[2]: function

    In [3]: simple
    Out[3]: <function __main__.simple>

    In [4]: simple()
    I am a simple function 8

Functions can call other functions, this makes an execution stack.
Each nested function call creates a new frame in the stack.
Here we define three functions two of which call another of the three.

.. code-block:: ipython

    In [5]: def exceptional():
       ...:     print(u"I am exceptional!")
       ...:     print(1/0)
       ...:
    In [6]: def passive():
       ...:     exceptional()
       ...:
    In [7]: def doer():
       ...:     passive()
       ...:

.. slide:: Calling Functions
    :level: 3

    You execute a function by calling it

    .. rst-class:: build
    .. container::

        To do so, use the ``call`` operator (parens)

        Each line of code in the body of the function is evaluated

        You can call other functions inside a function

        This creates an *execution stack*

        .. code-block:: ipython

            In [5]: def exceptional():
               ...:     print(u"I am exceptional!")
               ...:     print(1/0)
               ...:
            In [6]: def passive():
               ...:     exceptional()
               ...:
            In [7]: def doer():
               ...:     passive()
               ...:

Tracebacks
**********

Executing the ``doer()`` function will call the ``passive`` function, which will in turn call the ``exceptional`` function.
And what happens then?

.. code-block:: ipython

    In [36]: doer()
    I am exceptional
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-36-685a01a77340> in <module>()
    ----> 1 doer()

    <ipython-input-35-f26b1f9e69ad> in doer()
          1 def doer():
    ----> 2     passive()
          3

    <ipython-input-34-1ceb03279947> in passive()
          1 def passive():
    ----> 2     exceptional()
          3

    <ipython-input-33-af07a70629dd> in exceptional()
          1 def exceptional():
          2     print(u'I am exceptional')
    ----> 3     print(1/0)
          4

    ZeroDivisionError: division by zero

This output is called a "traceback".
In Python tracebacks, the Error message is always the last line printed.
Above this line you'll find one stanza for each frame in the execution stack when the error happened.
The last of these stanzas shows you the line of code (and the file) in which the error happened.
Learning to read tracebacks and understand what they tell you is key to becomming a profficient programmer.

.. slide:: Tracebacks
    :level: 3

    Errors happen in functions inside an execution stack

    .. rst-class:: build
    .. container::

        When this occurs, the result is a traceback:

        .. code-block:: ipython

            In [36]: doer()
            I am exceptional
            ---------------------------------------------------------------------------
            ZeroDivisionError                         Traceback (most recent call last)
            <ipython-input-36-685a01a77340> in <module>()
            ----> 1 doer()
            <ipython-input-35-f26b1f9e69ad> in doer()
                  1 def doer():
            ----> 2     passive()
            <ipython-input-34-1ceb03279947> in passive()
                  1 def passive():
            ----> 2     exceptional()
            <ipython-input-33-af07a70629dd> in exceptional()
                  ...
            ----> 3     print(1/0)
            ZeroDivisionError: division by zero

``return``
**********

In Python, every function ends by returning a value.
You can specify the value to return using the :keyword:`return <python2:return>` (:py:keyword:`py3 <return>`) statement:

.. code-block:: ipython

    def the_answer():
        return 42

if you don't explicilty put ``return``  there, Python will automatically return ``None``

.. code-block:: ipython

    In [9]: def fun():
       ...:     pass
       ...:
    In [10]: fun()
    In [11]: result = fun()
    In [12]: print(result)
    None

Note that the interpreter eats ``None`` values (no Out appears).

.. slide:: ``return``
    :level: 3

    Functions end by returning a value

    .. rst-class:: build
    .. container::

        You specify a value using the ``return`` statement:

        .. code-block:: python

            def the_answer():
                return 42

        Without a ``return`` statement, functions will return ``None``:

        .. code-block:: ipython

            In [9]: def fun():
               ...:     pass
               ...:
            In [10]: fun()
            In [11]: result = fun()
            In [12]: print(result)
            None

Only one return statement will ever be executed in a function.
Ever.
Anything after a executed return statement will never get run.
This can be useful when debugging!

.. code-block:: ipython

    In [14]: def no_error():
       ....:     return u'done'
       ....:     # the following will not be evaluated
       ....:     print(1/0)
       ....:
    In [15]: no_error()
    Out[15]: u'done'

.. slide:: Return Ends Execution
    :level: 3

    No statement after a return statement will be executed.

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [14]: def no_error():
               ....:     return u'done'
               ....:     # the following will not be evaluated
               ....:     print(1/0)
               ....:
            In [15]: no_error()
            Out[15]: u'done'


However, functions *can* return multiple results.
To do so, you put each result to return in the return statement, separated by commas:

.. code-block:: ipython

    In [16]: def fun():
       ....:     return 1, 2, 3
       ....:
    In [17]: fun()
    Out[17]: (1, 2, 3)

In combination with multiple assignment, this can be very useful:

.. code-block:: ipython

    In [18]: x,y,z = fun()
    In [19]: x
    Out[19]: 1
    In [20]: y
    Out[20]: 2
    In [21]: z
    Out[21]: 3

.. slide:: Returning Multiple Values
    :level: 3

    You can provide multiple return values in a function

    .. rst-class:: build
    .. container::

        Separate each value with a comma in a single return statement:

        .. code-block:: ipython

            In [16]: def fun():
               ....:     return 1, 2, 3
               ....:
            In [17]: fun()
            Out[17]: (1, 2, 3)

        Used with multiple assignment, this is powerful:

        .. code-block:: ipython

            In [18]: x,y,z = fun()
            In [19]: x
            Out[19]: 1
            In [20]: y
            Out[20]: 2
            In [21]: z
            Out[21]: 3


Parameters and Arguments
************************

In a ``def`` statement, the names written *inside* the parens are called **parameters**.

.. code-block:: ipython

    In [22]: def fun(x, y, z):
       ....:     q = x + y + z
       ....:     print(x, y, z, q)
       ....:

Parameters become *symbols* in the context of the function.
You can evaluate them, use them in statements, perform operations on them.
In this example, the symbols ``x``, ``y`` and ``z`` (as well as ``q``) are *local*.
They are bound only within the *scope* of the function.
They do not exist outside the function.

When you call a function, you pass values to the function as **arguments**:

.. code-block:: ipython

    In [23]: fun(3, 4, 5)
    3 4 5 12

Each value is *bound* to a *parameter* symbol inside the function and used.



.. slide:: Parameters and Arguments
    :level: 3

    Names in the parens in a ``def`` statement are *parameters*

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [22]: def fun(x, y, z):
               ....:     q = x + y + z
               ....:     print(x, y, z, q)
               ....:

        These names are available in the function

        They are *local* to the function

        They are not available outside the function

        *Arguments* passed when you call a function are bound to the parameters and used:

        .. code-block:: ipython

            In [23]: fun(3, 4, 5)
            3 4 5 12

Saving Your Code
================

Working in the Python interpreter (or in iPython) is a great way to learn the basic syntax of Python interactively.
But in order to do your homework for tonight, you'll need to be able to save your code.
For this, we need to talk briefly about python modules.
We'll cover just enough to get you going, and return for more tomorrow.

In Python, to a first approximation, a ``module`` is a text file that contains python code and ends with the file extension ``.py``
You write statements and expressions in this file, and then you can run the file to execute those statements and expressions.

Let's try this out.

A Simple Module
---------------

Quit iPython and create a new file in your current working directory.
Call it ``my_first_module.py``.

.. code-block:: bash

    (day1)$ touch my_first_module.py

.. slide:: Saving Code
    :level: 3

    Save your code in Python ``modules`` in order to preserve it.

    .. rst-class:: build
    .. container::

        A ``module`` is, roughly, any file that ends in ``.py``

        Create a new file named ``my_first_module.py``:

        .. code-block:: bash

            (day1)$ touch my_first_module.py

Now, open the file in your text editor and add the following code:

.. code-block:: python

    from __future__ import print_function


    def message():
        message = u'This is a message from my first Python module'
        return message


    print(message())

.. slide:: ``my_first_module.py``
    :level: 3

    Open this new file in your text editor

    .. rst-class:: build
    .. container::

        Add the following Python code:

        .. code-block:: python

            from __future__ import print_function


            def message():
                message = u'This is a message from my first Python module'
                return message


            print(message())

        Save the file

Save the changes you've made to this file.
This is now a very simple Python module.
The next step is to run the file.

The first way we should learn is to execute the file using Python itself.
We can do that from the command line, like so:

.. code-block:: bash

    (day1)$ python my_first_module.py
    This is a message from my first Python module

Notice that the final line of the file executed, and that we can see the results because it printed something.
When we ran that file, each line of code in the file was evaluated, starting at the top.
We can accomplish the same thing from inside iPython.
Start it back up:

.. code-block:: bash

    (day1)$ ipython
    Python 3.5.1 (default, Jan 18 2016, 14:50:30)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.1.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

.. code-block:: ipython

    In [1]: run my_first_module.py
    This is a message from my first Python module

    In [2]:

.. slide:: Running a Module
    :level: 3

    You can run this new file from the command line:

    .. rst-class:: build
    .. container::

        .. code-block:: bash

            (day1)$ python my_first_module.py
            This is a message from my first Python module

        You can also run it in iPython:

        .. code-block:: ipython

            In [1]: run my_first_module.py
            This is a message from my first Python module

Now, back in your editor make the following change to ``my_first_module.py``:

.. code-block:: python

    # update the last line:
    print(message(), u'plus a bit more')

Then, try running the code again in your iPython session

.. code-block:: ipython

    In [2]: run my_first_module.py
    This is a message from my first Python module plus a bit more

Notice that when you *run* code in iPython, changes to the original are automatically picked up.
Also notice that the ``message`` function you created is now available to be used iPython.
This will be useful as you work on your homework tonight.
You can learn a lot more by reading the iPython documentation for `the run magic`_.

.. _the run magic: https://ipython.org/ipython-doc/3/interactive/magics.html#magic-run

.. slide:: ``%run`` in iPython
    :level: 3

    Update your module like so:

    .. rst-class:: build
    .. container::

        .. code-block:: python

            # update the last line:
            print(message(), u'plus a bit more')

        When you run it again in iPython the changes are shown:

        .. code-block:: ipython

            In [2]: run my_first_module.py
            This is a message from my first Python module plus a bit more

        And you can call the ``message`` function in iPython:

        .. code-block:: ipython

            In [5]: message()
            Out[5]: 'This is a message from my first Python module'

        Read the documentation for the iPython ``run`` magic for more.
