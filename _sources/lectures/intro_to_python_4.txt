.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 4
******************************

.. slide:: Introduction To Python: Part 4
    :level: 1

    .. rst-class:: center

    In which we learn a few more data types and some Python quirks.

Today we'll be clearing up the differences between lists and tuples.
This will lead us to a discussion of the concept of mutability in Python.
The differences between mutable and immutable data types are important to understanding

Lists and  Tuples
=================

The *other* sequence types.

.. slide:: Lists and Tuples
    :level: 2

    The *other* sequence types

Lists
-----

We've see the :ref:`list <python2:typesseq>` (:py:class:`py3 <list>`) before.
And we know that we can construct them using the list object literal: ``[]``.

.. code-block:: ipython

    In [1]: []
    Out[1]: []
    In [2]: [1,2,3]
    Out[2]: [1, 2, 3]
    In [3]: [1, 'a', 7.34]
    Out[3]: [1, 'a', 7.34]

We can also call the ``list`` type object.
It can accept an optional argument which is any sequence type:

.. code-block:: ipython

    In [6]: list()
    Out[6]: []
    In [7]: list(range(4))
    Out[7]: [0, 1, 2, 3]
    In [8]: list('abc')
    Out[8]: ['a', 'b', 'c']

.. slide:: Lists
    :level: 3

    We've seen construction with list literals (``[]``):

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [1]: []
            Out[1]: []
            In [2]: [1,2,3]
            Out[2]: [1, 2, 3]
            In [3]: [1, 'a', 7.34]
            Out[3]: [1, 'a', 7.34]

        We can also call the ``list`` type object:

        .. code-block:: ipython

            In [6]: list()
            Out[6]: []
            In [7]: list(range(4))
            Out[7]: [0, 1, 2, 3]
            In [8]: list('abc')
            Out[8]: ['a', 'b', 'c']

A list is a *heterogenous*, *ordered* collection.
This means it can contain values of different types.
Each element in a list is a value.
Even if you add a name to a list, it is the value the name is bound to that is actually stored.
And like all values, the values in a list can have none, one, or more than one name bound to them.
When you store a value in a list, it creates a reference to that value.

.. code-block:: ipython

    In [9]: name = u'Brian'
    In [10]: a = [1, 2, name]
    In [11]: b = [3, 4, name]
    In [12]: a[2]
    Out[12]: u'Brian'
    In [13]: b[2]
    Out[13]: u'Brian'
    In [14]: a[2] is b[2]
    Out[14]: True

.. slide:: List Elements
    :level: 3

    Lists are *heterogenous*, *ordered* collections.

    .. rst-class:: build
    .. container::

        Elements need not be of a single type

        Each element in a list is a value

        Membership in a list adds a reference to the value

        .. code-block:: ipython

            In [9]: name = u'Brian'
            In [10]: a = [1, 2, name]
            In [11]: b = [3, 4, name]
            In [12]: a[2]
            Out[12]: u'Brian'
            In [13]: b[2]
            Out[13]: u'Brian'
            In [14]: a[2] is b[2]
            Out[14]: True


Tuples
------

We've also seen the :class:`tuple <python2:tuple>` (:py:class:`py3 <tuple>`) before.
We know that we can construct them using the tuple object literal: ``()``.

.. code-block:: ipython

    In [15]: ()
    Out[15]: ()
    In [16]: (1, 2)
    Out[16]: (1, 2)
    In [17]: (1, 'a', 7.65)
    Out[17]: (1, 'a', 7.65)
    In [18]: (1,)
    Out[18]: (1,)

.. slide:: Tuples
    :level: 3

    We've seen construction with using tuple literals (``()``):

    .. code-block:: ipython

        In [15]: ()
        Out[15]: ()
        In [16]: (1, 2)
        Out[16]: (1, 2)
        In [17]: (1, 'a', 7.65)
        Out[17]: (1, 'a', 7.65)
        In [18]: (1,)
        Out[18]: (1,)

As it turns out, though, you don't even need the parentheses to construct a tuple.
Separating a number of literal values, or bound names, with commas is enough:

.. code-block:: ipython

    In [161]: t = (1,2,3)
    In [162]: t
    Out[162]: (1, 2, 3)
    In [163]: t = 1,2,3
    In [164]: t
    Out[164]: (1, 2, 3)
    In [165]: type(t)
    Out[165]: tuple

In fact, the comma is actually the only required part.
If you try to construct a tuple with one element without a comma, it will not turn out as you expect:

.. code-block:: ipython

    In [156]: t = ( 3 )
    In [157]: type(t)
    Out[157]: int
    In [158]: t = (3,)
    In [160]: type(t)
    Out[160]: tuple

.. slide:: Tuples and Commas...
    :level: 3

    Tuples don't NEED parentheses...

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [161]: t = (1,2,3)
            In [162]: t
            Out[162]: (1, 2, 3)
            In [163]: t = 1,2,3
            In [164]: t
            Out[164]: (1, 2, 3)
            In [165]: type(t)
            Out[165]: tuple

        But they *do* need commas...!

        .. code-block:: ipython

            In [156]: t = ( 3 )
            In [157]: type(t)
            Out[157]: int
            In [158]: t = (3,)
            In [160]: type(t)
            Out[160]: tuple

You can also construct a tuple by calling the ``tuple`` type object.
It accepts an optional argument which can be any sequence type.
The sequence will be converted to a tuple:

.. code-block:: ipython

    In [20]: tuple()
    Out[20]: ()
    In [21]: tuple(range(4))
    Out[21]: (0, 1, 2, 3)
    In [22]: tuple('garbanzo')
    Out[22]: ('g', 'a', 'r', 'b', 'a', 'n', 'z', 'o')

.. slide:: Converting to Tuple
    :level: 3

    Use the ``tuple`` type object to convert any sequence into a tuple:

    .. code-block:: ipython

        In [20]: tuple()
        Out[20]: ()
        In [21]: tuple(range(4))
        Out[21]: (0, 1, 2, 3)
        In [22]: tuple('garbanzo')
        Out[22]: ('g', 'a', 'r', 'b', 'a', 'n', 'z', 'o')


A tuple is a *heterogenous*, *ordered* collection.
This means it can contain values of different types.
Each element in a tuple is a value.
Even if you add a name to a tuple, it is the value the name is bound to that is actually stored.
And like all values, the values in a list can have none, one, or more than one name bound to them.
When you store a value in a tuple, it creates a reference to that value.

.. slide:: Tuple Elements
    :level: 3

    Tuples are *heterogenous*, *ordered* collections.

    .. rst-class:: build
    .. container::

        Elements need not be of a single type

        Each element in a tuple is a value

        Membership in a tuple adds a reference to the value

        .. code-block:: ipython

            In [23]: name = u'Brian'
            In [24]: other = name
            In [25]: a = (1, 2, name)
            In [26]: b = (3, 4, other)
            In [27]: for i in range(3):
               ....:     print(a[i] is b[i], end=' ')
               ....:
            False False True

.. slide:: Lists vs. Tuples
    :level: 3

    .. rst-class:: center large

    So Why Have Both?

So if the list and the tuple are essentially identical, why does Python have both?

Mutability
==========

.. image:: /_static/transmogrifier.jpg
   :width: 35%
   :alt: Presto change-o

.. rst-class:: credit

image from flickr by `illuminaut`_, (CC by-nc-sa)

.. _illuminaut: https://www.flickr.com/photos/illuminaut/3595530403

.. slide:: Mutability
    :level: 2

    .. image:: /_static/transmogrifier.jpg
       :width: 35%
       :alt: Presto change-o

    .. rst-class:: credit

    image from flickr by `illuminaut`_, (CC by-nc-sa)

    .. _illuminaut: https://www.flickr.com/photos/illuminaut/3595530403


Mutability in Python
--------------------

All objects in Python fall into one of two camps: mutable and immutable.
Objects which are mutable may be *changed in place*.
Objects which are immutable *may not be changed*.

.. slide:: Mutability in Python
    :level: 3

    All objects in Python fall into one of two camps:

    * Mutable
    * Immutable

    .. rst-class:: build
    .. container::

        Objects which are mutable may be *changed in place*.

        Objects which are immutable may not be changed.

The Types We Know
-----------------

Here's a table showing the types we know so far, split into the two categories of mutable and immutable

======= =========
Mutable Immutable
======= =========
List    Unicode
Dict    String
Set     Integer
        Float
        Tuple
        FrozenSet
======= =========

.. slide:: The Types We Know
    :level: 3

    ========= =======
    Immutable Mutable
    ========= =======
    Unicode   List
    String    Dict
    Integer   Set
    Float
    Tuple
    FrozenSet
    ========= =======

Lists are mutable.
Try this out:

.. code-block:: ipython

    In [28]: food = [u'spam', u'eggs', u'ham']

    In [29]: food
    Out[29]: [u'spam', u'eggs', u'ham']

    In [30]: food[1] = u'raspberries'

    In [31]: food
    Out[31]: [u'spam', u'raspberries', u'ham']

.. slide:: Lists Are Mutable
    :level: 3

    Try this out:

    .. code-block:: ipython

        In [28]: food = [u'spam', u'eggs', u'ham']
        In [29]: food
        Out[29]: [u'spam', u'eggs', u'ham']
        In [30]: food[1] = u'raspberries'
        In [31]: food
        Out[31]: [u'spam', u'raspberries', u'ham']

Tuples, on the other hand, are immutable.
If we try the same thing with a tuple:

.. code-block:: ipython

    In [32]: food = (u'spam', u'eggs', u'ham')
    In [33]: food
    Out[33]: (u'spam', u'eggs', u'ham')
    In [34]: food[1] = u'raspberries'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-34-0c3401794933> in <module>()
    ----> 1 food[1] = u'raspberries'

    TypeError: 'tuple' object does not support item assignment

.. slide:: Tuples Are Not
    :level: 3

    And repeat the exercise with a Tuple:

    .. code-block:: ipython

        In [32]: food = (u'spam', u'eggs', u'ham')
        In [33]: food
        Out[33]: (u'spam', u'eggs', u'ham')
        In [34]: food[1] = u'raspberries'
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        <ipython-input-34-0c3401794933> in <module>()
        ----> 1 food[1] = u'raspberries'

        TypeError: 'tuple' object does not support item assignment

We must be aware of the mutability of the types we use when binding values.
For example, consider this short program:

.. code-block:: ipython

    In [36]: original = [1, 2, 3]
    In [37]: altered = original
    In [38]: for i in range(len(original)):
       ....:     if True:
       ....:         altered[i] += 1
       ....:

What is the result of running this code?

.. code-block:: ipython

    In [39]: altered
    Out[39]: [2, 3, 4]

    In [40]: original
    Out[40]: [2, 3, 4]

First we bind the symbol ``original`` to the list containing 1, 2 and 3.
Next, we bind the symbol ``altered``.
But to what?

Remember that we only ever bind names to values.
In [37] above, we are binding ``altered`` to the value that ``original`` is bound to.
In other words, both symbols *are bound to the same value*.

.. slide:: Watch When Binding
    :level: 3

    Be aware of what you are doing with lists:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [36]: original = [1, 2, 3]
            In [37]: altered = original
            In [38]: for i in range(len(original)):
               ....:     if True:
               ....:         altered[i] += 1
               ....:

        What is the result of this code?

        .. code-block:: ipython

            In [39]: altered
            Out[39]: [2, 3, 4]

        .. code-block:: ipython

            In [40]: original
            Out[40]: [2, 3, 4]

There are other potential gotchas involving mutability.
Consider the follow example of code.
It looks like a quick way to set up a bunch of bins for us to sort our words into.

.. code-block:: ipython

    In [13]: bins = [ [] ] * 5
    In [14]: bins
    Out[14]: [[], [], [], [], []]
    In [15]: words = [u'one', u'three', u'rough', u'sad', u'goof']
    In [16]: for word in words:
       ....:     bins[len(word)-1].append(word)
       ....:

But in fact, it's a deadly trap.
We are concatenating together a list five times.
That list contains one list.
The new list contains that same one list... *five times!*

.. code-block:: ipython

    In [65]: bins
    Out[65]:
    [[u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof']]


.. slide:: Other Gotchas
    :level: 3

    Easy container setup, or deadly trap?

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [13]: bins = [ [] ] * 5
            In [14]: bins
            Out[14]: [[], [], [], [], []]
            In [15]: words = [u'one', u'three', u'rough', u'sad', u'goof']
            In [16]: for word in words:
               ....:     bins[len(word)-1].append(word)
               ....:

        So, what is going to be in ``bins`` now?

.. slide:: There is Only **One** Bin
    :level: 3

    .. code-block:: ipython

        In [65]: bins
        Out[65]:
        [[u'one', u'three', u'rough', u'sad', u'goof'],
         [u'one', u'three', u'rough', u'sad', u'goof'],
         [u'one', u'three', u'rough', u'sad', u'goof'],
         [u'one', u'three', u'rough', u'sad', u'goof'],
         [u'one', u'three', u'rough', u'sad', u'goof']]

    .. rst-class:: build
    .. container::

        We multiplied a sequence containing a single *mutable* object.

        We got a list containing five pointers to a single *mutable* object.

We must also avoid using mutable objects as default values for functions:

.. code-block:: ipython

    In [71]: def accumulator(count, list=[]):
       ....:     for i in range(count):
       ....:         list.append(i)
       ....:     return list
       ....:

When the ``def`` statement is executed, the value of the default is baked into the constructed function object.
This means that the default value *any time the function is called* is a single, mutable object.
So the first time we call the function:

.. code-block:: ipython

    In [72]: accumulator(5)
    Out[72]: [0, 1, 2, 3, 4]

And the second time?

.. code-block:: ipython

    In [73]: accumulator(7)
    Out[73]: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6]

.. slide:: Mutable Default Argument
    :level: 3

    Avoid passing mutable objects as default values for function parameters:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [71]: def accumulator(count, list=[]):
               ....:     for i in range(count):
               ....:         list.append(i)
               ....:     return list
               ....:
            In [72]: accumulator(5)
            Out[72]: [0, 1, 2, 3, 4]

        what happens when we call it again?

        .. code-block:: ipython

            In [73]: accumulator(7)
            Out[73]: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6]


Mutable Sequence Methods
========================

We've seen a number of operations supported by all sequence types.
Mutable sequences (the List), have a number of other methods that are used to change the list.

We can find all these in the standard library documentation for :ref:`python2:typesseq-mutable` (:py:ref:`py3 <typesseq-mutable>`)

Assignment
----------

Using the *subscription operator* in combination with assignment allows us to change a single element within a list.
This operates pretty much the same as *arrays* in most languages:

.. code-block:: ipython

    In [100]: list = [1, 2, 3]
    In [101]: list[2] = 10
    In [102]: list
    Out[102]: [1, 2, 10]

.. slide:: Assignment
    :level: 3

    Change a single element of a list by assignment

    .. rst-class:: build
    .. container::

        Pretty much the same as "arrays" in most languages:

        .. code-block:: ipython

            In [100]: list = [1, 2, 3]
            In [101]: list[2] = 10
            In [102]: list
            Out[102]: [1, 2, 10]


Growing the List
----------------

We can grow a list using one of three methods.

The ``.append()`` method adds a single item to the end of the list.

.. code-block:: ipython

    In [74]: food = [u'spam', u'eggs', u'ham']
    In [75]: food.append(u'sushi')
    In [76]: food
    Out[76]: [u'spam', u'eggs', u'ham', u'sushi']

The ``.insert()`` method adds a single item at a given position in the list.

.. code-block:: ipython

    In [77]: food.insert(0, u'beans')
    In [78]: food
    Out[78]: [u'beans', u'spam', u'eggs', u'ham', u'sushi']

The ``.extend()`` method takes a sequence as its argument, and adds all the items in it to the end of the list.

.. code-block:: ipython

    In [79]: food.extend([u'bread', u'water'])
    In [80]: food
    Out[80]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']

.. slide:: Growing the List
    :level: 3

    .. rst-class:: build
    .. container::

        .. container::

            ``.append()``

            .. code-block:: ipython

                In [74]: food = [u'spam', u'eggs', u'ham']
                In [75]: food.append(u'sushi')
                In [76]: food
                Out[76]: [u'spam', u'eggs', u'ham', u'sushi']

        .. container::

            ``.insert()``

            .. code-block:: ipython

                In [77]: food.insert(0, u'beans')
                In [78]: food
                Out[78]: [u'beans', u'spam', u'eggs', u'ham', u'sushi']

        .. container::

            ``.extend()``

            .. code-block:: ipython

                In [79]: food.extend([u'bread', u'water'])
                In [80]: food
                Out[80]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']

Remember, we can pass *any* sequence type as an argument to ``extend``.
Sometimes this has unexpected results:

.. code-block:: ipython

    In [85]: food
    Out[85]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']
    In [86]: food.extend(u'spaghetti')
    In [87]: food
    Out[87]:
    [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water',
     u's', u'p', u'a', u'g', u'h', u'e', u't', u't', u'i']

.. slide:: More on Extend
    :level: 3

    You can pass any sequence to ``.extend()``:

    .. code-block:: ipython

        In [85]: food
        Out[85]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']
        In [86]: food.extend(u'spaghetti')
        In [87]: food
        Out[87]:
        [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water',
         u's', u'p', u'a', u'g', u'h', u'e', u't', u't', u'i']


Shrinking the List
------------------

There are also a number of methods available that allow us to shrink a list.

The ``.pop()`` method removes an item from the end of a list and returns its value.
If the optional ``index`` argument is passed, the item at that index is removed and returned instead.
If the method is called on an empty list, or the provided ``index`` argument is out of range, this causes an ``IndexError``.

.. code-block:: ipython

    In [203]: food = ['spam', 'eggs', 'ham', 'toast']
    In [204]: food.pop()
    Out[204]: 'toast'
    In [205]: food.pop(0)
    Out[205]: 'spam'
    In [206]: food
    Out[206]: ['eggs', 'ham']

The ``.remove()`` method removes the value provided as its argument from the list.
If that value is not present in the list, it causes a ``ValueError``.

.. code-block:: ipython

    In [207]: food.remove('ham')
    In [208]: food
    Out[208]: ['eggs']

.. slide:: Shrinking the List
    :level: 3

    .. rst-class:: build
    .. container::

        .. container::

            ``.pop()``

            .. code-block:: ipython

                In [203]: food = ['spam', 'eggs', 'ham', 'toast']
                In [204]: food.pop()
                Out[204]: 'toast'
                In [205]: food.pop(0)
                Out[205]: 'spam'
                In [206]: food
                Out[206]: ['eggs', 'ham']

            (``IndexError``) if out of range

        .. container::

            ``.remove()``

            .. code-block:: ipython

                In [207]: food.remove('ham')
                In [208]: food
                Out[208]: ['eggs']

            (``ValueError`` if not in list)

We can even remove entire chunks of a list using the ``del`` keyword on a slice of the list:

.. code-block:: ipython

    In [92]: nums = range(10)
    In [93]: nums
    Out[93]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [94]: del nums[1:6:2]
    In [95]: nums
    Out[95]: [0, 2, 4, 6, 7, 8, 9]
    In [96]: del nums[-3:]
    In [97]: nums
    Out[97]: [0, 2, 4, 6]

.. slide:: Removing Chunks of a List
    :level: 3

    Delete *slices* of a list with the ``del`` keyword:

    .. code-block:: ipython

        In [92]: nums = range(10)
        In [93]: nums
        Out[93]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        In [94]: del nums[1:6:2]
        In [95]: nums
        Out[95]: [0, 2, 4, 6, 7, 8, 9]
        In [96]: del nums[-3:]
        In [97]: nums
        Out[97]: [0, 2, 4, 6]


Copying Lists
-------------

We can create copies of ``list`` objects in Python using *slicing*.
If we provide no arguments to the slice operator, the result is to create a copy of the entire list:

.. code-block:: ipython

    In [227]: food = ['spam', 'eggs', 'ham', 'sushi']
    In [228]: some_food = food[1:3]
    In [229]: some_food[1] = 'bacon'
    In [230]: food
    Out[230]: ['spam', 'eggs', 'ham', 'sushi']
    In [231]: some_food
    Out[231]: ['eggs', 'bacon']

.. code-block:: ipython

    In [232]: food
    Out[232]: ['spam', 'eggs', 'ham', 'sushi']
    In [233]: food2 = food[:]
    In [234]: food is food2
    Out[234]: False

.. slide:: Copying Lists
    :level: 3

    You can make copies of part of a list using *slicing*:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [227]: food = ['spam', 'eggs', 'ham', 'sushi']
            In [228]: some_food = food[1:3]
            In [229]: some_food[1] = 'bacon'
            In [230]: food
            Out[230]: ['spam', 'eggs', 'ham', 'sushi']
            In [231]: some_food
            Out[231]: ['eggs', 'bacon']

        *no* arguments to the slice, copies the entire list:

        .. code-block:: ipython

            In [232]: food
            Out[232]: ['spam', 'eggs', 'ham', 'sushi']
            In [233]: food2 = food[:]
            In [234]: food is food2
            Out[234]: False

Making a copy this way results in what we call a *shallow copy*.
More about this in a bit.

.. slide:: Shallow Copies
    :level: 3

    The copy of a list made this way is a *shallow copy*.

    .. rst-class:: build
    .. container::

        The list is itself a new object, but the objects it contains are not.

        *Mutable* objects in the list can be mutated in both copies:

        .. code-block:: ipython

            In [249]: food = ['spam', ['eggs', 'ham']]
            In [251]: food_copy = food[:]
            In [252]: food[1].pop()
            Out[252]: 'ham'
            In [253]: food
            Out[253]: ['spam', ['eggs']]
            In [256]: food.pop(0)
            Out[256]: 'spam'
            In [257]: food
            Out[257]: [['eggs']]
            In [258]: food_copy
            Out[258]: ['spam', ['eggs']]

Copies can be useful in solving problems.
Consider the following common pattern:

.. code-block:: python

    for x in somelist:
        if should_be_removed(x):
            somelist.remove(x)

This looks benign enough.
But changing a list while you are iterating over it can be the cause of some pernicious bugs.
For example, try this out:

.. code-block:: ipython

    In [121]: lst = range(10)
    In [122]: lst
    Out[122]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [123]: for x in lst:
       .....:     lst.remove(x)
       .....:

At this point, what do we expect the ``list`` object to contain?

.. code-block:: ipython

    In [124]: lst
    Out[124]: [1, 3, 5, 7, 9]

We can use a copy of the list to solve this problem.
By iterating over the copy of the list while mutating the original, we get the results we wanted:

.. code-block:: ipython

    In [126]: lst = range(10)
    In [127]: for x in lst[:]:
       .....:     lst.remove(x)
       .....:
    In [128]: lst
    Out[128]: []

.. slide:: The Problem
    :level: 3

    For example:

    .. code-block:: ipython

        In [121]: list = range(10)
        In [122]: list
        Out[122]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        In [123]: for x in list:
           .....:     list.remove(x)
           .....:

    .. rst-class:: build
    .. container::

        What do you expect ``list`` to be now?

        .. code-block:: ipython

            In [124]: list
            Out[124]: [1, 3, 5, 7, 9]

.. slide:: The Solution
    :level: 3

    Iterate over a copy, and mutate the original:

    .. code-block:: ipython

        In [126]: list = range(10)
        In [127]: for x in list[:]:
           .....:     list.remove(x)
           .....:
        In [128]: list
        Out[128]: []

We've talked about this: mutable objects can have their contents changed in place.
Immutable objects can not.
This has implications when you have a container with mutable objects in it:

.. code-block:: ipython

    In [28]: list1 = [ [1,2,3], ['a','b'] ]

We can make a copy of this list.
And we can prove that they are different lists.

.. code-block:: ipython

    In [29]: list2 = list1[:]
    In [30]: list2 is list1
    Out[30]: False

Now, what if we set an element to a new value?

.. code-block:: ipython

    In [31]: list1[0] = [5,6,7]

    In [32]: list1
    Out[32]: [[5, 6, 7], ['a', 'b']]

    In [33]: list2
    Out[33]: [[1, 2, 3], ['a', 'b']]

The copied lists are independent of each-other.
But what if we mutate an element?

.. code-block:: ipython

    In [34]: list1[1].append('c')

    In [35]: list1
    Out[35]: [[5, 6, 7], ['a', 'b', 'c']]

    In [36]: list2
    Out[36]: [[1, 2, 3], ['a', 'b', 'c']]

Mutating an element in one list mutated the one in the other list.
Why is that?

.. code-block:: ipython

    In [38]: list1[1] is list2[1]
    Out[38]: True

The lists are different objects, but the list elements are the same object!

This is known as a "shallow" copy.
Python doesn't want to copy more than it needs to.
So in this case, it makes a new list, but does not make copies of the contents.

This holds as well for dicts (and any container type).
If the elements are immutable, it doesn't really make a differnce.
But be very careful with mutable elements.

The copy module
---------------

Most objects have a way to make copies (``dict.copy()`` for instance).
But if they do no, you can use the ``copy`` module to make one.

.. code-block:: ipython

    In [39]: import copy

    In [40]: list3 = copy.copy(list2)

    In [41]: list3
    Out[41]: [[1, 2, 3], ['a', 'b', 'c']]

.. slide:: The ``copy`` Module
    :level: 3

    For objects which have no way to make a copy

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [39]: import copy
            In [40]: list3 = copy.copy(list2)
            In [41]: list3
            Out[41]: [[1, 2, 3], ['a', 'b', 'c']]

        Still just a shallow copy

        .. code-block:: ipython

            In [42]: list4 = copy.deepcopy(list3)
            In [43]: list4[0].append(4)
            In [44]: list4
            Out[44]: [[1, 2, 3, 4], ['a', 'b', 'c']]
            In [45]: list3
            Out[45]: [[1, 2, 3], ['a', 'b', 'c']]

Copies made by ``copy.copy`` are still shallow.
But the ``copy`` module also offers ``copy.deepcopy``.
This function recurses through the object, making copies of everything as it goes.
The result is a copy that is entirely independent from the original, all the way down.

.. code-block:: ipython

    In [42]: list4 = copy.deepcopy(list3)
    In [43]: list4[0].append(4)
    In [44]: list4
    Out[44]: [[1, 2, 3, 4], ['a', 'b', 'c']]
    In [45]: list3
    Out[45]: [[1, 2, 3], ['a', 'b', 'c']]

I happened on `this thread on stack overflow <http://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep>`_
The OP is pretty confused -- can you sort it out?
Make sure you understand the difference between a reference, a shallow copy, and a deep copy.


Miscellaneous List Methods
--------------------------

These methods change a list in place and are not available on immutable sequence types.
Because these methods mutate the list in place, they have a return value of ``None``

The ``.reverse()`` method reverses a list in place:

.. code-block:: ipython

    In [129]: food = [u'spam', u'eggs', u'ham']
    In [130]: food.reverse()
    In [131]: food
    Out[131]: [u'ham', u'eggs', u'spam']

The ``.sort()`` method sorts the list in ascending order:

.. code-block:: ipython

    In [132]: food.sort()
    In [133]: food
    Out[133]: [u'eggs', u'ham', u'spam']

.. slide:: Miscellaneous List Methods
    :level: 3

    Mutate list in-place. Not available on immutable sequence types

    .. rst-class:: build
    .. container::

        .. container::

            ``.reverse()``:

            .. code-block:: ipython

                In [129]: food = [u'spam', u'eggs', u'ham']
                In [130]: food.reverse()
                In [131]: food
                Out[131]: [u'ham', u'eggs', u'spam']

        .. container::

            ``.sort()``:

            .. code-block:: ipython

                In [132]: food.sort()
                In [133]: food
                Out[133]: [u'eggs', u'ham', u'spam']

If we prefer a different order for your sorting, we can supply the optional ``key`` parameter.
The argument must be a function which takes one parameter.
It will be called for each item in the list.
The value it returns will be used as the value on which to sort the list:

.. code-block:: ipython

    In [137]: def third_letter(string):
       .....:     return string[2]
       .....:
    In [138]: food.sort(key=third_letter)
    In [139]: food
    Out[139]: [u'spam', u'eggs', u'ham']

.. slide:: Control Sorting
    :level: 3

    ``.sort()`` takes an optional ``key`` parameter.

    .. rst-class:: build
    .. container::

        Pass a function that takes one parameter.

        The items of the list will go in one at a time

        Return some aspect of the item to be used for sorting

        .. code-block:: ipython

            In [137]: def third_letter(string):
               .....:     return string[2]
               .....:
            In [138]: food.sort(key=third_letter)
            In [139]: food
            Out[139]: [u'spam', u'eggs', u'ham']

        Don't forget the ``sorted`` builtin, either.

If we would rather create a sorted copy of our list, we can make use of the :func:`sorted <python2:sorted` builtin (:py:func:`py3 <sorted>`).
This function takes a list as its first argument.
The remaining arguments are the same as for the ``list.sort`` method.
The function returns a new list which has been sorted, and leaves the original unmodified.

List Performance
================

Lists are optimized for access, and for operations on the end of the list.
Operating on the middle or front of the list is not fast.
Nor is membership.

* indexing is fast and constant time: O(1)
* ``x in s`` proportional to n: O(n)
* visiting all is proportional to n: O(n)
* operating on the end of list is fast and constant time: O(1)

  * append(), pop()

* operating on the front (or middle) of the list depends on n: O(n)

  * pop(0), insert(0, v)
  * But, reversing is fast. Also, collections.deque

.. slide:: List Performance
    :level: 3

    * indexing is fast and constant time: O(1)
    * x in s proportional to n: O(n)
    * visiting all is proportional to n: O(n)
    * operating on the end of list is fast and constant time: O(1)

      * append(), pop()

    * operating on the front (or middle) of the list depends on n: O(n)

      * pop(0), insert(0, v)
      * But, reversing is fast. Also, collections.deque

    http://wiki.python.org/moin/TimeComplexity


Choosing Lists or Tuples
------------------------

Here are a few guidelines on when to choose a list or a tuple:

* If it needs to mutable: list

* If it needs to be immutable: tuple

  * (safety when passing to a function)

Otherwise the choice is really down to taste and convention.
If you are contributing to an existing codebase, look around you and do what you see done.

Also consider the following thoughts:

Lists are Collections (homogeneous):
-- contain values of the same type
-- simplifies iterating, sorting, etc

tuples are mixed types:
-- Group multiple values into one logical thing
-- Kind of like simple C structs.

.. slide:: Choosing, List or Tuple?
    :level: 3

    .. rst-class:: build
    .. container::

        .. rst-class:: build

        * if you need mutability, choose a list
        * if you need immutability, choose a tuple

        Otherwise, taste and convention

        Lists can be collections of like things

        Simplifies iteration and sorting

        Tuples can be mixed types

        Represent ``data records`` in a sense

And a few final guidelines:

* Do the same operation to each element?

  * list

* Small collection of values which make a single logical item?

  * tuple

* To document that these values won't change?

  * tuple

* Build it iteratively?

  * list

* Transform, filter, etc?

  * list

.. slide:: Other Considerations
    :level: 3

    .. rst-class:: build

    * Do the same operation to each element?

      * list

    * Small collection of values which make a single logical item?

      * tuple

    * To document that these values won't change?

      * tuple

    * Build it iteratively?

      * list

    * Transform, filter, etc?

      * list

Exception Handling
==================

Exceptions in Python are used to control program flow when things go wrong.
To handle exceptions, we use the :keyword:`try <python2:try>` (:py:keyword:`py3 <try>`).
This keyword forms another branching structure, like ``if ... else``:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

If an error occurs as a result of any of the statements in the ``try`` block, that error will be compared with the exception class specified in the :keyword:`except <python2:except>` (:py:keyword:`py3 <except>`) block.
If the exception raised is an instance of, or an instance of a subclass of that exception class, the statements in the ``except`` block will be executed.

Using the ``except`` keyword without providing a comparison exception class is called a ``bare except``.
This is considered very bad style, as it can hide problems in our code.
It's not really better to use the ``Exception`` class as the comparison either.
That is the base class for *all* Python exceptions, so the end result is the same.

.. warning:: Never Do this:

             .. code-block:: python

                try:
                    do_something()
                    f = open('missing.txt')
                    process(f)   # never called if file missing
                except:
                    print("couldn't open missing.txt")

             And this is no better, really:

             .. code-block:: python

                try:
                    do_something()
                    f = open('missing.txt')
                    process(f)   # never called if file missing
                except Exception:
                    print("couldn't open missing.txt")

.. slide:: Exception Handling
    :level: 2

    .. rst-class:: large centered

    or: what to do when things go wrong

.. slide:: ``try ... except``
    :level: 3

    Another Branching structure:

    .. code-block:: python

        try:
            do_something()
            f = open('missing.txt')
            process(f)   # never called if file missing
        except IOError:
            print("couldn't open missing.txt")

.. slide:: Bare Except
    :level: 3

    Never Do this:

    .. code-block:: python

        try:
            do_something()
            f = open('missing.txt')
            process(f)   # never called if file missing
        except:
            print("couldn't open missing.txt")

.. slide:: Overly General
    :level: 3

    This is no better:

    .. code-block:: python

        try:
            do_something()
            f = open('missing.txt')
            process(f)
        except Exception:
            print("couldn't open missing.txt")

In programming there are two approaches to dealing with code that might cause errors to occur.
The first is to test first to see if the error will happen, and do something different if it won't:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)   # never called if file missing

The second approach is to allow the exceptions to happen, and then handle them when they do:

.. code-block:: python

    try:
        f = open('missing.txt')
    except IOError:
        deal_with_it()
    else:
        process(f)

This latter approach is considered to be *more Pythonic*.
We call this approach *EAFP*:

.. epigraph::

   it's Easier to Ask Forgiveness than Permission

   -- Grace Hopper

It isn't always that cut-and-dried, but it's a good starting point.
For a more nuanced take on this, you should watch `Alex Martelli's PyCon Talk from 2012 <http://www.youtube.com/watch?v=AZDWveIdqjY>`_

.. slide:: Exceptions > Tests
    :level: 3

    Use Exceptions, rather than tests

    .. rst-class:: build
    .. container::

        Don't do this:

        .. code-block:: python

            do_something()
            if os.path.exists('missing.txt'):
                f = open('missing.txt')
                process(f)   # never called if file missing

        It will almost always work

        but the *almost* will drive you crazy

.. slide:: EAFP
    :level: 3

    .. epigraph::

       It's Easier to Ask Forgiveness than Permission

       -- Grace Hopper

    http://www.youtube.com/watch?v=AZDWveIdqjY

    (Pycon talk by Alex Martelli)

In general, it's a good idea to allow exceptions to happen.
Python provides excellent tracebacks and error messages.
They are helpful to developers and even useful to end users.
We should only catch exceptions that happen if we *can* and *will* do something about them.

.. slide:: What to Catch?
    :level: 3

    For simple scripts, let exceptions happen.

    Only catch exceptions if you *can* and *will* do something about them.

    (much better debugging info when an error does occur)

The ``try ... except`` clause can be extended with an ``else`` clause.
The code in this block is executed only if *no exception* occurs.
This can be a great way to isolate code that is entirely dependent on the success of the code in the ``try`` block.

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print(u"couldn't open missing.txt")
    else:
        process(f)

.. slide:: ``else`` Clause
    :level: 3

    The ``try ... except`` block can be extended by ``else``

    .. rst-class:: build
    .. container::

        .. code-block:: python

            try:
                do_something()
                f = open('missing.txt')
            except IOError:
                print(u"couldn't open missing.txt")
            else:
                process(f)

        Code in the ``else:`` block is run only when *no exception*

We can also enhance ``try ... except`` with a ``finally`` clause.
The code in this block is executed *whether or not* an exception handles.
This is an opportunity to do tasks that must happen in any case: closing file handles, terminating network sessions, etc.

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print(u"couldn't open missing.txt")
    finally:
        do_some_clean_up

.. slide:: ``finally`` Clause
    :level: 3

    The ``try ... except`` block can be extended by ``finally``

    .. rst-class:: build
    .. container::

        .. code-block:: python

            try:
                do_something()
                f = open('missing.txt')
                process(f)   # never called if file missing
            except IOError:
                print(u"couldn't open missing.txt")
            finally:
                do_some_clean_up

        Code in the ``finally:`` block will *always* run

.. note:: The ``try`` keyword must always be paired with at least one other keyword.
          The most common pair is the ``try ... except`` pairing.
          You can even add more ``except`` clauses to handle different types of errors.
          But you *can* omit any ``except`` clause **if and only if** you use a ``finally`` clause.

When errors do occur, the exception instances that are raised often have information that can be used in handling the exception.
If you want to do so, you can use ``as`` in your except clause to bind the exception instance to a symbol.
Then in the except block, you can read attributes of the exception and use the information as you wish:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print(the_error)
        the_error.extra_info = "some more information"
        raise

Before the introduction of ``as`` in an ``except`` statement in Python 2.6, we could achieve this same thing by using a comma to separate the exception instance from the symbol to which it would be bound.
This form is still out there in legacy code bases.
If dropping support for Python 2.5 and earlier is possible (as it should usually be), you should update this form whenever you see it:

.. code-block:: python

    try:
        f = open('missing.txt')
    except IOError, the_error:
       print(the_error)

This can be particularly useful when you are handling several different exception types with a single except clause:

.. code-block:: python

    except (IOError, BufferError, OSError) as the_error:
        do_something_with(the_error)

.. slide:: Using Exception Instances
    :level: 3

    You can work with exception instances

    .. rst-class:: build
    .. container::

        .. code-block:: python

            try:
                do_something()
                f = open('missing.txt')
            except IOError as the_error:
                print(the_error)
                the_error.extra_info = "some more information"
                raise

        Particularly useful if you catch more than one exception:

        .. code-block:: python

            except (IOError, BufferError, OSError) as the_error:
                do_something_with(the_error)

When writing code, it can be useful for us to be able to control the exceptions that happen when our code is used.
The :keyword:`raise <python2:raise>` keyword (:py:keyword:`py3 <raise>`) allows us to create exception instances and throw them.

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b

You can create custom exceptions by sub-classing any of the :ref:`built-in exception types <python2:bltin-exceptions>` (:py:ref:`py3 <bltin-exceptions>`).
However, consider carefully using one of the existing classes instead.
There are 32 in Python 2 and 47 in Python 3.  Plenty to handle most situations well.

.. slide:: Raising Exceptions
    :level: 3

    .. code-block:: python

        def divide(a,b):
            if b == 0:
                raise ZeroDivisionError("b can not be zero")
            else:
                return a / b

    .. rst-class:: build
    .. container::

        when you call it:

        .. code-block:: ipython

            In [515]: divide(12,0)
            ZeroDivisionError: b can not be zero


.. slide:: Built in Exceptions
    :level: 3

    You can create your own custom exceptions, but...

    .. rst-class:: build
    .. container::

        .. code-block:: python

            exp = [name for name in dir(__builtin__) if "Error" in name]
            len(exp)
            47

        For the most part, you can/should use a built in one

Remember always that in programming exceptions are a form of communications.
The kind of exception that is raised tells developers about what went wrong.
We should always make an effort to choose the best possible exception class to describe our particular problem.

Consider the example of the Ackermann function we've been working on.
A user might attempt to call the function while providing non-integers as arguments.
We could protect ourselves against this problem like so::

    if (not isinstance(m, int)) or (not isinstance(n, int)):
        raise ValueError

But is it the *value* of the input that is the problem here?
Not really.
The real issue is the *type* that was passed.
This would be a better communication of the situation::

    if (not isinstance(m, int)) or (not isinstance(n, int)):
        raise TypeError

But again, *EAFP*, should we really be checking in the first place?

.. slide:: Exceptions are Communication
    :level: 3

    The kind of exception raised tells us about what went wrong

    Choose the best built in Exception you can find

    .. rst-class:: build
    .. container::

        Example (consider our Ackermann project)::

            if (not isinstance(m, int)) or (not isinstance(n, int)):
                raise ValueError

        Is the *value* of the input the problem here?

        Nope: the *type* is the problem::

            if (not isinstance(m, int)) or (not isinstance(n, int)):
                raise TypeError

        but should we be checking type anyway? (EAFP)

Advanced Argument Passing
=========================

When defining a function, we can specify only what we need -- in any order.

.. code-block:: ipython

    In [150]: from __future__ import print_function
    In [151]: def fun(x, y=0, z=0):
       .....:     print(x, y, z, end=" ")
       .....:
    In [152]: fun(1, 2, 3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(1, z=3, y=2)
    1 2 3

.. slide:: Keyword arguments
    :level: 3

    Allow you to specify only what you need

    .. rst-class:: build
    .. container::

        And provide in any order

        .. code-block:: ipython

            In [150]: from __future__ import print_function
            In [151]: def fun(x, y=0, z=0):
               .....:     print(x, y, z, end=" ")
               .....:
            In [152]: fun(1, 2, 3)
            1 2 3
            In [153]: fun(1, z=3)
            1 0 3
            In [154]: fun(1, z=3, y=2)
            1 2 3

One fun feature is that we can use *variables* as default values.

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print(u"x is: %s" % x)
       .....:
    In [158]: fun()
    x is: 4

Since defaults are evaluated when a function is defined, once the function object exists, the variable can be changed without altering the function.

.. code-block:: ipython

    In [159]: y = 6
    In [160]: fun()
    x is: 4

.. slide:: Variable Defaults
    :level: 3

    Can set defaults to variables

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [156]: y = 4
            In [157]: def fun(x=y):
                print(u"x is: %s" % x)
               .....:
            In [158]: fun()
            x is: 4

        Defaults are evaluated *at init time*

        .. code-block:: ipython

            In [159]: y = 6
            In [160]: fun()
            x is: 4

We've seen using ``*`` and ``**`` for variable parameter lists:

.. code-block:: ipython

    In [10]: def f(*args, **kwargs):
       ....:     print(u"the positional arguments are: %s" % unicode(args))
       ....:     print(u"the optional arguments are: %s" % unicode(kwargs))
       ....:
    In [11]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the optional arguments are: {'this': 5, 'that': 7}

What isn't immediately apparent from that usage is that *internally* to a function object, parameters are represented as

* a tuple of positional arguments
* a dict of keyword arguments

This has interesting implications.
For example, consider the following function:

.. code-block:: ipython

    In [1]: def f(x, y, w=0, h=0):
       ...:     msg = u"position: %s, %s -- shape: %s, %s"
       ...:     print(msg % (x, y, w, h))
       ...:

We can use the same ``*`` and ``**`` operators (splat and double-splat) to pass tuples and dicts as arguments:

.. code-block:: ipython

    In [2]: position = (3, 4)
    In [3]: size = {'h': 10, 'w': 20}
    In [4]: f(*position, **size)
    position: 3, 4 -- shape: 20, 10

Remember the string ``.format()`` method?
It can take keyword arguments if the placeholders in the format string are named.

.. code-block:: ipython

    In [24]: u"My name is {first} {last}".format(last=u"Ewing", first=u"Cris")
    Out[24]: u'My name is Cris Ewing'

You can also use a ``dict`` with keys and values to accomplish the same thing:

.. code-block:: ipython

    In [25]: d = {u"last": u"Ewing", u"first": u"Cris"}

    In [26]: u"My name is {first} {last}".format(**d)
    Out[26]: u'My name is Cris Ewing'

.. slide:: Parameters in Variables
    :level: 3

    We've seen using ``*`` and ``**`` for variable parameter lists:

    .. code-block:: ipython

        In [10]: def f(*args, **kwargs):
           ....:     print(u"the positional arguments are: %s" % unicode(args))
           ....:     print(u"the optional arguments are: %s" % unicode(kwargs))
           ....:
        In [11]: f(2, 3, this=5, that=7)
        the positional arguments are: (2, 3)
        the optional arguments are: {'this': 5, 'that': 7}

.. slide:: Arguments in Variables
    :level: 3

    From the inside, function arguments are really just:

    .. rst-class:: build
    .. container::

        * a tuple (positional arguments)
        * a dict (keyword arguments)

        .. code-block:: ipython

            In [1]: def f(x, y, w=0, h=0):
               ...:     msg = u"position: %s, %s -- shape: %s, %s"
               ...:     print(msg % (x, y, w, h))
               ...:

        .. code-block:: ipython

            In [2]: position = (3, 4)
            In [3]: size = {'h': 10, 'w': 20}
            In [4]: f(*position, **size)
            position: 3, 4 -- shape: 20, 10

.. slide:: This Works
    :level: 3

    Keyword args are really a dict, you can do this:

    .. rst-class:: build
    .. container::

        .. container::

            ``format`` method takes keyword arguments:

            .. code-block:: ipython

                In [24]: u"My name is {first} {last}".format(last=u"Ewing", first=u"Cris")
                Out[24]: u'My name is Cris Ewing'

        .. container::

            Build a dict of the keys and values:

            .. code-block:: ipython

                In [25]: d = {u"last": u"Ewing", u"first": u"Cris"}

        .. container::

            And pass to ``format()`` with ``**``

            .. code-block:: ipython

                In [26]: u"My name is {first} {last}".format(**d)
                Out[26]: u'My name is Cris Ewing'

Finally, a reminder about using mutable objects as default values for optional parameters.
We know the problem with this function:

.. code-block:: ipython

    In [11]: def fun(x, a=[]):
       ....:     a.append(x)
       ....:     print(a)
       ....:

It's often useful to use a *flag value* as a default to signal when you want a mutable object to be used:

.. code-block:: ipython

    In [15]: def fun(x, a=None):
       ....:     if a is None:
       ....:         a = []
       ....:     a.append(x)
       ....:     print(a)
    In [16]: fun(3)
    [3]
    In [17]: fun(4)
    [4]

.. slide:: Mutable Defaults
    :level: 3

    We've seen this before:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [11]: def fun(x, a=[]):
               ....:     a.append(x)
               ....:     print(a)
               ....:

        .. container::

            But:

            .. code-block:: ipython

                In [12]: fun(3)
                [3]

                In [13]: fun(4)
                [3, 4]

.. slide:: Avoid This Problem
    :level: 3

    The standard practice for such a mutable default argument:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [15]: def fun(x, a=None):
               ....:     if a is None:
               ....:         a = []
               ....:     a.append(x)
               ....:     print(a)
            In [16]: fun(3)
            [3]
            In [17]: fun(4)
            [4]

        You get a new list every time the function is called

Comprehensions
==============

Comprehensions (list, dict and set) allow us to compress loop expressions into a clean syntax.
They can also be very efficient because they save the creation of intermediate values.
They are one piece of the functional programming story in Python.

List Comprehensions
-------------------

Consider the following loop structure, a very common pattern:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression)

With a *list comprehension* we can express the same thing in one clean line of code:

.. code-block:: python

    new_list = [expression for variable in a_list]

.. slide:: Comprehensions
    :level: 2

    .. rst-class:: left
    .. container::

        A bit of functional programming

        .. rst-class:: build
        .. container::

            consider this common ``for`` loop structure:

            .. code-block:: python

                new_list = []
                for variable in a_list:
                    new_list.append(expression)

            This can be expressed with a single line using a "list comprehension"

            .. code-block:: python

                new_list = [expression for variable in a_list]

What about nested *for* loops?

.. code-block:: python

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expr)

We can use multiple ``for`` clauses in a comprehension to express the same thing:

.. code-block:: python

    new_list =  [expr for var in a_list for var2 in a_list2]

.. slide:: Nested Loops
    :level: 3

    What about nested for loops?

    .. rst-class:: build
    .. container::

        .. code-block:: python

            new_list = []
            for var in a_list:
                for var2 in a_list2:
                    new_list.append(expr)

        Can also be expressed in one line:

        .. code-block:: python

            new_list =  [expr for var in a_list for var2 in a_list2]

        You get the "outer product": all combinations.

We can even use ``if`` in a comprehension to account for conditionals in the loop:

.. code-block:: python

    new_list = []
    for var in a_list:
        if something_is_true:
            new_list.append(expr)

This can also be expressed in a single statement.

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]

.. slide:: Conditionals in Comprehensions
    :level: 3

    What happens if you have a conditional in the loop?

    .. rst-class:: build
    .. container::

        .. code-block:: python

            new_list = []
            for var in a_list:
                if something_is_true:
                    new_list.append(expr)

        You can add a conditional to the comprehension:

        .. code-block:: python

            new_list = [expr for var in a_list if something_is_true]

Examples
********

.. code-block:: ipython

    In [341]: [x ** 2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x + y for x in range(3) for y in range(5, 7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x * 2 for x in range(6) if not x % 2]
    Out[343]: [0, 4, 8]

.. code-block:: python

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',

.. slide:: Examples
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [341]: [x ** 2 for x in range(3)]
            Out[341]: [0, 1, 4]

            In [342]: [x + y for x in range(3) for y in range(5, 7)]
            Out[342]: [5, 6, 6, 7, 7, 8]

            In [343]: [x * 2 for x in range(6) if not x % 2]
            Out[343]: [0, 4, 8]

        .. code-block:: python

            [name for name in dir(__builtin__) if "Error" in name]
            ['ArithmeticError',
             'AssertionError',
             'AttributeError',
             ....


Set Comprehensions
------------------

We can create comprehensions that build sets, too.
Simple loops like this:

.. code-block:: python

    new_set = set()
    for value in a_sequence:
        new_set.add(value)

can be translated to this:

.. code-block:: python

    new_set = {value for value in a_sequence}

.. slide:: Set Comprehensions
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: python

            new_set = {value for value in a_sequence}


        the same as this ``for`` loop:

        .. code-block:: python

            new_set = set()
            for value in a_sequence:
                new_set.add(value)

Example
*******

How can we find all the vowels in a given string?

.. code-block:: ipython

    In [19]: s = "a not very long string"

    In [20]: vowels = set('aeiou')

    In [21]: { let for let in s if let in vowels }
    Out[21]: {'a', 'e', 'i', 'o'}

As a side note, why do we use ``set('aeiou')`` rather than just ``"aeiou"``\ ?

.. slide:: Example
    :level: 3

    Finding all the vowels in a string...

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [19]: s = "a not very long string"

            In [20]: vowels = set('aeiou')

            In [21]: { let for let in s if let in vowels }
            Out[21]: {'a', 'e', 'i', 'o'}

        Side note: why ``set('aeiou')`` rather than just ``"aeiou"``\ ?


Dict Comprehensions
-------------------

And of course, you can do comprehensions with ``dicts`` too.

A simple loop building a ``dict``

.. code-block:: python

    new_dict = {}
    for key, value in a_sequence:
        new_dict[key] = value

can be expressed instead like so:

.. code-block:: python

    new_dict = { key:value for key, value in a_sequence}

.. slide:: Dict Comprehensions
    :level: 3

    .. rst-class:: build
    .. container::

        .. code-block:: python

            new_dict = { key:value for key, value in a_sequence}


        the same as this ``for`` loop:

        .. code-block:: python

            new_dict = {}
            for key, value in a_sequence:
                new_dict[key] = value

Example
*******

Let's build a mapping of integers to string templates:

.. code-block:: ipython

    In [22]: {i: "this_{0}".format(i) for i in range(5)}
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}

Could you accomplish the same thing with the ``dict`` type object constructor?

.. slide:: Example
    :level: 3

    build a mapping of integers and matching strings

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [22]: {i: "this_%i" % i for i in range(5)}
            Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
                      3: 'this_3', 4: 'this_4'}

        Can you do the same thing with the ``dict()`` constructor?


Anonymous functions
===================

We can create *anonymous functions* using the :keyword:`lambda <python2:lambda>` keyword (:py:keyword:`py3 <lambda>`).
We call these functions anonymous because they do not require a name.
They can only contain an expression.
Never a statement.
Do you remember the difference between those two?

.. slide:: Anonymous Functions
    :level: 3

    ``lambda`` (λ)

    .. code-block:: ipython

        In [171]: f = lambda x, y: x+y
        In [172]: f(2,3)
        Out[172]: 5

    .. rst-class:: build
    .. container::

        Content can only be an expression -- not a statement

        Anyone remember what the difference is?

        Called "Anonymous": it doesn't need a name.

A lambda function is a python function object, it can be stored in a list or other container.

.. code-block:: ipython

    In [6]: l = [lambda x, y: x + y]

    In [7]: l
    Out[7]: [<function __main__.<lambda>>]

    In [8]: type(l[0])
    Out[8]: function

And then you can call them:

.. code-block:: ipython

    In [9]: l[0](3,4)
    Out[9]: 7

.. slide:: Lambdas are Objects
    :level: 3

    You can hold them in lists or other containers:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [6]: l = [lambda x, y: x + y]

            In [7]: l
            Out[7]: [<function __main__.<lambda>>]

            In [8]: type(l[0])
            Out[8]: function


        And you can call them:

        .. code-block:: ipython

            In [9]: l[0](3,4)
            Out[9]: 7

As it turns out, you can do the same thing with "regular" functions too.
They are also first-class objects and can be handled as if they were data:

.. code-block:: ipython

    In [12]: def fun(x,y):
       ....:     return x + y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3, 4)
    Out[15]: 7

.. slide:: Functions are Objects
    :level: 3

    You can do that with "regular" functions too:

    .. code-block:: ipython

        In [12]: def fun(x,y):
           ....:     return x + y
           ....:
        In [13]: l = [fun]
        In [14]: type(l[0])
        Out[14]: function
        In [15]: l[0](3, 4)
        Out[15]: 7

Comprehensions and lambdas are tools in the Python toolbox.
Using them appropriately can allow us to approach programming in a *functional* style.


Functional Programming
======================

Python is not primarily a functional language.
However, there is nothing to stop you using Python in a functional style.
In fact, there are a number of tools that are provided to facilitate just that.
We've met comprehensions and lambdas above.
Here are a few more you can use.

The :func:`map <python2:map>` function (:py:func:`py3 <map>`) is used to apply a function to a sequence of objects:

.. code-block:: ipython

    In [23]: lst = [2, 5, 7, 12, 6, 4]
    In [24]: def fun(x):
                 return x * 2 + 10
    In [25]: map(fun, lst)
    Out[25]: [14, 20, 24, 34, 22, 18]

But if the function is as small as that, and you aren't going to use it elsewhere, use a lambda:

.. code-block:: ipython

    In [26]: map(lambda x: x * 2 + 10, lst)
    Out[26]: [14, 20, 24, 34, 22, 18]

.. slide:: ``map``
    :level: 3

    "maps" a function onto a sequence of objects

    .. rst-class:: build
    .. container::

        Applies the function to each item in the list, returning another list

        .. code-block:: ipython

            In [23]: lst = [2, 5, 7, 12, 6, 4]
            In [24]: def fun(x):
                         return x * 2 + 10
            In [25]: map(fun, lst)
            Out[25]: [14, 20, 24, 34, 22, 18]


        But if it's a small function, and you only need it once:

        .. code-block:: ipython

            In [26]: map(lambda x: x * 2 + 10, lst)
            Out[26]: [14, 20, 24, 34, 22, 18]


The :func:`filter <python2:filter>` function (:py:func:`py3 <filter>`) omits items from a sequence using a boolean *filter function*.
The returned list will only contain values for which the function returns ``True``.
For example, to get only the even number in a sequence:

.. code-block:: ipython

    In [27]: lst = [2, 5, 7, 12, 6, 4]
    In [28]: filter(lambda x: not x % 2, lst)
    Out[28]: [2, 12, 6, 4]

.. slide:: ``filter``
    :level: 3

    "filters" a sequence of objects with a boolean function

    .. rst-class:: build
    .. container::

        Keeps only those for which the function evaluates to ``True``

            To get only the even numbers:

            .. code-block:: ipython

                In [27]: lst = [2, 5, 7, 12, 6, 4]
                In [28]: filter(lambda x: not x % 2, lst)
                Out[28]: [2, 12, 6, 4]

The :func:`reduce <python2:reduce>` function (:py:func:`py3 <reduce>`) reduces a sequence of objects to a single return value.
The provided function must take two arguments and return one value.
It is called on the first pair in the sequence, then called again with the result and the third item in the sequence, and so on:

For example, to get the sum of a series of integers:

.. code-block:: ipython

    In [30]: l = [2, 5, 7, 12, 6, 4]
    In [31]: reduce(lambda x, y: x + y, l)
    Out[31]: 36

Or to get the product:

.. code-block:: ipython

    In [32]: reduce(lambda x,y: x*y, l)
    Out[32]: 20160

.. slide:: ``reduce``
    :level: 3

    "reduces" a sequence of objects to a single object

    .. rst-class:: build
    .. container::

        Use a function that combines pairs of objects

        To get the sum:

        .. code-block:: ipython

            In [30]: l = [2, 5, 7, 12, 6, 4]
            In [31]: reduce(lambda x, y: x + y, l)
            Out[31]: 36

        To get the product:

        .. code-block:: ipython

            In [32]: reduce(lambda x,y: x*y, l)
            Out[32]: 20160

You might ask (and many have), couldn't we do all of this with comprehensions?
The answer is an unambiguous **yes**:

.. code-block:: ipython

    In [33]: [x + 2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]
    In [34]: [x for x in l if not x % 2]
    Out[34]: [2, 12, 6, 4]

The exception of course is ``reduce``, but BDFL Guido Van Rossum has been known to assert that almost all uses of reduce really just boil down to :func:`sum <python2:sum>` (:py:func:`py3 <sum>`) anyway.

.. slide:: Comprehensions
    :level: 3

    Couldn't you do all this with comprehensions?

    .. rst-class:: build
    .. container::

        Yes:

        .. code-block:: ipython

            In [33]: [x + 2 + 10 for x in l]
            Out[33]: [14, 17, 19, 24, 18, 16]
            In [34]: [x for x in l if not x % 2]
            Out[34]: [2, 12, 6, 4]

        (except for ``reduce``)

        But Guido thinks almost all uses of reduce are really ``sum()``

Comprehensions, lambdas, and ``map``, ``filter``, and ``reduce`` are *functional programming* tools.
Historically speaking, ``map``, ``filter``, and ``reduce`` predate comprehensions.
There are those who prefer that syntax.
In addition, the ``map-reduce`` algorithm is a big concept these days.
It's often used to manage the processing of large amounts of data in parallel.
It's good to be aware of these tools in Python and understand how they work.

.. slide:: Functional Programming
    :level: 3

    Comprehensions and map, filter, reduce: "functional programming" approaches

    .. rst-class:: build
    .. container::

        Historically ``map``, ``filter``  and ``reduce``  pre-date comprehensions

        Some people like that syntax better

        "map-reduce" is a big concept these days

        Used for parallel processing of "Big Data" in NoSQL databases.

        (Hadoop, EMR, MongoDB, etc.)

One final *nifty trick* with lambda functions.
Lambdas can, of course, use keyword arguments.
And if you remember, the default values for keyword arguments are evaluated *when a function is defined*.

This combination turns out to be pretty handy at times:

.. code-block:: ipython

    In [186]: l = []
    In [187]: for i in range(3):
       .....:     l.append(lambda x, e=i: x**e)
       .....:
    In [189]: for f in l:
       .....:     print(f(3))
    1
    3
    9

.. slide:: A Lambda Trick
    :level: 3

    Lambdas can also use keyword arguments

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [186]: l = []
            In [187]: for i in range(3):
               .....:     l.append(lambda x, e=i: x**e)
               .....:
            In [189]: for f in l:
               .....:     print(f(3))
            1
            3
            9

        Note when the keyword argument is evaluated

        This turns out to be very handy!
