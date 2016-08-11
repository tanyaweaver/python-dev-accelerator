.. slideconf::
    :autoslides: False

***************************************
Test Driven Development with ``pytest``
***************************************

.. slide:: Test Driven Development with ``pytest``
    :level: 1

    .. rst-class:: center

    In which we learn basic test driven development practices using ``pytest``

In this session, we will learn the basics of Test Driven Development.
Our tool for accomplishing this will be `pytest <http://pytest.org/latest/>`_, a powerful and pluggable test runner.

What is TDD
===========

.. epigraph::

   Untested code is broken by design

   -- Surely Somebody

As developers, we all "know" that we need to write tests.
But developing the discipline to do so is a burden.
Especially when you are brand new.
You have so many other things to deal with, so many things to learn.
Surely there are more important things you need to do, right?

**NO**

There is no more important discipline you can develop than writing tests.

.. slide:: Test Driven Development
    :level: 3

    .. epigraph::

       Untested code is broken by design

       -- Surely Somebody


Defining The Problem
--------------------

So why do so many of us not write tests?
I can't speak for anyone else.
But for me the biggest hurdle is that test writing is so *different* and so *unrelated* to the work I'm doing in developing software.

I develop interactively, building an understanding of the problem I'm facing by working in the interpreter until I feel I've got a good understanding of the problem.
Only then do I move to the editor and begin building actual code.
By that time, I'm so accustomed to working in the terminal, that interactively "testing" my work by poking at it in an interpreter seems intuitive.

Once I've finished a solution, and played with it enough interactively to believe it works, writing tests for it becomes *another thing* I have to do.
Now that I've done my primary job, I have to move over to this other file, write a bunch more code, and run it repeatedly.
The work feels so *extraneous* to what I consider my *real job* that I am sorely tempted to skip it.

(I'm embarassed to say I often give in to the temptation too)

The problem is that the act of *testing* is too far removed from *development*.
It happens at a different time than my development work.
And it happens in a different conceptual space than my development work.

.. slide:: Defining The Problem
    :level: 3

    Why do we fail to write tests?

    .. rst-class:: build
    .. container::

        I code interactively, exploring solutions

        Then I write functions, solving problems

        Comfort in the interpreter leads to testing there

        When *finished*, I feel *done*

        Don't want to switch gears to writing tests

        Testing is *too far removed* from development

Proposing a Solution
--------------------

The solution should be pretty clear.
If the problem is that development and testing are too far apart, then move them closer together.
This is the aim of Test Driven Development.
To close both the temporal and conceptual gaps between the worlds of development and testing.


Closing the Conceptual Gap
**************************

The conceptual gap is that space between what is perceived *development* work and what seems to be *testing* work.

Especially in interpreted languages like Python, it's easy to get started solving a problem by playing with the code.
We open an interpreter and write some lines.
We try different approaches, explore possible solutions.
We reject failed paths and zero in on a correct answer.
It's a process of coming to understand the shape of the problem we've been asked to solve.

What we don't notice is that this process is not actually one of *development* but of *testing*.
Thinking of this as development is actually backwards.

What if we were to put the label *testing* on this type of work instead?
Then we could start by writing *tests* that help us to determine the shape of our problem.
Then, implementing code to make the tests pass proves that we have achieved a *correct* solution.

.. slide:: The Conceptual Gap
    :level: 3

    We explore in the interpreter to find solutions

    .. rst-class:: build
    .. container::

        What we are really doing is *defining the problem*

        This lies more in the domain of *testing* than *development*

        Use writing tests to define the problem

        Use development to solve it

        Remove the conceptual gap between the two

Let's imagine that later we discover we have a poor understanding of the problem.
Maybe the problem is a little different than we at first believed.
Maybe there are edge cases we didn't anticipate.

At that point, we can return to our tests.
update them to better describe our new understanding.
Or we can add new tests to cover the unexpected circumstances we are now aware of.

These new tests will fail.
So we can return to our implementation code.
We update it so that our new tests pass, an ensure the other tests keep passing.
And when we are done, we know we have a working system.

.. slide:: Test-Implement Cycle
    :level: 3

    Understanding will deepen over time

    .. rst-class:: build
    .. container::

        May find the problem is different

        Update existing tests

        Update implementation

        May find unexpected edge cases

        Write new tests

        Update implementation


This is the cycle of Test Driven Development.
Some developers call it **"Red-Green-Refactor"**

We start by writing a test that shows what what want to have happen (**Red**)

Then we implement code that makes that test pass (**Green**)

And then as our understanding of the problem evolves, we update (**Refactor**)

It's a nice, neat cycle.

.. slide:: Red-Green-Refactor
    :level: 3

    .. rst-class:: red

    Write a test to show what should happen (**Red**)

    .. rst-class:: build
    .. container::

        .. rst-class:: green

        Implement code to make the test pass (**Green**)

        .. rst-class:: yellow

        Update when there is new understanding (**Refactor**)


Closing the Temporal Gap
************************

The temporal gap is the space in time between when we write implementation code and when we write tests.

Traditionally, we do our development and then, later, we write tests.
When we do this, the large temporal gap makes it hard to actually do the work of writing the tests.
It's entirely too tempting to say our *real work* is done.

What if we were to move the act of development and the act of testing much closer in time?
What if we focused on writing small tests, then small functions, then refactoring?
Could we bring the two so close in time that the two separate acts become one?

Test Driven Development seeks to close this gap.
In "true" TDD, you are supposed to write no more test than is needed to have it fail.
Then you write no more code than you need to make the test pass.
Then you repeat.

Again, this is the **"Red-Green-Refactor"** cycle.
If we successfully implement this approach, then the temporal gap between development and testing disappears.
The impediments to testing evaporate.
And we can write well tested code all the time.

.. slide:: The Temporal Gap
    :level: 3

    Traditional development:

    .. rst-class:: build

    * Develop some project code
    * Write tests to prove it works

    .. rst-class:: build
    .. container::

        There is a space in time between the two

        Space == *Intertia*

        Move testing and development closer together

        Make them overlap

        Only write enough test to fail

        Only write enough code to pass


Exploring TDD
=============

Enough theory, let's set about exploring TDD by building a little project using it.
At the same time, we'll learn a bit about the ``pytest`` testing framework.

Project Setup
-------------

Begin by creating a project directory, then move into that directory.

.. code-block:: bash

    Banks:~ cewing$ mkdir tdd-play
    Banks:~ cewing$ cd tdd-play
    Banks:tdd-play cewing$

Next, let's create a virtualenv in this directory and activate it.

.. code-block:: bash

    Banks:tdd-play cewing$ python3 -m venv ./
    Banks:tdd-play cewing$ source bin/activate
    [tdd-play]
    Banks:tdd-play cewing$

Development of ``pip`` and ``setuptools`` has been very rapid lately.
And the new developments in each are usually worth having on board.
So I generally follow the creation of a new virtualenv with a quick update of ``pip`` and ``setuptools``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install -U pip setuptools
    ...
    Successfully installed pip setuptools
    Cleaning up...
    [tdd-play]
    Banks:tdd-play cewing$


Now, let's install our tools for this project.
We'll start with ``pytest``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install pytest
    ...
    Successfully installed py-1.4.31 pytest-2.8.7
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Prepare for a Project
    :level: 3

    .. code-block:: bash

        Banks:~ cewing$ mkdir tdd-play
        Banks:~ cewing$ cd tdd-play

    .. rst-class:: build
    .. container::

        .. code-block:: bash

            Banks:tdd-play cewing$ python3 -m venv ./
            Banks:tdd-play cewing$ source bin/activate

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install -U pip setuptools

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install pytest

The ``pytest`` package provides a customized test runner with lots of bells and whistles.
It also makes it very easy to start writing tests.
When you invoke the command it begins looking for Python files with names that start with ``test_``.
Once it finds them, it reads them and looks for functions with names that start with ``test_``.
After gathering them together, it runs them all, one at a time.
At the end, it reports the results to you.

.. slide:: ``pytest`` Basics
    :level: 3

    Custom test runner

    .. rst-class:: build
    .. container::
    
        When invoked, finds modules named ``test_*``

        Finds functions in namespace named ``test_*``

        Runs them, reports results

        Works with ``unittest``\ -style tests

Let's make a directory to hold our code for this project.
We'll call it ``src`` because that's the conventional name for such directories.

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ mkdir src

Then, create a new file in this directory.
Call it ``test_ack.py``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ touch src/test_ack.py

Our First Test
--------------

We can get started with just that.
Open the ``src`` directory in your text editor.
In the ``test_ack.py`` file, add the following code:

.. code-block:: python

    # -*- coding: utf-8 -*-

    def test_foo():
        assert 1 == 0

.. slide:: First Test
    :level: 3

    .. code-block:: bash

        [tdd-play]
        Banks:tdd-play cewing$ mkdir src

    .. rst-class:: build
    .. container::
    
        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ touch src/test_ack.py

        Open ``src`` in your editor

        In ``test_ack.py``:

        .. code-block:: python

            # -*- coding: utf-8 -*-

            def test_foo():
                assert 1 == 0

We've now written a test.
Let's run it:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ py.test
    ======================= test session starts ========================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    collected 1 items

    src/test_ack.py F

    ============================= FAILURES =============================
    _____________________________ test_foo _____________________________

        def test_foo():
    >       assert 1 == 0
    E       assert 1 == 0

    src/test_ack.py:5: AssertionError
    ===================== 1 failed in 0.22 seconds =====================

The ``pytest`` test runner found our ``test_ack.py`` file.
It found the ``test_foo`` function defined in it.
And it ran the test.

The test raised an AssertionError because one is definitely not equal to two.
Then ``pytest`` captured that error and reported it to us as a failing test.

.. slide:: Run Your Test
    :level: 3

    ::

        [tdd-play]
        Banks:tdd-play cewing$ py.test
        ======================= test session starts ========================
        platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
        rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
        collected 1 items

        src/test_ack.py F

        ============================= FAILURES =============================
        _____________________________ test_foo _____________________________

            def test_foo():
        >       assert 1 == 0
        E       assert 1 == 0

        src/test_ack.py:5: AssertionError
        ===================== 1 failed in 0.22 seconds =====================


Next, let's make our test pass.
Change the code in ``test_foo`` so that the assertion is true:

.. code-block:: python

    # -*- coding: utf-8 -*-

    def test_foo():
        assert 1 == 1

And then re-run your tests:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ py.test
    ======================= test session starts ========================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    collected 1 items

    src/test_ack.py .

    ===================== 1 passed in 0.17 seconds =====================

Great!

We've made our first **"Red-Green-Refactor"** cycle.
But it's kind of a pain to have to go back and re-run our tests after changing that file.
Can we get ``pytest`` to do that for us?
Yes we can!

.. slide:: Fix The Test
    :level: 3

    Fix it and run again:

    .. rst-class:: build
    .. container::
    
        ::

            [tdd-play]
            Banks:tdd-play cewing$ py.test
            ======================= test session starts ========================
            platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
            rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
            collected 1 items

            src/test_ack.py .

            ===================== 1 passed in 0.17 seconds =====================

        Red-Green!!!

        **but too slow**

Test On Save
------------

The ``pytest`` system is pluggable.
We can install plugins to provide different kinds of functionality.
That includes letting us automatically re-run our tests every time a test in our project is updated.
To get that particular functionality, let's install ``pytest-watch``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ pip install pytest-watch
    ...
    Successfully installed apipkg-1.4 execnet-1.4.1 pytest-watch-4.1.0
    [tdd-play]
    Banks:tdd-play cewing$

.. slide:: Test On Save
    :level: 3

    ``pytest`` is pluggable

    .. rst-class:: build
    .. container::
    
        Plugins provide additional functions not in the core

        Like re-running your test when a file is updated

        .. code-block:: bash

            [tdd-play]
            Banks:tdd-play cewing$ pip install pytest-watch
            ...
            Successfully installed apipkg-1.4 execnet-1.4.1 pytest-watch-4.1.0
            [tdd-play]
            Banks:tdd-play cewing$

To use this new feature, we invoke a new command provided by our plugin: ``ptw``:

.. code-block:: bash

    [tdd-play]
    Banks:tdd-play cewing$ ptw
    ============================= test session starts ==============================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    plugins: xdist-1.14
    collected 1 items
    collected 1 items

    src/test_ack.py .

    =========================== 1 passed in 0.19 seconds ===========================
    ####################### waiting for changes ########################
    ### Watching:   /Users/cewing/projects/training/codefellows/tests/tdd-play

Now that that's in place, let's begin working on our project.

.. slide:: Invoking `failloop mode`
    :level: 3

    Run the new ``ptw`` command from ``pytest-watch``:

    .. rst-class:: build
    .. container::
    
        ::

            [tdd-play]
            Banks:tdd-play cewing$ ptw
            ============================= test session starts ==============================
            platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
            rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
            plugins: xdist-1.14
            collected 1 items
            collected 1 items

            src/test_ack.py .

            =========================== 1 passed in 0.19 seconds ===========================
            ####################### waiting for changes ########################
            ### Watching:   /Users/cewing/projects/training/codefellows/tests/tdd-play

The Ackermann Function
----------------------

The `Ackermann Function <http://en.wikipedia.org/wiki/Ackermann_function>`_ is a recursive mathematical function.
Its primary characteristic is that for even very small inputs it produces very large outputs.
It also recurses a very high number of times in computing its value.
For that reason, it is sometimes used to demonstrate the effectiveness of compiler's optimizations for recursion.

The function takes two inputs, ``m`` and ``n``, and produces a single numeric value.
The wikipedia page for the function gives a nice table of output values, given values for the two inputs.
Here's a sampling:

+------+---+----+----+----+-----+
| m\\n | 0 | 1  | 2  | 3  | 4   |
+======+===+====+====+====+=====+
| **0**| 1 | 2  | 3  | 4  | 5   |
+------+---+----+----+----+-----+
| **1**| 2 | 3  | 4  | 5  | 6   |
+------+---+----+----+----+-----+
| **2**| 3 | 5  | 7  | 9  | 11  |
+------+---+----+----+----+-----+
| **3**| 5 | 13 | 29 | 61 | 125 |
+------+---+----+----+----+-----+

.. slide:: Ackermann Function
    :level: 3

    Given inputs ``m`` and ``n``, return an output value:

    .. rst-class:: build
    .. container::

        +------+---+----+----+----+-----+
        | m\\n | 0 | 1  | 2  | 3  | 4   |
        +======+===+====+====+====+=====+
        | **0**| 1 | 2  | 3  | 4  | 5   |
        +------+---+----+----+----+-----+
        | **1**| 2 | 3  | 4  | 5  | 6   |
        +------+---+----+----+----+-----+
        | **2**| 3 | 5  | 7  | 9  | 11  |
        +------+---+----+----+----+-----+
        | **3**| 5 | 13 | 29 | 61 | 125 |
        +------+---+----+----+----+-----+

        This is our *problem domain*

So this is the problem domain we have to solve.
Without thinking too deeply about it, we can see we need to write a function that will take two numbers and return one.
We can also see that, for example, if both of the inputs are ``0``, then the output is expected to be ``1``.
That's testable, so lets test it.

Back in your text editor, add a new test to the ``test_ack.py`` file.
Let's call it ``test_ackermann_0_0``.
We'll start with the smallest amount of code that will fail:

.. code-block:: python

    def test_ackermann_0_0():
        from ackermann import ackermann

.. slide:: Break It Down
    :level: 3

    That's too much to think about dealing with right away

    .. rst-class:: build
    .. container::
    
        We should break it down into smaller pieces

        If m == 0 and n == 0, then the output is 1

        We can test that!

        Write the smallest test that can possibly fail

        .. code-block:: python

            def test_ackermann_0_0():
                from ackermann import ackermann

        Did your tests run again?

        What do you see?

Notice that our tests started running again as soon as we saved that file.
Here's what the error says:

.. code-block:: bash

    # MODIFIED /Users/cewing/projects/training/codefellows/tests/tdd-play/src/test_ack.py
    ============================= test session starts ==============================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    plugins: xdist-1.14
    collected 2 items
    collected 2 items

    src/test_ack.py .F

    =================================== FAILURES ===================================
    ______________________________ test_ackermann_0_0 ______________________________

        def test_ackermann_0_0():
    >       from ackermann import ackermann
    E       ImportError: No module named 'ackermann'

    src/test_ack.py:9: ImportError
    ====================== 1 failed, 1 passed in 0.21 seconds ======================
    ########################## LOOPONFAILING ###########################
    src/test_ack.py::test_ackermann_0_0
    ####################### waiting for changes ########################
    ### Watching:   /Users/cewing/projects/training/codefellows/tests/tdd-play

Okay, so we have an ImportError.
We don't have an ``ackermann.py`` module anywhere.
And it certainly doesn't contain an ``ackermann`` function.
Let's fix that, minimally.

Create a new file in the same ``src`` folder, called ``ackermann.py``.
Then add the following code:

.. code-block:: python

    # -*- coding: utf-8 -*-


    def ackermann(m, n):
        pass

.. slide:: Green Time
    :level: 3

    How do we solve the problem?

    .. rst-class:: build
    .. container::
    
        .. code-block:: python

            # -*- coding: utf-8 -*-

            def ackermann(m, n):
                pass

        How did the tests do this time?

        Notice our failed tests runs, then all tests run

        Are we done?

And again, our tests will run themselves.
This time, they'll run the failing test once.
And then, because that passes, they will re-run all the tests to make sure we didn't break anything else.

::

    # MODIFIED /Users/cewing/projects/training/codefellows/tests/tdd-play/src/ackermann.py
    ============================= test session starts ==============================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    plugins: xdist-1.14
    collected 3 items
    collected 3 items

    src/test_ack.py .

    =========================== 1 passed in 0.01 seconds ===========================
    ============================= test session starts ==============================
    platform darwin -- Python 3.5.1, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/cewing/projects/training/codefellows/tests/tdd-play, inifile:
    plugins: xdist-1.14
    collected 2 items
    collected 2 items

    src/test_ack.py ..

    =========================== 2 passed in 0.20 seconds ===========================
    ####################### waiting for changes ########################
    ### Watching:   /Users/cewing/projects/training/codefellows/tests/tdd-play

Let's return to our test now and make it test something useful.
Let's assert that when we call that function with ``0`` and ``0`` that we get ``1`` back:

.. code-block:: python

    # in test_ack.py
    def test_ackermann_0_0():
        from ackermann import ackermann
        assert ackermann(0, 0) == 1

And when our tests run again, there will be one failure.

Now let's return to our implementation code in ``ackermann.py``.
We can write just enough to make that test pass:

.. code-block:: python

    # in ackermann.py
    def ackermann(m, n):
        return 1

.. slide:: Red-Green-Refactor
    :level: 3

    Update the test to test our basic premise: ``A(0, 0) --> 1``

    .. rst-class:: build
    .. container::
    
        .. code-block:: python

            # in test_ack.py
            def test_ackermann_0_0():
                from ackermann import ackermann
                assert ackermann(0, 0) == 1

        Tests Fail... **Red**

        Implement minimal code in ``ackermann.py`` to fix them

        .. code-block:: python

            # in ackermann.py
            def ackermann(m, n):
                return 1

        Tests Pass... **Green**

        Are we done?

And again, the tests are green!

Let's try a different number combination.
For the inputs ``0`` and ``1`` the function should return ``2``.
Let's add a new test that claims that is true:

.. code-block:: python

    # in test_ack.py
    def test_ackermann_0_1():
        from ackermann import ackermann
        assert ackermann(0, 1) == 2

That turns our tests red again.
Two are passing, but one is not.
Let's add some code that fixes that.
Maybe at this point, we should look at the definition of the function.
Wikipedia says that if ``m`` is equal to ``0``, then the return value of the function is ``n + 1``.
We understand that.
Let's make our function do that.

.. code-block:: python

    # in ackermann.py
    def ackermann(m, n):
        if m == 0:
            return n + 1

.. slide:: Deepen Our Understanding
    :level: 3

    We also know ``A(0, 1) --> 2``

    .. rst-class:: build
    .. container::
    
        Write a test for that.

        .. code-block:: python

            # in test_ack.py
            def test_ackermann_0_1():
                from ackermann import ackermann
                assert ackermann(0, 1) == 2

        And then implement code to make it pass

        .. code-block:: python

            # in ackermann.py
            def ackermann(m, n):
                if m == 0:
                    return n + 1

        Are we done?

And our tests are back to being green.
Let's add another test and see if that holds true for the next values from our table.
For ``m = 0`` and ``n = 2`` the function should return ``3``.

.. code-block:: python

    # in test_ack.py
    def test_ackermann_0_2():
        from ackermann import ackermann
        assert ackermann(0, 2) == 3

Oooooh!  Our tests are *still green*!
Does that mean we are done?
Well, there are still quite a few tests left to write, even to finish out the table we have above.
We can't really be sure we are finished until all of them pass.
But who wants to write 16 more tests?

Let's use the power of our testing framework to help us out of this jam.

.. slide:: Repetition Sucks
    :level: 3

    Write one more test along these lines for ``A(0, 2) --> 3``

    .. rst-class:: build
    .. container::
    
        Notice a pattern evolving?

        Each test is the same, except for ``m``, ``n`` and the result

        We can write one test function and use *parameters*!

        Then delete the other three manual versions.

        .. code-block:: python

            # in test_ack.py
            def test_ackermann(m, n, result):
                from ackermann import ackermann
                assert ackermann(m, n) == result

        Notice the tests are red again.

        Why?

In ``pytest``, you can *parametrize* tests.
This allows you to specify a single test, and a list of inputs you will provide.
The framework will run the test once for each input in your list.
We can use this to write just one test that will test all the values in our handy chart above.

Let's begin by *refactoring* our test so we only need one.
Back in ``test_ack.py`` let's erase our ``test_ackerman_m_n`` tests.
We'll replace them with a single function where ``m``, ``n`` and the expected result are *paramters* of the test:

.. code-block:: python

    # in test_ack.py
    def test_ackermann(m, n, result):
        from ackermann import ackermann
        assert ackermann(m, n) == result

As expected, our tests are failing again.
Let's fix that.
First, at the top of the file, import the ``pytest`` package.
The tools we want are there.

.. code-block:: python

    # at the top of test_ack.py, just below the coding statement
    import pytest

Then, on the line just above our test function, add the following code:

.. code-block:: python

    @pytest.mark.parametrize('m, n, result', [(0,0,1), (0,1,2), (0,2,3)])
    def test_ackermann(m, n, result):
        # our test code here.

And if you've done your job correctly, then you should see *four* tests run and all pass.
For each of the input sets in our new line of code, a single test is run.

.. slide:: ``parametrize``
    :level: 3

    In ``pytest`` they call this ``parametrize``

    .. rst-class:: build
    .. container::
    
        Note the spelling

        We can add a bit of code that provides a list of tuples of parameters

        The test will be run once for each tuple

        .. code-block:: python

            # in test_ack.py
            import pytest 

            @pytest.mark.parametrize('m, n, result', [(0,0,1), (0,1,2), (0,2,3)])
            def test_ackermann(m, n, result):
                # our test code here.


The ``pytest.mark.parametrize`` call takes as its first argument a string that names the parameters for the test, separated by commas.
This list should exactly match the parameters you listed in the test below.
The second argument to the call is a list of tuples.
Each tuple will supply the arguments for one call of the test function.
So there must be the same number of items in each as in the parameter list of the test.

.. slide:: ``parametrize`` usage
    :level: 3

    ``pytest.mark.parametrize(argnames, argvals)``

    .. rst-class:: build
    .. container::

        ``argnames`` is a string, comma separated

        .. rst-class:: build
        .. container::

              same as parameter list for the test

              ``argvals`` is a list

              If there is only one parameter, it's a list of values

              If there are ``n`` parameters, a list of n-tuples


We can now add the rest of our chart to the file in the same place.
But that will make for a really long line of code.
It won't be very readable.
Let's make a module constant instead.
Then we can use that constant in the call to ``pytest.mark.parametrize``.

.. code-block:: python

    # in test_ack.py
    ACK_TABLE = [
        (0, 0, 1),
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 4),
        (0, 4, 5),
        (1, 0, 2),
        (1, 1, 3),
        ...
    ]

Fill out the entire table.
There should be twenty tuples.
Then, update the test code:

.. code-block:: python

    # in test_ack.py
    @pytest.mark.parametrize('m, n, result', ACK_TABLE)
    def test_ackermann(m, n, result):
        # our test code here.

.. slide:: Final Steps
    :level: 3

    We don't want to write all 20 tuples on that one line.

    .. rst-class:: build
    .. container::

        Bind a module-scope constant:

        .. code-block:: python

            # in test_ack.py
            ACK_TABLE = [
                (0, 0, 1),
                (0, 1, 2),
                (0, 2, 3),
                ...
            ]

        Update the call to ``parametrize``:

        .. code-block:: python

            # in test_ack.py
            @pytest.mark.parametrize('m, n, result', ACK_TABLE)
            def test_ackermann(m, n, result):
                # our test code here.

.. slide:: Ackermann's Function Defined
    :level: 3


    Fill in the whole table, and watch your tests fly

    .. rst-class:: build
    .. container::
    
        When one fails, fix it by updating the function

        ::

            If m == 0 --> n + 1

            if m > 0 and n == 0 --> ackerman(m - 1, 1)

            if m > 0 and n > 0 --> ackerman(m -1, ackerman(m, n - 1))

When you save your file, you should see 21 tests run.
Six of them will pass, but the rest will fail.
Now we can finish implementing our ackermann function.

Back in ``ackermann.py``, implement the rest of the function.
Wikipedia gives us this::

    if m > 0 and n == 0 --> ackerman(m - 1, 1)
    if m > 0 and n > 0 --> ackerman(m -1, ackerman(m, n - 1))

Armed with that information, can you finish implementing the ``ackermann`` function and make the tests pass?

Wrap Up
=======

We've learned a lot here.
We discussed the reasons that testing has traditionally been so hard to get done.
We learned about one approach to solving the problem: Test Driven Development.
We also learned about a testing framework in Python that has tools to help us to do TDD.
And finally, we implemented a little project using TDD principles.

Now, you go and use these tools for your work tonight and going forward.

.. slide:: Summary
    :level: 3

    Why is testing hard to get done?

    .. rst-class:: build
    .. container::
    
        What does TDD do to help solve that problem?

        How can we write simple tests with ``pytest``?

        How can we iterate quickly through Red-Green-Refactor?

        How can we save work with parameters?
