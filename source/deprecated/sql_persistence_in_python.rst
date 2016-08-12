*************************
SQL Persistence in Python
*************************

In this tutorial, you'll walk through some basic concepts of data persistence
using the most common Python DBAPI2 connector for the PostgreSQL database,
``pyscopg2``.

This will build a very basic understanding of working with PostgreSQL in
Python.  However you may wish to bookmark the `postgreSQL documentation`_ and
the `psycopg2 documentation`_ for future reference.

.. _psycopg2 documentation: http://initd.org/psycopg/docs/
.. _postgreSQL documentation: http://www.postgresql.org/docs/9.4/static/index.html


Begin by activating the virtualenv we created in class:

.. code-block:: bash

    heffalump:psycopg2 cewing$ workon psycopg2
    [psycopg2]
    heffalump:psycopg2 cewing$



Interacting With the Database
=============================

Once all that is in place, we're ready to interact with our database using
``psycopg2``.

Connections and Cursors
-----------------------

We'll begin by getting connected. Connecting to any database consists of
providing a specially-formatted string to the connector, called a **DSN** or
Data Source Name.

Each different type of database uses a different format for this string.  In
PostgreSQL it is typically a set of ``key=value`` pairs where the keys come
from a `defined set of possible keys`_.

.. _defined set of possible keys: http://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-PARAMKEYWORDS

There are a lot of possible keywords, but the ones you are most likely to see
and use are:

* **dbname**: the name of the database in the server you want to connect with.
* **host**: the hostname on which the server is listening. This can also be a
  pathname to a socket file if the system is using Unix Domain Socket
  connections.
* **port**: the port number on which the server is listening. This can also be
  a socket file extension if the system is using Unix Domain Socket
  connections.
* **user**: The username to use when connecting to the database. Default is the
  system name of the user who is running the connect command.
* **password**: The password of the user. This is only used if the system
  requires password authentication.

We set up our database to allow us to connect directly using *ident*
authorization. So the only parameters we must pass are the dbname and user.

Fire up an interactive Python session and get a connection:

.. code-block:: pycon

    [psycopg2]
    heffalump:psycopg2 cewing$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import psycopg2
    >>> conn = psycopg2.connect(dbname="psycotest", user="cewing")
    >>> conn
    <connection object at 0x7fafc8e005c0; dsn: 'user=cewing dbname=psycotest', closed: 0>
    >>> 

A connection represents our tie to the database. But to interact with it, we
want to use a *cursor*:

.. code-block:: pycon

    >>> cur = conn.cursor()
    >>> cur
    <cursor object at 0x10a370718; closed: 0>
    >>> 

The cursor is a local representation of the state of the database. You can
execute statements on it, and see the results of those statements, but until
you **commit** a transaction, the changes are not persisted to the system on
disk.

Simple Inserts and Selects
--------------------------

Use your cursor to insert a new record into the ``author`` table:

.. code-block:: pycon

    >>> insert = "INSERT INTO author (name) VALUES('Iain M. Banks');"
    >>> cur.execute(insert)
    >>> cur.rowcount
    1
    >>> 

Notice that we ``execute`` a statement using the cursor. After this is done, we
can interrogate the cursor to find out what happened. In this case, we can
learn that one row was inserted.

**NOTE**:

Every so often, you will make an error in typing an SQL command. When you try
to execute the statement, you'll be informed of the error. This is nice. It's
important to note, though, that many kinds of errors can result in the current
transaction with the database being "aborted".

When this happens, you'll see error messages like this:

.. code-block:: pycon

    >>> cur.execute(insert)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    psycopg2.InternalError: current transaction is aborted, commands ignored until end of transaction block

There is nothing to fear here. You simply have to end a transaction block so
that you can start interacting with the database again. The safest way is to
roll back the transaction, which ensures that nothing since the last commit
will be saved:

.. code-block:: pycon

    >>> conn.rollback()

(more about transactions soon)

We can also retrieve from the database the information we just inserted, using
a ``SELECT`` statement:

.. code-block:: pycon

    >>> query = "SELECT * from author;"
    >>> cur.execute(query)
    >>> cur.fetchall()
    [(1, 'Iain M. Banks')]
    >>> 

You'll see that our select query found one row in the database.  The row is
returned as a tuple with as many values as there are columns in the query. We
asked for all columns (\*) and so we got two. 

The order of the values in each tuple is dependent on the query. In this case
we asked for all columns so we got them in the database order (id, name).

Parameterized Statements
------------------------

Inserting static data one row at a time is tedious.

We are software engineers. We can do better than that.

In order to repeat a statement a number of times, with different values, we
must use *parameters*.

In DBAPI2 packages, these parameters are specialized forms of *placeholders*
used in the strings passed to the ``execute`` command. Each database system
uses its own format, but the general idea is the same. You create an SQL
statement with placeholders where you want values to be inserted. Then you call
the 'execute' command with *two* arguments: your parameterized statement, and
a tuple containing as many values as you have parameters.

There is also an ``executemany`` method on a cursor object that supports
passing an iterable of tuples. The SQL statement will be run one time for each
tuple in the iterable:

.. code-block:: pycon

    >>> insert = "INSERT INTO author (name) VALUES(%s);"
    >>> authors = [("China Mieville",), ("Frank Herbert",),
    ...            ("J.R.R. Tolkein",), ("Susan Cooper",),
    ...            ("Madeline L'Engle",), ]
    >>> cur.executemany(insert, authors)
    >>> cur.rowcount
    5
    >>> 

And we can read our inserted values back:

.. code-block:: pycon

    >>> cur.execute(query)
    >>> rows = cur.fetchall()
    >>> for row in rows:
    ...   print row
    ...
    (1, 'Iain M. Banks')
    (2, 'China Mieville')
    (3, 'Frank Herbert')
    (4, 'J.R.R. Tolkein')
    (5, 'Susan Cooper')
    (6, "Madeline L'Engle")
    >>> 

RED LETTER WARNING
------------------

**A SUPER IMPORTANT WARNING THAT YOU MUST PAY ATTENTION TO**

The placeholder for psycopg2 is ``%s``.  This placeholder is the same
regardless of the type of data you are passing in as your values.

**Do Not Be Fooled** into thinking that this means you can use string
formatting to build your SQL statements:

.. code-block:: python

    # THIS IS BAD:
    cur.execute("INSERT INTO author (name) VALUES(%s)" % "Bob Dobbins")

This syntax **does not properly escape the values passed in**.

This syntax leaves you wide open to **SQL Injection Attacks**.

.. warning::

    If I ever see you using this syntax I will personally take you out behind
    the woodshed and tan your hide.

    I'm not kidding.

Python provides you with a syntax that is safe from the kinds of attacks that
make you front page news.  Use it properly:

.. code-block:: python

    cur.execute("INSERT INTO author (name) VALUES(%s)", ("Bob Dobbins", ))


Transactions
------------

Transactions group operations together, allowing you to verify them *before*
the results hit the database.

In the DBAPI2 specification, data-altering statements require an explicit
``commit`` unless auto-commit has been enabled.

Thus far, we haven't actually committed a transaction. If we open a second
terminal and fire up the psql shell program, we can see that the data we've
inserted is not yet *in* our database:

.. code-block:: bash

    heffalump:training.python_web cewing$ psql -d psycotest
    psql (9.3.2)
    Type "help" for help.

.. code-block:: psql

    psycotest=# \d
                    List of relations
     Schema |        Name         |   Type   | Owner
    --------+---------------------+----------+--------
     public | author              | table    | cewing
     public | author_authorid_seq | sequence | cewing
     public | book                | table    | cewing
     public | book_bookid_seq     | sequence | cewing
    (4 rows)

    psycotest=# select * from author;
     authorid | name
    ----------+------
    (0 rows)

    psycotest=#

In order for the values we've inserted to actually be persisted to the
filesystem, making them available outside the cursor we have, we must commit a
transaction.

We do this using the connection object we first set up:

.. code-block:: pycon

    >>> conn
    <connection object at 0x7fafc8e005c0; dsn: 'user=cewing dbname=psycotest', closed: 0>
    >>> conn.commit()
    >>> 

And now, back in ``psql``, our data is finally on disk:

.. code-block:: psql

    psycotest=# select * from author;
     authorid |       name
    ----------+------------------
            1 | Iain M. Banks
            2 | China Mieville
            3 | Frank Herbert
            4 | J.R.R. Tolkein
            5 | Susan Cooper
            6 | Madeline L'Engle
    (6 rows)


Handling Errors with Rollback
=============================

The largest benefit of having a transactional system like this is that you can
fix errors before they make a hash of your actual database.

When you attempt to commit a transaction there are two possible outcomes:
success or failure. If the commit succeeds, you can be sure that the changes
you've made are final and complete.

If the commit fails for some reason, an exception will be raised. You can then
tell the connection to roll back the transaction. This will undo all changes
since the last transaction commit, leaving your database in a consistent,
well-known state.

To help visualize this, let's set up a quick exercise.

First, at your psql prompt, empty the table you just filled:

.. code-block:: psql

    psycotest=# delete from author;
    DELETE 6
    psycotest=# select * from author;
     authorid | name
    ----------+------
    (0 rows)

    psycotest=#

Next, create a new file in your project directory.  Call it ``populatedb.py``.
Add the following code:


.. code-block:: python

    import psycopg2

    DB_CONNECTION_PARAMS = {
        'dbname': 'psycotest',
        'user': 'cewing',
    }

    AUTHOR_INSERT = "INSERT INTO author (name) VALUES(%s);"
    AUTHOR_QUERY = "SELECT * FROM author;"

    BOOK_INSERT = """
    INSERT INTO book (title, authorid) VALUES(%s, (
        SELECT author FROM author WHERE name=%s ));
    """
    BOOK_QUERY = "SELECT * FROM book;"

    AUTHORS_BOOKS = {
        'China Mieville': ["Perdido Street Station", "The Scar", "King Rat"],
        'Frank Herbert': ["Dune", "Hellstrom's Hive"],
        'J.R.R. Tolkien': ["The Hobbit", "The Silmarillion"],
        'Susan Cooper': ["The Dark is Rising", "The Greenwitch"],
        'Madeline L\'Engle': ["A Wrinkle in Time", "A Swiftly Tilting Planet"]
    }

These module-level constants will let us write a bit less code below.  We have
a dictionary that represents the parameters we will use to connect to the
database, a number of useful SQL statements for inserting and querying data,
and a set of data we will use.

You might see an error in the SQL above.  Leave it where it is.  We will fix it
after demonstrating rollback.

Next, add the following helper functions to ``populatedb.py``:

.. code-block:: python

    def show_query_results(conn, query):
        with conn.cursor() as cur:
            cur.execute(query)
            had_rows = False
            for row in cur.fetchall():
                print row
                had_rows = True
            if not had_rows:
                print "no rows returned"

    def show_authors(conn):
        query = AUTHOR_QUERY
        show_query_results(conn, query)

    def show_books(conn):
        query = BOOK_QUERY
        show_query_results(conn, query)

    def populate_db(conn):
        with conn.cursor() as cur:
            authors = ([author] for author in AUTHORS_BOOKS.keys())
            cur.executemany(AUTHOR_INSERT, authors)

            params = ([book, author] for author in AUTHORS_BOOKS
                      for book in AUTHORS_BOOKS[author])
            cur.executemany(BOOK_INSERT, params)


The ``show_query_results`` function is a helper that will take a 'SELECT' query
and a connection, perform the query on that connection and then print the
results.

The ``show_authors`` and ``show_books`` functions are simple one-stage wrappers
that perform the correct query using ``show_query_results``.

The final function, ``populate_db``, inserts authors and books into our
database as two separate queries. Note the nested generator expression that
provides all books by all authors for inserting into the book table. Python can
be fun!

**Note**: The ``con.cursor()`` call in ``show_query_results`` and
``populate_db`` above is being used as a *context manager*. What this means is
that when the block defined by the ``with`` statement exits, the cursor will be
cleanly closed.

Finally, in order to actually use all of this, we need a ``__main__`` block
that will try to run our code and explicitly roll back in case of error.

Add the following to the bottom of the ``populatedb.py`` file:

.. code-block:: python
    :linenos:

    if __name__ == '__main__':

        conn1 = psycopg2.connect(**DB_CONNECTION_PARAMS)
        conn2 = psycopg2.connect(**DB_CONNECTION_PARAMS)
        try:
            populate_db(conn1)
            print "\nauthors and books on conn2 before commit:"
            show_authors(conn2)
            show_books(conn2)
        except psycopg2.Error:
            conn1.rollback()
            print "\nauthors and books on conn2 after rollback:"
            show_authors(conn2)
            show_books(conn2)
            raise
        else:
            conn1.commit()
            print "\nauthors and books on conn2 after commit:"
            show_authors(conn2)
            show_books(conn2)
        finally:
            conn1.close()
            conn2.close()

(L3-4) In this code we set up two separate connections to the database.  We
will do our write operations using the first, and our read operations on the
second to illustrate the effect of commit and rollback.

(L5-9) First, we try to write our data to the database.  If that is
successfull, we read the author and book tables from our second connection to
show that before committing, the tables remain empty.

(L16-20) In the case that no error occurs, we hit the ``else:`` block.  This
allows us to commit our transaction on the first connection and demonstrate
that afterward we can read our data back from the second connection.

(L10-15) If an error is raised, we enter the ``except`` block. Here, we roll
back our transaction, and demonstrate that after rollback no data has hit our
database. In the end, we re-raise the exception so that our script will fail
visibly.

**Note**: We are catching the base exception class for *all* psycopg2 database
errors. There are a `number of more specific errors`_ you can use to determine if
perhaps a transaction might be retried or must be rolled back. That's more
involved than we need to get for this demonstration, though.

(L21-23) At the last, we add a ``finally`` block that will happen even if
errors occur. Here we safely close the two connections we've opened to our
database so that we don't leave them hanging when the script exits.

.. _number of more specific errors: http://initd.org/psycopg/docs/module.html#exceptions

Now that we have all that in place, let's execute our ``populateddb.py`` script
from a terminal. In your active ``psycopg2`` virtualenv, try the following:

.. code-block:: bash

    [psycopg2]
    heffalump:psycopg2 cewing$ python populatedb.py

    authors and books on conn2 after rollback:
    no rows returned
    no rows returned
    Traceback (most recent call last):
      File "populatedb.py", line 64, in <module>
        populate_db(conn1)
      File "populatedb.py", line 56, in populate_db
        cur.executemany(BOOK_INSERT, params)
    psycopg2.ProgrammingError: column "authorid" is of type integer but expression is of type author
    LINE 2: ...TO book (title, authorid) VALUES('Perdido Street Station', (
                                                                          ^
    HINT:  You will need to rewrite or cast the expression.

    [psycopg2]
    heffalump:psycopg2 cewing$

Notice first that the initial write operation worked. The error that is raised
comes from the point in ``populate_db`` where we are inserting books. Despite
this, the ``conn.rollback()`` in our ``except`` block removes *all* changes to
the database made since the last commit. This means that when we look at the
database with our second connection, no data is available in either table.

Let's fix our SQL error and retry the process.

Edit the ``BOOK_INSERT`` constant at the top of our script as follows (change
the 'author' after ``SELECT`` in the second line to 'authorid'):

.. code-block:: python

    BOOK_INSERT = """
    INSERT INTO book (title, authorid) VALUES(%s, (
        SELECT authorid FROM author WHERE name=%s ));
    """

Now you can re-run the script and see what success looks like:

.. code-block:: bash

    [psycopg2]
    heffalump:psycopg2 cewing$ python populatedb.py

    authors and books on conn2 before commit:
    no rows returned
    no rows returned

    authors and books on conn2 after commit:
    (62, 'China Mieville')
    (63, 'Frank Herbert')
    (64, 'Susan Cooper')
    (65, 'J.R.R. Tolkien')
    (66, "Madeline L'Engle")
    (45, 'Perdido Street Station', 62)
    (46, 'The Scar', 62)
    (47, 'King Rat', 62)
    (48, 'Dune', 63)
    (49, "Hellstrom's Hive", 63)
    (50, 'The Dark is Rising', 64)
    (51, 'The Greenwitch', 64)
    (52, 'The Hobbit', 65)
    (53, 'The Silmarillion', 65)
    (54, 'A Wrinkle in Time', 66)
    (55, 'A Swiftly Tilting Planet', 66)
    [psycopg2]
    heffalump:psycopg2 cewing$


Wrap-Up
=======

The Python DBAPI2 specification provides for a uniform interface between Python
programs and the Relational databases they might use for persistence.

In this tutorial you've learned a bit about the general operations of DBAPI2
using one particular implementation, ``psycopg2``.

There are small variations between implementations, particularly in the arena
of *placeholders* in parameterized SQL statments and how they should be
formatted. But the general shape of a DB interaction should be very consistent
from one API packge to another.

Next, we'll learn about how to use these underlying API packages through the
lens of an Object Relational Manager, providing us with more automatic
connections between our Python object layer and the underlying persistence
model.

For reference, please download :download:`the ORM code </downloads/basic_sqla_models.py>` required to interact with this book/author database.
