*******************************
A Python Miscellany: Decorators
*******************************

.. ifslides::

    .. rst-class:: centered

    In which we meet another odd beasty from the Python zoo

.. ifnotslides::

    In this lesson we will discuss another of the available features of programming in Python.
    We'll be exploring the idea and implementation of "decorators".
    We'll see how this programming pattern can help us to be more flexible in our Python work.

Review of Functions
===================

.. rst-class:: left
.. container::

    **A Short Digression**

    .. ifslides::

        .. rst-class:: build
        .. container::

            Recall functions

            Values come in as parameters

            Values are returned

    .. ifnotslides::

        We've discussed them at length elsewhere, and have been using them for some time.
        But for a moment, cast your mind back to the basics of *functions*.
        They allow us to encapsulate some functionality.
        We can pass in values in the form of *parameters*.
        And we can return values from them after their operation is complete.

    .. code-block:: ipython

        In [1]: def multiply(x, y):
           ...:     return x * y
           ...:

        In [2]: multiply(3, 4)
        Out[2]: 12

Scope
-----

.. ifnotslides::

    Recall as well that functions have *scope*.
    The names they bind inside themselves are separate from names bound outside.
    We can see these *namespaces* in action using the `locals` and `globals` builtins:

.. ifslides::

    .. rst-class:: build
    .. container::

        Functions have *scope*

        Different namespaces inside and outside

        `locals` and `globals` expose these namespaces:

.. code-block:: ipython

    In [3]: x = "a value"
    In [4]: y = "another value"
    In [5]: def fun(x):
       ...:     x = "an internal value"
       ...:     print(locals())
       ...:
    In [6]: print(globals())
    {'x': 'a value', 'y': 'another value'}
    In [7]: fun(x)
    {'x': 'an internal value'}

.. nextslide::

.. ifnotslides::

    Still, just because there is a local namespace does not mean that we cannot access global values inside a function.
    Python looks *first* in the local function namespace.
    But if a name is not found there, it will move to the global namespace to find it:

.. ifslides::

    .. rst-class:: build
    .. container::

        Can still access *global* values

        Names are looked up locally *first*

        Then Python moves to the global namespace:

.. code-block:: ipython

    In [12]: global_val = "a global value"
    In [13]: def fun():
       ....:     print(global_val)
       ....:
    In [14]: fun()
    a global value

.. nextslide::

.. ifnotslides::

    However, it is the case that Python protects us from changing global values from inside a function.
    If we try to rebind a global name *inside* a scope, then the name becomes local.
    Note that this is different from *mutating* a global value (which is not prevented).

.. ifslides::

    .. rst-class:: build
    .. container::

        Can't rebind global names *inside* a function

        Names become *local* when bound

        This is different from *mutating* global values

.. code-block:: ipython

    In [15]: a_string = "I am outside"
    In [16]: def fun():
       ....:     a_string = "I am inside"
       ....:     print(locals())
       ....:
    In [17]: fun()
    {'a_string': 'I am inside'}
    In [18]: print(a_string)
    I am outside


Variable Lifetime
-----------------

.. ifnotslides::

    Remember also that scoping means that variables inside a function have a *lifetime*.
    They exist when the function is executed.
    But when it exits, they are gone.
    They *only exist for the duration of the function call*:

.. ifslides::

    .. rst-class:: build
    .. container::

        Scope also means *lifespan*

        Local names exist while functions execute

        They are gone when functions return:

.. code-block:: ipython

    In [24]: def fun():
       ....:     z = 5
       ....:     print(z)
       ....:
    In [25]: fun()
    5
    In [26]: z
    ...
    NameError: name 'z' is not defined


.. nextslide::

.. ifnotslides::

    And we also understand that parameters, when passed to our functions as arguments, become *locally bound names*.
    They are bound inside the function scope to the value of the arguments passed:

.. ifslides::

    .. rst-class:: build
    .. container::

        Parameters can be named in functon defs

        Values are passed as *arguments* to function calls

        The values are bound to parameter names *locally*:

.. code-block:: ipython

    In [27]: def fun(x, y=0):
       ....:     return x - y
       ....:
    In [28]: fun(3, 1)
    Out[28]: 2
    In [29]: fun(x=5, y=2)
    Out[29]: 3
    In [30]: fun(y=1, x=3)
    Out[30]: 2
    In [31]: fun(3)
    Out[31]: 3

.. nextslide::

.. ifnotslides::

    Python even allows function to be defined inside local scopes.
    You can define a function inside another function.
    And the name of the function is locally scoped just like any other name:

.. ifslides::

    .. rst-class:: build
    .. container::

        Functions can be defined in local scopes

        The can be defined in other functions

        Names are still locally scoped (as are values):

.. code-block:: ipython

    In [32]: def outer():
       ....:     x = 5
       ....:     def inner():
       ....:         print(x)
       ....:     inner()
       ....:
    In [33]: outer()
    5
    In [34]: x
    NameError: name 'x' is not defined
    In [35]: inner
    NameError: name 'inner' is not defined


First Class Objects
===================

.. ifnotslides::

    We've talked a number of times about this.
    What does it mean, though?
    Well, first of all, it means that like any other value in Python, functions are subclasses of `object`:

.. ifslides::

    .. rst-class:: build left
    .. container::

        What does that mean?

        Any value in python is an instance of a subclass of `object`

        Functions are too:

.. rst-class:: left
.. code-block:: ipython

    In [36]: issubclass((42).__class__, object)
    Out[36]: True
    In [37]: def fun():
       ....:     pass
       ....:
    In [38]: issubclass(fun.__class__, object)
    Out[38]: True

Functions as Arguments
----------------------

.. ifnotslides::

    Second, it means that we can pass functions in as arguments to other functions.
    The function object is bound to the parameter name inside the function scope.
    And we can use that passed function inside the function to do work:

.. ifslides::

    .. rst-class:: build
    .. container::

        We can pass functions as arguments

        Function objects are bound to param names

        Can be used via that name:

.. code-block:: ipython

    In [41]: def add(x, y):
       ....:     return x + y
       ....:
    In [42]: def apply(func, a, b):
       ....:     return func(a, b)
       ....:
    In [43]: apply(add, 3, 4)
    Out[43]: 7

Functions as Return Values
--------------------------

.. ifnotslides::

    Finally, it means that we can return functions as the result of calling other functions.
    A function object is bound locally to the name it takes.
    We can reference that name and get the function object.
    This means we can return the value by using the name of the function in the local scope:

.. ifslides::

    Inline function defs are bound to local names

    Those names reference the function object

    We can return that object as a value:

.. code-block:: ipython

    In [44]: def outer():
       ....:     def inner():
       ....:         print("this is the inner function")
       ....:     return inner
       ....:

    In [45]: fun = outer()
    In [46]: fun()
    this is the inner function

Closures
--------

.. ifnotslides::

    This finally brings us to the idea of a *closure*.
    Instead of defining it, let's look at a quick series of examples.

.. ifslides::

    A bit hard to define, so consider:

.. code-block:: ipython

    In [47]: def outer():
       ....:     x = 5
       ....:     def inner():
       ....:         print(x)
       ....:     return inner
       ....:
    In [48]: foo = outer()

.. ifnotslides::

    We understand now what foo is.
    It is the ``inner`` function object that was defined inside ``outer``.
    We also know the rules of Python scoping and variable lifetime.
    The question is, will ``foo`` run, or raise an error?

.. ifslides::

    .. rst-class:: build
    .. container::

        ``foo`` is a function object

        Think about *scope* and *variable lifetime*

        Will ``foo`` run or raise an error?


.. nextslide::

.. code-block:: ipython

    In [49]: foo()
    5

.. ifnotslides::

    Okay, that works.
    Python *remembers* the value that ``x`` was bound to when ``inner`` was defined.
    This allows the function to execute properly, even though it happens outside the scope of ``outer``.
    Let's take it one step farther, and make ``x`` a parameter of ``outer``:

.. ifslides::

    Python bakes the value of ``x`` into the definition of ``inner``

    What if ``x`` is a parameter passed to ``outer``:

.. code-block:: ipython

    In [50]: def outer(x):
       ....:     def inner():
       ....:         print(x)
       ....:     return inner
       ....:
    In [51]: foo1 = outer(1)
    In [52]: foo2 = outer(2)
    In [53]: foo1()
    1
    In [54]: foo2()
    2

.. nextslide::

.. ifnotslides::

    This pattern can be pretty powerful.
    It allows you to create a sort of *factory* that can manufacture functions, each with its own private internal variables.
    You can do alot with this idea alone.
    But what if the value you pass to ``outer`` is a *function*?

.. ifslides::

    This is powerful

    .. rst-class:: build
    .. container::

        Like a factory for custom functions

        Each shares functionality, but also has private internal variables

        You can take this a long way

        But what if the value you pass is a *function*?

Decorator Defined
=================

.. ifnotslides::

    There are many things you can do with a simple pattern like this one.
    So many, that it has been given a special name:

.. ifslides::

    .. rst-class:: left
    .. container::

        A useful pattern arises

        Useful enough for a special name

.. rst-class:: centered mlarge build

**Decorator**

.. ifnotslides::

    ::

       "A decorator is a function that takes a function as an argument and returns a function as a return value."

    That's nice and all, but why is it useful?

.. ifslides::

    .. rst-class:: build left
    .. container::

        "A function that takes a function as an argument and returns a function as a value"

        Nice, but why useful?

An Example
----------

.. ifnotslides::

    Imagine you are trying to debug a module with a number of simple functions like this:

.. ifslides::

    debugging functions like this:

.. code-block:: python

    def add(a, b):
        return a + b

.. ifnotslides::

    You want to see when each function is called.
    You'd like to know what arguments were used and what the result was.
    So you rewrite each function as follows:

.. ifslides::

    .. rst-class:: build
    .. container::

        When were functions called?

        What were the arguments?

        What was the result?

.. rst-class:: build
.. code-block:: python

    def add(a, b):
        print(u"Function 'add' called with args: %r" % locals())
        result = a + b
        print(u"\tResult --> %r" % result)
        return result

.. nextslide::

.. ifnotslides::

    That's not particularly nice, especially if you have lots of functions in your module.
    You rewrite a lot of code.
    And then the code is always logged, even if you don't want it.

    Now imagine we defined the following, more generic *decorator*:

.. ifslides::

    Works, but not so nice

    Lots of code needs rewriting

    Not flexible, always on

    How about a "decorator" version?

.. code-block:: python

    def logged_func(func):
        def logged(*args, **kwargs):
            print(u"Function %r called" % func.__name__)
            if args:
                print(u"\twith args: %r" % args)
            if kwargs:
                print(u"\twith kwargs: %r" % kwargs)
            result = func(*args, **kwargs)
            print(u"\t Result --> %r" % result)
            return result
        return logged

.. nextslide::

.. ifnotslides::

    This version *wraps* a call to the passed *func* relying on *closure* to bake in the reference.
    It then returns the wrapped function *as a new function object*.
    Since we can bind the result of calling this decorator to a new symbol, we can make logging versions of our module functions.
    And when we call them, we'll see the logging in action:

.. ifslides::

    .. rst-class:: build
    .. container::

        Wraps the passed *func* relying on *closures*

        Returns the wrapped function when called

        Bind it to a new symbol and call it to see logging:

.. code-block:: ipython

    In [36]: logging_add = logged_func(add)
    In [37]: logging_add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[37]: 7

.. nextslide::

.. ifnotslides::

    This is nice, but we have to call the new function wherever we originally had the old one.
    We still need to re-write all our code to get the advantage of our logging.
    It would be nicer if we could simply reference the same function name when calling it.
    We remember that we can easily rebind symbols in Python using *assignment*.
    So we can rebind our decorated function to the *same name*, and leave our calls unchanged:

.. ifslides::

    .. rst-class:: build
    .. container::

        Must call new function in place of old

        Still have to rewrite code

        Can rebind *same name* to decorated function object instead

        Call sites remain unchanged

.. code-block:: ipython

    In [39]: def add(a, b):
       ....:     return a + b
       ....:
    In [40]: add = logged_func(add)
    In [41]: add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[41]: 7

Python Syntax
-------------

.. ifnotslides::

    Rebinding the name of a function to the result of calling a decorator on that function is called **decoration**.
    This operation is so common, Python provides a special operator to do it *declaratively*: the ``@`` operator:

.. ifslides::

    .. rst-class:: build
    .. container::

        Rebind function name to a decorated version of the function

        This is called *decoration*

        It's common enough to get its own declarative operator: ``@``:

.. code-block:: python

    # this is the imperative version:
    def add(a, b):
        return a + b
    add = logged_func(add)

    # and this declarative form is exactly equal:
    @logged_func
    def add(a, b):
        return a + b

.. ifnotslides::

    The declarative form (called a decorator expression) is far more common.
    However, both have the identical result, and can be used interchangeably.

Callables
=========

.. ifnotslides::

    Our original definition of a *decorator* was nice and simple, but a tiny bit incomplete.
    In reality, decorators can be used with anything that is *callable*.
    In python a *callable* is a function, a method of a class, or even a class that implements the ``__call__`` special method.

    So in fact the definition should be updated as follows:

    .. rst-class:: centered

         "A decorator is a callable that takes a callable as an argument and returns a callable as a return value."

.. ifslides::

    .. rst-class:: left
    .. container::

        Originally defined a *decorator* as a *function*

        .. rst-class:: build
        .. container::

            Incomplete, is really a *callable*

            .. rst-class:: build

            * Function
            * Method of a class
            * Class with a ``__call__`` special method

            Update our definition:

            .. rst-class:: centered

                 "A decorator is a callable that takes a callable as an argument and returns a callable as a return value."

Decorator Class
---------------

.. ifnotslides::

    One use of a *callable class* as a decorator takes advantage of encapsulation.
    We can rely on an instance of the class keeping a "private" store of saved values.
    This allows us to *memoize* the results of some expensive function:

.. ifslides::

    A *callable class* allows us to *encapsulate* results

    Store values locally to a class instance

    Return stored values when called:

.. code-block:: python

    class Memoize:
        """Provide a decorator class that caches expensive function results

        from avinash.vora http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
        """
        def __init__(self, function):  # runs when memoize class is called
            self.function = function
            self.memoized = {}

        def __call__(self, *args):  # runs when memoize instance is called
            if args not in self.memoized:
                self.memoized = self.function(*args)
            return self.memoized[args]

.. nextslide::

Let's try that out with a potentially expensive function:

.. code-block:: ipython

    In [56]: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in range(n))
       ....:

    In [57]: sum2x(10000000)
    Out[57]: 99999990000000

    In [58]: sum2x(10000000)
    Out[58]: 99999990000000

Nested Decorators
-----------------

.. ifnotslides::

    It's nice to see that in action, but what if we want to know *exactly* how much difference it made?
    What if we want to calculate the timing of running the function repeatedly?
    How do we do that?

    We can stack decorator expressions.
    The result is like calling each decorator in order, from bottom to top:

.. ifslides::

    How much difference did that make, exactly?

    .. rst-class:: build
    .. container::

        It would be nice to *time* our memoized function

        We can stack decorators

        They are executed in order from nearest to farthest from decorated function:

.. code-block:: python

    @decorator_two
    @decorator_one
    def func(x):
        pass

    # is exactly equal to:
    def func(x):
        pass
    func = decorator_two(decorator_one(func))

.. nextslide::

Let's define another decorator that will time how long a given call takes:

.. code-block:: python

    import time
    def timed_func(func):
        def timed(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(u"time expired: %s" % elapsed)
            return result
        return timed

.. nextslide::

And now we can use this new decorator stacked along with our memoizing
decorator:

.. code-block:: ipython

    In [71]: @timed_func
       ....: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in xrange(n))
    In [72]: sum2x(10000000)
    time expired: 0.997071027756
    Out[72]: 99999990000000
    In [73]: sum2x(10000000)
    time expired: 4.05311584473e-06
    Out[73]: 99999990000000

Wrap Up
=======

.. ifnotslides::

    In this lecture, we've learned about decorators.
    We reminded ourselves first about some basics of how functions work.
    We reviewed the idea of *scope* and saw how it allows us to refer to values from inside nested scopes.
    We reminded ourselves that functions are in fact first-class objects.
    This helped us to see that we can pass functions into other functions as arguments, return them as values, and even define them inline in other functions.
    We then noted that defining a function inline allowed us to create a *closure* that baked runtime values into our function definitions.

    Putting this all together allows us to understand how a **decorator** works.
    We write a function that takes a function as an argument.
    We define a new function *inline* inside that function, using *closure* to bake our passed function into it.
    Then we return the newly defined function in place.

    Because this approach is so useful, we learned that Python supports a *declarative* operator for it: ``@``.
    And using that syntax we learned how to define both class-based and function based decorators that can memoize and time the operation of complex, expensive operations.

.. ifslides::

    .. rst-class:: left build
    .. container::
    
        Functions take args and return values

        Functions have *scope*

        Functions are *first-class objects*

        Functions have *closure* so we can bake values into them at runtime

        *Decorators* that take a function, return a new function, the passed function is baked in.

        Decorators can be *any callable*

        Decorators can be stacked to combine them.

