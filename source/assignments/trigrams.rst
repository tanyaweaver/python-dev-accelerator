.. slideconf::
    :autoslides: False

****************************************
Kata Fourteen: Tom Swift Under Milk Wood
****************************************

.. slide:: Kata Fourteen: Tom Swift Under Milk Wood
    :level: 1

    This document contains no slides.

Adapted from `Dave Thomas's work <http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/>`_.

Trigrams can be used to mutate text into new, surreal, forms.
But what heuristics do we apply to get a reasonable result?

As a boy, one of my treats was go to the shops on a Saturday and spend part of my allowance on books; for a nine-year old, I had quite a collection of Tom Swift and Hardy Boys.
Wouldn’t it be great to be able to create more and more of these classic books, to be able to generate a new Tom Swift adventure on demand?

OK, perhaps not.
But that won’t stop us trying.
I coded up a quick program to generate some swash-buckling scientific adventure on demand.
It came up with::

    ... it was in the wind that was what he thought was his companion. I
    think would be a good one and accordingly the ship their situation
    improved. Slowly so slowly that it beat the band! You’d think no one
    was a low voice. "Don’t take any of the elements and the
    inventors of the little Frenchman in the enclosed car or cabin completely
    fitted up in front of the gas in the house and wringing her hands.
    "I’m sure they’ll fall!"

    She looked up at them. He dug a mass of black vapor which it had
    refused to accept any. As for Mr. Swift as if it goes too high I’ll
    warn you and you can and swallow frequently. That will make the airship was
    shooting upward again and just before the raid wouldn’t have been
    instrumental in capturing the scoundrels right out of jail."</em>


Stylistically, it’s Victor Appleton meets Dylan Thomas.
Technically, it’s all done with **trigrams**.

Trigram analysis is very simple.
Look at each set of three adjacent words in a document.
Use the first two words of the set as a key, and remember the fact that the third word followed that key.
Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document.
For example, given the input::

  I wish I may I wish I might

You might generate::

    "I wish" => ["I", "I"]
    "wish I" => ["may", "might"]
    "may I"  => ["wish"]
    "I may"  => ["I"]

This says that the words "I wish" are twice followed by the word "I", the words "wish I" are followed once by "may" and once by "might" and so on.

To generate new text from this analysis, choose an arbitrary word pair as a starting point.
Use these to look up a random next word (using the table above) and append this new word to the text so far.
This now gives you a new word pair at the end of the text, so look up a potential next word based on these.
Add this to the list, and so on.
In the previous example, we could start with "I may".
The only possible next word is "I", so now we have::

  I may I

The last two words are "may I", so the next word is "wish".
We then look up "I wish", and find our choice is constrained to another "I"::

   I may I wish I

Now we look up "wish I", and find we have a choice.
Let’s choose "may"::

   I may I wish I may

Now we’re back where we started from, with "I may."
Following the same sequence, but choosing "might" this time, we get::

   I may I wish I may I wish I might

At this point we stop, as no sequence starts "I might."

Given a short input text, the algorithm isn’t too interesting.
Feed it a book, however, and you give it more options, so the resulting output can be surprising.

Tasks
=====

For this kata, try implementing a trigram algorithm that generates a couple of hundred words of text using a book-sized file as input.
`Project Gutenberg <http://www.gutenberg.org/>`_ is a good source of online books (Tom Swift and His Airship is `here <http://sailor.gutenberg.org/etext02/03tom10.txt>`_.)

Be warned that these files have DOS line endings (carriage return followed by newline).

Create a new repository called ``trigrams``.
Create a Python module ``trigrams.py`` in this repository which holds the code you use to implement a solution.

Create a ``main`` function which implements the core of your algorithm.
It should take two arguments, the path to a source file and an integer representing the number of words to generate.

Try to keep your code well-factored by creating functions to execute discreet steps of the processing.
You might have one function that processes the input into your trigram source.
Perhaps there is another that is responsible for selecting a new word, given a pair of input words.
Maybe there are others.

Add a ``tests.py`` module to your code.
For each function you write, with the exception of ``main``, create one or more tests that prove it works as intended.

Finally, add an ``if __name__ == '__main__':`` block to your code.
In this block, use `sys.argv` to get the name of a source file from the command line.
When the ``trigrams.py`` module is executed as a script (``$ python trigrams.py some_text.txt 200``) it should print 200 words of text to ``stdout``.

If you install any additional Python packages (like ``pytest``) to accomplish your work, make sure you use ``pip freeze`` to create a ``requirements.pip`` file and include it in your repository.

Resources
---------

For convenience you can download a copy of "Sherlock Holmes" :download:`here </downloads/sherlock.txt>`.

There is also a :download:`shorter copy </downloads/sherlock_small.txt>` you can use for testing purposes.
You should add this shorter version to your repository as a resource to be used for running your tests.

Objectives
-----------

Kata’s are about trying something many times.
In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text.
What do we do with punctuation?
Paragraphs?
Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

Submitting Your Work
====================

Submit a link to your repository with your work.

In addition, run your script once at the command line and create an example output file.
You can save this output by using the ``redirect`` shell operator (``>``) like so:

.. code-block:: bash

    $ python trigrams.py some_book.txt 500 > my_submission.txt

Upload this generated file as well.
**Do Not** include this file in your repository (nor should you include any full-length book text you download to play with).