.. slideconf::
    :autoslides: False

***************************
Network Protocols in Python
***************************

.. slide:: Network Protocols in Python
    :level: 1

    .. rst-class:: center

    In which we learn how rules govern interactions over a network

During this walkthrough we'll learn the basics of network protocols.

We'll take a look at sample interactions in common network protocols and compare and contrast them.
Doing so can often help us to understand in what situations one protocol would be more appropriate than another.

Finally, we'll interact with one of these protocols using a Python implementation from the standard library.
These library implementations will help you to use a protocol without needing to remember the exact specifics of each.

What is a Protocol?
===================

A protocol is, at it's heart, a set of rules or conventions governing communications.
There are a lot of rules in real life that govern how we do things.
For example, what do you say when you get on an elevator?
How should you behave when you are on a first date?
What do you wear when you go on a job interview?
What sorts of topics are okay to discuss at a dinner party?
All of these questions are answered by sets of rules, spoken or unspoken.
These rules form *protocols*.

.. slide:: What is a Protocol?
    :level: 3

    A set of rules or conventions governing communications

    .. rst-class:: build

    * What do you say when you get on the elevator?

    * What do you do on a first date?

    * What do you wear to a job interview?

    * What do (and don't) you talk about at a dinner party?

    * ...?

.. figure:: /_static/icup.png
    :align: center
    :width: 58%

    http://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/

.. slide:: ICUP
    :level: 3

    .. figure:: /_static/icup.png
        :class: fill

        http://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/

Digital life has lots of rules too.
When two computers make contact they have to greet each-other.
They need to identify themselves to each-other.
There are rules about how to ask for information and how answers will be provided.
There are even rules about how to say goodbye when they are finished.


.. slide:: Digital Rules
    :level: 3

    Digital life has rules too:

    .. rst-class:: build

    * how to say hello

    * how to identify yourself

    * how to ask for information

    * how to provide answers

    * how to say goodbye


Protocol Examples
=================

To get an idea of what network protocols look like, we'll investigate a few of them here.
We'll look at three common protocols leading up to our discussion of `HTTP <http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ (the Hypertext Trasfer Protocol).
Our examples will be `SMTP <http://tools.ietf.org/html/rfc5321#appendix-D>`_ (Simple Message Transfer Protocol),
`POP3 <http://www.faqs.org/docs/artu/ch05s03.html>`_ (Post Office Protocol, version 3),
and `IMAP <http://www.faqs.org/docs/artu/ch05s03.html>`_ (Internet Message Access Protocol).

.. slide:: Protocol Examples
    :level: 3

    What does this look like in practice?

    .. rst-class:: build
    .. container::

        * SMTP (Simple Message Transfer Protocol)
          http://tools.ietf.org/html/rfc5321#appendix-D

        * POP3 (Post Office Protocol, version 3)
          http://www.faqs.org/docs/artu/ch05s03.html

        * IMAP (Internet Message Access Protocol)
          http://www.faqs.org/docs/artu/ch05s03.html

        * HTTP (Hyper-Text Transfer Protocol)
          http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol


The SMTP Protocol
-----------------

The SMTP Protocol governs the sending of email messages.
Let's first look at a few interactions in this protocol.

A few words first about what you are looking at.
Each interaction is line-based, each line represents one message.
Messages from the Server to the Client are prefaced with ``S (<--)``.
Messages from the Client to the Server are prefaced with ``C (-->)``.
**All** lines end with the character sequence ``<CRLF>`` (``\r\n``).

Throughout this document and others, I will be using <CRLF> to represent the combination of two ASCII *escape sequences*: ``"\r\n"``
Although you will see this in **all** of the examples you read in this documentation, you should **never** type it.
It should always be replaced with "\r\n".


.. slide:: A Word on Typography
    :level: 3

    Over the next few slides we'll be looking at server/client interactions.

    .. rst-class:: build
    .. container::

        Each interaction is line-based, each line represents one message.

        Messages from the Server to the Client are prefaced with ``S (<--)``

        Messages from the Client to the Server are prefaced with ``C (-->)``

        **All** lines end with the character sequence ``<CRLF>`` (``\r\n``)

In this first frame, we see a server identifying itself to a client.
The client asks for information from the server about the extensions it supports.
The server responds with a list.

::

    S (<--): 220 foo.com Simple Mail Transfer Service Ready
    C (-->): EHLO bar.com
    S (<--): 250-foo.com greets bar.com
    S (<--): 250-8BITMIME
    S (<--): 250-SIZE
    S (<--): 250-DSN
    S (<--): 250 HELP

.. slide:: SMTP (greetings)
    :level: 3

    .. rst-class:: build
    .. container::

        SMTP (Say hello and identify yourself)::

            S (<--): 220 foo.com Simple Mail Transfer Service Ready
            C (-->): EHLO bar.com
            S (<--): 250-foo.com greets bar.com
            S (<--): 250-8BITMIME
            S (<--): 250-SIZE
            S (<--): 250-DSN
            S (<--): 250 HELP

In this next frame, the client informs the server that it has mail to deliver.
The server acknowledges this.
The client checks the addressees of the outgoing mail.
One of them is known to the server, the other is not.
The client indicates that it will transmit the message, and the server acknowledges this.
The client delivers the message, terminating it with a single dot on aline by itself.
The server acknowledges that it has received the message.

::

    C (-->): MAIL FROM:<Smith@bar.com>
    S (<--): 250 OK
    C (-->): RCPT TO:<Jones@foo.com>
    S (<--): 250 OK
    C (-->): RCPT TO:<Green@foo.com>
    S (<--): 550 No such user here
    C (-->): DATA
    S (<--): 354 Start mail input; end with <CRLF>.<CRLF>
    C (-->): Blah blah blah...
    C (-->): ...etc. etc. etc.
    C (-->): .
    S (<--): 250 OK

.. slide:: SMTP (questions and answers)
    :level: 3

    SMTP (Ask for information, provide answers)::

        C (-->): MAIL FROM:<Smith@bar.com>
        S (<--): 250 OK
        C (-->): RCPT TO:<Jones@foo.com>
        S (<--): 250 OK
        C (-->): RCPT TO:<Green@foo.com>
        S (<--): 550 No such user here
        C (-->): DATA
        S (<--): 354 Start mail input; end with <CRLF>.<CRLF>
        C (-->): Blah blah blah...
        C (-->): ...etc. etc. etc.
        C (-->): .
        S (<--): 250 OK

In the final frame, the client indicates that it is done.
The server acknowledges this, and closes the socket.

::

    C (-->): QUIT
    S (<--): 221 foo.com Service closing transmission channel

.. slide:: SMTP (Say goodbye)
    :level: 3

    ::

        C (-->): QUIT
        S (<--): 221 foo.com Service closing transmission channel

A few characteristics of the SMTP protocol become clear looking at this conversation.
First, the interaction consists of commands and replies.

Each command or reply is *one line* terminated by ``<CRLF>``.
The glaring exception to the one-line rule is message payload.
To accomodate this, the protocol specifies that payload should be terminated by ``<CRLF>.<CRLF>``.

Each command has a *verb* (``DATA``, ``RCPT``, ``EHLO``) and zero or more *arguments* (``TO:<Green@foo.com>``, ``FROM:<Smith@bar.com>``).
Each reply has a formal *code* (``250``, ``550``) and an informal *explanation* (``OK``, ``No such user here``).

.. slide:: SMTP Characteristics
    :level: 3

    .. rst-class:: build

    * Interaction consists of commands and replies
    * Each command or reply is *one line* terminated by <CRLF>
    * The exception is message payload, terminated by <CRLF>.<CRLF>
    * Each command has a *verb* and one or more *arguments*
    * Each reply has a formal *code* and an informal *explanation*

The POP3 Protocol
-----------------

POP3 is an older protocol that governs the reception of emails.
It is similar in structure to SMTP, though reversed in role.

In this first frame, a client connects and the server indicates it is ready.
The client provides a username and the server indicates the user is known.
The client provides a password and the server accepts it, returning basic information about the user's mailbox.

::

    C (-->): <client connects to service port 110>
    S (<--): +OK POP3 server ready <1896.6971@mailgate.dobbs.org>
    C (-->): USER bob
    S (<--): +OK bob
    C (-->): PASS redqueen
    S (<--): +OK bob's maildrop has 2 messages (320 octets)

.. slide:: POP3 (greetings and identification)
    :level: 3

    ::

        C (-->): <client connects to service port 110>
        S (<--): +OK POP3 server ready <1896.6971@mailgate.dobbs.org>
        C (-->): USER bob
        S (<--): +OK bob
        C (-->): PASS redqueen
        S (<--): +OK bob's maildrop has 2 messages (320 octets)

In the next frame, the client asks for the status of the mailbox.
The server replies that there are two messages with a total of 320 ``octets`` of data.
The client requests a listing, and the server lists the first message and its size.
The client asks the server to send the message, and the server does.
Again, this interaction takes many lines, and is terminated with a ``<CRLF>.<CRLF>``.
Finally, the client asks the server to delete the message, and the server replies that is has done so.

::

    C (-->): STAT
    S (<--): +OK 2 320
    C (-->): LIST
    S (<--): +OK 1 messages (120 octets)
    S (<--): 1 120
    S (<--): .
    C (-->): RETR 1
    S (<--): +OK 120 octets
    S (<--): <server sends the text of message 1>
    S (<--): .
    C (-->): DELE 1
    S (<--): +OK message 1 deleted

.. slide:: POP3 (questions and answers)
    :level: 3

    ::

        C (-->): STAT
        S (<--): +OK 2 320
        C (-->): LIST
        S (<--): +OK 1 messages (120 octets)
        S (<--): 1 120
        S (<--): .
        C (-->): RETR 1
        S (<--): +OK 120 octets
        S (<--): <server sends the text of message 1>
        S (<--): .
        C (-->): DELE 1
        S (<--): +OK message 1 deleted

In the final frame, the client indicates it is ready to quit.
The server signs off and the client terminates the connection.

::

    C (-->): QUIT
    S (<--): +OK dewey POP3 server signing off (maildrop empty)
    C (-->): <client hangs up>

.. slide:: POP3 (Say goodbye)
    :level: 3

    ::

        C (-->): QUIT
        S (<--): +OK dewey POP3 server signing off (maildrop empty)
        C (-->): <client hangs up>

Again, a set of characteristics emerges from this interaction.

Everything is a series of commands and replies.
Each command or reply is *one line* terminated by ``<CRLF>``.
Again, the exception to this rule is message payload, which is terminated by ``<CRLF>.<CRLF>``.

Each command has a *verb* (``STAT``, ``LIST``, ``RETR``) and zero or more *arguments* (``1``).
Each reply has a formal *code* (``+OK``) and an informal *explanation* (``message 1 deleted``).
The codes don't really look the same, though, do they?

.. slide:: POP3 Characteristics
    :level: 3

    Again, a set of characteristics emerges:

    .. rst-class:: build

    * Interaction consists of commands and replies
    * Each command or reply is *one line* terminated by <CRLF>
    * The exception is message payload, terminated by <CRLF>.<CRLF>
    * Each command has a *verb* and one or more *arguments*
    * Each reply has a formal *code* and an informal *explanation*
    * The codes don't really look the same, though, do they?

There's one other important difference between SMTP and POP3.
In both protocols an exception to the one-line-per-message rule exists for the payload of an email.
In both protocols, the delineation of this message (the sequence used to indicate it is over) is ``<CRLF>.<CRLF>``.
But in SMTP, it is the *client* that has this ability, whereas in POP3 it is the *server*.

What does that tell you about the *purpose* of the protocol.
Could you tell what these protocols were for, even if you didn't know the names of them?


.. slide:: One Other Difference
    :level: 3

    .. rst-class:: build
    .. container::

        The exception to the one-line-per-message rule is *payload*

        In both SMTP and POP3 this is terminated by <CRLF>.<CRLF>

        In SMTP, the *client* has this ability

        But in POP3, it belongs to the *server*.  Why?


The IMAP Protocol
-----------------

The IMAP protocol is a more modern protocol for receiving email messages.
It has largely supplanted POP3.
Looking at the protocol can help us to understand why.

In this first frame, the client and the server exchange greetings.
The client provides authentication information and the server accepts it.
Then the client selects a folder to work in and the server provides information about that folder.

::

    C (-->): <client connects to service port 143>
    S (<--): * OK example.com IMAP4rev1 v12.264 server ready
    C (-->): A0001 USER "frobozz" "xyzzy"
    S (<--): * OK User frobozz authenticated
    C (-->): A0002 SELECT INBOX
    S (<--): * 1 EXISTS
    S (<--): * 1 RECENT
    S (<--): * FLAGS (\Answered \Flagged \Deleted \Draft \Seen)
    S (<--): * OK [UNSEEN 1] first unseen message in /var/spool/mail/esr
    S (<--): A0002 OK [READ-WRITE] SELECT completed


.. slide:: IMAP (greetings, information)
    :level: 3

    IMAP (Say hello and identify yourself)::

        C (-->): <client connects to service port 143>
        S (<--): * OK example.com IMAP4rev1 v12.264 server ready
        C (-->): A0001 USER "frobozz" "xyzzy"
        S (<--): * OK User frobozz authenticated

    IMAP (Ask for information, provide answers [connect to an inbox])::

        C (-->): A0002 SELECT INBOX
        S (<--): * 1 EXISTS
        S (<--): * 1 RECENT
        S (<--): * FLAGS (\Answered \Flagged \Deleted \Draft \Seen)
        S (<--): * OK [UNSEEN 1] first unseen message in /var/spool/mail/esr
        S (<--): A0002 OK [READ-WRITE] SELECT completed

Next, the client asks the server for the size of the first email listed.
The server replies with the data.
The client then asks the server to download the headers from the email.
The server indicates how much data will be sent and then sends it.

::

    C (-->): A0003 FETCH 1 RFC822.SIZE
    S (<--): * 1 FETCH (RFC822.SIZE 2545)
    S (<--): A0003 OK FETCH completed
    C (-->): A0004 FETCH 1 BODY[HEADER]
    S (<--): * 1 FETCH (RFC822.HEADER {1425}
    <server sends 1425 octets of message payload>
    S (<--): )
    S (<--): A0004 OK FETCH completed

.. slide:: IMAP (questions and answers)
    :level: 3

    IMAP (Ask for information, provide answers [Get message sizes])::

        C (-->): A0003 FETCH 1 RFC822.SIZE
        S (<--): * 1 FETCH (RFC822.SIZE 2545)
        S (<--): A0003 OK FETCH completed

    IMAP (Ask for information, provide answers [Get first message header])::

        C (-->): A0004 FETCH 1 BODY[HEADER]
        S (<--): * 1 FETCH (RFC822.HEADER {1425}
        <server sends 1425 octets of message payload>
        S (<--): )
        S (<--): A0004 OK FETCH completed

Finally, the client asks for the body of the first email.
The server tells the client how much data to expect and then sends it.
The client logs out, indicating that it is done.
The server acknowledges this and the client disconnects.

::

    C (-->): A0005 FETCH 1 BODY[TEXT]
    S (<--): * 1 FETCH (BODY[TEXT] {1120}
    <server sends 1120 octets of message payload>
    S (<--): )
    S (<--): * 1 FETCH (FLAGS (\Recent \Seen))
    S (<--): A0005 OK FETCH completed
    C (-->): A0006 LOGOUT
    S (<--): * BYE example.com IMAP4rev1 server terminating connection
    S (<--): A0006 OK LOGOUT completed
    C (-->): <client hangs up>

.. slide:: IMAP (questions and goodbye)
    :level: 3

    IMAP (Ask for information, provide answers [Get first message body])::

        C (-->): A0005 FETCH 1 BODY[TEXT]
        S (<--): * 1 FETCH (BODY[TEXT] {1120}
        <server sends 1120 octets of message payload>
        S (<--): )
        S (<--): * 1 FETCH (FLAGS (\Recent \Seen))
        S (<--): A0005 OK FETCH completed

    IMAP (Say goodbye)::

        C (-->): A0006 LOGOUT
        S (<--): * BYE example.com IMAP4rev1 server terminating connection
        S (<--): A0006 OK LOGOUT completed
        C (-->): <client hangs up>

What characteristics emerge from this conversation?

Like with our other protocol examples, interactions consists of commands and replies.
Again, each command or reply is *one line* terminated by ``<CRLF>``.
Again, each command has a *verb* (``FETCH``, ``LOGOUT``) and zero or more *arguments* (`` 1 BODY[TEXT]``, ``1 RFC822.SIZE``).
And again, each reply has a formal *code* (``OK``) and an informal *explanation* (``[READ-WRITE] SELECT completed``, ``FETCH completed``).

But there are important differences too.
For example, in IMAP each command or reply is prefixed by a *sequence identifier* (``A0006``).
And multi-line replies such as fetching message headers or bodies are prefixed with the expected size of the data to be transmitted.
There is no special delineating character that marks the end of the data.

Compared with POP3, what do these differences suggest?
What can you do when you know which replies go with which requests?
What can you do if you know ahead of time how much data will be downloaded?


.. slide:: IMAP Characteristics
    :level: 3

    Similarities:

    .. rst-class:: build

    * Interaction consists of commands and replies
    * Each command or reply is *one line* terminated by <CRLF>
    * Each command has a *verb* and one or more *arguments*
    * Each reply has a formal *code* and an informal *explanation*

    .. rst-class:: build
    .. container::

        And differences:

        .. rst-class:: build

        * Commands and replies are prefixed by 'sequence identifier'
        * Payloads are prefixed by message size, rather than terminated by reserved
          sequence

        Compared with POP3, what do these differences suggest?

Using Protocols in Python
=========================

To help make these protocols a bit more clear, let's play with one ourselves.
Go ahead and start up an iPython interpreter.

Begin by importing the :mod:`imaplib <python2:imaplib>` module (:py:mod:`py3 <imaplib>`) from the Python standard library.
Then, set the ``Debug`` attribute of the module to ``4`` so that we can see the messages sent back and forth between the server and ourselves.

.. code-block:: ipython

    In [1]: import imaplib
    In [2]: dir(imaplib)
    Out[2]:
    ['AllowedVersions',
     'CRLF',
     'Commands',
    ...
     'timedelta',
     'timezone']
    In [3]: imaplib.Debug = 4

.. slide:: Playing with IMAP
    :level: 3

    start iPython and import ``imaplib``:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [1]: import imaplib
            In [2]: dir(imaplib)
            Out[2]:
            ['AllowedVersions',
             'CRLF',
             'Commands',
            ...
             'timedelta',
             'timezone']
            In [3]: imaplib.Debug = 4

        Setting ``imap.Debug`` shows us what is sent and received

I've prepared a server for us to use, but we'll need to set up a client to speak to it.
Our server requires SSL (Secure Socket Layer) for connecting to IMAP servers, so let's initialize an IMAP4_SSL client.
Then we will authenticate by providing a username and password.
The correct values to use here will be passed out via the class slack channel.

.. code-block:: ipython

    In [4]: conn = imaplib.IMAP4_SSL('mail.webfaction.com')
      22:40.32 imaplib version 2.58
      22:40.32 new IMAP4 connection, tag=b'IMKC'
      22:40.38 < b'* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot ready.'
      22:40.38 > b'IMKC0 CAPABILITY'
      22:40.45 < b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN'
      22:40.45 < b'IMKC0 OK Capability completed.'
      22:40.45 CAPABILITIES: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS', 'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
    In [5]: conn.login('username', 'password')
      22:59.92 > b'IMKC1 LOGIN username "password"'
      23:01.79 < b'* CAPABILITY IMAP4rev1 SASL-IR SORT THREAD=REFERENCES MULTIAPPEND UNSELECT LITERAL+ IDLE CHILDREN NAMESPACE LOGIN-REFERRALS STARTTLS AUTH=PLAIN'
      23:01.79 < b'IMKC1 OK Logged in.'
    Out[5]: ('OK', [b'Logged in.'])

.. slide:: Connecting and Authenticating
    :level: 3

    .. rst-class:: build
    .. container::

        Our server requires SSL (Secure Socket Layer) for connecting to IMAP
        servers, so let's initialize an IMAP4_SSL client and authenticate:

        .. code-block:: ipython

            In [4]: conn = imaplib.IMAP4_SSL('mail.webfaction.com')
              22:40.32 imaplib version 2.58
              22:40.32 new IMAP4 connection, tag=b'IMKC'
              22:40.38 < b'* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot ready.'
              22:40.38 > b'IMKC0 CAPABILITY'
              22:40.45 < b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN'
              22:40.45 < b'IMKC0 OK Capability completed.'
              22:40.45 CAPABILITIES: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS', 'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
            In [5]: conn.login('username', 'password')
              22:59.92 > b'IMKC1 LOGIN username "password"'
              23:01.79 < b'* CAPABILITY IMAP4rev1 SASL-IR SORT THREAD=REFERENCES MULTIAPPEND UNSELECT LITERAL+ IDLE CHILDREN NAMESPACE LOGIN-REFERRALS STARTTLS AUTH=PLAIN'
              23:01.79 < b'IMKC1 OK Logged in.'
            Out[5]: ('OK', [b'Logged in.'])

Once we have logged in, we can start by :meth:`listing <python2:imaplib.IMAP4.list>` (:py:meth:`py3 <imaplib.IMAP4.list>`) the mailboxes we have on the server.

.. code-block:: ipython

    In [6]: conn.list()
      26:30.64 > b'IMKC2 LIST "" *'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Trash"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Drafts"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Sent"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Junk"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "INBOX"'
      26:30.72 < b'IMKC2 OK List completed.'
    Out[6]:
    ('OK',
     [b'(\\HasNoChildren) "." "Trash"',
      b'(\\HasNoChildren) "." "Drafts"',
      b'(\\HasNoChildren) "." "Sent"',
      b'(\\HasNoChildren) "." "Junk"',
      b'(\\HasNoChildren) "." "INBOX"'])

.. slide:: Listing Mailboxes
    :level: 3

    .. code-block:: ipython

        In [6]: conn.list()
          26:30.64 > b'IMKC2 LIST "" *'
          26:30.72 < b'* LIST (\\HasNoChildren) "." "Trash"'
          26:30.72 < b'* LIST (\\HasNoChildren) "." "Drafts"'
          26:30.72 < b'* LIST (\\HasNoChildren) "." "Sent"'
          26:30.72 < b'* LIST (\\HasNoChildren) "." "Junk"'
          26:30.72 < b'* LIST (\\HasNoChildren) "." "INBOX"'
          26:30.72 < b'IMKC2 OK List completed.'
        Out[6]:
        ('OK',
         [b'(\\HasNoChildren) "." "Trash"',
          b'(\\HasNoChildren) "." "Drafts"',
          b'(\\HasNoChildren) "." "Sent"',
          b'(\\HasNoChildren) "." "Junk"',
          b'(\\HasNoChildren) "." "INBOX"'])

To interact with our email, we must :meth:`select <python2:imaplib.IMAP4.select>` (:py:meth:`py3 <imaplib.IMAP4.select>`) a mailbox from the list we received earlier.
We use the name of the mailbox as the argument to the method.
Then the commands we give will be taken on messages held in that mailbox only.

.. code-block:: ipython

    In [7]: conn.select('INBOX')
      27:20.96 > b'IMKC3 SELECT INBOX'
      27:21.04 < b'* FLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft)'
      27:21.04 < b'* OK [PERMANENTFLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*)] Flags permitted.'
      27:21.04 < b'* 1 EXISTS'
      27:21.04 < b'* 0 RECENT'
      27:21.04 < b'* OK [UNSEEN 1] First unseen.'
      27:21.04 < b'* OK [UIDVALIDITY 1357449499] UIDs valid'
      27:21.04 < b'* OK [UIDNEXT 24] Predicted next UID'
      27:21.04 < b'IMKC3 OK [READ-WRITE] Select completed.'
    Out[7]: ('OK', [b'1'])

.. slide:: Selecting an Inbox
    :level: 3

    .. code-block:: ipython

        In [7]: conn.select('INBOX')
          27:20.96 > b'IMKC3 SELECT INBOX'
          27:21.04 < b'* FLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft)'
          27:21.04 < b'* OK [PERMANENTFLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*)] Flags permitted.'
          27:21.04 < b'* 1 EXISTS'
          27:21.04 < b'* 0 RECENT'
          27:21.04 < b'* OK [UNSEEN 1] First unseen.'
          27:21.04 < b'* OK [UIDVALIDITY 1357449499] UIDs valid'
          27:21.04 < b'* OK [UIDNEXT 24] Predicted next UID'
          27:21.04 < b'IMKC3 OK [READ-WRITE] Select completed.'
        Out[7]: ('OK', [b'1'])

We can :meth:`search <python2:imaplib.IMAP4.search>` (:py:meth:`py3 <imaplib.IMAP4.search>`) our selected mailbox for messages matching one or more criteria.
The syntax for searching asks for an encoding (if you are using special unicode characters) and then a special statement indicating what you are searching for and in what part of messages to look.

.. rst-class:: build
.. container::

    The return value is a list of bytestrings containing the UIDs of messages
    that match our search:

    .. code-block:: ipython

        In [8]: conn.search(None, '(FROM "cris")')
          28:43.02 > b'IMKC4 SEARCH (FROM "cris")'
          28:43.09 < b'* SEARCH 1'
          28:43.09 < b'IMKC4 OK Search completed.'
        Out[8]: ('OK', [b'1'])

.. slide:: Searching
    :level: 3

    .. rst-class:: build
    .. container::

        The return value is a list of bytestrings containing the UIDs of messages
        that match our search:

        .. code-block:: ipython

            In [8]: conn.search(None, '(FROM "cris")')
              28:43.02 > b'IMKC4 SEARCH (FROM "cris")'
              28:43.09 < b'* SEARCH 1'
              28:43.09 < b'IMKC4 OK Search completed.'
            Out[8]: ('OK', [b'1'])


Once we've found a message we want to look at, we can use the :meth:`fetch <imaplib.IMAP4.fetch>` (:py:meth:`py3 <imaplib.IMAP4.fetch>`) command to read it from the server.
The command requires two arguments, the ID of the message we want, and then a designator of the message part we want to fetch.

.. code-block:: ipython

    In [9]: conn.fetch('1', 'BODY[HEADER]')
      ...
    Out[9]: ('OK', ...)

    In [10]: conn.fetch('1', 'FLAGS')
      ...
    Out[10]: ('OK', [b'1 (FLAGS (\\Seen))'])

    In [11]: conn.fetch('1', 'BODY[TEXT]')
      ...
    Out[11]: ('OK', ...)

.. slide:: Fetching
    :level: 3

    IMAP allows fetching each part of a message independently:

    .. rst-class:: build
    .. container::

        .. code-block:: ipython

            In [9]: conn.fetch('1', 'BODY[HEADER]')
              ...
            Out[9]: ('OK', ...)

            In [10]: conn.fetch('1', 'FLAGS')
              ...
            Out[10]: ('OK', [b'1 (FLAGS (\\Seen))'])

            In [11]: conn.fetch('1', 'BODY[TEXT]')
              ...
            Out[11]: ('OK', ...)

        What does the message say?


Python Means Batteries Included
-------------------------------

It's a bit hard to decipher the message from the body text we downloaded directly via IMAP.
We can use the :mod:`email <python2:email>` module (:py:mod:`py3 <email>`) to construct an email object from the RFC822 format message.
Begin by fetching the message from the IMAP server in the appropriate format:

.. code-block:: ipython

    In [12]: import email
    In [13]: code, data = conn.fetch('1', '(RFC822)')
      13:14.75 > b'BLBK5 FETCH 1 (RFC822)'
      13:14.91 < b'* 1 FETCH (RFC822 {5310}'
      13:14.91 read literal size 5310
      13:15.01 < b')'
      13:15.01 < b'BLBK5 OK Fetch completed.'

    In [14]: code
    Out[14]: 'OK'

    In [15]: data
    Out[15]:
    [(b'1 (RFC822 {5310}',
      b'Return-Path: <cris@crisewing.com>\r\n
      ...

.. slide:: Batteries Included
    :level: 3

    download an entire message in RFC822 format:

    .. rst-class:: build
    .. container::
    
        .. code-block:: ipython

            In [12]: import email
            In [13]: typ, data = conn.fetch('1', '(RFC822)')
              13:14.75 > b'BLBK5 FETCH 1 (RFC822)'
              13:14.91 < b'* 1 FETCH (RFC822 {5310}'
              13:14.91 read literal size 5310
              13:15.01 < b')'
              13:15.01 < b'BLBK5 OK Fetch completed.'

            In [14]: typ
            Out[14]: 'OK'

            In [15]: data
            Out[15]:
            [(b'1 (RFC822 {5310}',
              b'Return-Path: <cris@crisewing.com>\r\n
              ...

The return value is a code and the data we requested.
The data is in the format of a tuple, which we can use to build an email message using the :func:`python2:email.message_from_string` function (in Python 3 this is renamed to :py:func:`email.message_from_bytes`).
The resulting :class:`message object <python2:email.Message>` (:py:class:`py3 <email.Message>`) holds headers from the original email in key-value pairs (like a ``dict``):

.. code-block:: ipython

    In [16]: for part in data:
       ....:     if isinstance(part, tuple):
       ....:         msg = email.message_from_bytes(part[1])
       ....:
    In [17]:

.. code-block:: ipython

    In [18]: msg.keys()
    Out[18]:
    ['Return-Path',
     'X-Original-To',
     'Delivered-To',
     ...

    In [19]: msg['To']
    Out[19]: 'demo@crisewing.com'


.. slide:: Build an Email Object
    :level: 3

    Parse the returned data to get to the actual message:

    .. code-block:: ipython

        In [16]: for part in data:
           ....:     if isinstance(part, tuple):
           ....:         msg = email.message_from_bytes(part[1])
           ....:
        In [17]:

    .. rst-class:: build
    .. container::
    
        .. code-block:: ipython

            In [18]: msg.keys()
            Out[18]:
            ['Return-Path',
             'X-Original-To',
             'Delivered-To',
             ...

            In [19]: msg['To']
            Out[19]: 'demo@crisewing.com'


And we can get the payload of the message, and print the non-html portion of it:

.. code-block:: ipython

    In [29]: print(msg.get_payload()[0].as_string())
    Content-Transfer-Encoding: quoted-printable
    Content-Type: text/plain;
        charset=us-ascii

    If you are reading this email, you've managed to download it from the =
    mailbox using IMAP.

    Don't you feel accomplished?

    Now, on to bigger and better tasks!


    Cris Ewing
    --------------------------------------------------
    Principal, Cris Ewing, Developer LLC
    http://www.crisewing.com
    cris@crisewing.com
    1.206.724.2112

.. slide:: Read the Email
    :level: 3

    We can read the message payload:

    .. code-block:: ipython

        In [29]: print(msg.get_payload()[0].as_string())
        Content-Transfer-Encoding: quoted-printable
        ...

        If you are reading this email, you've managed to download it from the =
        mailbox using IMAP.

        Don't you feel accomplished?

        Now, on to bigger and better tasks!


        Cris Ewing


Wrap Up
=======

In this lesson we have learned that protocols are just a set of rules for how to communicate.
We've learned that among these rules are ones to tell us how we can parse messages sent using a protocol.
We can also tell which messages are valid according to a protocol.

If we properly format messages we send *to* a server, we can get messages in response *from* the server.
Python has built-in modules to support a number of these protocols.
The modules allow you to use a Python API to interact with the protocol, so you don't have to remember exactly how to format the messages you send.

But in every case we've seen today, you could accomplish the same things by properly formatting a byte string and sending it through a socket to a server.

Armed with this knowledge, we'll next look at a particular protocol.
One we will be using for the rest of our class.
This protocol is HTTP.

.. slide:: Summary
    :level: 3

    .. rst-class:: build

    * Protocols are just a set of rules for how to communicate

    * Protocols tell us how to parse and delimit messages

    * Protocols tell us what messages are valid

    * If we properly format messages to a server, we can get responses back

    * Python supports a number of these protocols

    * We don't have to remember how to format the commands ourselves

    * But we can do the same thing with a socket and some properly formatted strings
