.. slideconf::
    :autoslides: False

*******************
Break This Function
*******************

.. slide:: Break This Function
    :level: 1

    This document contains no slides.

In class we covered, briefly, :ref:`Python Exceptions <python2:bltin-exceptions>` (:py:ref:`py3 <bltin-exceptions>`).
We spoke specifically about a few exception types that you are likely to see most often:

* ``NameError``
* ``TypeError``
* ``AttributeError``
* ``SyntaxError``

Tasks
=====

Create a python module called ``break_me.py``.
In this file create three functions:

* ``name_error()``: when called, this function will cause a NameError
* ``type_error()``: when called, this function will cause a TypeError
* ``attribute_error()``: when called, this function will cause an AttributeError

Then add a few other simple functions.
Write these such that when one is called, the result will be that an exception is caused.
However, the exception should occur at a stack depth of 4 frames.

Finally, write a function that would cause a ``SyntaxError``.
Your editor, if it is properly configured, should show an indication of this problem.
Take a screen shot showing that your editor *does* show the problem.
Once you have taken this screenshot, you should remove this function from your file so that it will run.

Submitting Your Work
====================

Upload two files: your ``break_me.py`` file, and the screenshot you took of your editor.

