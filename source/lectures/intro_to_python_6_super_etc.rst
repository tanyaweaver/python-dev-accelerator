*************************
A Python Class Miscellany
*************************

.. ifslides::

    .. rst-class:: centered

    In which we meet a few of the odd beasties in Python class programming

.. ifnotslides::

    In this lesson we will discuss some of the available features of Class programming in Python.
    We'll cover the :func:`super <python2:super>` function (:py:func:`py3 <super>`) and how to use it.
    We'll discuss classmethods and how they can be used.
    And we'll discover static methods and discuss why they are rare in Python.


Super
=====

.. ifnotslides::

    The ``super`` function is used in conjunction with subclasses.
    The function takes as its two arguments a class object and an instance of that class.
    The return value is a proxy for "the correct" parent class.

.. ifslides::

    .. rst-class:: left

    ``super`` allows you to call a method on "the right superclass" from a subclass.

.. rst-class:: build left
.. container::

    instead of:

    .. code-block:: python

        class A(B):
            def __init__(self, *args, **kwargs)
                B.__init__(self, *args, **kwargs)
                ...

    You can do:

    .. code-block:: python

        class A(B):
            def __init__(self, *args, **kwargs)
                super(A, self).__init__(*args, **kwargs)
                ...

.. nextslide:: Caveats

.. ifnotslides::

    Be careful, though.
    There are some subtle differences between these two usages.
    One difference is in syntax.
    It's a bit hard to understand all of the *stuff* in a call to ``super``:

    .. code-block:: python

        super(A, self).__init__(*args, **kwargs)

    In english, we can read this like "create a ``super`` object for the superclass of A."
    "Then, call the __init__ method on that object, using this instance as ``self``."

    It's important to realize that the value returned by the call to ``super`` **is not** the superclass object itself.
    However, it **is** a proxy that ensures that the method you call will be invoked on the superclass object.

.. ifslides::

    Caution: There are some subtle differences.

    .. rst-class:: build
    .. container::

        The syntax is a bit confusing:

        .. code-block:: python

            super(A, self).__init__(*args, **kwargs)

        ``super()`` **does not** return the superclass object!

        The return value is a *proxy* that finds the right object and calls the right method.

.. nextslide:: Compatibility

.. code-block:: python

    super().__init__(*args, **kwargs)

.. ifnotslides::

    Note that in Python 3, it is possible (and encouraged) to call ``super`` with *no arguments*.
    It just does the right thing.

    This syntax is **not** compatible with Python 2.x.
    If you have to maintain compatibility, you **must** provide the class name and self.

.. ifslides::

    .. rst-class:: build
    .. container::

        In Python 3, you can call super with no arguments.

        This does not work in Python 2

        Keep ``classname`` and ``self`` for compatibility

super() issues...
-----------------

.. ifnotslides::

    There are a few issues around using super that you must keep track of.
    The method that is being called by ``super`` needs to exist.
    And every occurence of that method in superclasses must *also* use ``super``.
    All the way back up to the first class that implements that method.

    The long-and-short of it is that if you use it, be consistent in using it.
    When you do, it is part of the public interface for your class, like it or not.
    So you should document the fact that you use it.

.. ifslides::

    Some facts you must understand:

    .. rst-class:: build

    * The method being called by super() needs to exist
    * Every occurrence of the method needs to use super():

      - Use it consistently, and document that you use it, as it is part of
        the external interface for your class, like it or not.

.. nextslide:: calling super()

.. ifnotslides::

    When using ``super``, the call signature is important.
    Both the method in which super is invoked, and the method invoked by it *must have the same parameter list*.
    You should *never* call super with anything but the exact arguments that came in to the method you use it inside.
    If you *need* to add one or more optional arguments, then you should always accept ``*args`` and ``**kwargs``.
    If you do this, then you should invoke ``super`` like this:

    .. code-block:: python

        super(MyClass, self).method(<args_declared>, *args, **kwargs)

.. ifslides::

    The caller and callee need to have a matching argument signature.

    .. rst-class:: build
    .. container::

        **Never** call super with anything but the exact arguments received

        .. container::

            If you **have to** add one or more optional arguments, always accept:

            .. code-block:: python

                *args, **kwargs

        .. container::

            and call super like:

            .. code-block:: python

                super(MyClass, self).method(args_declared, *args, **kwargs)

Static and Class Methods
========================

.. rst-class:: left build
.. container::

    You've seen how methods of a class are *bound* to an instance when it is
    created.

    And you've seen how the argument ``self`` is then automatically passed to
    the method when it is called.

    And you've seen how you can call *unbound* methods on a class object so
    long as you pass an instance of that class as the first argument.

    .. rst-class:: centered

    **But what if you don't want or need an instance?**


Static Methods
--------------

A *static method* is a method that doesn't get self:

.. code-block:: ipython

    In [36]: class StaticAdder(object):
       ....:     def add(a, b):
       ....:         return a + b
       ....:     add = staticmethod(add)
       ....:

    In [37]: StaticAdder.add(3, 6)
    Out[37]: 9


.. nextslide:: Syntactic Sugar

Static methods can be written *declaratively* using the ``staticmethod`` built-in as a *decorator*:

.. code-block:: python

    class StaticAdder(object):
        @staticmethod
        def add(a, b):
            return a + b

.. nextslide:: Why?

.. rst-class:: build
.. container::

    Where are static methods useful?

    Usually they aren't

    99% of the time, it's better just to write a module-level function

    An example from the Standard Library (tarfile.py):

    .. code-block:: python

        class TarInfo(object):
            # ...
            @staticmethod
            def _create_payload(payload):
                """Return the string payload filled with zero bytes
                   up to the next 512 byte border.
                """
                blocks, remainder = divmod(len(payload), BLOCKSIZE)
                if remainder > 0:
                    payload += (BLOCKSIZE - remainder) * NUL
                return payload


Class Methods
-------------

A class method gets the class object, rather than an instance, as the first
argument

.. code-block:: ipython

    In [41]: class Classy(object):
       ....:     x = 2
       ....:     def a_class_method(cls, y):
       ....:         print(u"in a class method: ", cls)
       ....:         return y ** cls.x
       ....:     a_class_method = classmethod(a_class_method)
       ....:
    In [42]: Classy.a_class_method(4)
    in a class method:  <class '__main__.Classy'>
    Out[42]: 16

.. nextslide:: Syntactic Sugar

Once again, the ``classmethod`` built-in can be used as a *decorator* for a
more declarative style of programming:

.. code-block:: python

    class Classy(object):
        x = 2
        @classmethod
        def a_class_method(cls, y):
            print(u"in a class method: ", cls)
            return y ** cls.x

.. nextslide:: Why?

.. rst-class:: build
.. container::

    Unlike static methods, class methods are quite common.

    They have the advantage of being friendly to subclassing.

    Consider this:

    .. code-block:: ipython

        In [44]: class SubClassy(Classy):
           ....:     x = 3
           ....:

        In [45]: SubClassy.a_class_method(4)
        in a class method:  <class '__main__.SubClassy'>
        Out[45]: 64

.. nextslide:: Alternate Constructors

Because of this friendliness to subclassing, class methods are often used to
build alternate constructors.

Consider the case of wanting to build a dictionary with a given iterable of
keys:

.. code-block:: ipython

    In [57]: d = dict([1,2,3])
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-57-50c56a77d95f> in <module>()
    ----> 1 d = dict([1,2,3])

    TypeError: cannot convert dictionary update sequence element #0 to a sequence


.. nextslide:: ``dict.fromkeys()``

The stock constructor for a dictionary won't work this way. So the dict object
implements an alternate constructor that *can*.

.. code-block:: python

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.

        '''
        self = cls()
        for key in iterable:
            self[key] = value
        return self

(this is actually from the OrderedDict implementation in ``collections.py``)

See also datetime.datetime.now(), etc....
