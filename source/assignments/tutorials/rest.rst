:orphan:

.. _rest_exercise:

*****************************************
Consuming Data from a RESTful Web Service
*****************************************

As an example of a RESTful web service, let's add some more information to our
list of restaurant health inspection metadata from a previous exercise.

We'll use a common, public API provided by Google.

.. rst-class:: centered

**Geocoding**

Geocoding with Google APIs
==========================

https://developers.google.com/maps/documentation/geocoding

Open a python interpreter using your ``souptests`` virtualenv:

.. code-block:: bash

    [souptests]
    heffalump:souptests cewing$ python

Then, import the ``requests`` library and prepare to make an HTTP request to
the google geocoding service resource:

.. code-block:: pycon

    >>> import requests
    >>> import json
    >>> from pprint import pprint
    >>> url = 'http://maps.googleapis.com/maps/api/geocode/json'
    >>> addr = '511 Boren Ave. N, Seattle, 98109'
    >>> parameters = {'address': addr, 'sensor': 'false' }
    >>> resp = requests.get(url, params=parameters)
    >>> data = json.loads(resp.text)
    >>> if data['status'] == 'OK':
    ...     pprint(data)
    ...
    {u'results': [{u'address_components': [{u'long_name': u'511',
                                            u'short_name': u'511',
                                            u'types': [u'street_number']},
                                           {u'long_name': u'Boren Avenue North',
                                            u'short_name': u'Boren Ave N',
                                            u'types': [u'route']},
                                           {u'long_name': u'South Lake Union',
                                            u'short_name': u'SLU',
                                            u'types': [u'neighborhood',
                                                       u'political']},
                                           {u'long_name': u'Seattle',
                                            u'short_name': u'Seattle',
                                            u'types': [u'locality',
                                                       u'political']},
                                           {u'long_name': u'King County',
                                            u'short_name': u'King County',
                                            u'types': [u'administrative_area_level_2',
                                                       u'political']},
                                           {u'long_name': u'Washington',
                                            u'short_name': u'WA',
                                            u'types': [u'administrative_area_level_1',
                                                       u'political']},
                                           {u'long_name': u'United States',
                                            u'short_name': u'US',
                                            u'types': [u'country',
                                                       u'political']},
                                           {u'long_name': u'98109',
                                            u'short_name': u'98109',
                                            u'types': [u'postal_code']}],
                   u'formatted_address': u'511 Boren Avenue North, Seattle, WA 98109, USA',
                   u'geometry': {u'location': {u'lat': 47.6235481,
                                               u'lng': -122.336212},
                                 u'location_type': u'ROOFTOP',
                                 u'viewport': {u'northeast': {u'lat': 47.6248970802915,
                                                              u'lng': -122.3348630197085},
                                               u'southwest': {u'lat': 47.6221991197085,
                                                              u'lng': -122.3375609802915}}},
                   u'types': [u'street_address']}],
     u'status': u'OK'}
    >>>

You can also do the reverse, provide a location as latitude and longitude and
receive address informatin back:

.. code-block:: pycon

    >>> location = data['results'][0]['geometry']['location']
    >>> latlng="{lat},{lng}".format(**location)
    >>> parameters = {'latlng': latlng, 'sensor': 'false'}
    >>> resp = requests.get(url, params=paramters)
    >>> data = json.loads(resp.text)
    >>> if data['status'] == 'OK':
    ...     pprint(data)
    ...
    {u'results': [{u'address_components': [{u'long_name': u'511',
                                            u'short_name': u'511',
                                            u'types': [u'street_number']},
                                           {u'long_name': u'Boren Avenue North',
                                            u'short_name': u'Boren Ave N',
                                            u'types': [u'route']},
                                           {u'long_name': u'South Lake Union',
                                            u'short_name': u'SLU',
                                            u'types': [u'neighborhood',
                                                       u'political']},
                                           {u'long_name': u'Seattle',
                                            u'short_name': u'Seattle',
                                            u'types': [u'locality',
                                                       u'political']},
                                           {u'long_name': u'King County',
                                            u'short_name': u'King County',
                                            u'types': [u'administrative_area_level_2',
                                                       u'political']},
                                           {u'long_name': u'Washington',
                                            u'short_name': u'WA',
                                            u'types': [u'administrative_area_level_1',
                                                       u'political']},
                                           {u'long_name': u'United States',
                                            u'short_name': u'US',
                                            u'types': [u'country',
                                                       u'political']},
                                           {u'long_name': u'98109',
                                            u'short_name': u'98109',
                                            u'types': [u'postal_code']}],
                   u'formatted_address': u'511 Boren Avenue North, Seattle, WA 98109, USA',
                   u'geometry': {u'location': {u'lat': 47.6235481,
                                               u'lng': -122.336212},
                                 u'location_type': u'ROOFTOP',
                                 u'viewport': {u'northeast': {u'lat': 47.6248970802915,
                                                              u'lng': -122.3348630197085},
                                               u'southwest': {u'lat': 47.6221991197085,
                                                              u'lng': -122.3375609802915}}},
                   u'types': [u'street_address']},
                  ...
                  ],
     u'status': u'OK'}
    >>>

Notice that in the response there are actually a number of results.  These are
decreasingly specific designations for the location you provided.  The
``types`` values for each indicate the level of geographical specificity for
each result.

Using this geocoding service is nice, but who wants to properly format all
those parameters all the time?  Moreover, do you really want to be tied only to
google as a provider?

And finally, although the data handed to us by google is ``json``, if we want
to simplify the process of mapping it, we might prefer to have `geojson`_
instead.

For this reason, we're going to interact with google's REST api through a
wrapper library written in Python: `geocoder`_.

.. _geocoder: http://geocoder.readthedocs.org/en/latest/
.. _geojson: http://geojson.org

Go ahead and install this new library in your scraper project virtualenv:

.. code-block:: bash

    [souptests]
    192:souptests cewing$ pip install geocoder
    Downloading/unpacking geocoder
      ...
    Successfully installed geocoder ratelim decorator
    Cleaning up...
    [souptests]
    192:souptests cewing$

Mashup!
=======

Let's create a simple mashup by combining geocoded data from google about our
restaurant with the metadata we extracted earlier.  Then we'll map the results.

The first step will be to move the entire body of the ``main`` block into a
function that generates the metadata results for our listings one at a time. We
can then iterate over the results and geocode them individually.

Go ahead and create a new function in ``scraper.py``.  Call it
``generate_results`` and have it do everything the ``main`` block does now.
The only difference is that it will be a *generator* function and *yield* its
results instead of printing them.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def generate_results(test=False):
        kwargs = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98109'
        }
        if test:
            html, encoding = load_inspection_page('inspection_page.html')
        else:
            html, encoding = get_inspection_page(**kwargs)
        doc = parse_source(html, encoding)
        listings = extract_data_listings(doc)
        for listing in listings:
            metadata = extract_restaurant_metadata(listing)
            score_data = extract_score_data(listing)
            metadata.update(score_data)
            yield metadata

Then update the ``main`` block like so:

.. code-block:: python

    if __name__ == '__main__':
        test = len(sys.argv) > 1 and sys.argv[1] == 'test'
        for result in generate_results(test):
            print result

If you run your script now, it should behave exactly as before. But now we're
ready to push further.

Add Geocoding
-------------

The API for geocoding with ``geocoder`` is the same for all providers. You give
an address, it returns geocoded data. You provide latitude and longitude, it
provides address data:

.. code-block:: python

    >>> response = geocoder.google(<address>)
    >>> response.json
    # json result data
    >>> response.geojson
    # geojson result data

Add a new function ``get_geojson`` to ``scraper.py``.  It will

* Take a result from our search as it's input
* Get geocoding data from google using the address of the restaurant
* Return the geojson representation of that data

Try to write this function on your own.

.. hidden-code-block:: python
    :label: Peek At a Solution

    # add an import at the top
    import geocoder

    def get_geojson(result):
        address = " ".join(result.get('Address', ''))
        if not address:
            return None
        geocoded = geocoder.google(address)
        return geocoded.geojson


You'll need to bolt the new function into your script so that the results it
gives are added to each listing. You'll need to make some updates to your
``if __name__ == "__main__":`` block.

.. hidden-code-block:: python
    :label: Peek At A Solution

    if __name__ == '__main__':
        import pprint
        test = len(sys.argv) > 1 and sys.argv[1] == 'test'
        for result in generate_results(test):
            geo_result = get_geojson(result)
            pprint.pprint(geo_result)

Give it a whirl, using the test approach so you don't hit King County while
trying it out:

.. code-block:: bash

    [souptests]
    192:souptests cewing$ python scraper.py test
    {'bbox': [-122.3582706802915,
              47.6234354197085,
              -122.3555727197085,
              47.6261333802915],
     'geometry': {'coordinates': [-122.3569217, 47.6247844], 'type': 'Point'},
     'properties': {'accuracy': 'ROOFTOP',
                    'address': '601 Queen Anne Avenue North, Seattle, WA 98109, USA',
                    'city': 'Seattle',
                    'city_long': 'Seattle',
                    'confidence': 9,
                    'country': 'US',
                    'country_long': 'United States',
                    'county': 'King County',
                    'encoding': 'utf-8',
                    'housenumber': '601',
                    'lat': 47.6247844,
                    'lng': -122.3569217,
                    'location': u'601 QUEEN ANNE AVE N Seattle, WA 98109',
                    'neighborhood': 'Lower Queen Anne',
                    'ok': True,
                    'postal': '98109',
                    'provider': 'google',
                    'quality': u'street_address',
                    'road_long': 'Queen Anne Avenue North',
                    'state': 'WA',
                    'state_long': 'Washington',
                    'status': 'OK',
                    'street': 'Queen Anne Ave N'},
     'type': 'Feature'}
     ...
    [souptests]
    192:souptests cewing$

Nifty, eh?

Notice though that running the script now takes quite some time. Let's update
the ``generate_results`` function so that it accepts a second keyword argument
that indicates the number of results to run through.  Call the parameter
``count`` and give it a sensible default value, like 10.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def generate_results(test=False, count=10):
        # ... unchanged above here
        listings = extract_data_listings(doc)
        for listing in listings[:count]:
            # ... unchanged below here

Ahhhhh.  That's better

But still, all those ``properties`` in the geojson, and none of them are truly
that important to us. Let's replace them with the metadata and inspection
scores we build previously.

Update the ``get_geojson`` function. This time it will:

* Build a dictionary containing only the values we want from our
  inspection record.
* Convert list values to strings (geojson requires this)
* Add only the 'address' property from the existing geojson properties,
  replacing the one we have in our metadata.
* Replace the rest of the properties of our geojson with this new data
* Return the modified geojson record

Try making these updates on your own.

.. hidden-code-block:: python
    :label: Peek At a Solution

    def get_geojson(result):
        address = " ".join(result.get('Address', ''))
        if not address:
            return None
        geocoded = geocoder.google(address)
        geojson = geocoded.geojson
        inspection_data = {}
        use_keys = (
            'Business Name', 'Average Score', 'Total Inspections', 'High Score',
            'Address',
        )
        for key, val in result.items():
            if key not in use_keys:
                continue
            if isinstance(val, list):
                val = " ".join(val)
            inspection_data[key] = val
        new_address = geojson['properties'].get('address')
        if new_address:
            inspection_data['Address'] = new_address
        geojson['properties'] = inspection_data
        return geojson


Map the Results
---------------

We are now generating a series of ``geojson`` *Feature* objects. To map these
objects, we'll need to create a file which contains a ``geojson``
*FeatureCollection*.

The structure of such a collection looks like this:

.. code-block:: text

    {'type': 'FeatureCollection', 'features': [...]}

Update your ``main`` function to append each feature to such a structure. Then
you can dump the structure as ``json`` to a file. In ``scraper.py`` update the
``main`` block like so:

.. code-block:: python

    # add an import at the top:
    import json

    if __name__ == '__main__':
        import pprint
        test = len(sys.argv) > 1 and sys.argv[1] == 'test'
        total_result = {'type': 'FeatureCollection', 'features': []}
        for result in generate_results(test):
            geo_result = get_geojson(result)
            pprint.pprint(geo_result)
            total_result['features'].append(geo_result)
        with open('my_map.json', 'w') as fh:
            json.dump(total_result, fh)

When you run the script not only will your results print, but the new file will
appear in the current working directory.

.. code-block:: bash

    [souptests]
    192:souptests cewing$ python scraper.py test
    ...
    [souptests]
    192:souptests cewing$ ls
    blog_list.html          my_map.json
    inspection_page.html    scraper.py

Once the new file is written you are ready to display your results. Open your
web browser and go to http://geojson.io. Then drag and drop the new file you
wrote onto the map you see there.

.. figure:: /_static/geojson-io.png
    :align: center
    :width: 75%

Going Further
=============

Take a few more steps on your own to polish this mashup a bit.

Begin by sorting the results of our search by the average score.

Then, update your script to allow the user to choose how to sort, by
average, high score or most inspections::

    [souptests]
    192:souptests cewing$ python mashup.py highscore

Next, allow the user to choose how many results to map::

    [souptests]
    192:souptests cewing$ python mashup.py highscore 25

Or allow them to reverse the results, showing the lowest scores first::

    [souptests]
    192:souptests cewing$ python mashup.py highscore 25 reverse

To simplify the passing of arguments from the command line, use the `argparse`_
module from the standard library to handle command line arguments

.. _argparse: https://docs.python.org/2/library/argparse.html#module-argparse


Next, try adding a bit of information to your map by adding ``marker-color`` to
the geojson properties dict. This will display a marker with the provided
css-style color (``#FF0000``)

See if you can make the color change according to the values used for the
sorting of the list.  Either vary the intensity of the color, or the hue.

Finally, if you are feeling particularly frisky, you can update your script
to automatically open a browser window with your map loaded on
*geojson.io*.

To do this, you'll want to read about the `webbrowser`_ module from the
standard library.

In addition, you'll want to read up on using the URL parameters API for
*geojson.io*.  Click on the **help** tab in the sidebar to view the
information.

You will also need to learn about how to properly quote special characters
for a URL, using the `urllib`_ ``quote`` function.

.. _urllib: https://docs.python.org/2/library/urllib.html#urllib.quote
.. _webbrowser: https://docs.python.org/2/library/webbrowser.html

