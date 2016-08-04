.. slideconf::
    :autoslides: False

***************************************
Python Practice: Spell Check a Document
***************************************

.. slide:: Python Practice: Spell Check a Document
    :level: 1

    This document contains no slides.

Create a function that reads a text document (``.txt`` only) from file.
When run, this function will return a ``list`` of words that are potentially misspelled.

Recall that a list of words from the English dictionary can be found in your file system at the path ``/usr/share/dict/words`` (on Mac). 
If you decide to make a copy of this file in your working directory (you really don't need to), **make sure it's in your** ``.gitignore``.
It is a very, *very* large file.

Here is a sample text you may want to use for testing your code: :doc:`Sample Text </downloads/spellcheck_sample>`

Stretch Goal
------------

Add a parameter to your function for auto-suggesting corrections.
When ``True`` your function outputs a ``dict`` instead of a ``list``. 
Each key within the dict will be a misspelled word, and each value is a list of possible corrections.
If there are no possible corrections, the ``list`` is simply empty.

Submitting Your Work
====================

Create a ``spell-check`` branch in your ``code-katas`` repository. 
Do all of your work on this branch.

Add documentation about your code in the repo's ``README.md``.
Write appropriate tests for your code, and save them in a ``test_spell_check.py`` file.

After you've pushed your code solution over into GitHub, send a pull request
to your master branch.
**Submit the URL of that pull request to Canvas.**

Use the comment box in Canvas to talk about your thought process, as well as any difficulty you had with this code kata.