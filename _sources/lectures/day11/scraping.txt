****************************
Extracting Data from the Web
****************************

.. rst-class:: left
.. container::

    The internet makes a vast quantity of data available.

    .. rst-class:: build
    .. container::
    
        But not always in the form or combination you want.

        It can be nice to combine data from different sources to create
        *meaning*.


Part 1: Web Scraping
====================

.. rst-class:: left
.. container::

    Data online comes in many different formats:

    .. rst-class:: build
    .. container::
    
        .. rst-class:: build

        * Simple websites with static (or perhaps dynamic) data in HTML
        * Web services providing structured data
        * Web services providing tranformative service (geocoding)
        * Web services providing presentation (mapping)

        Let's concentrate for now on that first class of data, HTML.


HTML Data
---------

Ideally HTML would be well-formed and strictly correct in it's structure:

.. code-block:: html

    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
        <p>A nice clean paragraph</p>
        <p>And another nice clean paragraph</p>
      </body>
    </html>

.. nextslide::

But in fact, it usually ends up looking more like this:

.. code-block:: html

    <html>
     <form>
      <table>
       <td><input name="input1">Row 1 cell 1
       <tr><td>Row 2 cell 1
      </form>
      <td>Row 2 cell 2<br>This</br> sure is a long cell
     </body>
    </html>

This is the result of one of the fundamental laws of the internet:

**"Be strict in what you send and tolerant in what you receive"**

.. nextslide::

.. rst-class:: centered
.. container::

    .. figure:: /_static/scream.jpg
        :align: center
        :width: 35%

        Photo by Matthew via Flickr (http://www.flickr.com/photos/purplemattfish/3918004964/) - CC-BY-NC-ND


Cleaning Up the Mess
--------------------

.. ifnotslides::

    My favorite library for dealing with the mess that HTML can become is
    `BeautifulSoup`_. So let's go ahead and create a virtualenv for playing
    with it a bit:

.. ifslides::

    I use `BeautifulSoup`_ to clean up messy HTML

    .. rst-class:: build
    .. container::
    
        Let's make a virtualenv and play with it a bit.

        .. code-block:: bash

            heffalump:~ cewing$ mkproject souptests
            New python executable in souptests/bin/python
            Installing setuptools, pip...done.
            Creating /Users/cewing/projects/souptests
            Setting project for souptests to /Users/cewing/projects/souptests
            [souptests]
            heffalump:souptests cewing$

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

.. nextslide:: Install BeautifulSoup

Then, install the correct version of BeautifulSoup (you want 4, not 3):

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ pip install beautifulsoup4
    Downloading/unpacking beautifulsoup4
      Downloading beautifulsoup4-4.3.2.tar.gz (143kB): 143kB downloaded
      Running setup.py (path:/Users/cewing/virtualenvs/souptests/build/beautifulsoup4/setup.py) egg_info for package beautifulsoup4

    Installing collected packages: beautifulsoup4
      Running setup.py install for beautifulsoup4

    Successfully installed beautifulsoup4
    Cleaning up...
    [souptests]
    heffalump:souptests cewing$

.. nextslide:: HTML Parsers

BeautifulSoup can use the Python HTMLParser.

.. rst-class:: build
.. container::

    **PRO**: Batteries Included.  It's already there

    **CON**: It's not great, especially before Python 2.7.3

    BeautifulSoup also supports using other parsers.

    There are two good choices: `lxml`_  and `html5lib`_.

.. _lxml: http://lxml.de
.. _html5lib: http://html5lib.readthedocs.org.

.. nextslide:: Install ``html5lib``

``lxml`` is better, but it can be much harder to install.  For our exercise,
Let's use ``html5lib``:

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ pip install html5lib
    Downloading/unpacking html5lib
      Downloading html5lib-0.999.tar.gz (885kB): 885kB downloaded
      Running setup.py (path:/Users/cewing/virtualenvs/souptests/build/html5lib/setup.py) egg_info for package html5lib

    Downloading/unpacking six (from html5lib)
      Downloading six-1.5.2-py2.py3-none-any.whl
    Installing collected packages: html5lib, six
      Running setup.py install for html5lib

    Successfully installed html5lib six
    Cleaning up...
    [souptests]
    heffalump:souptests cewing$

.. nextslide:: Defaults and Configuration

Once installed, BeautifulSoup will choose ``html5lib`` automatically. 

.. rst-class:: build
.. container::

    Actually, BeautifulSoup will choose the "best" available.

    You can specify the parser if you need to control it *and* you have more
    than one parser available.

Getting Webpages
----------------

As with IMAP, FTP and other web protocols, Python provides tools for using HTTP
as a client. They are spread across the ``urllib`` and ``urllib2`` packages.

.. rst-class:: build
.. container::

    These packages have pretty unintuitive APIs.

    The ``requests`` library is becoming the de-facto standard for this type of
    work.  Let's install it too.

    .. code-block:: bash

        [souptests]
        heffalump:souptests cewing$ pip install requests
        Downloading/unpacking requests
          Downloading requests-2.2.1-py2.py3-none-any.whl (625kB): 625kB downloaded
        Installing collected packages: requests
        Successfully installed requests
        Cleaning up...
        [souptests]
        heffalump:souptests cewing$

.. nextslide:: The ``requests`` API

In ``requests``, each HTTP method is provided by a module-level function:

.. rst-class:: build

* ``GET`` == ``requests.get(url, **kwargs)``
* ``POST`` == ``requests.post(url, **kwargs)``
* ...

.. rst-class:: build
.. container::

    Those unspecified ``kwargs`` represent other parts of an HTTP request:

    .. rst-class:: build

    * ``params``: a dict of url query parameters (?foo=bar&baz=bim)
    * ``headers``: a dict of headers to send with the request
    * ``data``: the body of the request, if any (form data for POST goes here)
    * ...

.. nextslide::

The return value from one of these functions is a ``response`` which provides:

.. rst-class:: build

* ``response.status_code``: see the HTTP Status Code returned
* ``response.ok``: True if ``response.status_code`` is not an error
* ``response.raise_for_status()``: call to raise a python error if it is
* ``response.headers``: The headers sent from the server
* ``response.text``: Body of the response, decoded to unicode
* ``response.encoding``: The encoding used to decode
* ``response.content``: The original encoded response body as bytes

.. rst-class:: build
.. container::

    You can `read more about this library`_ on your own.

    I urge you to do so.

    .. _read more about this library: http://requests.readthedocs.org


An Example: Scraping Blog Posts
===============================

.. rst-class:: left
.. container::

    Let's use the tools we've set up here to play with scraping a simple
    structure, a list of blog posts.

    Begin by firing up a Python interpreter:

    .. code-block:: bash

        [souptests]
        heffalump:souptests cewing$ python
        Python 2.7.5 (default, Aug 25 2013, 00:04:04)
        [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

Fetching a Page
---------------

The first step is to fetch the page we'll be scraping.

.. ifnotslides::

    I've created a shortened url that points to a feed aggregator for open
    source blog posts.  Unfortunately, ``tinyurl`` won't issue a proper
    redirect response for requests that come from the ``requests`` library, so
    we'll have to pretend we are a real web browser.

.. ifnotslides::

    Open the developer tools for your browser and make sure you are viewing the
    *Network* tab so you can see network traffic your browser sends and
    receives. Load the url http:/tinyurl.com/sample-oss-posts in a new tab.
    Back in the network tab, click on the requests that went to tinyurl.  Find
    the headers for the request and copy the ``User-Agent`` header value. Then
    begin to follow along in your Python interpreter:

.. ifslides::

    .. rst-class:: build

    * Open the url http://tinyurl.com/sample-oss-posts in your browser
    * Check the network tab of your developer tools and get the value of the
      ``User-Agent`` header
    * We'll use it to bypass ``tinyurl``\ 's efforts to block us.

.. nextslide::

.. code-block:: pycon

    >>> import requests
    >>> url = 'http://tinyurl.com/sample-oss-posts'
    >>> ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'
    >>> headers = {'User-Agent': ua}
    >>> resp = requests.get(url, headers=headers)
    >>> resp
    <Response [200]>
    >>> foo = resp.text
    >>> len(foo)
    601747
    >>> resp.encoding
    'utf-8'
    >>> type(foo)
    <type 'unicode'>

.. nextslide::

Let's prevent ourselves from having to repeat that step by writing our fetched
webpage out to the filesystem:

.. code-block:: pycon

    >>> bytes = resp.content
    >>> len(bytes)
    602455
    >>> with open('blog_list.html', 'w') as outfile:
    ...     outfile.write(bytes)
    ...
    >>> import os
    >>> os.listdir(os.getcwd())
    ['blog_list.html', ...]
    >>>

.. nextslide::

You should now be able to open the new file in your web browser.  Do so.

.. rst-class:: build
.. container::

    The first step is to identify the smallest container element comment to all
    the things you want to extract.  We want to get all blog posts, so let's
    find the container that wraps each one.

    **What's the best tool for getting this information from a web page?**


Parsing HTML
------------

.. ifnotslides::

    When you look at the HTML from this webpage in your browser's devtools, it
    displays as a formatted structure of HTML tags.  We can interact with those
    tags in devtools because they are actually just representations of a DOM node.
    (DOM stands for `Document Object Model`_)

    In order to work with the page in the same fashion in Python, we need to
    **parse** it into the same kind of structure.  That's what ``BeautifulSoup``
    does for us.

.. ifslides::

    .. rst-class:: build

    * The ``devtools`` in Chrome or other browsers show a structure of HTML
      tags
    * You can interact with them because they are representations of a code
      *object*, a *DOM Node*.
    * The *DOM* (`Document Object Model`_) represents HTML as a tree of these
      nodes.
    * We must parse our big HTML string into a *DOM Tree*.
    * This is what ``BeautifulSoup`` does for us:

.. rst-class:: build
.. code-block:: pycon

    >>> from bs4 import BeautifulSoup
    >>> parsed = BeautifulSoup(resp.text)
    >>> len(parsed)
    2
    >>>

.. _Document Object Model: http://en.wikipedia.org/wiki/Document_Object_Model

.. nextslide:: DOM Objects

So parsing the document took the length from 601747 characters to 2 *??*. What
are those two things?

.. rst-class:: build
.. code-block:: pycon

    >>> [type(t) for t in parsed]
    [<class 'bs4.element.Doctype'>, <class 'bs4.element.Tag'>]
    >>>

.. rst-class:: build
.. container::

    Once an html page has been parsed by ``BeautifulSoup``, everything becomes a
    ``node``.  The parsed document itself is a ``node`` and ``nodes`` are iterable.

    When you iterate over a node, you get the nodes that it contains in the DOM
    tree.

.. nextslide:: Node Types

These nodes can be roughly classed into two types, ``NavigableString`` and
``Tag``

.. rst-class:: build
.. container::

    The main difference is that ``Tag`` nodes can contain text or other nodes,
    where ``NavigableStrings`` contain **only** text.

    You can interact with these node types in a number of ways.

    The most common are  *Searching* and *Traversing*

    Let's start with the simpler of the two, *searching*.


Searching HTML
--------------

A ``Tag`` in ``BeautifulSoup`` has a couple of methods that support searching:

``tag.find()``:
  will find the first instance of a node that matches the search specification

``tag.find_all()``:
  will find **all** instances that match the search specification.

.. nextslide:: Search Specifications

So, How do we build a specification for searching? The call signature for
``find_all`` helps a bit::

    tag.find_all(name, attrs, recursive, text, limit, **kwargs)

.. rst-class:: build

* ``name`` is the name of an html tag type ('a', 'p', 'div', etc.)
* ``attrs`` is a dictionary of key-value pairs where the key is an html
  attribute name and the value is the value you want to match.
* ``recursive`` controls whether to find *descendents* (the default) or just
  *children* (recursive=False)
* ``text`` allows you to find ``NavigableString`` nodes instead of ``Tag`` nodes.
* ``limit`` controls how many to find, maximum.

.. nextslide:: Arbitrary Arguments

.. rst-class:: build
.. container::

    The last element **kwargs** allows you to pass arbitrary keyword arguments.

    If the argument you pass is not recognized as one of the other arguments,
    it will be treated as the name of an *HTML attribute* to filter on.

    Passing ``id="my-div"`` would result in a search for any item with the id
    "my-div":

    .. code-block:: html

        <div id="my-div">This is found</div>
        <div id="other-div">This would not be</div>


    .. ifslides::

        **NOTE** ``class`` is a keyword in Python. You can't use it as a
        symbol. You'll have to use ``class_`` instead: (``class_="button"``)

.. ifnotslides::

    .. note::

        because ``class`` is a keyword in python, you can't use it as a keyword
        argument.  Instead you should use ``class_`` (``class_="button"``)

.. nextslide:: Building Our Search

Looking at the blog listing, we can see that the container that is wrapped
around each post shares a common *CSS class*: ``feedEntry``. Let's grab all of
them:

.. code-block:: pycon

    >>> entries = parsed.find_all('div', class_='feedEntry')
    >>> len(entries)
    70
    >>>

Okay. That works.

.. nextslide:: Extracting Titles

Let's see if we can extract a list of the titles of each post.

For this, we want to make sure we find the **first** anchor tag in each entry,
and then extract the text it contains:

.. code-block:: pycon

    >>> e1 = entries[0]
    >>> e1.find('a').text
    u'\n            Dimitri Fontaine: PostgreSQL, Aggregates and Histograms\n        '
    >>> e1.find('a').find('h2').string
    u'Dimitri Fontaine: PostgreSQL, Aggregates and Histograms'
    >>> titles = [e.find('a').find('h2').string for e in entries]
    >>> len(titles)
    70
    >>>

.. nextslide:: Extracting Sources

.. ifnotslides::

    We can also find the set of possible sources for our blog posts.  The
    byline is contained in a ``<p>`` tag with the CSS class ``discreet``.
    Let's gather up all of those and see what we have:

.. ifslides::

    Find the ``<p class="discreet" />`` nodes that contain the bylines:

.. code-block:: pycon

    >>> byline = e1.find('p', class_='discreet')
    >>> len(list(byline.children))
    3
    >>> [type(n) for n in list(byline.children)]
    [<class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>,
     <class 'bs4.element.NavigableString'>]
    >>> classifier = list(byline.children)[0].strip()
    >>> classifier
    u'From Planet PostgreSQL.\n            \n            \n                Published on'
    >>> all_bylines = [e.find('p', class_='discreet') for e in entries]
    >>> len(all_bylines)
    70
    >>> all_classifiers = [list(b.children)[0].strip() for b in all_bylines]
    >>> len(all_classifiers)
    70
    >>> all_classifiers[0]
    u'From Planet PostgreSQL.\n            \n            \n                Published on'

.. nextslide:: Find Unique Sources

.. ifslides::

    There is a limited set of unique values in that pool of bylines:

.. code-block:: pycon

    >>> unique_classifiers = set(all_classifiers)
    >>> len(unique_classifiers)
    30
    >>> import pprint
    >>> pprint.pprint(unique_classifiers)
    set([u'u'By Will McGugan from Django community aggregator:\n ...
    >>>

If we look these over, we find that we have some from ``Planet Django``, some
from ``Planet PostgreSQL`` and maybe some others as well (I get one from
``plope`` too).

.. nextslide:: Categorizing Posts

Let's take one more step, and divide our post titles into categories based on
whether they are Django, PostgreSQL or other.

Start by defining a function to get the *classifier* for an entry:

.. code-block:: pycon

    >>> def get_classifier(entry):
    ...     byline = entry.find('p', class_='discreet')
    ...     for classifier in ['django', 'postgresql']:
    ...         if classifier in byline.text.lower():
    ...             return classifier
    ...     return 'other'
    ...
    >>>

.. nextslide::

Then use that function to find the unique set of classifiers

.. code-block:: pycon

    >>> classifiers = [get_classifier(e) for e in entries]
    >>> len(set(classifiers))
    3
    >>> set(classifiers)
    set(['other', 'postgresql', 'django'])

.. nextslide::

We can also extract titles for each post with a function:

.. code-block:: pycon

    >>> def get_title(entry):
    ...     return entry.find('a').find('h2').string.strip()
    ...
    >>> titles = [get_title(e) for e in entries]
    >>> len(titles)
    70
    >>> titles[0]
    u'A method for rendering templates with Python'

.. nextslide::

Put it all together to build a dictionary of categorized post titles:

    >>> paired = [(get_classifier(e), get_title(e)) for e in entries]
    >>> paired[0]
    ('django', u'A method for rendering templates with Python')
    >>> groups = {}
    >>> for cat, title in paired:
    ...     list = groups.setdefault(cat, [])
    ...     list.append(title)
    ...
    >>> groups['django']
    [u'A method for rendering templates with Python',
     u"Don't import (too much) in your django settings",
     ...]

Neat!


Going Farther
=============

.. rst-class:: left

Okay, so that's the basics. For your assignment you'll take this a step farther
and
:ref:`build a list of restaurant health inspection data <scraper_assignment>`
using the King County government website.

