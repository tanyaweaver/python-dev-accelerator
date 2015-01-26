*************
Which Python?
*************

There are two versions of Python we might possibly use for this course: 2.7.x
or 3.x.

For a number of reasons, we have chosen to teach this course in Python 2.7. For
the time being, Python 2 is the version you are most likely to see in a
professiona situation. Every company we spoke with here in Seattle uses it, and
the large pre-existing code base built in Python 2 means that it will be a
while before Python 3 is the default Python to learn.

That being said, there are some things you can do now to begin writing code
that will be more portable forward to Python 3.  This class will be taught with
those steps in mind.

Bytes and Unicode
=================

One of the largest changes from Python 2 to Python three concerns the
difference in handling bytes and unicode.

In Python 2, a ``string`` literal is written thusly:

.. code-block:: python

    'I am a string'

.. ifslides::

    * Common in Python 2 to represent *textual* objects
    * Fine, so long as your text is *ASCII* only (English)
    * Not so good for foreign languages with accents/other characters.

.. ifnotslides::

    It is extremely common in Python 2 code to use string literals to represent
    textual objects--things meant to be read as text by humans. This is fine so
    long as the only characters in your text are in the ASCII character set
    (basic English). However, this is less and less often the case. It is very
    common these days to see international characters in text that passes
    through your programs.

.. nextslide::

Python 2 can handle these international characters using a ``unicode`` literal:

.. code-block:: python

    u'I am a string with élan'

Enocding a ``unicode`` literal transforms it to a string literal:

.. code-block:: python

    >>> foo = u'I am a string with élan'
    >>> bar = foo.encode('utf8')
    >>> bar
    'I am a string with \xc3\xa9lan'

This shows that in fact, a ``string`` is a sequence of **bytes**.

.. nextslide::

Python 2 allows for implicit conversion between unicode and bytes, but Python 3
does not.

In Python 3 you must hold text in your Python programs as ``unicode`` objects,
and only encode to ``bytes`` when passing that data out (to file, network,
buffer).

Similarly, you must *decode* bytes into unicode when you bring data in to your
program.

.. nextslide:: Handling the Difference

To help build the rigor needed to support this while still writing Python 2, we
will follow this convention:

* All textual data in our programs should be *explicitly* unicode: ``u'élan'``.
* All binary data will be written *explicitly* as byte string: ``b'\xc3\xa9lan``.


Integer vs. Float Division
==========================

In Python there are two division operators: ``/`` and ``//``. In Python 3 these
are ``division`` and ``integer division`` (also known as ``floored division``):

.. code-block:: pycon

    >>> 1 / 2
    0.5
    >>> 1 // 2
    0
    >>> 3 / 2
    1.5
    >>> 3 // 2
    1

.. nextslide::

But in Python 2, things are a bit different. The ``//`` operator works
similarly (it still gives you the ``floored`` result). The ``/`` operator is a
completely different story. The return values for both depend on what you give
them, and the ``/`` operator may work as floored division if you give use
integers:

.. code-block:: pycon

    >>> 1 // 2
    0
    >>> 1 / 2
    0
    >>> 1.0 / 2
    0.5
    >>> 1.0 // 2
    0.0

.. nextslide:: Handling the Difference

You should always be explicit which version of division you are using.  If you
want integer or floored results, Explicitly use the ``//`` operator.

And remember to be aware that much existing code does not carefully make this
distinction. You should always be alert for potential problems arising from
this discrepancy.

Test Test Test
==============

Subtle differences like floored versus true division are sure to result in bugs
during transition from Python 2 to Python 3.

For this reason, one of the keys to successful porting is establishing
excellent test coverage.

The more of your code is covered by extensive, thorough tests, the more easily
you can rest assured that a port from 2 to 3 will go as smoothly as possible.

.. nextslide::

For this reason, we will emphasize testing in this class.

You will write unit tests, integration tests and functional tests.

Establishing a habit of solid testing is the best tool you can use to ensure
safe transitions to Python 3.

More to Learn
=============

There are other techniques we will touch on as the class wears on, but that's
enough to go on for now.

Please take some time to watch `this video`_ by Tres Seaver from PyCon 2014
about porting code to Python 3 to get a sense of the larger picture.

.. _this video: https://www.youtube.com/watch?v=nx0sXSeJbmI

In addition, you will want to bookmark `Porting to Python 3`_ by Lennart
Regebro. In particular, the chapter on `preparing for Python 3`_ is an
excellent guide to strategies you can use today.

.. _preparing for Python 3: http://python3porting.com/preparing.html
.. _Porting to Python 3: http://python3porting.com
