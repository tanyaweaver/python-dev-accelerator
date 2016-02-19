.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 2
******************************

.. slide:: Introduction To Python: Part 2
    :level: 1

    .. rst-class:: center

    In which we meet with some basic language constructs.

In this lecture we'll get to know more about some of the core constructs of Python programming:

* Functions
* Conditionals and Booleans
* Simple Looping and Containers
* Modules and Packages

.. slide:: Quick Review
    :level: 2

    .. rst-class:: left
    .. container::

        Let's discuss questions from the previous lecture:

        .. rst-class:: build

            * Values and Types
            * Expressions and Statements
            * Blocks
            * Introduction to Functions
            * REPL, iPython, ``help``, and ``dir``

.. slide:: Today's Topics
    :level: 2

    .. rst-class:: left build

        * More About Functions
        * Booleans and Conditionals
        * Containers and Looping
        * Modules and Packages

Functions
=========

Previously, you've been introduced to writing simple functions.
You've learned about the :keyword:`def <python2:def>` (:py:keyword:`py3 <def>`) statement.
You've learned about specifying parameters when defining a function.
And about passing arguments when you call a function.
And you've learned that in a simple function like the one below, the symbols ``x``, ``y``, and ``z`` are *local* names.

.. code-block:: python

    def fun(x, y):
        z = x + y
        return z

.. slide:: Function Review
    :level: 2

    .. rst-class:: left
    .. container::

        .. code-block:: python

            def fun(x, y):
                z = x + y
                return z

        You've learned about:

        .. rst-class:: build

            * the ``def`` statement
            * specifying parameters
            * passing arguments
            * *local* names (``x``, ``y``, and ``z``)

But what does *local* really mean in Python?

Local vs. Global
----------------

Symbols bound in Python have a *scope*.
That *scope* determines where a symbol is visible, or what value it has in a given block.
Consider this example code (try it out in your own interpreter):

.. code-block:: ipython

    In [14]: x = 32
    In [15]: y = 33
    In [16]: z = 34
    In [17]: def fun(y, z):
       ....:     print(x, y, z)
       ....:
    In [18]: fun(3, 4)
    32 3 4

.. slide:: Local vs. Global
    :level: 3

    .. rst-class:: build

    * Symbols have *scope*
    * Scope determines visibility
    * Scope determines value

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [14]: x = 32
            In [15]: y = 33
            In [16]: z = 34
            In [17]: def fun(y, z):
               ....:     print(x, y, z)
               ....:

        .. container::

            What will happen?

            .. code-block:: ipython

                In [18]: fun(3, 4)

Notice that the value printed for x comes from *outside* the function, even though the symbol is used *inside* the function.
This is a *global* name.
Conversely, even though there are a ``y`` and ``z`` defined *globally*, the value used for them is *local* to the function.
But did that change the value of ``y`` and ``z`` in the *global* scope?

But, did the value of y and z change in the *global* scope?

.. code-block:: ipython

    In [19]: y
    Out[19]: 33

    In [20]: z
    Out[20]: 34

Names in *local* scope **mask** names bound in the *global* scope.
They are really different names in a different place.
Binding different values to them does not change the binding of the name in the global scope.

.. slide:: Local vs. Global
    :level: 3

    .. code-block:: ipython

        In [18]: fun(3, 4)
        32 3 4

    .. rst-class:: build
    .. container::

        What about the values of ``y`` and ``z`` *outside* the function?

        .. code-block:: ipython

            In [19]: y
            Out[19]: 33

            In [20]: z
            Out[20]: 34

        .. rst-class:: build

        * *Global* bindings vs. *Local* bindings
        * different scope
        * different name
        * masking

In Python, you should use global bindings mostly for constants (values that are meant to be used everywhere and are not changed).
It is conventional in Python to designate global constants by typing the symbols we bind to them in ALL_CAPS:

.. code-block:: python

    INSTALLED_APPS = [u'foo', u'bar', u'baz']
    CONFIGURATION_KEY = u'some secret value'
    ...

Again, this is just a convention, but it's a good one to follow.
It helps you to keep straight what symbols are bound in the global scope.

.. slide:: Python Convention
    :level: 3

    Reserve *global* bindings for **constants**

    .. rst-class:: build
    .. container::

        Symbols should be ALL_CAPS:

        .. code-block:: python

            INSTALLED_APPS = [u'foo', u'bar', u'baz']
            CONFIGURATION_KEY = u'some secret value'

        Helps to prevent confusing *local* and *global*

There's a trap in this interplay of *global* and *local* names.
Take a look at this function definition:

.. code-block:: ipython

    In [21]: x = 3

    In [22]: def f():
       ....:     y = x
       ....:     x = 5
       ....:     print(x)
       ....:     print(y)
       ....:

What is going to happen when we call ``f``?
The Zen of Python tells us "In the face of ambiguity, refuse the temptation to guess."
So try it out and see:

.. code-block:: ipython

    In [23]: f()
    ---------------------------------------------------------------------------
    UnboundLocalError                         Traceback (most recent call last)
    <ipython-input-23-0ec059b9bfe1> in <module>()
    ----> 1 f()

    <ipython-input-22-9225fa53a20a> in f()
          1 def f():
    ----> 2     y = x
          3     x = 5
          4     print(x)
          5     print(y)

    UnboundLocalError: local variable 'x' referenced before assignment

The symbol ``x`` is *going to be* bound locally.
Because of this it becomes a local name and masks the fact that a global name with a bound value already exists.
This causes the ``UnboundLocalError``.

This is another example of why it's a good idea to keep your global names as ALL_CAPS.
It makes it easier to avoid this type of mistake.

.. slide:: The "UnboundLocal" Trap
    :level: 3

    .. code-block:: ipython

        In [21]: x = 3
        In [22]: def f():
           ....:     y = x
           ....:     x = 5
           ....:     print(x)
           ....:     print(y)
           ....:

    .. rst-class:: build
    .. container::

        What happens when we call ``f``:

        .. code-block:: ipython

            In [23]: f()

        .. code-block:: ipython

            UnboundLocalError: local variable 'x' referenced before assignment

        Why?


Parameters
----------

So far we've seen simple parameter lists:

.. code-block:: python

    def fun(x, y, z):
        print(x, y, z)

These types of parameters are called *positional*.
When you call a function, you **must** provide arguments for all *positional* parameters *in the order they are listed*.

You can provide *default values* for parameters in a function definition.
When parameters are given with default values, they become *optional*.

.. code-block:: ipython

    In [24]: def fun(x=1, y=2, z=3):
       ....:     print(x, y, z)
       ....:

    In [25]: fun()
    1 2 3

.. slide:: Parameters
    :level: 3

    You have seen simple parameter lists:

    .. rst-class:: build
    .. container::

        .. code-block:: python

            def fun(x, y, z):
                print(x, y, z)

        These params are *positional* and *required*

        .. container::

            Default values are allowed:

            .. code-block:: ipython

                In [24]: def fun(x=1, y=2, z=3):
                   ....:     print(x, y, z)
                   ....:

        .. container::

            Params with defaults are *optional*:

            .. code-block:: ipython

                In [25]: fun()
                1 2 3

When you have *optional* parameters, you can still provide arguments to a function call positionally.
But you have to start with the first one.
You can also use the parameter name as a *keyword* to indicate which you mean.
This is called a *keyword argument* to set them apart from just-plain *arguments*

.. code-block:: ipython

    In [26]: fun(6)
    6 2 3
    In [27]: fun(6, 7)
    6 7 3
    In [28]: fun(6, 7, 8)
    6 7 8

    In [29]: fun(y=4, x=1)
    1 4 3

Once you've provided a *keyword* argument to a function call, you can no longer provide any *positional* arguments:

.. code-block:: ipython

    In [30]: fun(x=5, 6)
      File "<ipython-input-30-4529e5befb95>", line 1
        fun(x=5, 6)
    SyntaxError: non-keyword arg after keyword arg

.. slide:: Using Keywords
    :level: 3

    Optional parameters may be provided as *positional arguments*:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [26]: fun(6)
            6 2 3
            In [27]: fun(6, 7)
            6 7 3

        Use parameter names as *keyword arguments* to skip around:

        .. code-block:: ipython

            In [29]: fun(y=4, x=1)
            1 4 3

        Arguments must come before keyword arguments:

        .. code-block:: ipython

            In [30]: fun(x=5, 6)
              File "<ipython-input-30-4529e5befb95>", line 1
                fun(x=5, 6)
            SyntaxError: non-keyword arg after keyword arg

You do not have to use only one style or the other when writing functions.
You can use both *positional* and *optional* parameters.
But any *positional* parameters **must** come before any *optional* parameters.

.. code-block:: python

    def mixed(a, b, c='maybe'):
        print(a, b, c)

This brings us to a fun feature of Python function definitions.
You can define a parameter list that requires an **unspecified** number of *positional* or *optional* parameters.
The key is the ``*`` (splat) or ``**`` (double-splat) operator:

.. code-block:: ipython

    In [31]: def fun(*args, **kwargs):
       ....:     print(args, kwargs)
       ....:
    In [32]: fun(1)
    (1,) {}
    In [33]: fun(1, 2, zombies=u"brains")
    (1, 2) {'zombies': u'brains'}
    In [34]: fun(1, 2, 3, zombies=u"brains", vampires=u"blood")
    (1, 2, 3) {'vampires': u'blood', 'zombies': u'brains'}

By convention, use **args** and **kwargs** for this style of parameters.


.. slide:: Args and Kwargs
    :level: 3

    Functions may use both types of parameters:

    .. rst-class:: build
    .. container::

        .. code-block:: python

            def mixed(a, b, c='maybe'):
                print(a, b, c)

        ``*`` and ``**`` pack multiple positional or optional arguments:

        .. code-block:: ipython

            In [31]: def fun(*args, **kwargs):
               ....:     print(args, kwargs)
               ....:
            In [32]: fun(1)
            (1,) {}
            In [33]: fun(1, 2, zombies=u"brains")
            (1, 2) {'zombies': u'brains'}
            In [34]: fun(1, 2, 3, zombies=u"brains", vampires=u"blood")
            (1, 2, 3) {'vampires': u'blood', 'zombies': u'brains'}

        Arbitrary parameter lists!!!

Documentation
-------------

It's often helpful to leave information in your code about what you were thinking when you wrote it.
This can help reduce the number of `WTFs per minute <http://www.osnews.com/story/19266/WTFs_m>`_ in reading it later.
In Python, we have two approaches to this, *comments* and *docstrings*.

Comments
********

Comments go inline in the body of your code, to explain reasoning:

.. code-block:: python

    if (frobnaglers > whozits):
        # borangas are shermed to ensure frobnagler population
        # does not grow out of control
        sherm_the_boranga()

You can use them to mark places you want to revisit later:

.. code-block:: python

    for partygoer in partygoers:
        for balloon in balloons:
            for cupcake in cupcakes:
                # TODO: Reduce time complexity here.  It's killing us
                #  for large parties.
                resolve_party_favor(partygoer, balloon, cupcake)

Be judicious in your use of comments.
Use them only when you need to.
And make sure that the comments you leave are useful.
This is not useful:

.. code-block:: python

    for sponge in sponges:
        # apply soap to each sponge
        worker.apply_soap(sponge)

Remember also that every comment you add is as much a maintenance burden as a line of code.
Comments that are out-of-date are misleading at best, and dangerous at worst.
You have to update them as your code changes to prevent them becoming hazards to your work.

.. slide:: Comments
    :level: 3

    Use comments to clarify intent or usage:

    .. code-block:: python

        if (frobnaglers > whozits):
            # sherm borangas to control frobnagler population
            sherm_the_boranga()

    .. rst-class:: build
    .. container::

        .. container::

            Or to mark places to return to in the future:

            .. code-block:: python

                # TODO: Reduce time complexity here.  It's killing us for large parties.
                for partygoer in partygoers:
                    for balloon in balloons:
                        for cupcake in cupcakes:
                            resolve_party_favor(partygoer, balloon, cupcake)
        .. container::

            Make them useful (this is *not*):

            .. code-block:: python

                for sponge in sponges:
                    # apply soap to each sponge
                    worker.apply_soap(sponge)

.. slide:: WARNING
    :level: 3

    .. rst-class:: large center

    Comments are a maintenance burden. Keep them up to date.

Docstrings
**********

In Python, ``docstrings`` are used to provide in-line documentation in a number of places.

The first place we will see is in the definition of ``functions``.
To define a function you use the ``def`` keyword.
If a ``string literal`` is the first thing in the function block following the header, it is a ``docstring``:

.. code-block:: python

    def complex_function(arg1, arg2, kwarg1=u'bannana'):
        """Return a value resulting from a complex calculation."""
        # code block here

You can then read this in an interpreter as the ``__doc__`` attribute of the function object.
It will also be used by the interpreter help system.

.. code-block:: ipython

    In [2]: complex_function.__doc__
    Out[2]: 'Return a value resulting from a complex calculation.'
    In [3]: complex_function?
    Signature: complex_function(arg1, arg2, kwarg1='bannana')
    Docstring: Return a value resulting from a complex calculation.
    File:      ~/projects/training/codefellows/existing_course_repos/python-dev-accelerator/<ipython-input-1-1def4182e947>
    Type:      function


A ``docstring`` should be a complete sentence in the form of a command describing what the function does:

    """Return a list of values based on blah blah""" is a good docstring.
    """Returns a list of values based on blah blah""" is *not*.

A good ``docstring`` fits onto a single line.
If more description is needed, make the first line a complete sentence and add more lines below for enhancement.

Docstrings should always be enclosed with triple-quotes.
This allows you to expand them more easily in the future if required.
You should always close the string on the same line if the docstring is only one line.

Python has :pep:`a styleguide <0257>` for creating docstrings.
You should read it and get familiar.
Well-formed ``docstrings`` are good evidence of your commitment to your code.

But as with inline comments, please remember that docstrings are a maintenance burden.
Always keep your own docstrings up to date as you make changes.
And remember that contributing to documentation is a great way to help out an Open Source library.

.. slide:: Docstrings
    :level: 3

    A docstring is a *string literal*.

    .. rst-class:: build
    .. container::

        Must be the first line in a function block.

        Is set as the ``__doc__`` attribute of the function object.

        Will be used by the interpreter help system:

        .. code-block:: ipython

            In [2]: complex_function.__doc__
            Out[2]: 'Return a value resulting from a complex calculation.'
            In [3]: complex_function?
            Signature: complex_function(arg1, arg2, kwarg1='bannana')
            Docstring: Return a value resulting from a complex calculation.
            ...

        Can also be used by documentation builders

.. slide:: Docstring Style
    :level: 3

    One line if possible

    .. rst-class:: build
    .. container::

        Keep it in the form of a command or direct action::

            """Return value based on matrix multiplication of inputs"""
            not
            """This function returns a value based on..."""

        You can add extra information in additional lines

        Always use triple-quotes.

        Use the pep257 Docstring Style Guide.

        **Keep them up to date**

Recursion
---------

You've seen functions that call other functions.
A function can also call *itself*.
We call that **recursion**.

Like with other functions, a call within a call establishes a *call stack*.
With recursion, if you are not careful, this stack can get *very* deep.
Python has a maximum limit to how much it can recurse. This is intended to save your machine from running out of RAM.

Recursion is especially useful for a particular set of problems.
For example, take the case of the *factorial* function.
In mathematics, the *factorial* of an integer is the result of multiplying that integer by every integer smaller than it down to 1.
We can use a recursive function nicely to model this mathematical function::

    5! == 5 * 4 * 3 * 2 * 1

Try writing this function in Python yourself!

.. hidden-code-block:: python
    :label: Peek At A Solution

    def factorial(n):
        if n == 1:
            return n
        return n * factorial(n - 1)

.. slide:: Recursion
    :level: 3

    Functions can call other functions.

    .. rst-class:: build
    .. container::

        They can also call themselves

        This also creates a *call stack*

        Python limits the maximum depth for recursion.

        You can change the limit (but be careful).

.. slide:: Recursion Example
    :level: 3

    Recursion is good for a particular kind of problem.

    .. rst-class:: build
    .. container::

        Once example is the *factorial* function::

            5! == 5 * 4 * 3 * 2 * 1

        Let's try writing a recursive solution to this problem here

        [demo]
















Conditionals and Booleans
=========================

Making decisions in programming is quite important.
We call the language constructs that support decision making *conditionals*.
Conditionals depend on *boolean logic* (logic based on ``True`` and ``False``).
Let's learn more about how Python handles conditionals and booleans.

Conditionals
------------

Python supports conditionals through the :keyword:`if <python2:if>` (:py:keyword:`py3 <if>`) statement.
It looks an awful lot like ``if`` in other languages::

    if <expression>:
        <do truthy things>

And like in other languages, there is support for an :keyword:`else <python2:else>` (:py:keyword:`py3 <else>`) clause.
This is executed when the ``<expression>`` is falsy::

    if <expression>:
        <do truthy things>
    else:
        <do falsy things>

Python also supports multiple test expressions through the use of the :keyword:`elif <python2:elif>` (:py:keyword:`py3 <elif>`) clause.
You may have as many alternate tests as you wish.
They are evaluated in order from the top to the bottom.
The block of code contained under the first one that matches is executed and all other clauses are ignored.

::

    if <expression1>:
        <do truthy things>
    elif <expression2>:
        <do other truthy things>
    else:
        <do falsy things>

.. slide:: Conditionals
    :level: 3

    Use the ``if`` statement:

    .. code-block:: python

        if a:
            print(u'a is true')

.. slide:: Conditionals
    :level: 3

    Use the ``if`` statement:

    .. code-block:: python

        if a:
            print(u'a is true')
        else:
            print(u'a is false')

.. slide:: Conditionals
    :level: 3

    Use the ``if`` statement:

    .. code-block:: python

        if a:
            print(u'a is true')
        elif b:
            print(u'b is true')
        elif c:
            print(u'c is true')
        else:
            print(u'is there no truth in the world?')

Make certain you understand the difference between these two programs:

.. code-block:: python

    if a:
        print(u'a')
    elif b:
        print(u'b')

.. code-block:: python

    if a:
        print(u'a')
    if b:
        print(u'b')

Notice that the test expression can be any valid Python expression.
Remember, evaluating an expression always results in a value.
Since all Python values have a boolean value, any valid expression will work.

Also notice that the test expression does not need to be contained in parentheses.
This is quite different from most other languages.
Only use parentheses in test expressions if you are trying to defeat standard operator precedence.

.. slide:: Conditional Details
    :level: 3

    Make sure you understand the difference:

    .. rst-class:: build
    .. container::

        .. code-block:: python

            if a:
                print(u'a')
            elif b:
                print(u'b')
            # versus
            if a:
                print(u'a')
            if b:
                print(u'b')

        Any valid Python expression can be used as a test

        You don't need to put the test in parentheses

        Python has **No Switch Construct**

Switch
******

Many languages (JavaScript among them) have a ``switch`` construct.

.. code-block:: js

    switch (expr) {
      case "Oranges":
        document.write("Oranges are $0.59 a pound.<br>");
        break;
      case "Apples":
        document.write("Apples are $0.32 a pound.<br>");
        break;
      case "Mangoes":
      case "Papayas":
        document.write("Mangoes and papayas are $2.79 a pound.<br>");
        break;
      default:
        document.write("Sorry, we are out of " + expr + ".<br>");
    }

This form is **not present in Python**.
Instead, you are encouraged to use the ``if...elif...else`` conditional construction.
Another option is to use a dictionary (more on what that means in our next lesson).

So we can make decisions using ``if``, depending on whether the test statement is true or False.
But what does it mean to be true or false in Python?

Booleans
--------

In Python, there are two boolean objects: ``True`` and ``False``.
Each is an *object literal*, that is to say, simply writing them as-is evaluates to the object itself.

In the abstract sense, though, the concept of truthiness in Python comes down to the question of "Something or Nothing".
If a value is nothing then it is **falsy**, otherwise it is **truthy**.

In a more concrete sense, this is a list of all the things in Python that count as **falsy**:

* the ``None`` type object
* the ``False`` boolean object
* **Nothing:**

    * zero of any numeric type: ``0, 0L, 0.0, 0j``.
    * any empty sequence, for example, ``"", (), []``.
    * any empty mapping, for example, ``{}`` .
    * instances of user-defined classes, if the class defines a ``__nonzero__()``
      or ``__len__()`` method, when that method returns the integer zero or bool
      value ``False``.

You can read more in the `python docs <http://docs.python.org/library/stdtypes.html>`_.

Everything else is *truthy*

.. slide:: Booleans
    :level: 3

    ``True`` and ``False`` object literals

    .. rst-class:: build
    .. container::

        "Something or Nothing"

        Falsy things:

        .. rst-class:: build

            * the ``None`` type object
            * the ``False`` boolean object
            * zero of any numeric type: ``0, 0L, 0.0, 0j``.
            * any empty sequence, for example, ``"", (), []``.
            * any empty mapping, for example, ``{}`` .
            * Class instance with a ``__nonzero__()`` or ``__len__()`` method that returns the integer zero or ``False``.

        Truthy things:

        **Everything Else**

Any object in Python, when passed to the ``bool()`` type object, will evaluate to ``True`` or ``False``.
But you rarely need to use this feature yourself.
When you use the :keyword:`if <python2:if>` (:py:keyword:`py3 <if>`) statement, it automatically reads the boolean value of its test expression.
Which means that these forms are redundant, and not Pythonic:

.. code-block:: python

    # bad
    if xx is True:
        do_something()
    # worse
    if xx == True:
        do_something()
    # truly terrible:
    if bool(xx) == True:
        do_something()

Instead, you should use what Python gives you:

.. code-block:: python

    if xx:
        do_something()


.. slide:: Pythonic ``if``
    :level: 3

    The ``if`` statement checks boolean value automatically

    .. rst-class:: build
    .. container::

        These are not Pythonic:

        .. code-block:: python

            # bad
            if xx is True:
                do_something()
            # worse
            if xx == True:
                do_something()
            # truly terrible:
            if bool(xx) == True:
                do_something()

        This is:

        .. code-block:: python

            if xx:
                do_something()

Boolean Operators
*****************

Boolean operators allow us to combine and alter boolean values in a number of ways.
Python has three boolean operators, :keyword:`and <python2:and>` (:py:keyword:`py3 <and>`), :keyword:`or <python2:or>` (:py:keyword:`py3 <or>`) and :keyword:`not <python2:not>` (:py:keyword:`py3 <not>`).
Both ``and`` and ``or`` are binary operators (require a operand on the left and right of the keyword), and evaluate from left to right.

The ``and`` operator will return the first operand that evaluates to ``False``, or the last operand if none are ``True``

.. code-block:: ipython

    In [35]: 0 and 456
    Out[35]: 0

The ``or`` operator will return the first operand that evaluates to ``True``, or the last operand if none are ``True``

.. code-block:: ipython

    In [36]: 0 or 456
    Out[36]: 456

The ``not`` operator is *unary* operator (takes only one operand on the right) and inverts the boolean value of its operand:

.. code-block:: ipython

    In [39]: not True
    Out[39]: False

    In [40]: not False
    Out[40]: True

.. slide:: Boolean Operators
    :level: 3

    ``and``, binary, returns first False value or last operand

    .. code-block:: ipython

        In [35]: 0 and 456
        Out[35]: 0

    .. rst-class:: build
    .. container::

        .. container::

            ``or``, binary, returns first True value or last operand

            .. code-block:: ipython

                In [36]: 0 or 456
                Out[36]: 456

        .. container::

            ``not``, unary, inverts boolean value:

            .. code-block:: ipython

                In [39]: not True
                Out[39]: False

                In [40]: not False
                Out[40]: True

Shortcutting
************

Because of the return value of statements with these operators, Python allows very concise (and readable) boolean statements:

::

                      if x is false,
    x or y               return y,
                         else return x

                      if x is false,
    x and y              return  x
                         else return y

                      if x is false,
    not x                return True,
                         else return False


Chaining
********

In Python, you can *chain* these boolean operators.
They are evaluated from left to right.
The first value that defines the result is returned.

.. code-block:: python

    a or b or c or d
    a and b and c and d
    a and b or c and not d

.. ifslides::

    .. rst-class:: centered

    (demo)


.. slide:: Shortcutting and Chaining
    :level: 3

    The first deciding operand is returned.

    .. rst-class:: build
    .. container::

        ::

                              if x is false,
            x or y               return y,
                                 else return x

                              if x is false,
            x and y              return  x
                                 else return y

                              if x is false,
            not x                return True,
                                 else return False

        .. container::

            And it allows for chaining boolean operations:

            .. code-block:: python

                a or b or c or d
                a and b and c and d
                a and b or c and not d

Ternary Expressions
*******************

In most programming languages, this is a fairly common idiom:

.. code-block:: python

    if something:
        x = a_value
    else:
        x = another_value

In other languages, this can be compressed with a "ternary operator"::

    result = a > b ? x : y;

In python, the same is accomplished with the :pep:`ternary expression <0308>`:

.. code-block:: python

    y = 5 if x > 2 else 3


.. slide:: Ternary Expressions
    :level: 3

    Common Idiom:

    .. code-block:: python

        if something:
            x = a_value
        else:
            x = another_value

    .. rst-class:: build
    .. container::

        .. container::

            Other languages have a *ternary operator* (``?``)::

                result = a > b ? x : y;

        .. container::

            In python, it's an expression:

            .. code-block:: python

                y = 5 if x > 2 else 3


Boolean Return Values
*********************

Remember that Python objects themselves have boolean values.
Remember too that boolean expressions will always return an object with a boolean value.
Making use of this can lead to some very terse but readable (Pythonic) code:

Consider a function to calculate if you can sleep in (from an exercise at http://codingbat.com).
You can sleep in if it is not a weekday or if you are on vacation.
You could write this function like so:

.. code-block:: python

    def sleep_in(weekday, vacation):
        if weekday == True and vacation == False:
            return False
        else:
            return True

That's a correct solution.
But it's not a particularly Pythonic way of solving the problem.
Here's a better solution:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return not (weekday == True and vacation == False)

But remember that comparing to a boolean is never required in Python.
Here's an even better solution:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return (not weekday) or vacation

.. slide:: Boolean Return Values
    :level: 3

    Pythonic code uses Python-style boolean returns.

    Lets build a function that tells us if we can sleep in (from codingbat).

    You can if it isn't a weekday or you are on vacation.

    [demo]

.. note:: **Pythoon Trivia**: the boolean objects are subclasses of integer, so the following holds:

          .. code-block:: ipython

            In [1]: True == 1
            Out[1]: True
            In [2]: False == 0
            Out[2]: True

          And you can even do math with them (though it's a bit odd to do so):

          .. code-block:: ipython

              In [6]: 3 + True
              Out[6]: 4


Simple Looping and Containers
=============================

In order to do something interesting for homework, we are going to need to touch on looping and containers.
We will visit them more in-depth in a later lesson.
This is just a quick introduction


Lists
-----

A :class:`list <python2:list>` (:py:class:`py3 <list>`) is a container that stores values in order.
It is pretty much like an "array" or "vector" in other languages.
We can construct one using the ``list`` object literal: ``[]``:

.. code-block:: python

    a_list = [2, 3, 5, 9]
    a_list_of_strings = [u'this', u'that', u'the', u'other']
    one, two, three = [1, 2, 3]
    newlist = [one, two, three]

You can place values directly into the list, or symbols.
If you use symbols, the values to which they are bound are actually stored.
This creates another *reference* to the value, in addition to the reference from the symbol.

Tuples
------

The :class:`tuple <python2:tuple>` (:py:class:`py3 <tuple>`) is another container type.
It also stores values in order.
We construct a ``tuple`` using the ``()`` object literal:

.. code-block:: python

    a_tuple = (2, 3, 4, 5)
    a_tuple_of_strings = (u'this', u'that', u'the', u'other')
    one, two, three = (1, 2, 3)
    newlist = (one, two, three)

Like lists, you can place values or symbols into a tuple
Like lists, placing a symbol stores its value and creates a new *reference* to that value.

However, tuples are **not** the same as lists.
The exact difference is a topic for next session.

There are other container types, but these two will do for now.

For Loops
---------

The :keyword:`for <python2:for>` (:py:keyword:`py3 <for>`) statement in Python defines a *for loop*.
The *for loop* is also sometimes called a 'determinate' loop, because it will repeat a determined number of times.
You use a *for loop* when you need to take some action on every item in a container.

.. code-block:: ipython

    In [10]: a_list = [2, 3, 4, 5]

    In [11]: for item in a_list:
       ....:     print(item)
       ....:
    2
    3
    4
    5

As the loop repeats, each item from the container is bound, successively, to the *loop variable*.
Notice that after the loop has finished, the *loop variable* is still *in scope*:

.. code-block:: ipython

    In [12]: item
    Out[12]: 5


Range
-----

The :func:`range <python2:range>` builtin automatically builds a list of numbers.
In :class:`python 3 <range>` it operates differently (more on that in a later lesson).
You can use it when you need to perform some operatin a set number of times.

.. code-block:: ipython

    In [12]: range(6)
    Out[12]: [0, 1, 2, 3, 4, 5]

    In [13]: for i in range(6):
       ....:     print(u'*', end=u' ')
       ....:
    * * * * * *

That will be enough to work with for the time being.
Each of these has intricacies we will explore further in later lessons.
For now, let's turn to the issue of the larger organization of our code, and ``Modules`` and ``Packages``.

