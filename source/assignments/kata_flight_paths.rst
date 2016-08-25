.. slideconf::
    :autoslides: False

****************************************
Python Practice: Distance Between Points
****************************************

.. slide:: Python Practice: Distance Between Points
    :level: 1

    This document contains no slides.

Below is a function that will calculate the sortest distance between any two 
points on the Earth's surface. 
**Do not worry about how it works.**
**It is simply a tool for this exercise.**::

    def calculate_distance(point1, point2):
        """
        Calculate the distance (in miles) between point1 and point2.
        point1 and point2 must have the format [latitude, longitude].
        The return value is a float.

        Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
        """
        import math

        def convert_to_radians(degrees):
            return degrees * math.pi / 180

        radius_earth = 6.371E3 # km
        phi1 = convert_to_radians(point1[0])
        phi2 = convert_to_radians(point2[0])
        delta_phi = convert_to_radians(point1[0] - point2[0])
        delta_lam = convert_to_radians(point1[1] - point2[1])

        a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.sin(0.5 * delta_lam)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return radius_earth * c / 1.60934 # convert km to miles

The JSON file :download:`at this URL </downloads/cities_with_airport.json>` contains some cities with international airports, each with 
a latitude, a longitude, and a city that it connects to. 
For the curious, the list of airports comes from `Wikipedia`_.

.. _Wikipedia: https://en.wikipedia.org/wiki/List_of_international_airports_by_country

Write a function that, 

* given a starting city and an ending city, will return a path between the two cities (including the two cities). 
* also returns the total distance traveled between cities.
* appropriately handles the situation where no path exists.

Stretch Goals
-------------

Try to incorporate any (or all) of these. They are/can be independent of each other.

* Add to your function a parameter that makes it return the **shortest path** (lowest distance) between the two cities.
* Add to your function a parameter that makes it return the **path with the fewest stops** between the two cities.
* Have your function take a parameter for a limit to the distance between any two cities. If specified, your function returns a path where each city-to-city jump is less than or equal to that limit.

Submitting Your Work
====================

Create a ``flight-paths`` branch in your ``code-katas`` repository.
Add this function in a script to your ``flight-paths`` branch. 

The tests that demonstrate your code works should be in a ``test_flight_paths.py`` file.
Add documentation about your code in the repo's ``README.md``.
Make sure to add notes about and resources or collaborators you worked with in
solving this problem.

After you've added your code solution into GitHub, send a pull request
to your master branch.
**Submit the link to that pull request to Canvas.**

Use the comment box in Canvas to add any questions, comments or reflections on this
assignment and your approach to it.