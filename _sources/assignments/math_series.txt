.. slideconf::
    :autoslides: False

*******************
Mathematical Series
*******************

.. slide:: Mathematical Series
    :level: 1

    This document contains no slides.

The `Fibonacci Series <http://en.wikipedia.org/wiki/Fibbonaci_Series>`_ is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us::

    0, 1, 1, 2, 3, 5, 8, 13, ...

The `Lucas Numbers <http://en.wikipedia.org/wiki/Lucas_number>`_ are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
The resulting series looks like this::

    2, 1, 3, 4, 7, 11, 18, 29, ...

Tasks
=====

Along with your partner for the week, create a github repository called `math-series`.
In this new repository, create a module ``series.py``.
In this same ``math-series`` repository, create a virtualenv.
Install ``pytest`` and ``pytest-xdist``.
Use a ``.gitignore`` file to ensure that the artifacts of your virtual environment do not end up in GitHub.

Add a file ``test_series.py`` to your repository.
As you work on the tasks below, use TDD practices.
Write tests first, then implement code.
Make small changes with many cycles of **Red-Green-Refactor**

*This is not an overly long assignment, so take the time to do the testing right.*

Create a function called ``fibonacci``.
The function should have one parameter ``n``. The function should return the ``nth`` value in the fibonacci series.
You may implement the function using recursion or iteration.
If you are feeling particularly frisky, do *both* as separate functions.

Ensure that your function(s) has a well-formed ``docstring``

In your ``series.py`` module, add a new function ``lucas`` that returns the ``nth`` value in the *lucas numbers*
Again, you may use recursion or iteration, or both.
Again, ensure that your function has a well-formed ``docstring``.

Both the *fibonacci series* and the *lucas numbers* are based on an identical formula.
Add a third function called ``sum_series`` with one required parameter and two optional parameters.
The required parameter will determine which element in the series to print.
The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the *fibonacci series*.
Calling it with the optional arguments 2 and 1 will produce values from the *lucas numbers*.
Other values for the optional parameters will produce other series.
Again, you may use recursion or iteration, or both.
Again, ensure that your function has a well-formed ``docstring``.

Add an ``if __name__ == "__main__":`` block to the end of your ``series.py`` module.

In this block, write code that demonstrates the use of the functions defined in the module.
If I run the module from the command line I should see output like this:

.. code-block:: bash

    $ python series.py

    This module defines functions that implement mathematical series.
    ...

    fibonacci(n):

        Returns the nth value in the fibonacci series

    >>> fibonacci(2)
    1

and so on.

Add your ``series.py`` and ``test_series.py`` modules to your git clone and commit frequently while working on your implementation.
Include good commit messages that explain concisely both *what* you are doing and *why*.

Submitting Your Work
====================

When you are finished and all your tests are passing, push your changes to your github repository.
Submit a link to your repository for the assignment submission in Canvas.

Use the comment feature in canvas to submit the following:

* At least one well-formed question about the work you did for this assignment
* At least one comment on what went well
* At least one comment on what was particularly difficult or challenging
