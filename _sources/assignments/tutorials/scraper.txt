.. _scraper_assignment:

************************************************
Scraping Health Inspection Data from King County
************************************************

Work through this exercise to create a Python script to extract restaurant
health inspection data from King County by ZIP Code and Date

While working, you should use the virtualenv project we created in class for
learning about the BeautifulSoup package.

.. code-block:: bash

    heffalump:~ cewing$ workon souptests
    [souptests]
    heffalump:souptests cewing$

Begin by creating a new Python file, call it ``scraper.py``. Open it in your
editor.

Step 1: Fetch Search Results
============================

The first step is to use the ``requests`` library to fetch a set of search
results from the King County government website.

In order to do so, we will need to assemble a *query* that fits with the search
form present on the `Restaurant Inspection Information`_ page.

.. _Restaurant Inspection Information: http://info.kingcounty.gov/health/ehs/foodsafety/inspections/search.aspx

The complexity of this webservice means the easiest way to extract this
information is to submit a search manually and then copy the URL that results.

After you've done this, you should know the domain name and path to the search
results page and know the set of *query parameters* available to be used (along
with some default values).  Begin by recording these three items as *constants*
at the top of your ``scraper.py`` file:

.. hidden-code-block:: python
    :label: Peek At a Solution

    INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
    INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
    INSPECTION_PARAMS = {
        'Output': 'W',
        'Business_Name': '',
        'Business_Address': '',
        'Longitude': '',
        'Latitude': '',
        'City': '',
        'Zip_Code': '',
        'Inspection_Type': 'All',
        'Inspection_Start': '',
        'Inspection_End': '',
        'Inspection_Closed_Business': 'A',
        'Violation_Points': '',
        'Violation_Red_Points': '',
        'Violation_Descr': '',
        'Fuzzy_Search': 'N',
        'Sort': 'H'
    }

Be aware that the results page is quite sensitive about having *all* the
parameters in each request, even if they have no values set.

Your next job is to write a single Python function (``get_inspection_page``)
that will fetch a set of search results for you. Here are the requirements for
this function:

* It must accept keyword arguments for the possible query parameters
* It will build a dictionary of request query parameters from incoming keywords
* It will make a request to the King County server using this query
* It will return the bytes content of the response and the encoding if there is
  no error
* It will raise an error if there is a problem with the response
  
As you work on building this function, try out various approaches in your
Python interpreter first.  See what works and what fails before you try to
write the function.

Here is one possible solution for this function:

.. hidden-code-block:: python
    :label: Peek At A Solution

    import requests

    def get_inspection_page(**kwargs):
        url = INSPECTION_DOMAIN + INSPECTION_PATH
        params = INSPECTION_PARAMS.copy()
        for key, val in kwargs.items():
            if key in INSPECTION_PARAMS:
                params[key] = val
        resp = requests.get(url, params=params)
        resp.raise_for_status() # <- This is a no-op if there is no HTTP error
        # remember, in requests `content` is bytes and `text` is unicode
        return resp.content, resp.encoding


Write the results of your search to a file, ``inspection_page.html`` so that
you can work on it without needing to hammer the King County servers.

Write a ``load_inspection_page`` function which reads this file from disk and
returns the content and encoding in the same way as the above function. Then
you can switch between the two without altering the API. I'll leave this
exercise entirely to you.

Step 2: Parse Search Results
============================

Next, we need a function ``parse_source`` to set up the HTML as DOM nodes for
scraping. It will need to:

* Take the response body from the previous function (or the file read from
  disk)
* Parse it using BeautifulSoup
* Return the parsed object for further processing

This function can be quite simple. Add it to ``scraper.py``.

.. hidden-code-block:: python
    :label: Peek At A Solution

    # add this import at the top
    from bs4 import BeautifulSoup

    # then add this function lower down
    def parse_source(html, encoding='utf-8'):
        parsed = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
        return parsed

In order to see the results we have at this point, we'll need to make our
``scraper.py`` executable by adding a ``__main__`` block. Since you have
alternate sources for listing data (``load_inspectioon_page`` and
``get_inspection_page``), you should allow a command-line argument such as
'test' to switch between the two.

Go ahead and set the ZIP code and dates for your search statically in this
block. You can work on providing them dynamically later.

.. hidden-code-block:: python
    :label: Peek At A Solution

    # add another import at the top
    import sys

    if __name__ == '__main__':
        kwargs = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98109'
        }
        if len(sys.argv) > 1 and sys.argv[1] == 'test':
            # you will likely have something different here, depending on how
            # you implemented the load_inspection_page function.
            html, encoding = load_inspection_page('inspection_page.html')
        else:
            html, encoding = get_inspection_page(**kwargs)
        doc = parse_source(html, encoding)
        print doc.prettify(encoding=encoding)

Now, you can execute your scraper script in one of two ways:

1. ``python scraper.py`` will fetch results directly from King County.
2. ``python scraper.py test`` will use your stored results from file.


Step 3: Extract Listing Information
===================================

You are going to build a series of functions that extracts useful information
from each of the restaurant listings in the parsed HTML search results. From
each listing, we should extract the following information:

* Metadata about the restaurant (name, category, address, etc.)
* The average inspection score for the restaurant
* The highest inspection score for the restaurant
* The total number of inspections performed

You'll be building this information one step at a time, to simplify the task.

3a: Find Individual Listings
----------------------------

The first job is to find the container that holds each individual listing. Use
your browser's devtools to identify the container that holds each. Then, write
a function that takes in the parsed HTML and returns a list of the restaurant
listing container nodes.

Pay attention to the fact that there are *two* containers for each restaurant.
What is the difference between them?  Which do you want? Remember the
BeautifulSoup allows you to search based on HTML attributes, and that
`different types of filters`_ can be used. Which kind of filter would be most
effective for this task?

.. _different types of filters: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters

Call this function ``extract_data_listings``.

.. hidden-code-block:: python
    :label: Peek At A Solution

    # add a new import at the top
    import re

    def extract_data_listings(html):
        id_finder = re.compile(r'PR[\d]+~')
        return html.find_all('div', id=id_finder)

If you update your ``__main__`` block to use this new function, you can verify
the results visually:

.. code-block:: python

    if __name__ == '__main__':
        kwargs = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98109'
        }
        if len(sys.argv) > 1 and sys.argv[1] == 'test':
            html, encoding = load_inspection_page('inspection_page.html')
        else:
            html, encoding = get_inspection_page(**kwargs)
        doc = parse_source(html, encoding)
        listings = extract_data_listings(doc) # add this line
        print len(listings)                   # and this one
        print listings[0].prettify()          # and this one too

Call your script from the command line (in test mode), to see your results:

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ python scraper.py test
    362
    <div id="PR0020232~" name="PR0020232~" onclick="toggleShow(this.id);" onmouseout="this.style.cursor = 'auto';window.status = '';" onmouseover="this.style.cursor = 'pointer';window.status = 'Click to hide business and inspection details';" style="display: none" xmlns="">
     <table style="width: 635px;">
      <tbody>
       <tr>
       ...
       </tr>
      </tbody>
     </table>
    </div>

    [souptests]
    heffalump:souptests cewing$

3b: Extract Metadata
--------------------

When you take a close look at the structure of the data ``<div>`` for each
restaurant, you'll see that the metadata about the restaurant is located in the
rows of a table. The rows we are interested in all have a few shared properties
that set them apart from other rows in the table.

The first is that all the rows that contain this information have *two* cells
in them.  One that might contain a *label* for the metadata and a second that
contains the *value*.

The second is that the two ``<td>`` elements it contains are immediate
children, not contained within some nested structure.

BeautifulSoup allows us to `use functions as filters`_. These functions must
take an *element* as their only argument, and return `True` if the element
should pass through the filter, and `False` if not.

.. _use functions as filters: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function

Add a new function to ``scraper.py`` called ``has_two_tds`` that will take an
element as an argument and return ``True`` if the element is both a ``<tr>``
*and* contains exactly two ``<td>`` elements immediately within it.

.. hidden-code-block:: python
    :label: Peek At A Solution

    def has_two_tds(elem):
        is_tr = elem.name == 'tr'
        td_children = elem.find_all('td', recursive=False)
        has_two = len(td_children) == 2
        return is_tr and has_two

Demonstrate that your filter works properly by trying it out.  Start by
updating our ``main`` block with a few lines of code that will catch the
metadata rows from each div and print a count of them:

.. code-block:: python

    if __name__ == '__main__':
        # ... existing code up here need not be changed
        doc = parse_source(html, encoding)
        listings = extract_data_listings(doc)
        for listing in listings:  # <- add this stuff here.
            metadata_rows = listing.find('tbody').find_all(
                has_two_tds, recursive=False
            )
            print len(metadata_rows)

And now, executing this script at the command line should return the following:

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ python scraper.py test
    7
    7
    7
    ...
    7
    7
    [souptests]
    heffalump:souptests cewing$

Great! Nice, consistent results means we've done our job correctly.  If you are
getting values that vary widely, please review your filter function.

You'll work next on extracting the data from those rows you have found.

BeautifulSoup provides a pair of attributes to represent the visible contents
of ``Tag`` objects. The ``tag.text`` attribute will return all visible
contents, including those of enclosed tags.  But this is often more than you
want or need.  The ``tag.string`` text will return only the visible contents
directly contained in this particular element, and only that which is *before*
any nested tags.  Try updating your ``main`` block to peek at the contents of
your rows for the first few matched restaurant listings.  Try ``tag.text``
first:

.. code-block:: python

    if __name__ == '__main__':
        ...
        for listing in listings[:5]:
            metadata_rows = listing.find('tbody').find_all(
                has_two_tds, recursive=False
            )
            for row in metadata_rows:
                for td in row.find_all('td', recursive=False):
                    print td.text,
                print
            print

Try running the script again to see the output:

.. code-block:: bash

    [souptests]
    192:souptests cewing$ python scraper.py test

                - Business Name

                TOULOUSE KITCHEN & LOUNGE


                Business Category:

                Seating 151-250 - Risk Category III

Hmmm.  Where'd all that extra whitespace come from?  the values from the first
and second cells should have printed on the same row in our output, but they
didn't.  There's extra stuff in there we don't want.  Try it again with
``tag.string``:

.. code-block:: python

    if __name__ == '__main__':
        # ...
        for listing in listings[:5]:
            metadata_rows = listing.find('tbody').find_all(
                has_two_tds, recursive=False
            )
            for row in metadata_rows:
                for td in row.find_all('td', recursive=False):
                    print td.string,
                print
            print

You should see that this makes no difference in our output.  This means that
we'll need to clean up the values we get from these cells.  We need a function
that will do this for us.  It should take a cell as it's sole argument and
return the ``tag.string`` attribute with extraneous characters stripped.  Call
the function ``clean_data``.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def clean_data(td):
        data = td.string
        try:
            return data.strip(" \n:-")
        except AttributeError:
            return u""


Add that into your ``main`` block and see the results:

.. code-block:: python

    if __name__ == '__main__':
        # ...
        for listing in listings[:5]:
            metadata_rows = listing.find('tbody').find_all(
                has_two_tds, recursive=False
            )
            for row in metadata_rows:
                for td in row.find_all('td', recursive=False):
                    print repr(clean_data(td)),
                print
            print

.. code-block:: bash

    [souptests]
    192:souptests cewing$ python scraper.py test
    u'Business Name' u'TOULOUSE KITCHEN & LOUNGE'
    u'Business Category' u'Seating 151-250 - Risk Category III'
    u'Address' u'601 QUEEN ANNE AVE N'
    u'' u'Seattle, WA 98109'
    u'Phone' u'(206) 283-1598'
    u'Latitude' u'47.6247323574'
    u'Longitude' u'122.3569098631'
    ...

Ahhh, much better.

3c: Store Metadata
------------------

Next, we want to put this data into a data structure that will represent a
single restaurant.  Our data is paired as labels and values. That should
suggest a proper data structure.

We need to create a function that will put these pieces together.  The function
should take the listing for a single restaurant, and return a Python dictionary
containing the metadata we've extracted.

It'd be easy enough to simply walk through the rows and add an entry in our
dictionary for each, but look at the data above. Does each row contain a label
and a value?  Which one does not? What is suggested by this?  You'll need to
account for this in your function.

Call the function ``extract_restaurant_metadata`` and add it to ``scraper.py``.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def extract_restaurant_metadata(elem):
        metadata_rows = elem.find('tbody').find_all(
            has_two_tds, recursive=False
        )
        rdata = {}
        current_label = ''
        for row in metadata_rows:
            key_cell, val_cell = row.find_all('td', recursive=False)
            new_label = clean_data(key_cell)
            current_label = new_label if new_label else current_label
            rdata.setdefault(current_label, []).append(clean_data(val_cell))
        return rdata

Replace the rough work you added to your ``main`` block with a single clean
call to this function and print out the results to verify your work:

.. code-block:: python

    if __name__ == '__main__':
        # ...
        for listing in listings[:5]:
            metadata = extract_restaurant_metadata(listing)
            print metadata
            print

.. code-block:: bash

    [souptests]
    192:souptests cewing$ python scraper.py test
    {u'Business Category': [u'Seating 151-250 - Risk Category III'],
     u'Longitude': [u'122.3569098631'], u'Phone': [u'(206) 283-1598'],
     u'Business Name': [u'TOULOUSE KITCHEN & LOUNGE'],
     u'Address': [u'601 QUEEN ANNE AVE N', u'Seattle, WA 98109'],
     u'Latitude': [u'47.6247323574']}
    ...

Outstanding.  You've built the first part of this script and are ready to move
on.


3d: Extract Inspection Data
---------------------------

The next step is to extract the information we need to build our inspection
data for each restaurant. As a reminder, we have said that we want to store the
average inspection score, the highest inspection score and the total number of
inspection performed.

Let's think for a moment about what we want to find. We'll need to find rows in
the tables in our restaurant that represent the results of an inspection. We
don't need individual inspection items, just the total score. And we don't care
about rows that contain non-inspection information.

Use your browser's dev tools to inspect the structure of a listing again. Can
you spot commonalities for all the rows that contain the data we want? There
are four chief common points we can use to find our rows:

* Each row is a table row, or ``<tr>`` element.
* Each row contains exactly four table cell, or ``<td>`` elements.
* Each row has text in the first cell that contains the word "inspection"
* In that text, the word "inspection" is *not* the first word

Your next task is to write a filter function that can be used to find these
rows. Remember, a filter function takes an HTML element as its sole argument
and returns ``True`` if the element matches the criteria of the filter,
``False`` otherwise. Call the function ``is_ispection_row`` and add it to
``scraper.py``.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def is_inspection_row(elem):
        is_tr = elem.name == 'tr'
        if not is_tr:
            return False
        td_children = elem.find_all('td', recursive=False)
        has_four = len(td_children) == 4
        this_text = clean_data(td_children[0]).lower()
        contains_word = 'inspection' in this_text
        does_not_start = not this_text.startswith('inspection')
        return is_tr and has_four and contains_word and does_not_start

Update your ``main`` block.  Use this new filter to find the inspection rows in
each listing.  Print out the text in each row for the first few listings to
verify that you've got it right:

.. code-block:: python

    if __name__ == '__main__':
        # ...
        for listing in listings[:5]:
            metadata = extract_restaurant_metadata(listing)
            inspection_rows = listing.find_all(is_inspection_row)
            for row in inspection_rows:
                print row.text

Once you've confirmed that you are only seeing rows that contain useful data,
your filter will be correct. Next move on to building the aggregated data you
want to store about inspection scores.

You'll need to add a new function ``extract_score_data`` to ``scraper.py``.
This function will:

* Take a restaurant listing as an argument.
* Use the filter you just created to find inspection data rows.
* Extract the score for each inspection.
* Keep track of the number of inspections made.
* Keep track of the highest score.
* Calculate the average score for all inspections.
* Return a dictionary containing the average score, high score, and total
  inspection values.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def extract_score_data(elem):
        inspection_rows = elem.find_all(is_inspection_row)
        samples = len(inspection_rows)
        total = high_score = average = 0
        for row in inspection_rows:
            strval = clean_data(row.find_all('td')[2])
            try:
                intval = int(strval)
            except (ValueError, TypeError):
                samples -= 1
            else:
                total += intval
                high_score = intval if intval > high_score else high_score
        if samples:
            average = total/float(samples)
        data = {
            u'Average Score': average,
            u'High Score': high_score,
            u'Total Inspections': samples
        }
        return data

Update your ``main`` block to include this new function.  Print out the results
for the first few listings to verify that it worked.

.. code-block:: python

    if __name__ == '__main__':
        kwargs = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98109'
        }
        if len(sys.argv) > 1 and sys.argv[1] == 'test':
            html, encoding = load_inspection_page('inspection_page.html')
        else:
            html, encoding = get_inspection_page(**kwargs)
        doc = parse_source(html, encoding)
        listings = extract_data_listings(doc)
        for listing in listings[:5]:
            metadata = extract_restaurant_metadata(listing)
            score_data = extract_score_data(listing)
            print score_data

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ python scraper.py test
    {u'High Score': 90, u'Average Score': 28.6, u'Total Inspections': 5}
    {u'High Score': 80, u'Average Score': 27.5, u'Total Inspections': 4}
    {u'High Score': 80, u'Average Score': 27.5, u'Total Inspections': 4}
    {u'High Score': 70, u'Average Score': 17.5, u'Total Inspections': 4}
    {u'High Score': 70, u'Average Score': 32.25, u'Total Inspections': 4}
    [souptests]
    heffalump:souptests cewing$

Alright.  That's working nicely.  The final step for today is to knit the two
sets of data together into a single dictionary of data. Go ahead and do that in
your ``main`` block. When you're done, remove the constraint on how many
listings to process and run the scraper over the full set. Finish up by running
it one more time without the ``test`` in the call so you fetch fresh data from
the King County servers.

Congratulations, you've built a successful web scraper.  Fun, eh?
