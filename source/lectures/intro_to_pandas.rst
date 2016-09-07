***************
Intro to Pandas
***************

It always helps to have data well-organized.
`Pandas <http://pandas.pydata.org/>`_ is a package that's great for keeping your data well organized, giving you access to fast NumPy-like math capabilities with Excel-like access to your data in visible columns and rows.
It accomplishes this through a new data structure called the DataFrame.
DataFrames are fairly easy to build from a standard Python ``dict``.
Pandas is not part of the Python standard library, so it was included in the ``data_science_requirements.txt`` file that was downloaded yesterday.
If you want to download it yourself for other environments just ``pip install pandas``.

.. ipython::

    In [1]: import pandas as pd

    In [2]: from datetime import datetime

    In [3]: fmt = "%b %d, %Y"

    In [4]: finances = {
       ...: "Name": ["Pablo", "Marcel", "Lisa", "Joanne"],
       ...: "Assets": [120000, 80000, 110000, 230000],
       ...: "Debts": [90000, 80000, 30000, 50000],
       ...: "Updated": [
       ...: datetime.strptime("Jun 10, 2011", fmt),
       ...: datetime.strptime("Dec 30, 2005", fmt),
       ...: datetime.strptime("May 4, 2000", fmt),
       ...: datetime.strptime("Feb 16, 2007", fmt),
       ...: ],
       ...: "Total Rating": [3.5, 2.5, 4.0, 5.0]
       ...: }

    In [5]: finances_df = pd.DataFrame(finances)

    In [6]: print(finances_df)
       Assets  Debts    Name  Total Rating    Updated
    0  120000  90000   Pablo           3.5 2011-06-10
    1   80000  80000  Marcel           2.5 2005-12-30
    2  110000  30000    Lisa           4.0 2000-05-04
    3  230000  50000  Joanne           5.0 2007-02-16

When creating a DataFrame from a dictionary, Pandas takes the keys from the dictionary and turns them into column names.
You can then access the columns in a ``dict``-like fashion with bracket notation, or in Javascript-like dot notation.

.. ipython::

    In [7]: print(finances_df["Total Rating"])
    0    3.5
    1    2.5
    2    4.0
    3    5.0
    Name: Rating, dtype: float64

    In [8]: print(finances_df.Debts)
    0     Pablo
    1    Marcel
    2      Lisa
    3    Joanne
    Name: Name, dtype: object

The indices on the left side allow you to access individual rows or a series of rows.
Accessing rows isn't as simple as with ``list``-like objects.

.. ipython::

    In [9]: finances_df[0]

This raises a ``KeyError`` because it's attempting to look at the input "0" as a column name. 
To access the "ith" row, you must use the integer-location indexer on the DataFrame.

.. ipython::

    In [10]: finances_df.iloc[0]
    Out[10]: 
    Assets                       120000
    Debts                         90000
    Name                          Pablo
    Total Rating                    3.5
    Updated         2011-06-10 00:00:00
    Name: 0, dtype: object

    In [11]: finances_df.iloc[0:2]
    Out[11]: 
       Assets  Debts    Name  Total Rating    Updated
    0  120000  90000   Pablo           3.5 2011-06-10
    1   80000  80000  Marcel           2.5 2005-12-30

Like ``NumPy`` arrays we can do quick aggregate statistics on individual columns.

.. ipython::

    In [12]: finances_df.Assets.mean()
    Out[12]: 135000.0

    In [13]: finances_df.Debts.median()
    Out[13]: 115000.0

    In [14]: finances_df["Total Rating"].min()
    Out[14]: 2.5

    In [15]: finances_df.Updated.max()
    Out[15]: Timestamp('2011-06-10 00:00:00')

And math across the entirety of a column.

.. ipython::

    In [16]: finances_df.Assets / 1000.0

Also like ``NumPy`` arrays we can filter based on criteria that yields boolean values.
The major difference though is that our cuts return not just pieces of an array, but pieces of the whole DataFrame.

.. ipython::

    In [17]: finances_df[finances_df.Assets > 100000]
    Out[17]: 
       Assets  Debts    Name  Total Rating    Updated
    0  120000  90000   Pablo           3.5 2011-06-10
    2  110000  30000    Lisa           4.0 2000-05-04
    3  230000  50000  Joanne           5.0 2007-02-16

This is all well and good, but you'll likely want to work with data sets coming in from the outside world.
They will be substantial and hopefully well-structured, and ``Pandas`` can read them for you if the columns are well-separated.
For example, a CSV file like so (:download:`download here </downloads/my_neighborhood_map.csv>`_):

.. code-block:: bash

    # my_neighborhood_map.csv

    City Feature,Common Name,Address,Website,Longitude,Latitude,Location
    Alternative Schools,Pathfinder,1901 SW Genesee St,http://www.seattleschools.org/schools/pathfinder/welcome.html,-122.358,47.5636,"(47.5636, -122.358)"
    Alternative Schools,The New School At Southshore,4800 S Henderson St,http://www.seattleschools.org/schools/southshore/,-122.27201,47.52374,"(47.52374, -122.27201)"
    Alternative Schools,Catharine Blaine K-8,2550 34th Ave W,http://www.seattleschools.org/schools/blaine/,-122.399261,47.642257,"(47.642257, -122.399261)"
    Alternative Schools,As #1 At Pinehurst,11530 12th Ave NE,http://as1web.com/,-122.31466,47.713431,"(47.713431, -122.31466)"
    Alternative Schools,Nova,301 21st Ave E,,-122.30524,47.6216,"(47.6216, -122.30524)"
    Alternative Schools,The Center School,305 Harrison,http://www.centerschoolseattle.org,-122.353983,47.622078,"(47.622078, -122.353983)"
    Alternative Schools,Thornton Creek K-8,7711 43rd Ave NE,http://www.seattleschools.org/schools/ae2/,-122.282669,47.685032,"(47.685032, -122.282669)"
    Alternative Schools,Orca K-8,5215 46th Ave S,http://www.orcapta.org,-122.27596,47.55478,"(47.55478, -122.27596)"
    Alternative Schools,South Lake Hs,8601 Rainier Ave S,http://www.seattleschools.org/schools/southlake/,-122.27092,47.52526,"(47.52526, -122.27092)"
    Alternative Schools,Madrona K-8,1121 33rd Ave,http://www.seattleschools.org/schools/madrona/,-122.290868,47.612237,"(47.612237, -122.290868)"
    Alternative Schools,Salmon Bay,1810 NW 65th St,http://www.salmonbayschool.org/,-122.38051,47.676298,"(47.676298, -122.38051)"
    Alternative Schools,Tops K-8,2500 Franklin Ave E,http://www.topsk8.org/,-122.324177,47.642286,"(47.642286, -122.324177)"
    Basketball Courts,Hiawatha Playfield,2700 California Ave. SW,http://www.seattle.gov/parks/park_detail.asp?ID=456,-122.38523,47.578526,"(47.578526, -122.38523)"
    Basketball Courts,E.C. Hughes Playground,2805 SW Holden St.,http://www.seattle.gov/parks/park_detail.asp?ID=458,-122.370211,47.532807,"(47.532807, -122.370211)"
    Basketball Courts,Bryant Playground,4103 NE 65th St.,http://www.seattle.gov/parks/park_detail.asp?ID=482,-122.283764,47.675545,"(47.675545, -122.283764)"
    ...

This can be easily read with Pandas:

.. code-block:: ipython

    In [18]: sample_data = pd.read_csv("my_neighborhood_map.csv")

If it was separated with anything besides commas, like say tabs, I'd use

.. code-block:: ipython

    In [19]: sample_data = pd.read_csv("my_neighborhood_map.csv", sep="\t")

Since the data file itself is a little difficult to read from your shell, use Pandas to tell you stuff about it like what the columns are actually named.

.. code-block:: ipython

    In [20]: sample_data.columns
    Out[20]: 
    Index(['City Feature', 'Common Name', 'Address', 'Website',
           'Longitude', 'Latitude', 'Location'],
          dtype='object')

Or how long it is.

.. code-block:: ipython

    In [21]: len(sample_data)
    Out[21]: 2072

Or how many Basketball Courts exist in this city.

.. code-block:: ipython

    In [22]: sum(sample_data["City Feature"] == "Basketball Courts")
    Out[22]: 47

Pandas provides a great structure for you to investigate a whole data set, instead of trying to read through your file line by line by eye.