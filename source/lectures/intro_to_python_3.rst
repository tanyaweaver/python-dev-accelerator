.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 3
******************************

.. slide:: Introduction To Python: Part 3
    :level: 1

    .. rst-class:: center

    In which we learn about a few Python data structures and interacting with the file system.


During this lecture, we'll learn a bit about Python sequences, strings and dictionaries.
We'll also cover looping, both determinate and indeterminate.
Finally, we'll talk about how to interact with data from the file system.

Sequences
=========

Python is both strongly typed and dynamically typed.
This combination leads to an approach to programming we call "Duck Typing".
So long as an object behaves like the kind of thing we want, we can assume it *is* the kind of thing we want.

Sequences are a prime example of this type of thinking.

In Python, a sequence refers to an ordered collection of objects.
To be counted as a sequence, the object should support at least the following operations:

* Indexing
* Slicing
* Membership
* Concatenation
* Length
* Iteration

.. slide:: Sequences
    :level: 2

    .. rst-class:: center large

    Ordered collections of objects

.. slide:: What is a Sequence?
    :level: 3

    Remember Duck Typing?

    .. rst-class:: build
    .. container::

        Anything that supports *at least* these operations:

        .. rst-class:: build

        * Indexing
        * Slicing
        * Membership
        * Concatenation
        * Length
        * Iteration

There are a number of standard data types in Python that fulfill this contract.

========================= ====================
Python 2                  Python 3
========================= ====================
byte string (str)         byte string (bytes)
unicode string (unicode)  unicode string (str)
list                      list
tuple                     tuple
bytearray                 bytearray
buffer                    memoryview
xrange object             range object
========================= ====================

Of these types, the ones you will most often use are the string types, lists and tuples.
The others are largely crafted for special purposes and you will rarely see them.
However, the operations we will discuss next apply to all of them (with a few caveats).

.. slide:: Sequence Types
    :level: 3

    .. rst-class:: build
    .. container::

        .. rst-class:: build

            * strings
            * Unicode strings
            * lists
            * tuples
            * bytearrays
            * buffers
            * array.arrays
            * xrange objects (py2) or range objects (py3) [almost]

        Mostly use the string types, lists, tuples -- others are special purpose.

        The following applies to all of them (with some caveats)

Indexing
--------

We can look up an object from within a sequence using the subscription operator: ``[]``.
We use the ``index`` (position) of the object in the sequence to look it up.
In Python, indexing always starts at ``0``.

.. code-block:: ipython

    In [98]: s = u"this is a string"
    In [99]: s[0]
    Out[99]: u't'
    In [100]: s[5]
    Out[100]: u'i'

.. slide:: Indexing
    :level: 3

    Look up items by *index* using the subscription operator: ``[]``

    .. rst-class:: build
    .. container::

        Indexing in Python always starts at zero.

        .. code-block:: ipython

            In [98]: s = u"this is a string"
            In [99]: s[0]
            Out[99]: u't'
            In [100]: s[5]
            Out[100]: u'i'


We can also pass a negative integer as the index.
This returns the object ``n`` positions from the end of the sequence:

.. code-block:: ipython

    In [105]: s = u"this is a string"
    In [106]: s[-1]
    Out[106]: u'g'
    In [107]: s[-6]
    Out[107]: u's'

.. slide:: Negative Indexes
    :level: 3

    Count from the end:

    .. code-block:: ipython

        In [105]: s = u"this is a string"
        In [106]: s[-1]
        Out[106]: u'g'
        In [107]: s[-6]
        Out[107]: u's'

If you ask for an object by an index that is beyond the end of the sequence, this causes an ``IndexError``:

.. code-block:: ipython

    In [4]: s = [0, 1, 2, 3]
    In [5]: s[4]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-5-42efaba84d8b> in <module>()
    ----> 1 s[4]

    IndexError: list index out of range

.. slide:: Out of Range
    :level: 3

    It is an ``IndexError`` to ask for items beyond the end:

    .. code-block:: ipython

        In [4]: s = [0, 1, 2, 3]
        In [5]: s[4]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        <ipython-input-5-42efaba84d8b> in <module>()
        ----> 1 s[4]

        IndexError: list index out of range

Slicing
-------

Indexing returns one object from a sequence.
To get a new sequence containing elements from the original, we use ``slicing``.
This also uses the subscription operator, but with a bit of a syntactic twist.
We use one or more colons (``:``) to separate the three available arguments, *start*, *stop*, and *step*::

    seq[start:stop:step]

In slicing, asking for ``seq[start:stop]`` will return a new sequence (of the same type) containing all the elements of the original where ``start <= index < stop``.

.. code-block:: ipython

    In [121]: s = u"a bunch of words"
    In [122]: s[2]
    Out[122]: u'b'
    In [123]: s[6]
    Out[123]: u'h'
    In [124]: s[2:6]
    Out[124]: u'bunc'
    In [125]: s[2:7]
    Out[125]: u'bunch'

.. slide:: Slicing
    :level: 3

    Create a new sequence with a range from the original.

    .. rst-class:: build
    .. container::

        Also uses the subscription operator (``[]``)

        ``seq[start:finish]`` => seq[i] where start <= i < finish:

        .. code-block:: ipython

            In [121]: s = u"a bunch of words"
            In [122]: s[2]
            Out[122]: u'b'
            In [123]: s[6]
            Out[123]: u'h'
            In [124]: s[2:6]
            Out[124]: u'bunc'
            In [125]: s[2:7]
            Out[125]: u'bunch'

It can often be helpful in slicing to think of the index values as pointing to the spaces *between the items* in the sequence::

       a       b   u   n   c   h       o   f
     |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9

.. slide:: Helpful Hint
    :level: 3

    Indexes point to the spaces between the items::

           a       b   u   n   c   h       o   f
         |   |   |   |   |   |   |   |   |   |
         0   1   2   3   4   5   6   7   8   9

.. slide:: Slicing
    :level: 3

    ``start`` and ``finish`` are not required:

    .. code-block:: ipython

        In [6]: s = u"a bunch of words"
        In [7]: s[:5]
        Out[7]: u'a bun'
        In [8]: s[5:]
        Out[8]: u'ch of words'

    .. rst-class:: build
    .. container::

        Combine with negative indexing:

        .. code-block:: ipython

            In [4]: s = u'this_could_be_a_filename.txt'
            In [5]: s[:-4]
            Out[5]: u'this_could_be_a_filename'
            In [6]: s[-4:]
            Out[6]: u'.txt'


So why do we start with zero?
Why is the ``stop`` index in the slice **not** included?
Because doing things this way leads to some very nice properties for slices::

    len(seq[a:b]) == b-a

    seq[:b] + seq[b:] == seq

    len(seq[:b]) == b

    len(seq[-b:]) == b

As a result of these properties, it's easier to avoid off-by-one errors in Python.

.. slide:: Why start from zero?
    :level: 3

    Why is the "first" item indexed with zero?

    .. rst-class:: build
    .. container::

        Why is the last item in the slice **not** included?

        Nifty properties that result::

            len(seq[a:b]) == b-a

            seq[:b] + seq[b:] == seq

            len(seq[:b]) == b

            len(seq[-b:]) == b

        Fewer "off by one" errors as a result.

The third argument to the slice operation is the *step*.
It is used to control which items between *start* and *stop* are returned.

.. code-block:: ipython

    In [289]: string = u"a fairly long string"
    In [290]: string[0:15]
    Out[290]: u'a fairly long s'
    In [291]: string[0:15:2]
    Out[291]: u'afil ogs'
    In [292]: string[0:15:3]
    Out[292]: u'aallg'

Using a negative value for *step* can lead to a nifty way to reverse a sequence:

.. code-block:: ipython

    In [293]: string[::-1]
    Out[293]: u'gnirts gnol ylriaf a'

.. slide:: The Step Argument
    :level: 3

    Slicing takes a third argument, ``step``

    .. rst-class:: build
    .. container::

        Controls which items are returned:

        .. code-block:: ipython

            In [289]: string = u"a fairly long string"
            In [290]: string[0:15]
            Out[290]: u'a fairly long s'
            In [291]: string[0:15:2]
            Out[291]: u'afil ogs'
            In [292]: string[0:15:3]
            Out[292]: u'aallg'
            In [293]: string[::-1]
            Out[293]: u'gnirts gnol ylriaf a'

As we've mentioned before, indexing a sequence returns a single object.
Slicing returns a new sequence.
There's one other major difference between the two.
Slicing past the end of a sequence **does not cause an error**:

.. code-block:: ipython

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range
    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: "

.. slide:: Slicing vs. Indexing
    :level: 3

    Slicing and indexing have a few important differences:

    .. rst-class:: build
    .. container::

        Indexing returns one object always

        Slicing returns a sequence always.

        Slicing beyond the end is not an error:

        .. code-block:: ipython

            In [129]: s = "a bunch of words"
            In [130]: s[17]
            ----> 1 s[17]
            IndexError: string index out of range
            In [131]: s[10:20]
            Out[131]: ' words'
            In [132]: s[20:30]
            Out[132]: "

Membership
----------

Sequence types support using the membership operators: :keyword:`in <python2:in>` (:py:keyword:`py3 <in>`) and :keyword:`not in <python2:not in>` (:py:keyword:`py3 <not in>`).
These allow us to test for the presence (or absence) of an object in a sequence.

.. code-block:: ipython

    In [15]: s = [1, 2, 3, 4, 5, 6]
    In [16]: 5 in s
    Out[16]: True
    In [17]: 42 in s
    Out[17]: False
    In [18]: 42 not in s
    Out[18]: True

.. slide:: Membership
    :level: 3

    Membership operators (``in``, ``not in``):

    .. code-block:: ipython

        In [15]: s = [1, 2, 3, 4, 5, 6]
        In [16]: 5 in s
        Out[16]: True
        In [17]: 42 in s
        Out[17]: False
        In [18]: 42 not in s
        Out[18]: True

When used with the string types, the membership operators behave like ``substring`` in other languages.
Use them to test whether a string contains another, shorter string:

.. code-block:: ipython

    In [20]: s = u"This is a long string"
    In [21]: u"long" in s
    Out[21]: True

This is *only* true for the string-type sequences.  Can you think of why that might be?

.. slide:: Membership in Strings
    :level: 3

    Membership operations ≈ ``substring`` in other languages:

    .. code-block:: ipython

        In [20]: s = u"This is a long string"
        In [21]: u"long" in s
        Out[21]: True

    .. rst-class:: build
    .. container::

        **Not** for sub-sequences of other types

        .. code-block:: ipython

            In [22]: s = [1, 2, 3, 4]
            In [23]: [2, 3] in s
            Out[23]: False

        Why?

Concatenation
-------------

When used with sequences as operands, the ``+`` and ``*`` operators will *concatenate* sequences.

.. code-block:: ipython

    In [25]: s1 = u"left"
    In [26]: s2 = u"right"
    In [27]: s1 + s2
    Out[27]: u'leftright'
    In [28]: (s1 + s2) * 3
    Out[28]: u'leftrightleftrightleftright'

.. slide:: Concatenation
    :level: 3

    ``+`` or ``*`` will *concatenate* sequences:

    .. code-block:: ipython

        In [25]: s1 = u"left"
        In [26]: s2 = u"right"
        In [27]: s1 + s2
        Out[27]: u'leftright'
        In [28]: (s1 + s2) * 3
        Out[28]: u'leftrightleftrightleftright'

Since slicing returns *a new sequence*, this applies to slices as well.
This fact can allow for some very concise code.

For example (from CodingBat) lets assume you need to create a new string that contains three repetitions of a given string.
But if the given string is longer than three characters, you only want to use the first three.

A not-particularly-Pythonic solution to the problem might look like this:

.. code-block:: python

    def front3(str):
      if len(str) < 3:
        return str+str+str
      else:
        return str[:3]+str[:3]+str[:3]

But the truly Pythonic programmer can express the same thing this way:

.. code-block:: python

    def front3(str):
        return str[:3] * 3


.. slide:: Multiplying and Slicing
    :level: 3

    Applies to slices as well

    .. rst-class:: build
    .. container::

        Allows very concise code

        from CodingBat: Warmup-1 -- front3

        .. container::

            Non-Pythonic:

            .. code-block:: python

                def front3(str):
                  if len(str) < 3:
                    return str+str+str
                  else:
                    return str[:3]+str[:3]+str[:3]

        .. container::

            Pythonic:

            .. code-block:: python

                def front3(str):
                    return str[:3] * 3

Length
------

Sequences have *length*.
To get the length of a sequence we use the :func:`len <python2:len>` builtin (:py:func:`py3 <len>`).

.. code-block:: ipython

    In [36]: s = u"how long is this, anyway?"
    In [37]: len(s)
    Out[37]: 25

.. slide:: Length
    :level: 3

    Sequences have length

    .. rst-class:: build
    .. container::

        Use the ``len`` builtin to get it

        .. code-block:: ipython

            In [36]: s = u"how long is this, anyway?"
            In [37]: len(s)
            Out[37]: 25

        Zero-based indexing, last index is ``len(s) - 1``

        .. code-block:: ipython

            In [38]: count = len(s)
            In [39]: s[len(s)]
            ------------------------------------------------------------
            IndexError                Traceback (most recent call last)
            <ipython-input-39-5a33b9d3e525> in <module>()
            ----> 1 s[count]
            IndexError: string index out of range

        Who cares? Use ``s[-1]``

Because of zero-based indexing, you must remember that the last index in a sequence is always ``len(s) -1``:

.. code-block:: ipython

    In [38]: count = len(s)
    In [39]: s[len(s)]
    ------------------------------------------------------------
    IndexError                Traceback (most recent call last)
    <ipython-input-39-5a33b9d3e525> in <module>()
    ----> 1 s[count]
    IndexError: string index out of range

But honestly, using that is not Pythonic anyway.
Always use ``seq[-1]`` to find the last item in a sequence.

If you care (and some do) about why Python uses ``len(x)`` instead of ``x.length()``, you can `read this post <http://effbot.org/pyfaq/why-does-python-use-methods-for-some-functionality-e-g-list-index-but-functions-for-other-e-g-len-list.htm>`_ with an explanation of the rationale from BDFL Guido Van Rossom.

Miscellaneous
-------------

There are a few other :ref:`common operations <python2:typesseq>` (:py:ref:`py3 <typesseq-common>`) on sequences you'll want to know about.

The :func:`min <python2:min>` (:py:func:`py3 <min>`) and :func:`max <python2:max>` (:py:func:`py3 <max>`) builtins work as you might expect:

.. code-block:: ipython

    In [42]: all_letters = u"thequickbrownfoxjumpedoverthelazydog"
    In [43]: min(all_letters)
    Out[43]: u'a'
    In [44]: max(all_letters)
    Out[44]: u'z'

.. slide:: Min and Max
    :level: 3

    Sequences support ``min`` and ``max`` builtins:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [42]: all_letters = u"thequickbrownfoxjumpedoverthelazydog"
            In [43]: min(all_letters)
            Out[43]: u'a'
            In [44]: max(all_letters)
            Out[44]: u'z'

        Why does that work?

The ``index`` method returns the position of an object in a sequence.
If the object is not in the sequence, this causes a ``ValueError``:

.. code-block:: ipython

    In [46]: all_letters.index(u'd')
    Out[46]: 21

.. code-block:: ipython

    In [47]: all_letters.index(u'A')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-47-2db728a46f78> in <module>()
    ----> 1 all_letters.index(u'A')

    ValueError: substring not found

.. slide:: Index
    :level: 3

    Sequences also support the ``index`` method

    .. code-block:: ipython

        In [46]: all_letters.index(u'd')
        Out[46]: 21

    .. rst-class:: build
    .. container::

        ``ValueError`` if item not in sequence:

        .. code-block:: ipython

            In [47]: all_letters.index(u'A')
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-47-2db728a46f78> in <module>()
            ----> 1 all_letters.index(u'A')

            ValueError: substring not found

Finally, the ``count`` method will count the total number of occurances of an object within a sequence.
With strings, the object can be a single letter, or a substring.
With the ``count`` method, if the object is not in the sequence, then no error is raised.
The return value is ``0``:

.. code-block:: ipython

    In [52]: all_letters.count(u'o')
    Out[52]: 4
    In [53]: all_letters.count(u'the')
    Out[53]: 2

.. code-block:: ipython

    In [54]: all_letters.count(u'A')
    Out[54]: 0

.. slide:: Count
    :level: 3

    Sequence supports the ``count`` method.

    .. code-block:: ipython

        In [52]: all_letters.count(u'o')
        Out[52]: 4
        In [53]: all_letters.count(u'the')
        Out[53]: 2

    .. rst-class:: build
    .. container::

        No errors from this:

        .. code-block:: ipython

            In [54]: all_letters.count(u'A')
            Out[54]: 0

Iteration
=========

Repetition, Repetition, Repetition, Repe...

.. slide:: Iteration
    :level: 2

    .. rst-class:: left

    Repetition, Repetition, Repetition, Repe...

For Loops
---------

We've already seen simple iteration over a sequence using ``for ... in``:

.. code-block:: ipython

    In [170]: for x in "a string":
       .....:         print(x)
       .....:
    a

    s
    t
    r
    i
    n
    g

.. slide:: For Loops
    :level: 3

    We've seen simple iteration over a sequence with ``for ... in``:

    .. code-block:: ipython

        In [170]: for x in "a string":
           .....:         print(x)
           .....:
        a

        s
        t
        r
        i
        n
        g

Other languages build and use an ``index``, which is then used to extract each item from the sequence:

.. code-block:: javascript

    for(var i=0; i<arr.length; i++) {
        var value = arr[i];
        console.log(i + ") " + value);

Python does not require this.
But if you need to have the index for some reason, you can use the :func:`enumerate <python2:enumerate>` builtin (:py:func:`py3 <enumerate>`):

.. code-block:: ipython

    In [140]: for idx, letter in enumerate(u'Python'):
       .....:     print(idx, letter, end=' ')
       .....:
    0 P 1 y 2 t 3 h 4 o 5 n


.. slide:: No Indexing Required
    :level: 3

    Other languages build and use an ``index``:

    .. code-block:: javascript

        for(var i=0; i<arr.length; i++) {
            var value = arr[i];
            alert(i + ") " + value);

    .. rst-class:: build
    .. container::

        If you need an index, though you can use ``enumerate``:

        .. code-block:: ipython

            In [140]: for idx, letter in enumerate(u'Python'):
               .....:     print(idx, letter, end=' ')
               .....:
            0 P 1 y 2 t 3 h 4 o 5 n

We've seen how the ``range`` function (it's a type in Python3) can be useful for looping a known number of times.
This is especially true when you don't care about the value of the item from the sequence:

.. code-block:: ipython

    In [171]: for i in range(5):
       .....:     print('hello')
       .....:
    hello
    hello
    hello
    hello
    hello

.. slide:: ``range`` and For Loops
    :level: 3

    Useful for looping a known number of times:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [171]: for i in range(5):
               .....:     print(i)
               .....:
            0
            1
            2
            3
            4

        ``i`` is not used (though it could be)

.. slide:: No Namespace
    :level: 3

    Loops do not create a local namespace:

Remember that in Python, loops do not create a local namespace.
The loop variable you use is *still in scope* after the loop terminates:

.. code-block:: ipython

    In [172]: x = 10
    In [173]: for x in range(3):
       .....:     pass
       .....:
    In [174]: x
    Out[174]: 2


Loop control
------------

Sometimes you want to interrupt or alter the flow of control through a loop.
Loops can be controlled in two ways, with ``break`` and ``continue``.

.. slide:: Loop Control
    :level: 3

    Interrupt or alter the flow of control through a loop

    .. rst-class:: build
    .. container::

        Two possibilities:

        ``break``

        ``continue``

The ``break`` statement causes a loop to terminate immediately:

.. code-block:: ipython

    In [141]: for i in range(101):
       .....:     print(i)
       .....:     if i > 50:
       .....:         break
       .....:
    0 1 2 3 4 5... 46 47 48 49 50 51

.. slide:: Break
    :level: 3

    Causes a loop to immediately terminate:

    .. code-block:: ipython

        In [141]: for i in range(101):
           .....:     print(i)
           .....:     if i > 50:
           .....:         break
           .....:
        0 1 2 3 4 5... 46 47 48 49 50 51

And ``continue`` returns you immediately to the head of the loop.
It allows you to skip statements later in the loop block while continuing the loop itself:

.. code-block:: ipython

    In [143]: for in in range(101):
       .....:     if i > 50:
       .....:         break
       .....:     if i < 25:
       .....:         continue
       .....:     print(i),
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. slide:: Continue
    :level: 3

    Skip statements later in the loop block

    .. rst-class:: build
    .. container::

        Allow iteration to continue:

        .. code-block:: ipython

            In [143]: for in in range(101):
               .....:     if i > 50:
               .....:         break
               .....:     if i < 25:
               .....:         continue
               .....:     print(i),
               .....:
               25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

An interesting feature of Python loops is that there is an optional ``else`` clause.
The statements in this optional block are only executed if the loop exits *normally*.
That means only if ``break`` was not used to stop iteration:

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print(u'finished')
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print(x)
       .....:         break
       .....: else:
       .....:     print(u'finished')
    5

This can be surprisingly useful, even if the name is a bit hard to remember.

.. slide:: Else
    :level: 3

    For loops can also take an optional ``else`` block

    .. rst-class:: build
    .. container::

        Executed only when the loop exits *normally* (not via break):

        .. code-block:: ipython

            In [147]: for x in range(10):
               .....:     if x == 11:
               .....:         break
               .....: else:
               .....:     print(u'finished')
            finished
            In [148]: for x in range(10):
               .....:     if x == 5:
               .....:         print(x)
               .....:         break
               .....: else:
               .....:     print(u'finished')
            5

        Useful, if poorly named

While Loops
-----------

The ``while`` keyword is for when you don't know how many loops you need.
It continues to execute the body until condition is not ``True``::

    while a_condition:
       some_code
       in_the_body

.. slide:: While Loops
    :level: 3

    When you don't know when you will stop

    .. rst-class:: build
    .. container::

        Continues until ``condition`` is not ``True``::

            while a_condition:
               some_code
               in_the_body

While loops are more general than ``for`` loops.
You can always express a ``for`` loop using the ``while`` structure, but the reverse is not always true.
On the other hand, ``while`` is more error prone.
You must remember to make progress in the body of the loop in order to allow the condition to become ``False``.
Otherwise you can fall victim to *infinite loops*.

.. code-block:: python

    i = 0;
    while i < 5:
        print(i)

.. slide:: ``while`` vs. ``for``
    :level: 3

    ``while``  is more general than ``for``

    .. rst-class:: build
    .. container::

        You can always express ``for`` as ``while``,

        Not always the reverse

        ``while``  is more error-prone

        Loop body must make progress, so condition can become ``False``

        Potential error -- infinite loops:

        .. code-block:: python

            i = 0;
            while i < 5:
                print(i)

There are three approaches to terminating a ``while`` loop.
You can use the ``break`` statement to end iteration:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print(i, end=' ')
       .....:
    1 2 3 4 5 6 7 8 9 10

.. slide:: Terminating via ``break``
    :level: 3

    .. code-block:: ipython

        In [150]: while True:
           .....:     i += 1
           .....:     if i > 10:
           .....:         break
           .....:     print(i, end=' ')
           .....:
        1 2 3 4 5 6 7 8 9 10

Another approach is to set a ``flag variable``.
The boolean value of this variable starts as ``True``
Operations inside the loop update it to ``False``, terminating the loop:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print(num)
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. slide:: Terminating via flag
    :level: 3

    .. code-block:: ipython

        In [156]: import random
        In [157]: keep_going = True
        In [158]: while keep_going:
           .....:     num = random.choice(range(5))
           .....:     print(num)
           .....:     if num == 3:
           .....:         keep_going = False
           .....:
        3

Finally, you can use a straight conditional statement as the test.
Here, you update the value of the ``test variable`` such that the condition will evaluate to ``False``:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print(i)
       .....:
    0 0 2 3 4 6 8 8 8 9 12

.. slide:: Terminating via condition
    :level: 3

    .. code-block:: ipython

        In [161]: while i < 10:
           .....:     i += random.choice(range(4))
           .....:     print(i)
           .....:
        0 0 2 3 4 6 8 8 8 9 12

Similarities
------------

Both ``for`` and ``while`` loops can use ``break`` and ``continue`` for internal flow control.
Both ``for`` and ``while`` loops can have an optional ``else`` block.
In both loops, the statements in the ``else`` block are only executed if the loop terminates normally (no ``break``).

.. slide:: Similarities
    :level: 3

    ``break`` and ``continue``

    .. rst-class:: build
    .. container::

        optional ``else``

        ``else`` only reached with *normal termination*

String Features
===============

.. rst-class:: center large

  Fun with Strings

.. slide:: String Features
    :level: 2

    .. rst-class:: large center

    Fun with Strings

Unicode v. Bytes
----------------

Python has two string types: ``byte strings`` and ``unicode objects``.

Unicode is a classification system intended to allow a representation of *all possible characters* in all possible languages.
Each character has a *code point* that is a byte or bytes which represents that character.
When printed, these code points are translated into appropriate glyphs by the operating system.

When working in Python, you should always handle *text* as ``unicode objects``.
Text can be defined as any string meant to be read by a human via some output device.

Handling of unicode and bytes in Python3 is *significantly different* from Python2.
In order to create compatible code (that will run the same in both systems), you should use one of the following two strategies:

You can import ``unicode_literals`` from the ``__future__`` library.
This must be the *first line of code* in your Python module.

.. code-block:: python

    from __future__ import unicode_literals
    'this is a unicode string with élan'

Another approach is to be explicit about what type of string you are writing, using ``object literals``:

.. code-block:: python

    u'this is a unicode string with élan'

The former strategy is a bit easier, but is not always safe in older legacy code bases, as it is an all-or-nothing operation.
It makes *every single string* in the file a unicode object.
The latter strategy is safer in this respect, as you get to choose which is which.

You can `read more about compatible string handling <http://python-future.org/compatible_idioms.html#strings-and-bytes>`_ at the Python-Future website.

.. slide:: Unicode
    :level: 3

    Unicode is a system for representing *all* the characters

    .. rst-class:: build
    .. container::

        When handling text *in* Python, always use unicode

        For compatibility:

        .. code-block:: python

            from __future__ import unicode_literals
            'this is a unicode string with élan'

        .. code-block:: python

            u'this is a unicode string with élan'

        The former is easier, the latter safer (esp for legacy code)

Byte strings are strings that are composed entirely of numbers.
This can be a bit confusing because they often appear to be letters.
The string ``b"a"`` appears to contain the letter ``a``, but really it contains the number ``97`` (or ``01100001``).
Your terminal, your text editor, your OS is responsible for translating those numbers into characters when showing you the content of the string.
But it's still the number underneath.
Be cautious about your assumptions.

Again, you have two strategies to work with bytestrings safely in Python 2 and Python 3.
You can import ``unicode_literals`` and then specifically mark certain strings as bytestrings.
Or you can mark certain strings as bytestrings.
In either case, you have to mark bytestrings:

.. code-block:: python

    from __future__ import unicode_literals
    b'polishing my resum\xc3\xa9 this week'

.. code-block:: python

    b'polishing my resum\xc3\xa9 this week'

.. slide:: Bytes
    :level: 3

    *Bytestrings* are strings composed entirely of numbers.

    .. rst-class:: build
    .. container::

        You see a letter "a"

        The bytestring *contains* ``97`` (really ``01100001``)

        This hurts heads a bit.  Be careful about assumptions

        For compatibility:

        .. code-block:: python

            from __future__ import unicode_literals
            b'polishing my resum\xc3\xa9 this week'

        .. code-block:: python

            b'polishing my resum\xc3\xa9 this week'

The conversion of bytes to unicode and vice-versa should always take place at the *I/O boundary*.
That means on the point where data is passing out of Python to the filesystem or network.
Or the point where data enters Python from the filesystem or network.

At the point of crossing *outbound*, we can use the ``encode`` method of unicode objects to convert them to bytes.
The argument to this function controls which ``codec`` is used to make the conversion.
``UTF8`` is the most common codec in web work.

.. code-block:: ipython

    In [1]: fancy = u"Resumé"
    In [2]: fancy
    Out[2]: 'Resumé'
    In [3]: fancy.encode('utf8')
    Out[3]: b'Resum\xc3\xa9'

When data is *inbound* to Python, we can use the ``decode`` method of a byte string to convert it to Unicode.
Again, passing a ``codec`` name selects which should be used for the conversion:

.. code-block:: ipython

    In [4]: bytes = _
    In [5]: bytes
    Out[5]: b'Resum\xc3\xa9'
    In [6]: bytes.decode('utf8')
    Out[6]: 'Resumé'

If no ``codec`` is specified, Python defaults to using the default encoding for the Python instance.
This is usually ``ascii`` and is almost never the thing you really want.
Be specific.

.. slide:: Bytes <===> Unicode
    :level: 3

    Always convert at the I/O boundary

    .. rst-class:: build
    .. container::

        *Encode* unicode to bytes when crossing *outbound*

        .. code-block:: ipython

            In [1]: fancy = u"Resumé"
            In [2]: fancy
            Out[2]: 'Resumé'
            In [3]: fancy.encode('utf8')
            Out[3]: b'Resum\xc3\xa9'

        *Decode* bytes to unicode when crossing *inbound*

        .. code-block:: ipython

            In [4]: bytes = _
            In [5]: bytes
            Out[5]: b'Resum\xc3\xa9'
            In [6]: bytes.decode('utf8')
            Out[6]: 'Resumé'

In Python 2, conversion of bytes to unicode and back was one of the largest sources of problems in programs.
Both the ``encode`` and ``decode`` methods were supported by both byte strings and unicode objects.
This led to a lot of *implicit conversion*, which of course uses default encoding.

It's very easy when working entirely in English to have these types of problems an not know about them.
If the characters in a string fall entirely within the ascii set, then no errors will occur.
But as soon as characters beyond ascii are used, all sorts of trouble pops up.

Watch for ``UnicodeDecodeError`` and ``UnicodeEncodeError`` and write tests that use non-ascii characters.

.. slide:: Legacy Problems
    :level: 3

    Once of the biggest sources of problems in Python 2

    .. rst-class:: build
    .. container::

        Bytestrings can be "encoded"

        Unicode objects can be "decoded"

        Implicit type conversions

        No encoding specified

        Falls back to ``sys.getdefaultencoding()`` (usually ``ascii``)

        **BOOM!** ``UnicodeDecodeError`` or ``UnicodeEncodeError``

String Manipulation
-------------------

You can break strings apart using the :meth:`split <python2:str.split>` (:py:meth:`py3 <str.split>`) method.
You have to make sure that the string you are splitting and the string you are using to split it are of the same type (bytes or unicode).
The result is a list of the pieces:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']

In the other direction, calling the :meth:`join <python2:str.join>` (:py:meth:`py3 <str.join>`) method will connect a sequence of *pieces* using the string on which it is called:

.. code-block:: ipython

    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'

.. slide:: Manipulation
    :level: 3

    ``split`` and ``join``:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [167]: csv = "comma, separated, values"
            In [168]: csv.split(', ')
            Out[168]: ['comma', 'separated', 'values']
            In [169]: psv = '|'.join(csv.split(', '))
            In [170]: psv
            Out[170]: 'comma|separated|values'

        Use the same type (bytes and bytes, unicode and unicode)

        Mixing types causes ``TypeError``

There are methods that allow us to change the case of text:

.. code-block:: ipython

    In [171]: sample = u'A long string of words'
    In [172]: sample.upper()
    Out[172]: u'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: u'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: u'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: u'A Long String Of Words'

.. slide:: Case Switching
    :level: 3

    .. code-block:: ipython

        In [171]: sample = u'A long string of words'
        In [172]: sample.upper()
        Out[172]: u'A LONG STRING OF WORDS'
        In [173]: sample.lower()
        Out[173]: u'a long string of words'
        In [174]: sample.swapcase()
        Out[174]: u'a LONG STRING OF WORDS'
        In [175]: sample.title()
        Out[175]: u'A Long String Of Words'

And there are methods that allow us to test the nature of the characters in the text:

.. code-block:: ipython

    In [181]: number = u"12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = u"Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False

.. slide:: Testing
    :level: 3

    .. code-block:: ipython

        In [181]: number = u"12345"
        In [182]: number.isnumeric()
        Out[182]: True
        In [183]: number.isalnum()
        Out[183]: True
        In [184]: number.isalpha()
        Out[184]: False
        In [185]: fancy = u"Th!$ $tr!ng h@$ $ymb0l$"
        In [186]: fancy.isalnum()
        Out[186]: False

Every character in a string has a numeric value.
To see this value, use the :func:`ord <python2:ord>` (:py:func:`py3 <ord>`) builtin.
The :func:`chr <python2:chr>` (:py:func:`py3 <chr>`) builtin reverses the process:

.. code-block:: ipython

    In [109]: for i in 'Cris':
       .....:     print(ord(i), end=' ')
    67 114 105 115
    In [110]: for i in (67,114,105,115):
       .....:     print(chr(i), end=' ')
    C r i s

.. slide:: Ordinal Values
    :level: 3

    Every character is *also* a number

    .. rst-class:: build
    .. container::

        Use the ``ord`` builtin to see it

        Use the ``chr`` builtin to get the character back

        "ASCII" values: 1-127

        "ANSI" values: 1-255

        .. code-block:: ipython

            In [109]: for i in 'Chris':
               .....:     print(ord(i), end=' ')
            67 104 114 105 115
            In [110]: for i in (67,104,114,105,115):
               .....:     print(chr(i), end=' ')
            C h r i s

Building Strings
----------------

The concatenation operator ``+`` works for building strings out of fragments.
But it's not an efficient way to work.
Avoid it.

Instead, use *string formatting*:

.. code-block:: python

    'Hello {0}!'.format(name)

It's faster, and easier to maintain over time.

.. slide:: Building Strings
    :level: 3

    You can, but please don't do this:

    .. code-block:: python

        'Hello ' + name + '!'

    .. rst-class:: build
    .. container::

        Do this instead:

        .. code-block:: python

            'Hello {0}!'.format(name)

        Faster and safer, and easier to modify

        https://docs.python.org/3/library/string.html#formatstrings


When building a format string, the *placeholder* is a pair of curly braces.
They can be empty, but it's better to put an integer into one, indicating the *index* of the argument to :meth:`format <python2:str.format>` (:py:meth:`py3 <str.format>`) to use.
You can also pass keyword arguments to ``format``, if the placeholders contain names instead of integers:

.. code-block:: python

    "My name is {1} {0}".format('Ewing', 'Cris')

.. code-block:: python

    "The {name} are {status}!".format(
        name='Seahawks', status='awesome'
    )


.. slide:: String Formatting
    :level: 3

    ``str.format(*args, **kwargs)``

    .. rst-class:: build
    .. container::

        placeholders are curly braces

        .. container::

            *args* are matched positionally:

            .. code-block:: python

                "My name is {1} {0}".format('Ewing', 'Cris')

        .. container::

            *kwargs* are matched by name:

            .. code-block:: python

                "The {name} are {status}!".format(
                    name='Seahawks', status='awesome'
                )

Especially in legacy code you will see another method of formatting, using the ``%`` operator.

.. code-block:: python

    "This is a %s %s" % ('format', 'template')

This is still a functioning alternative and there is no pressing need to update.
But you should prefer the new style in writing new code.
The only dividing line is that the ``%`` operator supports both bytes and unicode objects, where in Python 3, ``.format`` is only a method on unicode objects.

There is a `good website <https://pyformat.info/>`_ available that will help you learn everything you  want to know about the formatting mini-language you can use to control these format specifiers.

.. slide:: The Old Way
    :level: 3

    You'll see this too:

    .. code-block:: python

        "This is a %s %s" % ('format', 'template')

    .. rst-class:: build
    .. container::

        This is being phased out, though it is still common

        Lots of good information about both:

        https://pyformat.info/

        Compatibility Announcement:

        .. rst-class:: build

        * ``%``: bytestrings and unicode
        * ``.format``: unicode only

        Text as Text should always be unicode

Dictionaries and Sets
=====================

Dictionaries in Python are a *mapping* of keys to values.
In other languages, they are called:

* associative array
* map
* hash table
* hash
* key-value pair

The correct name of the type in Python is :class:`dict <python2:dict>` (:py:class:`py3 <dict>`)

.. slide:: Dictionary
    :level: 2

    .. rst-class:: left
    .. container::

        Python calls it a ``dict``

        .. rst-class:: build
        .. container::

            Also referred to by the category ``mapping types``

            Other languages call it:

            .. rst-class:: build

            * dictionary
            * associative array
            * map
            * hash table
            * hash
            * key-value pair


You can build a new ``dict`` in a number of ways.

You can use the *object literal*:

.. code-block:: python

    {'key1': 3, 'key2': 5}

You can call the ``dict`` type object with a sequence of two-tuples.
The first in each will become the key, the second the value:

.. code-block:: python

    >>> dict([('key1', 3),('key2', 5)])
    {'key1': 3, 'key2': 5}

You can also use *keyword arguments* to the ``dict`` type object.
In this case, you are limited to keys which are *legal python names*:

.. code-block:: python

    >>> dict(key1=3, key2=5)
    {'key1': 3, 'key2': 5}

.. slide:: Dict Constructors
    :level: 3

    Object literal (``{}``):

    .. code-block:: python

        {'key1': 3, 'key2': 5}

    .. rst-class:: build
    .. container::

        .. container::

            The ``dict`` type object with a sequence of two-tuples:

            .. code-block:: python

                >>> dict([('key1', 3),('key2', 5)])
                {'key1': 3, 'key2': 5}

        .. container::

            Or with keyword arguments:

            .. code-block:: python

                >>> dict(key1=3, key2=5)
                {'key1': 3, 'key2': 5}

Indexing
--------

To look up a value in a ``dict``, we use the *subscription* operator, just like with sequences:

.. code-block:: python

    >>> d = {'name': 'Brian', 'score': 42}
    >>> d['score']
    42
    >>> d = {1: 'one', 0: 'zero'}
    >>> d[0]
    'zero'

If you provide a key that is *not* in the dictionary, a ``KeyError`` is caused:

.. code-block:: python

    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'

In a certain sense, Python is built on ``dicts``.
Namespaces are implemented as dicts.
For this reason, the performance of lookup is *highly optimized*.
Lookup time for any object is constant, regardless of the size of the ``dict``.

.. slide:: Dictionary Indexing
    :level: 3

    Uses the ``subscription`` operator (like list/tuple indexing)

    .. code-block:: python

        >>> d = {'name': 'Brian', 'score': 42}
        >>> d['score']
        42
        >>> d = {1: 'one', 0: 'zero'}
        >>> d[0]
        'zero'
        >>> d['non-existing key']
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 'non-existing key'

    Lookup is *highly optimized* (namespaces are dicts)

When storing a value in a ``dict``, you use a ``key``.
This key can be any *immutable object* (more on that later).
In actuality, any object that is *hashable* can be used.
What does that mean, though?

.. slide:: Dictionary Keys
    :level: 3

    Keys can be any **immutable** object:

    .. rst-class:: build

    * number
    * string
    * tuple

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [325]: d[3] = 'string'
            In [326]: d[3.14] = 'pi'
            In [327]: d['pi'] = 3.14
            In [328]: d[ (1,2,3) ] = 'a tuple key'
            In [329]: d[ [1,2,3] ] = 'a list key'
               TypeError: unhashable type: 'list'


        Actually -- any "hashable" type.

Hashing
-------

Hashing is the process of converting arbitrarily large data to a small proxy (usually an integer).
You can use any number of different algorithms to do this, MD5, SHA, etc.
The *key* (if you'll forgive the pun) is that the algorithm must *always* return the same proxy for the same input.
In a ``dict``, keys are hashed to an integer proxy, which is used to find a location in an array behind the scenes.
This is efficient because a good hashing algorithms means only a very few key/value pairs correlate to any proxy.

What would happen if the proxy changed *after* a value was stored in the ``dict``?
Hashability requires that the object being hashed be immutable.



.. slide:: Hashing
    :level: 3

    Convert arbitrarily large data to a small proxy (usually int)

    .. rst-class:: build
    .. container::

        Always return the same proxy for the same input

        MD5, SHA, etc

        Dict keys are hashed to an integer proxy which is used to find the key and value.

        Efficient, hash leads directly to a bucket with very few keys (often just one)

        What would happen if the proxy changed after storing a key?

        Hashability requires immutability

        Key lookup is very efficient

        Same average time regardless of size

``Dicts`` are inherently *unordered* collections.
When you print them out, or look at them in the interpreter, this is not apparent.
You will be fooled into thinking that you can rely on the order of the pairs.
This is *not true*.

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: d
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: ['three', 'two', 'one']

.. slide:: Unordered
    :level: 3

    Dictionaries have no defined order

    .. code-block:: ipython

        In [352]: d = {'one':1, 'two':2, 'three':3}
        In [353]: d
        Out[353]: {'one': 1, 'three': 3, 'two': 2}
        In [354]: d.keys()
        Out[354]: ['three', 'two', 'one']

    .. rst-class:: build
    .. container::

        You will be fooled by what you see

        Think that the order of pairs can be relied on.

        It cannot.

Iteration and Dicts
-------------------

You can use a ``dict`` with a for loop.
By default, the keys are what are iterated over.

.. code-block:: ipython

    In [15]: d = {'name': 'Brian', 'score': 42}

    In [16]: for x in d:
       ....:     print(x)
       ....:
    score
    name

.. slide:: Iteration
    :level: 3

    ``for``  iterates over the keys

    .. code-block:: ipython

        In [15]: d = {'name': 'Brian', 'score': 42}

        In [16]: for x in d:
           ....:     print(x)
           ....:
        score
        name

    (note the different order...)

If you want to iterate over values, or perhaps over the key/value pairs in the ``dict`` there are methods to support that.

.. code-block:: ipython

    In [2]: d.keys()
    Out[2]: dict_keys(['score', 'name'])

.. code-block:: ipython

    In [3]: d.values()
    Out[3]: dict_values([42, 'Brian'])

.. code-block:: ipython

    In [4]: d.items()
    Out[4]: dict_items([('score', 42), ('name', 'Brian')])

.. slide:: Iterator Methods
    :level: 3

    .. code-block:: ipython

        In [1]: d = {'name': 'Brian', 'score': 42}

    .. rst-class:: build
    .. container::

        Get all keys with ``dict.keys()``:

        .. code-block:: ipython

            In [2]: d.keys()
            Out[2]: dict_keys(['score', 'name'])

        All values with ``dict.values()``:

        .. code-block:: ipython

            In [3]: d.values()
            Out[3]: dict_values([42, 'Brian'])

        All key/value pairs with ``dict.items()``:

        .. code-block:: ipython

            In [4]: d.items()
            Out[4]: dict_items([('score', 42), ('name', 'Brian')])

In Python 2, there were nine methods on ``dicts`` that supplied these behaviors.
The ``keys``, ``values`` and ``items`` methods returned lists.
The ``iter...`` methods (``iterkeys``, etc.) returned iterators, which were much more efficient for large ``dicts``.
The ``view...`` methods (``viewkeys``, etc.) return *dict views* which behaved as iterators, but also updated themselves as the dictionary changed.

In Python 3, the three remainin methods operate like the last of those.
To get semantically equivalent code in Python 3, use the following map:

=============== =================
Python 2        Python 3
=============== =================
d.keys()        list(d.keys())
d.values()      list(d.values())
d.items()       list(d.items())
d.iterkeys()    iter(d.keys())
d.itervalues()  iter(d.values())
d.iteritems()   iter(d.items())
d.viewkeys()    d.keys()
d.viewvalues()  d.values()
d.viewitems()   d.items()
=============== =================

You should also refer to `Python Futures <http://python-future.org/compatible_idioms.html#dict-keys-values-items-as-a-list>`_ for additional compatible idioms.

.. slide:: Compatibility Note
    :level: 3

    In Python 2, these methods return lists

    .. rst-class:: build
    .. container::

        Each method has an ``iter...`` twin (``iterkeys``,...)

        Those produce iterators (don't materialize the list)

        Also have ``view...`` twin (``viewkeys``,...)

        Those produce iterables that change as the dictionary changes

        This the the standard in Python 3

.. slide:: A Compatibility Chart
    :level: 3

    .. rst-class:: small

    =============== =================
    Python 2        Python 3
    =============== =================
    d.keys()        list(d.keys())
    d.values()      list(d.values())
    d.items()       list(d.items())
    d.iterkeys()    iter(d.keys())
    d.itervalues()  iter(d.values())
    d.iteritems()   iter(d.items())
    d.viewkeys()    d.keys()
    d.viewvalues()  d.values()
    d.viewitems()   d.items()
    =============== =================

    See also http://python-future.org/compatible_idioms.html#dict-keys-values-items-as-a-list


.. slide:: Common Idiom
    :level: 3

    Iterating on everything

    .. code-block:: ipython

        In [26]: d = {'name': 'Brian', 'score': 42}

        In [27]: for k, v in d.items():
           ....:     print("%s: %s" % (k,v))
           ....:
        score: 42
        name: Brian

    More memory intensive in Python 2, but safe in both


Performance
-----------

Dictionaries are optimized for inserting and retrieving values:

* indexing is fast and constant time: O(1)
* Membership (``x in s``) constant time: O(1)
* visiting all is proportional to n: O(n)
* inserting is constant time: O(1)
* deleting is constant time: O(1)

more on what exactly that means soon.

.. slide:: Dictionary Performance
    :level: 3

    .. rst-class:: build

    * indexing is fast and constant time: O(1)
    * Membership (``x in s``) constant time: O(1)
    * visiting all is proportional to n: O(n)
    * inserting is constant time: O(1)
    * deleting is constant time: O(1)

    http://wiki.python.org/moin/TimeComplexity


Miscellaneous
-------------

You can find all the methods of the ``dict`` type in `the Python standard library documentation <https://docs.python.org/library/stdtypes.html#mapping-types-dict>`_.
But here are a number of interesting methods you may find useful:

Membership (on keys):

.. code-block:: ipython

    In [5]: d
    Out[5]: {'that': 7, 'this': 5}

    In [6]: 'that' in d
    Out[6]: True

    In [7]: 'this' not in d
    Out[7]: False


.. slide:: Other Dict Operations
    :level: 3

    See them all here:

    https://docs.python.org/library/stdtypes.html#mapping-types-dict

    .. rst-class:: build
    .. container::

        Membership

        .. code-block:: ipython

            In [5]: d
            Out[5]: {'that': 7, 'this': 5}

            In [6]: 'that' in d
            Out[6]: True

            In [7]: 'this' not in d
            Out[7]: False

        Membership is on the keys.

The :meth:`get <python2:dict.get>` method (:py:meth:`py3 <dict.get>`) allows you to get a value or returns a default if the key you seek is not in the ``dict``.
The default value returned is ``None``, but you can control it.
It has the advantage of never causing a ``KeyError``:

.. code-block:: ipython

    In [9]: d.get('this')
    Out[9]: 5

.. code-block:: ipython

    In [11]: d.get(u'something', u'a default')
    Out[11]: u'a default'

.. slide:: Getting Something
    :level: 3

    (like indexing)

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [9]: d.get('this')
            Out[9]: 5

        But you can specify a default

        .. code-block:: ipython

            In [11]: d.get(u'something', u'a default')
            Out[11]: u'a default'

        Never raises an Exception (default default is None)

To remove a key/value pair from a ``dict``, we use the :meth:`pop <python2:dict.pop>` method (:py:meth:`py3 <dict.pop>`).
It takes a key as the optional argument.
The value corresponding to the key is return and the key/value pair are removed.
If no argument is supplied, an arbitrary key/value pair is removed, and the value returned.

.. code-block:: ipython

    In [19]: d.pop('this')
    Out[19]: 5
    In [20]: d
    Out[20]: {'that': 7}

.. code-block:: ipython

    In [23]: d.popitem()
    Out[23]: ('that', 7)
    In [24]: d
    Out[24]: {}

.. slide:: Popping
    :level: 3

    gets the value at a given key while removing it

    .. rst-class:: build
    .. container::

        Pop just a key

        .. code-block:: ipython

            In [19]: d.pop('this')
            Out[19]: 5
            In [20]: d
            Out[20]: {'that': 7}

        pop out an arbitrary key, value pair

        .. code-block:: ipython

            In [23]: d.popitem()
            Out[23]: ('that', 7)
            In [24]: d
            Out[24]: {}

One of the most useful methods on the ``dict`` type is :meth:`setdefault <python2:dict.setdefault>` (:py:meth:`py3 <dict.setdefault>`).
You pass it a key and a default value.
If the key is present in the ``dict``, the stored value is returned.
If the key is *not* present, then the default value is stored and returned.

.. code-block:: ipython

    In [26]: d = {}
    In [27]: d.setdefault(u'something', u'a value')
    Out[27]: u'a value'
    In [28]: d
    Out[28]: {u'something': u'a value'}
    In [29]: d.setdefault(u'something', u'a different value')
    Out[29]: u'a value'
    In [30]: d
    Out[30]: {u'something': u'a value'}

.. slide:: Handy Method
    :level: 3

    ``setdefault(key[, default])``

    .. rst-class:: build
    .. container::

        gets the value if it's there, sets it if it's not

        .. code-block:: ipython

            In [26]: d = {}

            In [27]: d.setdefault(u'something', u'a value')
            Out[27]: u'a value'
            In [28]: d
            Out[28]: {u'something': u'a value'}
            In [29]: d.setdefault(u'something', u'a different value')
            Out[29]: u'a value'
            In [30]: d
            Out[30]: {u'something': u'a value'}


Sets
----

A ``set`` is an unordered collection of distinct values.
You can think of a set as a dict which has only keys and no values.

.. slide:: Sets
    :level: 3

    Unordered collection of distinct values

    .. rst-class:: build
    .. container::

        Like a Dict

        But only keys, no values

.. slide:: Constructors
    :level: 3

    .. code-block:: ipython

        In [5]: set()
        Out[5]: set()
        In [6]: set([1, 2, 3])
        Out[6]: {1, 2, 3}
        In [7]: {1, 2, 3}
        Out[7]: {1, 2, 3}
        In [8]: s = set()
        In [9]: s.update([1, 2, 3])
        In [10]: s
        Out[10]: {1, 2, 3}
        In [11]: s.add(4)
        In [12]: s
        Out[12]: {1, 2, 3, 4}


.. slide:: Set Properties
    :level: 3

    ``Set``  members must be hashable

    .. rst-class:: build
    .. container::

        Like dictionary keys -- and for same reason (efficient lookup)

        No indexing (unordered)

        .. code-block:: ipython

            >>> s[1]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'set' object does not support indexing

.. slide:: Set Methods
    :level: 3

    .. code-block:: ipython

        In [1]: s = set([1])
        In [2]: s.pop()
        Out[2]: 1
        In [3]: s.pop()
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-3-e76f41daca5e> in <module>()
        ----> 1 s.pop()
        KeyError: 'pop from an empty set'

        In [4]: s = set([1,2,3])
        In [5]: s.remove(2)
        In [6]: s.remove(2)
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-6-542ac1b736c7> in <module>()
        ----> 1 s.remove(2)
        KeyError: 2

.. slide:: Sets Are Sets
    :level: 3

    All the "set" operations from math class...

    .. code-block:: python

        s.isdisjoint(other)

        s.issubset(other)

        s.union(other, ...)

        s.intersection(other, ...)

        s.difference(other, ...)

        s.symmetric_difference( other, ...)

.. slide:: Frozen Set
    :level: 3

    Another kind of set

    immutable -- for use as a key in a dict (or another set...)

    .. code-block:: python

        >>> fs = frozenset((3,8,5))
        >>> fs.add(9)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'frozenset' object has no attribute 'add'

File Reading and Writing
========================

Handling files in Python.

.. slide:: Files
    :level: 3

    Text Files

    .. code-block:: python

        import io
        f = io.open('secrets.txt', encoding='utf-8')
        secret_data = f.read()
        f.close()

    ``secret_data`` is a (unicode) string

    ``encoding`` defaults to ``sys.getdefaultencoding()``

    switch away from using the ``open`` builtin

.. slide:: Binary Files
    :level: 3

    .. code-block:: python

        f = io.open('secrets.bin', 'rb')
        secret_data = f.read()
        f.close()

    ``secret_data``  is a byte string


.. slide:: File Opening Modes
    :level: 3

    .. code-block:: python

        f = io.open('secrets.txt', [mode])
        'r', 'w', 'a'
        'rb', 'wb', 'ab'
        r+, w+, a+
        r+b, w+b, a+b
        U
        U+

    .. rst-class:: build
    .. container::

        Modes follow Unix conventions

        Not well documented by Python, but better here

        http://www.manpagez.com/man/3/fopen/

        **Gotcha** -- 'w' modes always clear the file

.. slide:: Text File Notes
    :level: 3

    Text is default

    * ``io.open()`` defaults to "Universal" newline mode for text
    * newlines are translated: ``\r\n -> \n``
    * this happens both on read and write.
    * Always use \*nix-style in your code: ``\n``
    * ``io.open()`` returns "stream" objects
    * You can treat them as file objects (more soon on what that means)


.. slide:: Gotcha
    :level: 3

    No difference between text and binary on \*nix

    .. rst-class:: build
    .. container::

        You'll be tempted to open everything in ``text`` mode

        This will break binary files on Windows

        Get in the habit of thinking about whether you want data or text.


.. slide:: ``io.open()`` Parameters:
    :level: 3

    .. code-block:: python

        io.open(file, mode='r', buffering=-1, encoding=None,
                errors=None, newline=None, closefd=True)

    .. rst-class:: build
    .. container::
    
        ``file`` file name or full path (generally)

        ``mode`` mode for opening: 'r', 'w', etc.

        ``buffering`` controls the buffering mode (0 for no buffering)

        ``encoding`` sets the unicode encoding (only for text), if set file is text only

        ``errors`` sets the encoding error mode: 'strict', 'ignore', 'replace',...

        ``newline`` controls Universal Newline mode: lets you write DOS-type files on
          \*nix, for instance (text mode only).

        ``closedfd`` controls close() behavior if a file descriptor, rather than a
          name is passed in (advanced usage!)

(https://docs.python.org/2/library/io.html?highlight=io.open#io.open)


.. slide:: File Reading
    :level: 3

    Reading part of a file

    .. code-block:: python

        header_size = 4096
        f = open('secrets.txt')
        secret_header = f.read(header_size)
        secret_rest = f.read()
        f.close()

.. slide:: Common Idioms
    :level: 3

    .. code-block:: python

        for line in io.open('secrets.txt'):
            print line

    .. rst-class:: build
    .. container::

        (the file object is an iterator!)

        .. code-block:: python

            f = io.open('secrets.txt')
            while True:
                line = f.readline()
                if not line:
                    break
                do_something_with_line()

.. slide:: File Writing
    :level: 3

    .. code-block:: python

        outfile = io.open('output.txt', 'w')
        for i in range(10):
            outfile.write("this is line: {0}\n".format(i))

.. slide:: File Methods
    :level: 3

    .. code-block:: python

        f.read() f.readline() f.readlines()

    .. rst-class:: build
    .. container::

        .. container::

            .. code-block:: python

                f.write(str) f.writelines(seq)

            .. code-block:: python

                f.seek(offset) f.tell()

            .. code-block:: python

                f.flush() f.close()

.. slide:: File Like Objects
    :level: 3

    Many classes implement the file interface:

    .. rst-class:: build

        * loggers
        * ``sys.stdout``
        * ``urllib.open()``
        * pipes, subprocesses
        * StringIO

    .. rst-class:: build
    .. container::

        In general, two methods make an object *file-like*

        ``obj.read()``

        ``obj.write()``

.. slide:: StringIO
    :level: 3

    .. code-block:: python

        In [417]: from io import StringIO
        In [420]: f = StringIO.StringIO()
        In [421]: f.write(u"somestuff")
        In [422]: f.seek(0)
        In [423]: f.read()
        Out[423]: 'somestuff'

    .. rst-class:: build
    .. container::

        (handy for testing file handling code...)

        You'll see mention of ``StringIO`` and ``cStringIO``

        Ignore it.  Always import from ``io`` module

Paths and Directories
=====================

In Python, paths are often handled with simple strings (or Unicode strings)

.. slide:: Paths and Directories
    :level: 3

    Often handled with simple strings (bytes or unicode ok)

    .. rst-class:: build
    .. container::

        .. container::

            Relative paths:

            .. code-block:: python

                u'secret.txt'
                u'./secret.txt'

        .. container::

            Absolute paths:

            .. code-block:: python

                u'/home/chris/secret.txt'

        Either work with ``open()`` , etc.

.. slide:: ``os`` Module
    :level: 3

    .. code-block:: python

        os.getcwd() -- os.getcwdu() (u for Unicode)
        os.chdir(path)
        os.path.abspath()
        os.path.relpath()

    .. rst-class:: build
    .. container::

        .. code-block:: python

            os.listdir()
            os.mkdir()
            os.walk()


.. slide:: ``os.path`` Module
    :level: 3

    .. code-block:: python

        os.path.split()
        os.path.splitext()
        os.path.basename()
        os.path.dirname()
        os.path.join()

    .. rst-class:: build
    .. container::

        (all platform independent)

        (higher level stuff in ``shutil``  module)

.. slide:: ``pathlib`` Module
    :level: 3

    ``pathlib`` is a newer library. Handles paths in an OO way:

    http://pathlib.readthedocs.org/en/pep428/

    .. rst-class:: build
    .. container::

        In the Python3 standard library, back-ported for Python2:

        .. code-block:: bash

            $ pip install pathlib

.. slide:: Quick Intro
    :level: 3

    All the stuff in os.path and more:

    .. code-block:: ipython

        In [1]: import pathlib
        In [2]: pth = pathlib.Path('.')
        In [3]: pth.is_dir()
        Out[3]: True
        In [4]: pth.absolute()
        Out[4]: PosixPath('/Users/cewing/projects/training/codefellows/existing_course_repos/python-dev-accelerator')
        In [5]: for f in pth.iterdir():
           ...:     print(f)
           ...:
        .git
        .gitignore
        bin
        build
        cfpython.sublime-project
        ...
