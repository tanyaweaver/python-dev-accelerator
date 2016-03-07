*****************
The HTTP Protocol
*****************

.. ifnotslides::

    We've seen a number of network protocols so far.
    Each of them consisted of a set of allowed commands and possible responses, *messages* that are passed from client to server and then from server to client.
    In each protocol we've seen so far, these commands and responses have been *delimited*.
    And for each of the protocols we've seen so far, that delimiter has been consistent: <CRLF>

    A further consistency is shared between these protocols.
    In each case we've seen so far, the *client* is responsible for initiating the interaction.
    The *server* is passive until it receives some sort of request.

.. ifslides::

    .. rst-class:: left
    .. container::

        We've seen a number of network protocols so far.

        .. rst-class:: build

        * Each has a set of allowed *messages* to be sent back and forth
        * Each legal message is *delimited* in some way
        * The delimiter thus far is consistent: <CRLF>
        * Client-initiated communications are also consistent.
        * The Server does not speak until spoken to.


HTTP Characteristics
====================

.. ifnotslides::

    HTTP is no different.
    It is also a message-centered protocol, supporting two-way communications between a client and a server.
    Messages sent from the client to the server are called *requests*.
    Messages sent from the server to the client are called *responses*.

.. ifslides::

    .. rst-class:: left build
    .. container::

        HTTP is no different

        also message-centered

        also two-way communications

        here we call them *requests* and *responses*.

        .. rst-class:: build

        * Requests (Asking for information)
        * Responses (Providing answers)

An HTTP Interaction
-------------------

.. ifnotslides::

    In HTTP, both requests and responses share a common format.
    There is a *required* initial line which contains either a command or a response code.
    This is followed by one or more lines of *headers* (more on these below).
    After all the headers, a single blank line separates the headers from the optional *body*.
    As with our other protocols, the delimiter for lines is the ``<CRLF>``.

    Here are some examples:

HTTP Request (Ask for information)::

    GET /index.html HTTP/1.1<CRLF>
    Host: www.example.com<CRLF>
    <CRLF>

HTTP Response (Provide answers)::

    HTTP/1.1 200 OK<CRLF>
    Date: Mon, 23 May 2005 22:38:34 GMT<CRLF>
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)<CRLF>
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT<CRLF>
    Etag: "3f80f-1b6-3e1cb03b"<CRLF>
    Accept-Ranges:  none<CRLF>
    Content-Length: 438<CRLF>
    Connection: close<CRLF>
    Content-Type: text/html; charset=UTF-8<CRLF>
    <CRLF>
    <438 bytes of content>

.. ifslides::

    .. nextslide:: HTTP Req/Resp Format

    Both share a common basic format:

    .. rst-class:: build
    .. container::

        .. rst-class:: build

        * A *required* initial line (a command or a response code)
        * A *(mostly) optional* set of headers, one per line
        * A blank line
        * An *optional* body
        * Line separators are <CRLF> (familiar, no?)

        Let's look at each a bit more closely.


HTTP Requests
=============

.. ifnotslides::

    Let's start our investigation by looking a bit more closely at the HTTP *request*.
    It has evolved across time from version 1.0 of the HTTP specification to the current version 1.1

Format
------

In HTTP 1.0, the only required line in an HTTP request looks like this::

    GET /path/to/index.html HTTP/1.0<CRLF>
    <CRLF>

.. ifnotslides::

    As the years passed, it grew more and more common to host more than one website (with different domain names) on a single machine.
    This led to *virtual hosting*, which imposed a new requirement.
    There had to be a way to tell a request for one website apart from one for another.
    Version 1.1 of the HTTP specification added a single required *header*, **Host**:

HTTP 1.1 added a required header **Host**, to support virtual hosting::

    GET /path/to/index.html HTTP/1.1<CRLF>
    Host: www.mysite1.com:80<CRLF>
    <CRLF>

.. nextslide::

.. ifnotslides::

    Every HTTP request **must** begin with a single line, broken by whitespace into three parts.
    The three parts are called the *method*, the *URI* and the *protocol*.
    We'll look at each in turn below.

.. ifslides::

    Requests start with a *required* first line

    .. rst-class:: build
    .. container::

        Delimited by whitespace into three parts

        *method*, *URI*, *protocol*

        Let's look at each in turn.

::

    GET /path/to/index.html HTTP/1.1


HTTP Methods
------------

**GET** ``/path/to/index.html HTTP/1.1``

.. ifnotslides::

    Every HTTP request first line must start with a *method*.
    Although there are a total of eight possible HTTP methods, four are more commonly seen than others.
    And among these, just two are by far the most common.

    * **GET**
    * **POST**
    * PUT
    * DELETE

.. ifslides::

    .. rst-class:: build

        * HTTP requests must start with a *method*

        * Four main HTTP methods

          .. rst-class:: build

          * GET
          * POST
          * PUT
          * DELETE

        * GET and POST are by far most common

        * Others (8 in all) are not common

.. nextslide::

.. ifnotslides::

    These four methods can be mapped to the four basic steps (*CRUD*) of persistent storage:

.. ifslides::

    Methods map to *CRUD* storage stages

.. rst-class:: build

* POST = Create
* GET = Read
* PUT = Update
* DELETE = Delete


Safe <--> Unsafe
----------------

.. ifnotslides::

    HTTP methods can be categorized as **safe** or **unsafe**, based on whether they might *change persistent data* on the server.
    The distinction is entirely *normative*, which means that it is more a suggestion than a rule.
    You, as an application developer are responsbile for ensuring that this holds true for your websites.
    And you should never assume that other websites follow this rule.

.. ifslides::

    HTTP methods are **safe** or **unsafe**

    .. rst-class:: build
    .. container::

        Depends on if they might *change data* on the server

        Distinction is *normative* only

.. rst-class:: build

* Safe HTTP Methods

  * GET

* Unsafe HTTP Methods

  * POST
  * PUT
  * DELETE


Idempotent <--> Non-Idempotent
------------------------------

.. ifnotslides::

    HTTP methods can be categorized as **idempotent**.
    This is based on whether a given request using the method will **always** have the same result.
    As with safe/unsafe, this distinction is *normative*.
    Things *should* work this way, but do not always.
    You should make sure that your sites *do*.

.. ifslides::

    Can also classify methods as **idempotent**

    .. rst-class:: build
    .. container::

        Means a repeated request will always have the same result

        Also *normative*, be careful

.. rst-class:: build

* Idempotent HTTP Methods

  * GET
  * PUT
  * DELETE

* Non-Idempotent HTTP Methods

  * POST


HTTP Requests: URI
------------------

``GET`` **/path/to/index.html** ``HTTP/1.1``

.. ifnotslides::

    Every HTTP request must include a **URI** used to determine the **resource** to be returned.
    What is a URI?
    How does it relate to the more familiar term URL?
    `This stack overflow question <http://stackoverflow.com/questions/176264/whats-the-difference-between-a-uri-and-a-url/1984225#1984225>`_ provides a solid explanation.

    In static systems, the URI maps directly to a filesystem location on the server.
    In dynamic systems, it may still do so (PHP, CGI, the *Aspen* Python web framework).
    However, it's more common that it is used to determine what program should be used to build a response.

.. ifslides::

    .. rst-class:: build

    * Request must include a **URI**, determines the **resource** to be returned

    * URI??
      http://stackoverflow.com/questions/176264/whats-the-difference-between-a-uri-and-a-url/1984225#1984225

    * Static sites: URI maps to a filesystem location on the server

    * Dynamic systems may also do so (PHP, CGI, *Aspen*)

    * More commonly determines what program should be run to build a response

.. nextslide::

.. ifnotslides::

    Static or dynamic, we call whatever that end point might be a *resource*.
    A *resource* might refer to a file (.html, .jpg, .png, .css, .js), but it can also refer to dynamic scripts, raw data (csv, json, xml), or even api endpoints.
    In any server application, this job of connecting the URI requested to the appropriate end point is very important.

.. ifslides::

    ``GET`` **/path/to/index.html** ``HTTP/1.1``

    The URI points to a *resource*

    .. rst-class:: build

    * Resource?  Files (html, img, .js, .css), but also:

        .. rst-class:: build

        * Dynamic scripts
        * Raw data
        * API endpoints

    * Connecting to the right endpoint is an important task

HTTP Requests: Protocol
-----------------------

``GET /path/to/index.html`` **HTTP/1.1**

.. ifnotslides::

    The *protocol* specified by a request indicates which features a client is able to handle.
    Version 1.1 of the specification added a number of useful advanced features.
    In addition to virtual hosting, connections between clients and servers may be kept open across multiple request/response cycles.

    It is quite rare now to see clients that only support version 1.0.
    A new version (HTTP/2.0) is now finalized, and some services and browsers support it.
    But it is still not widely seen and you can safely ignore it for the time being.
    It is *very* different from the current version.

.. ifslides::

    Determines the features supported by the client

    .. rst-class:: build
    .. container::

        HTTP/1.1 allows holding connections open and other more advanced features

        You will only rarely see ``HTTP/1.0``.

        `HTTP/2.0 <http://http2.github.io>`_ is coming, *very* different

        You can safely ignore it for now


HTTP Responses
==============

.. rst-class:: left

::

    HTTP/1.1 200 OK
    Content-Type: text/plain
    <CRLF>
    this is a pretty minimal response

.. ifnotslides::

    In both HTTP 1.0 and 1.1, a proper response must contain an intial line.
    This is followed by optional headers.
    A single blank line finishes the header section and may be followed by an optional response body.
    As with requests, the initial line of the response is strictly formatted, divided by whitespace into a *protocol* and a *response code*.

.. ifslides::

    .. rst-class:: left
    .. container::

        Responses also require an initial line.

        .. rst-class:: build
        .. container::

            They may also have any number of headers.

            A single blank line ends the header section

            An option body may follow

            Initial line is also divided by whitespace into *protocol* and *response code*

HTTP Response Codes
-------------------

``HTTP/1.1`` **200 OK**

.. ifnotslides::

    All HTTP responses must include a **response code** indicating the outcome of the request.
    The *code* itself is a three-digit number.
    The *explanation* provides a clear-text, human readable description of the condition indicated.

    There are five *categories* of response code.
    Each indicates a different basic condition.
    Individual codes within the categories provide more specific information.

.. ifslides::

    **response codes** indicate the outcome of a request

    .. rst-class:: build
    .. container::

        Codes are three digit numbers

        Explanations are human readable, clarify

        Five basic categories

.. rst-class:: build

* 1xx (HTTP 1.1 only) - Informational message
* 2xx - Success of some kind
* 3xx - Redirection of some kind
* 4xx - Client Error of some kind
* 5xx - Server Error of some kind


Common Response Codes
---------------------

.. ifnotslides::

    There are certain HTTP response codes you are likely to see (and use) most often.
    However, you should not feel constrained to using only these.
    There are a lot of codes available, and using them well is communicative in the same way that using Python exceptions can be.
    For a list of available, official response codes, see `RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`_.

.. ifslides::

    Some codes are common

    .. rst-class:: build
    .. container::

        Don't be afraid of using others

        Response codes are *communication*

        See them all in `RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`_.

.. rst-class:: build

* ``200 OK`` - Everything is good
* ``301 Moved Permanently`` - You should update your link
* ``304 Not Modified`` - You should load this from cache
* ``404 Not Found`` - You've asked for something that doesn't exist
* ``500 Internal Server Error`` - Something bad happened


HTTP Headers
============

.. ifnotslides::

    Headers allow clients and servers to exchange additional structured information.
    They come after the initial line of a request or response.
    Some headers may be used only for a request, some only for a response, and some are fine in either.

    Headers always take the form of key/value pairs: ``<name>: <value>``.
    Names are always fully left-justified.
    They must appear as the first characters on a line.
    They must also be followed by a colon.

    Any number of spaces or tabs may separate the name from the *value* of a header.
    A header value can occupy multiple lines.
    If the first character on a line in the header section of a request or response starts with whitespace, then it is considered to be part of the value for the last named header.

    The names of headers are not case-sensitive.
    However, the values may be, depending on the header.

    It is well worth being familiar with the possible headers for HTTP.
    You can `read more about them here <http://www.cs.tut.fi/~jkorpela/http.html>`_

    There are a couple of headers we'll talk about immediately, because they are so common.

.. ifslides::

    .. rst-class:: left
    .. container::

        Headers carry structured data between client and server

        .. rst-class:: build
        .. container::

            Headers take the form ``<Name>: <Value>``

            Any number of spaces or tabs may separate the *name* from the *value*

            If a header line starts with spaces or tabs, it is considered part of the *value* for the previous header

            Header *names* are **not** case-sensitive, but *values* may be

            Know your headers, learn them `here <http://www.cs.tut.fi/~jkorpela/http.html>`_

            Let's meet some common headers

``Content-Type``
----------------

.. ifnotslides::

    The first is the ``Content-Type`` header.
    It tells the receiver how to treat the data that is in the body of the request or response.
    The header uses the **mime-type** system (Multi-purpose Internet Mail Extensions).
    The list below gives you an idea how files of different types map to particular mime-types.
    There are *many* `mime-type identifiers <http://www.freeformatter.com/mime-types-list.html>`_ and more are being registered all the time.

.. ifslides::

    What *kind of data* is being sent in the body

    .. rst-class:: build
    .. container::

        Uses the **mime-type** system

        Many `mime-types <http://www.freeformatter.com/mime-types-list.html>`_ are registered, more all the time

.. rst-class:: build

* foo.jpeg - ``Content-Type: image/jpeg``
* foo.png - ``Content-Type: image/png``
* bar.txt - ``Content-Type: text/plain``
* baz.html - ``Content-Type: text/html``

.. nextslide:: Mimetypes in Python

.. ifnotslides::

    The Python standard library provides a module that helps in determining the mimetype of a given file.
    It's called :mod:`mimetypes <python2:mimetypes>` (:py:mod:`py3 <mimetypes>`).
    Using this module, you can guess the mime-type of a file based on the filename.
    You can also map a particular file extension to a given mime-type.

    .. code-block:: ipython

        In [1]: textfile = "/path/to/textfile.txt"
        In [2]: import mimetypes
        In [3]: mimetypes.guess_type(textfile)
        Out[3]: ('text/plain', None)
        In [4]: import os
        In [5]: text_extension = os.path.splitext(textfile)
        In [6]: text_extension
        Out[6]: ('/path/to/textfile', '.txt')
        In [7]: mimetypes.types_map[text_extension[1]]
        Out[7]: 'text/plain'

.. ifslides::

    ``mimetypes`` module provides tools for determining mime-type

    .. rst-class:: build
    .. container::

        guess the mime-type based on filename

        map file extension to mime-type

        .. code-block:: ipython

            In [1]: textfile = "/path/to/textfile.txt"
            In [2]: import mimetypes
            In [3]: mimetypes.guess_type(textfile)
            Out[3]: ('text/plain', None)
            In [4]: import os
            In [5]: text_extension = os.path.splitext(textfile)
            In [6]: text_extension
            Out[6]: ('/path/to/textfile', '.txt')
            In [7]: mimetypes.types_map[text_extension[1]]
            Out[7]: 'text/plain'

``Date``
--------

.. ifnotslides::

    Another common HTTP header is the ``Date`` header.
    It represents the date and time that a response was generated.

    The value for this header must be expressed in GMT, not local time.
    It must be in a very specific format::

        Fri, 12 Feb 2010 16:23:03 GMT

    The Python standard library also provides a way of getting exactly this format.
    Since the format is almost exactly the same as that required for email headers, this method is found in a slightly unexpected module:

    .. code-block:: ipython

        In [9]: import email.utils
        In [10]: email.utils.formatdate(usegmt=True)
        Out[10]: 'Mon, 07 Mar 2016 00:57:58 GMT'

.. ifslides::

    ``Date`` header shows date/time that request/respnse was generated

    .. rst-class:: build
    .. container::

        Must be expressed in GMT, not local time

        Must have specific format: ``Fri, 12 Feb 2010 16:23:03 GMT``

        Build it in Python:

        .. code-block:: ipython

            In [9]: import email.utils
            In [10]: email.utils.formatdate(usegmt=True)
            Out[10]: 'Mon, 07 Mar 2016 00:57:58 GMT'

``Content-Length``
------------------

.. ifnotslides::

    A third common HTTP header is the ``Content-Length`` header.
    This header is used to inform the receiver of a request or response how many bytes data to expect in the body.
    Since HTTP does not specify a delimiter for a response body (unlike the SMTP, POP3 and IMAP protocols), this header is particularly important.

    The value for the header should correspond to the number of bytes of data that will be returned (excluding headers).

.. ifslides::

    Represents number of bytes in the *body*

    .. rst-class:: build
    .. container::

        Important since there is not delimiter for the HTTP request/response body

        Only counts length of the body, not headers

.. nextslide:: Calculating ``Content-Length``

.. ifnotslides::

    For binary files like images calculating this value is quite straightforward:

.. ifslides::

    Simple to do for binary files

.. code-block:: pycon

    In [1]: with open('Mars1.jpg', 'rb') as file_handle:
      ....:     mars_image = file_handle.read()
      ....:
    In [2]: length = len(mars_image)
    In [3]: length
    Out[3]: 1161387

.. ifnotslides::

    However, when text is involved it gets a bit more complicated.
    Best practice in Python is to keep text that you are working with as ``unicode`` objects:

.. ifslides:

    With text, more complicated

    Text *in* Python should be unicode:

.. code-block:: ipython

    In [4]: body = u'éclaire'
    In [5]: len(body)
    Out[5]: 7

.. nextslide:: Network Traffic is Bytes

.. ifnotslides::

    Remember that a socket can **only** transmit bytes.
    It cannot handle decoded unicode objects.
    In Python you must be sure that the content of the response body you send has been encoded before it is handed off to the socket for transmission:

.. ifslides::

    Sockets only handle bytes

    Unicode must be encoded before transmission:

.. code-block:: ipython

    In [6]: bytes = body.encode('utf-8')
    In [7]: len(bytes)
    Out[7]: 8

.. ifnotslides::

    Notice that the length of the encoded byte string is *longer* than the decoded unicode string.
    This is because the encoded form of the ``é`` character is actually *two bytes* in length.

.. ifslides::

    Byte representation is longer

    ``é`` character is *two* bytes long

.. nextslide:: Communicating Codecs

.. ifnotslides::

    If the content you send over HTTP is text, the receiver should be able to decode it properly.
    To do so, they must know what *codec* was used to encode it to bytes.
    It is best practice to include information about what *codec* was used in a header.

    It's tempting to think of the ``Content-Encoding`` header as the proper place to send this data.
    In fact that header is used to inform the client of *compressed* data (.zip or similar).
    Instead, the correct way to inform the client of the encoding used is to append a ``charset <name>`` value to the ``Content-Type`` header:

.. ifslides::

    Encoded text needs decoding

    .. rst-class:: build
    .. container::

        Receiver needs to know how to decode it

        Sender must include this information in a header

        Often think of ``Content-Encoding``, but that's for compression

        Use ``charset`` extension to ``Contet-Type`` header value:

::

    Content-Type: text/plain; charset=utf-8


Cookie
------

.. ifnotslides::

    The last HTTP header to call out explicitly is the ``Cookie`` header.
    This particular header is used both by the *client* and by the *server*.
    The server can send data to the client in a ``Cookie`` header.
    The client will send it back on the next request.
    Cookies are thus the primary means of persisting data between individual request/response cycles.
    They are used commonly to store *session-bound* data such as authentication state.

.. ifslides::

    Used by both *client* and *server*

    .. rst-class:: build
    .. container::

        Server sends data to client in header

        Client sends data back to server on next request

        Allows persisting data in *stateless* HTTP

        Used commonly to store session-bound data like authentication state

Wrap Up
=======

.. ifnotslides::

    We've learned about the HTTP protocol in this lesson.
    We learned that there are Requests and Responses.
    That each has a specific format.
    That the header section of each will be separated from the body section by a blank line.
    That the first line of each may be parsed to find out *methods*, *uris*, *status codes* and *protocol versions*.
    We've also learned that headers are used to pass structured data.
    And we've learned about a number of common headers.

    For your assignments, you'll be using this knowledge to build a rudimentary HTTP server.

.. ifslides::

    .. rst-class:: build

    * HTTP is requests and responses
    * Headers are separated from bodies by a blank line
    * The first line contains information about

        - methods
        - uris
        - protocols
        - status codes

    * HTTP headers can pass structured data
    * There are headers that will be very common