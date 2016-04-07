.. slideconf::
    :autoslides: False

********************************
Implement a Hash Table in Python
********************************

.. slide:: Implement a Hash Table in Python
    :level: 1

    This document contains no slides.

Python is all about the *namespaces*.
Namespaces in Python are really just Python ``dicts`` with some special sauce.
Python's ``dict`` is implemented as a ``hash table``.

In this assignment, you'll add a simple implementation of a `Hash Table <http://en.wikipedia.org/wiki/Hash_table>`_ to your data-structures repository.

Tasks
=====

The key to a solid implementation of a hash table is a good hashing function.
Read quickly over this `list of hashing functions <http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx>`_ to get some sense of the variety available, and the issues involved in designing one.
For the purposes of this assignment you can use a naive hashing function, such as the "Additive Hash" described in that reading.
For a stretch goal, try one of the more complex hashing functions instead.

For an extra credit point, design your hash table to accept different hashing function at construction time, and add tests demonstrating the differences between them.

Your table should have the following properties:

* It should be of fixed size.
  The number of slots in the table should be determined when the table is initialized, by passing an argument: ``foo = HashTable(1024)``
* It should handle hash collisions by using 'buckets' to contain any values that share a hash
* It should accept *only* strings as keys.
  If a non-string is provided, the 'set' method should raise an appropriate Python exception.

Your table should implement the following methods:

* **get(key)** - should return the value stored with the given key
* **set(key, val)** - should store the given val using the given key
* **_hash(key)** - should hash the key provided (note that this is an *internal* api)

Add tests to your data-structures repository to verify that your hash table works properly.
Ensure that your data-structures tests are hooked up to Travis CI so that you are covered by continuous integration tests as you add this new structure.

Add notes to the README explaining your approach and listing any resources and collaborations you used.

.. note:: **A note on testing**

          Testing a hash table consists largely of inserting values with keys and then using the keys to retrieve the values.
          Since it is difficult to provide enough tests manually to ensure that your bucket system works properly, I propose the following strategy:

          Every Unix-like operating system provides a list of dictionary words in a file at /usr/share/dict/words.
          This very long list (over 250,000 on my system) can provide a reasonable test bed for a hash table.
          For your tests, use this file.
          Insert all the words from the file into your hash table, with the key and the value being the same (in other words, ``my_table.set('pear', 'pear')``).
          Then, you can test by using each word as a key, and verify that the result you get back is the same word.



Submitting Your Work
====================

As usual, do your work on a branch.
When you are finished (and all tests are passing) create a new Pull Request containing only the work on balancing.
Submit the URL of your pull request.
When that is done, you may merge the pull request.

Add documentation of your changes to your README file.
Include any sources or collaborations.
