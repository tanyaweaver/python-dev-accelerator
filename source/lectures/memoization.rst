===================
Memoization and You
===================

Timing a Recursive Function
===========================

Recursive functions are a consistent pain to deal with that you will encounter throughout your programming career. The deeper you have to go into your recursive stack, the more hairy that function can get (and the slower it can get). Consider the Fibonacci sequence, written with recursion in mind.

.. code-block:: ipython

    In [1]: def fib(n):
                """Return nth number of Fibonacci Sequence."""
                if n == 1:
                    return 0
                elif n == 2:
                    return 1
                else:
                    return fib(n - 1) + fib(n - 2)

When timed we see that it takes about 2.7 milliseconds to run

.. code-block:: ipython

    In [2]: timeit.timeit("fib(20)", setup="from __main__ import fib", number=1000)
    Out[2]: 2.675891876220703 # milliseconds

This may seem like a short time, but for computers it's actually quite a bit. This becomes especially clear if you try to excute the same recursive function several thousand, hundred thousand, or million times. Milliseconds add up into seconds, minutes, hours, and sometimes days.

Refactor and Go Faster
======================

Can it go faster? What if we only calculated once? What built-in data structure can we use?

.. code-block:: ipython

    In [3]: def fibonacci(n):
                """Return nth number of Fibonacci sequence."""
                if n <= 0:
                    return 0
                l = [0, 1]
                while len(l) < n:
                    l.append(l[-1] + l[-2])
                return l[n-1]
    In [4]: timeit.timeit("fibonacci(20)", setup="from __main__ import fibonacci", number=1000)
    Out[4]: 0.012011051177978516 # milliseconds

This is significantly faster, clocking in at roughly 12 microseconds per execution. What did we do differently? We cut out recursion, reducing some load on the machine. We also stored each new calculation in a list, which was updated in a ``while`` loop as we worked our way up to the "nth" number. What limitations are there to this approach?

Even Faster with Memoization
============================

There is another way to speed up code execution and value-calculation in recursive code. In the last example, we sped up our process by storing the data internally instead of going through a recursive rabbit hole. In this example, we'll store data outside of the recursive function in a data structure with constant-time lookup. This is **memoization**.

With memoization, you calculate your result once and only once, then *remember* the result for calculations up-to and including that final one. This makes lookup very fast. Observe

.. code-block:: ipython

    In [4]: memo = {}
    In [5]: def fib_memoized(n):
                """Return the nth number of Fibonacci Sequence"""
                if n in memo:
                    return memo[n]
                if n == 1:
                    f = 0
                elif n == 2:
                    f = 1
                else:
                    f = fib_memoized(n - 1) + fib_memoized(n - 2)
                memo[n] = f
                return f
    In [6]: timeit.timeit("fib_memoized(20)", setup="from __main__ import fib_memoized", number=1000)
    Out[6]: 0.0007169246673583984 # milliseconds

Our original function took 2.7 ms to execute. The memoized version of essentially the same function took 0.7 microseconds (0.0007 ms). This is more than 3500-times faster than the original version!

There is a faster algorithm. Look up `Knuth <https://en.wikipedia.org/wiki/Donald_Knuth>`_ and other ways to do this in Python. `Warning: do not directly copy and paste code from the internet <https://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/>`_.
