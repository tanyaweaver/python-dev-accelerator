************
Data Munging
************

Real world data is rarely clean or well-structured.
The data scientist must know how and when to clean their data, and what it means to even have data that's clean.
We'll get into that later when we talk about validating your data and accounting for bad rows.

Pandas
======

To even begin to clean your data well, it helps to have it well-organized.
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
For example, a CSV file like so:

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
We're going to use this moving forward to ensure our data is valid, and if it isn't then to take some action so that our data is still usable.


What is Valid?
==============

When working with a data set, a decent first approximation comes from removing records with invalid information.
You can determine what's valid based on auxiliary information about the set, or just from looking at the set itself.
If you're looking at data about people and it includes negative ages, those records with negative ages are to some degree invalid.
If your data looks at rental prices of apartments around the city, chances are that prices won't be in the 10's of thousands of dollars are above.
Whatever the data, think about it, think about values are plausible, and reject those rows with data that fall outside of that realm of plausability.

We'll discuss two ways of handling bad data: **removal**, **filling**.
You can also manually alter data, but you had better have a damn good reason to do so.

Removing Bad Data
-----------------

Maybe the data got corrupted on entry?
Perhaps some records aren't relevant to the question at hand.
Whatever the case, sometimes you just need to be able to filter out what you don't want.

Note that this **doesn't** mean that you should *DELETE* data.
Your data is your data, whether it's good or not.
It's valuable in some way, shape, or form, and to artificially remove data in its entirety is an unacceptable practice.
When you filter out information, you must say why and how otherwise your analysis is seen as questionable at best.

Let's say that we have the following data set.

.. code-block:: ipython:

    In [23]: print(data)
             ages    heights
    0   -1.000000  61.623766
    1   34.850545  61.231887
    2   -1.000000  62.012366
    3   -1.000000  60.776548
    4   -1.000000  71.331092
    5   32.454987  70.932109
    6   34.324364  70.600538
    7   28.425111  66.755211
    8   -1.000000  61.205107
    9   -1.000000  69.932608
    10  32.226644  70.130044
    11  34.633665  70.428263
    12  35.582740  68.087174
    13  39.245149  69.507355
    14  39.364419  71.366009
    15  35.780590  61.853659
    16  -1.000000  66.879470
    17  -1.000000  66.495248
    18  -1.000000  60.654402
    19  -1.000000  63.833324
    20  -1.000000  71.715755
    ...

Clearly, folks shouldn't have negative ages, and those entries would be useless for an analysis of ages or ages vs heights.
Recall from the previous section that we can filter out rows in Pandas fairly easily.

.. code-block:: ipython:

    In [24]: print(data[data.ages != -1])
             ages    heights
    1   34.850545  61.231887
    5   32.454987  70.932109
    6   34.324364  70.600538
    7   28.425111  66.755211
    10  32.226644  70.130044
    11  34.633665  70.428263
    12  35.582740  68.087174
    13  39.245149  69.507355
    14  39.364419  71.366009
    15  35.780590  61.853659
    22  34.967948  66.308030
    23  26.754890  70.697276
    24  39.388898  70.603496
    27  40.060202  71.432532
    29  42.883102  67.030701
    32  30.602126  63.557139
    36  37.374404  67.276436
    40  43.892979  61.926341
    41  38.357550  67.625260
    42  28.814544  65.478372
    46  31.351512  66.442712
    47  36.443522  69.275935

You can assign this filtered DataFrame to a new variable and then move forward with your analysis from there.
If of course you don't care about the ages, then you could go with the data as it was and think about your heights.

Making Assumptions on Bad Data
------------------------------

Data tends to come in bad.
However, we may not want to just throw it out wholesale; there may be some portions of bad data that are entirely valid.
As an example, I have the following information in a file called "nmhw_sample_data.csv":

.. code-block:: bash

    Name,Age,Hometown,Country,Desired Income,Favorite Food,Number of Cats
    James,22,New York,,75000,,0
    Bob,25,Seattle,USA,0,pad thai,2
    Annette,28,San Francisco,USA,,spaghetti,1
    Florence,23,Beijing,China,60000,xiaolong bao,4
    Martha,30,Kansas City,,,corn,3
    Desean,27,Newark,USA,85000,,
    Jamal,28,New York,,65000,pizza,3
    Kaede,31,Kyoto,Japan,65000,sushi,4
    Milton,23,Austin,,78000,bbq,
    Ivana,29,Moscow,Russia,,borscht,1
    Jorge,35,Rio de Janeiro,Brasil,90000,farofa,2

If I were to read it in as-is, I'd get the following

.. code-block:: ipython

    In [25]: data = pd.read_csv("./downloads/nmhw_sample_data.csv")

    In [26]: print(data)
            Name  Age        Hometown Country  Desired Income Favorite Food  Number of Cats
    0      James   22        New York     NaN         75000.0           NaN             0.0 
    1        Bob   25         Seattle     USA             0.0      pad thai             2.0
    2    Annette   28   San Francisco     USA             NaN     spaghetti             1.0
    3   Florence   23         Beijing   China         60000.0  xiaolong bao             4.0
    4     Martha   30     Kansas City     NaN             NaN          corn             3.0
    5     Desean   27          Newark     USA         85000.0           NaN             NaN
    6      Jamal   28        New York     NaN         65000.0         pizza             3.0
    7      Kaede   31           Kyoto   Japan         65000.0         sushi             4.0
    8     Milton   23          Austin     NaN         78000.0           bbq             NaN
    9      Ivana   29          Moscow  Russia             NaN       borscht             1.0
    10     Jorge   35  Rio de Janeiro  Brasil         90000.0        farofa             2.0

Those "NaN"s are "Not a Number"s, the way for Pandas and NumPy to identify missing or otherwise invalid data.
Here, they're not consistent across rows.
Some entries have no country, some have no income, etc.
We can make some assumptions about what the missing data should be filled with based on the data that surrounds it.
This works especially well if our data comes in sorted in some way.
Pandas DataFrames have a method "``.fillna()``" for filling in data in a variety of ways.

.. code-block:: ipython

    In [27]: data.fillna(method="ffill")
    Out[27]:
            Name  Age        Hometown Country  Desired Income Favorite Food  Number of Cats
    0      James   22        New York     NaN         75000.0           NaN             0.0 
    1        Bob   25         Seattle     USA             0.0      pad thai             2.0
    2    Annette   28   San Francisco     USA             0.0     spaghetti             1.0
    3   Florence   23         Beijing   China         60000.0  xiaolong bao             4.0
    4     Martha   30     Kansas City   China         60000.0          corn             3.0
    5     Desean   27          Newark     USA         85000.0          corn             3.0
    6      Jamal   28        New York     USA         65000.0         pizza             3.0
    7      Kaede   31           Kyoto   Japan         65000.0         sushi             4.0
    8     Milton   23          Austin   Japan         78000.0           bbq             4.0
    9      Ivana   29          Moscow  Russia         78000.0       borscht             1.0
    10     Jorge   35  Rio de Janeiro  Brasil         90000.0        farofa             2.0    

The above is the result of a "forward fill".
Whatever data came before the invalid entry IN ITS OWN COLUMN will fill that invalid entry in with its own value.

Similarly, there's a "backward fill", which fills in missing data with information that comes after.

.. code-block:: ipython

    In [28]: data.fillna(method="bfill")
    Out[28]:
            Name  Age        Hometown Country  Desired Income Favorite Food  Number of Cats
    0      James   22        New York     USA         75000.0      pad thai             0.0 
    1        Bob   25         Seattle     USA             0.0      pad thai             2.0
    2    Annette   28   San Francisco     USA         60000.0     spaghetti             1.0
    3   Florence   23         Beijing   China         60000.0  xiaolong bao             4.0
    4     Martha   30     Kansas City     USA         85000.0          corn             3.0
    5     Desean   27          Newark     USA         85000.0         pizza             3.0
    6      Jamal   28        New York   Japan         65000.0         pizza             3.0
    7      Kaede   31           Kyoto   Japan         65000.0         sushi             4.0
    8     Milton   23          Austin  Russia         78000.0           bbq             1.0
    9      Ivana   29          Moscow  Russia         90000.0       borscht             1.0
    10     Jorge   35  Rio de Janeiro  Brasil         90000.0        farofa             2.0    

Finally, you can fill in individual columns instead of doing global fills.

.. code-block:: ipython

    In [29]: data["Desired Income"].fillna(data["Desired Income"].mean())

Doing the above with a mean or a median gives you plausible values based on the rest of the data set.
This way you can still use all the data in the column and (more or less) not change how it's distributed.

Note the above methods have their obvious consequences.
Blindly filling with information can at times produce more data artifacts than you originally had.
Be aware of what you're filling with and how you're doing it before you go ahead and do it.
Perhaps re-sorting your data would be a better idea before forward or backward-filling.
It's never a perfect process, and you should always document what you do and why you do it.
Use the Markdown cells in your Jupyter Notebooks to inject that rationale into your data report.
That way, your choices don't seem quite as arbitrary (even if they were entirely arbitrary to begin with).


Recap
=====

Real data is without fail imperfect.
As analysts, you need to use your chosen language to handle that data before you proceed with your work.
Pandas gives us the tools to handle our data in a structured way, and the methods needed to fill and remove data as need be.

Tonight you will use these methods to clean some data of your own.
Never forget to document your rationale; until you do, only you know why you did what you did.
Keep those intermediate steps in mind while you finalize your report.



