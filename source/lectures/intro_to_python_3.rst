.. slideconf::
    :autoslides: False

******************************
Introduction To Python: Part 3
******************************

.. slide:: Introduction To Python: Part 3
    :level: 1

    .. rst-class:: center

    In which we learn about Python data structures and interacting with the file system.


Sequences
=========


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


.. slide:: Negative Indexes
    :level: 3

    Count from the end:

    .. code-block:: ipython

        In [105]: s = u"this is a string"
        In [106]: s[-1]
        Out[106]: u'g'
        In [107]: s[-6]
        Out[107]: u's'

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



Lists and Tuples
================

include here?

Iteration
=========

Repetition, Repetition, Repetition, Repe...

.. slide:: Iteration
    :level: 2

    .. rst-class:: left

    Repetition, Repetition, Repetition, Repe...

For Loops
---------

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
=================

.. rst-class:: center large

  Fun with Strings

.. slide:: String Features
    :level: 2

    .. rst-class:: large center

    Fun with Strings

Unicode v. Bytes
----------------

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

foobar

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


.. slide:: Dictionary Performance
    :level: 3

    .. rst-class:: build

    * indexing is fast and constant time: O(1)
    * Membership (``x in s``) constant time: O(1)
    * visiting all is proportional to n: O(n)
    * inserting is constant time: O(1)
    * deleting is constant time: O(1)

    http://wiki.python.org/moin/TimeComplexity


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

File Handling
=============

Paths
=====