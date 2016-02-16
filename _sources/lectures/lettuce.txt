****************************************
Behavior Driven Development with Lettuce
****************************************

.. ifnotslides::

    .. note::

        The code built in this short demonstration is available as
        :download:`fizzbuzz.tgz </downloads/fizzbuzz.tgz>`

.. rst-class:: left
.. container::

    Let's imagine that the whiteboard exercise we did previously, FizzBuzz, was
    actually a project we had to implement for a client.

    In order to ensure that the work we did for that project fulfilled the
    client's requirements, we would definitely want to test the code. But unit
    tests--and the output they produce--are not the easiest things for clients
    to read.

    So instead, you decide to use this opportunity to use We're going to use
    the Python package `lettuce`_ to incorporate
    `behavior driven development`_. That way, the tests will be clear
    demonstrations of the business value of your code to your client.

.. _lettuce: http://lettuce.it
.. _behavior driven development: http://en.wikipedia.org/wiki/Behavior-driven_development

Practice Safe Development
=========================

.. rst-class:: left

Because this is a client project, you'll set up a *virtualenv project* for it
as you always do.

Install Lettuce
---------------

Then you'll install ``lettuce``:

.. code-block:: bash

    [fizzbuzz]
    [master=]
    heffalump:fizzbuzz cewing$ pip install lettuce
    Downloading/unpacking lettuce
      ...

    Successfully installed lettuce sure fuzzywuzzy nose rednose python-termstyle
    Cleaning up...
    [fizzbuzz]
    [master=]

.. nextslide:: What You Got

Once that's finished, we should find that we have a new command available in
our shell: ``lettuce``:

.. code-block:: bash

    [fizzbuzz]
    [master=]
    heffalump:fizzbuzz cewing$ which lettuce
    /Users/cewing/virtualenvs/fizzbuzz/bin/lettuce

.. nextslide:: Project Structure

After this, make sure to use ``pip freeze > requirements.txt`` to dump your
requirements out to a file for easy replication.

At this point, your project directory would look something like this::

    fizzbuzz/
    ├── LICENSE
    ├── README.rst
    ├── fizzbuzz.py
    └── requirements.txt

.. nextslide:: The ``fizzbuzz.py`` File

Since you haven't actually written any code for the project yet, your
``fizzbuzz.py`` file might look like this:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """The module provides two functions, fizzbuzz and fizzbuzz_extended
    """

    def fizzbuzz(n):
        """return a fizzbuzz-formatted representation of n"""
        pass


Working With Lettuce
====================

.. rst-class:: left

There's a nice walkthrough for lettuce `on the website`_. If you're starting a
project totally from scratch, try it out.

.. _on the website: http://lettuce.it/tutorial/simple.html#tutorial-simple

Getting Started
---------------

.. ifnotslides::

    .. container::
    
        The basic gist of the walkthrough tells us that ``lettuce`` works by
        convention. To have lettuce tests, you have to set up an appropriate directory
        structure in your Python project.

        We'll create a directory called ``features``.  And in it we'll create two
        files: ``fizzbuzz.feature`` and ``steps.py``.

        The ``<name>.feature`` file is where we'll create our BDD tests.  The
        name of the file is arbitrary, the extension is not.

        The ``<name>.py`` file is where we will create the Python code that
        implements steps in our BDD tests.  Again, the name is arbitrary, and
        ``lettuce`` will scan for any ``.py`` files that contain step
        definitions.

        .. code-block:: bash

            [fizzbuzz]
            [master=]
            heffalump:fizzbuzz cewing$ mkdir features
            [fizzbuzz]
            [master=]
            heffalump:fizzbuzz cewing$ touch features/fizzbuzz.feature
            [fizzbuzz]
            [master=]
            heffalump:fizzbuzz cewing$ touch features/steps.py

.. ifslides::

    .. rst-class:: build

    * ``lettuce`` works by convention
    * Must have a ``features`` directory in your project
    * It must contain one or more ``<feature_name>.feature`` files

      * BDD tests go in these files
      * The name of the file is arbitrary, but the file extension is not.
    
    * It should also contain one or more Python files where the ``steps`` will
      be defined

      * more on what a step is soon.

.. nextslide:: New Layout

Once you create the files you'll need, your directory structure will look
something like this::

    fizzbuzz/
    ├── README.rst
    ├── features
    │   ├── fizzbuzz.feature
    │   └── steps.py
    ├── fizzbuzz.py
    └── requirements.txt

Write a Scenario
----------------

If we wanted to express the fizzbuzz game as a user story, it might go
something like this::

    As a user, when I call fizzbuzz with the number 5, I see 'Buzz'.

.. rst-class:: build
.. container::

    Expressed in BDD form, this translates to something like this::

        Given the number 5, when I call fizzbuzz, then I see the output 'Buzz'

.. rst-class:: build
.. container::

    Let's add this 'Scenario' to our BDD tests:

    .. code-block:: cucumber

        Feature: Simple FizzBuzz
            Implement a simple version of the FizzBuzz game

            Scenario: FizzBuzz of 5
                Given the number 5
                When I call FizzBuzz
                Then I see the output Buzz


Implement The Steps
-------------------

We have three steps.  Lettuce will match our steps to Python functions using
the text we set in the scenario, so we need to create three steps.

.. ifnotslides::

    Steps are defined as Python functions decorated with the ``@step`` decorator
    factory from lettuce. The decorator factory takes a single argument which is
    the text used for the step in scenarios. Variable values are matched by regular
    expression.

.. ifslides::

    .. rst-class:: build

    * Steps are Python functions
    * Decoration with the ``@step`` decorator registers a function as a step.
    * The argument to the decorator is a string used to match phrases in
      scenarios
    * Variable values to be used in tests are matched by regular expression.

.. nextslide:: The First Step

.. ifnotslides::

    Let's implement the first step first.  In ``steps.py`` add the following:

.. code-block:: python

    from lettuce import step
    from lettuce import world

    from fizzbuzz import fizzbuzz

    @step('the number (\d+)')
    def the_number(step, num):
        world.number = int(num)

.. ifnotslides::

    Here we can see that the ``@step`` decorator is passed the argument "the number
    (\d+)".  How does that match? The secret is that there are a few 'magic' words
    in ``lettuce``. When the test parser sees ``Given``, ``When`` or ``Then`` it
    uses these to determine that the following text on the line is a step. That
    text is what is considered for the match.

    The regular expression ``(\d+)`` will match a sequence of one or more digits,
    and the value it finds will be passed to the function decorated by ``@step``.

    Also notice that the Python function decorated by ``@step`` takes *two*
    arguments. The first will always be the step itself. The second comes from the
    matched regular expression.

.. ifslides::

    .. rst-class:: build

    * ``Given``, ``When`` and ``Then`` are markers for steps

      * Those words **should not** be included in the matching text.
      
    * The regular expression ``(\d+)`` matches a sequence of one or more digits

      * The matched value will be passed into the decorated function
    
    * Notice that the decorated function accepts *two* arguments.

      * The first is the ``step`` instance build by ``lettuce``.
      * The remaining argument(s) come from regexp *match groups*.

.. nextslide::

How do you expect you might handle a step like this:

.. code-block:: cucumber

    Given the numbers 5 and 7

What would the argument passed to the ``@step`` decorator look like? How many
arguments would the Python function need to expect?

.. nextslide:: Moar Steps!

Go ahead and add two more steps for the remaining parts of the scenario:

.. code-block:: python

    @step('when I call fizzbuzz')
    def call_fizzbuzz(step):
        world.fb = fizzbuzz(world.number)
    
    @step('I see the output (\w+)')
    def compare(step, expected):
        assert world.fb == expected, "Got %s" % expected

Notice that the ``world`` object provided by ``lettuce`` allows passing values
from one function context to another.

Run Your Tests - Red
--------------------

Once you've done this, you should be able to run your BDD tests from the
command line:

.. code-block:: bash

    [fizzbuzz]
    [master *=]
    heffalump:fizzbuzz cewing$ lettuce
    Feature: Simple FizzBuzz                          # features/fizzbuzz.feature:1
      Implement a simple version of the FizzBuzz game # features/fizzbuzz.feature:2
      Scenario: FizzBuzz of 5                         # features/fizzbuzz.feature:4
        Given the number 5                            # features/steps.py:8
        When I call FizzBuzz                          # features/steps.py:13
        Then I see the output Buzz                    # features/steps.py:18
        Traceback (most recent call last):
          ...
        AssertionError: Got None
    1 feature (0 passed)
    1 scenario (0 passed)
    3 steps (1 failed, 2 passed)

.. ifnotslides::

    You can see, the tests report that we've run 1 feature, 1 scenario and 3
    steps. They also tell us that one of our steps failed. And they kindly
    provide a traceback that shows us where in our steps things went awry.

Implement Your Code
-------------------

Now, back in ``fizzbuzz.py`` implement your fizzbuzz function:

.. code-block:: python

    def fizzbuzz(n):
        """return a fizzbuzz-formatted representation of n"""
        if n == 0:
            return str(0)
        out = ''
        data = [(3, 'Fizz'), (5, 'Buzz')]
        for divisor, replacement in data:
            if not n % divisor:
                out += replacement
        if not out:
            out = str(n)
        return out

Run Your Tests - Green
----------------------

Now you can re-run your test:

.. code-block:: bash

    [fizzbuzz]
    [master *=]
    heffalump:fizzbuzz cewing$ lettuce

    Feature: Simple FizzBuzz                          # features/fizzbuzz.feature:1
      Implement a simple version of the FizzBuzz game # features/fizzbuzz.feature:2

      Scenario: FizzBuzz of 5                         # features/fizzbuzz.feature:4
        Given the number 5                            # features/steps.py:8
        When I call FizzBuzz                          # features/steps.py:13
        Then I see the output Buzz                    # features/steps.py:18

    1 feature (1 passed)
    1 scenario (1 passed)
    3 steps (3 passed)

.. rst-class:: build
.. container::

    Wonderful! Your first passing BDD test!

Iterating Over Multiple Calls
=============================

.. ifnotslides::

    But it really isn't enough to just test with one value. FizzBuzz is a
    dynamic process that returns different values depending on what you pass
    in. We should cover at least a reasonable range of alternative
    possibilities.

    We could write a new scenario for each different value we want to pass in.
    But that would mean re-writing the same lines over and over with only two
    variations. Not very programmerish.

    Luckily, there's a solution. With the syntax supported by ``lettuce`` we
    can replace the *specific* numbers in our current scenario with
    *placeholders*. Then we can provide a set of data for the scenario to use,
    and ``lettuce`` will automatically plug in our values and run the same
    scenario over and over for us.

.. ifslides::

    .. rst-class:: left

    These are not really great BDD tests yet.

    .. rst-class:: build left

    * You should test a range of values, not just one
    * You don't want to write one scenario per value tested
    * You can use *Scenario Outlines* to iteratively re-run tests over a set of
      defined values.

A Scenario Outline
------------------

Update ``fizzbuzz.feature`` like so:

.. code-block:: cucumber

        Scenario Outline: FizzBuzz [just enough]
            Given the number <input>
            When I call FizzBuzz
            Then I see the output <output>

        Examples:
        | input | output   |
        | 0     | 0        |
        | 1     | 1        |
        | 3     | Fizz     |
        | 5     | Buzz     |
        | 6     | Fizz     |
        | 10    | Buzz     |
        | 15    | FizzBuzz |

.. ifnotslides::

    We've changed our *scenario* into a **Scenario Outline**. This lets
    ``lettuce`` know that we expect this scenario to be run multiple times.

    We also replaced the specific input ``5`` and output ``Buzz`` with
    placeholders, marked by angle brackets.

    Finally, we provided a table of example data for our outline to use. The
    first row of the table contains the names of our placeholders, and then
    each row represents a set of values to be used for one iteration.

Run Your Tests - Refactor
-------------------------

.. ifnotslides::

    Now when we run the tests again, we can see that we get more passes through
    the scenario automatically:

.. code-block:: cucumber

    [fizzbuzz]
    [master=]
    heffalump:fizzbuzz cewing$ lettuce
    Feature: Simple FizzBuzz                          # features/fizzbuzz.feature:1
      Implement a simple version of the FizzBuzz game # features/fizzbuzz.feature:2
      Scenario Outline: FizzBuzz [just enough]        # features/fizzbuzz.feature:4
        Given the number <input>                      # features/steps.py:8
        When I call FizzBuzz                          # features/steps.py:13
        Then I see the output <output>                # features/steps.py:18
      Examples:
        | input | output   |
        | 0     | 0        |
        ...

    1 feature (1 passed)
    7 scenarios (7 passed)
    21 steps (21 passed)

Next Steps
==========

.. ifnotslides::

    We've written one scenario that covers our simple implementation of
    FizzBuzz. But the assignment had a second implementation. That version was
    supposed to be extensible with additional numbers and the values that
    should be printed in their place.  For example, if the number 7 was
    supplied, the value 'Sizz' should be returned.

    You may also wish to read more of `the documentation`_ for ``lettuce`` and
    see if you can't figure out how to add a new scenario and new steps that
    will cover that version of the game.

    To complete this task you'll need to learn a bit more about the syntax of
    the language you are using to write these tests.  It's called ``Gherkin``
    (the first implementation was called ``cucumber``). There is a very nice
    outline of `the features of Gherkin syntax`_ you can read to learn more.

    You should be aware that not **all** the features of the ``Gherkin`` syntax
    are supported by ``lettuce.`` Moreover, some features are supported in
    alternate forms, for example, ``Gherkin`` backgrounds are implemented as
    hooks in ``lettuce``.

.. ifslides::

    .. rst-class:: left

    * You may wish to read more of `the documentation`_.
    * The syntax used by ``lettuce`` is called *Gherkin*.
    * You can read more about `the features of Gherkin syntax`_.
    * You should be aware that not **all** the features are supported.

      * Some are supported, but in different forms
      * Backgrounds in ``gherkin`` are replaced by ``hooks``.

.. _the documentation: http://lettuce.it
.. _the features of Gherkin syntax: http://docs.behat.org/guides/1.gherkin.html

.. rst-class:: left

**Happy testing!**
