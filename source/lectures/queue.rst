.. slideconf:: 
    :autoslides: False

.. slide:: Queue 
    :level: 1

    .. rst-class:: left

    If you're British, you basically already know what it is. For everyone else, a *Queue* is a data structure where elements are inserted into the head and removed from the tail of the container (or vice versa).

    .. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png
        :width: 400px
        :alt: An example of a data Queue. Source: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

.. slide:: Motivation 
    :level: 2

    .. rst-class:: build

    * Sequential 
    * Limited access
    * First-In First-Out (FIFO) access
    * **When might I actually use this?**
        - Building a task manager
        - Modeling traffic patterns
        - Printing a document (or several documents) in proper order
       

.. slide:: Attributes 
    :level: 2

    .. rst-class:: build

    * head
    * is_empty
    * size


.. slide:: Operations 
    :level: 2

    .. rst-class:: build

    * enqueue()
    * dequeue()
    * clear()



=====
Queue
=====

Definition
==========

A *Queue* is a data structure where elements are inserted into and removed from the head of the container.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png
    :width: 400px
    :alt: An example of a data Queue. Source: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

Motivation
==========

    * Sequential 
    * Limited access
    * First-In First-Out (FIFO) access
    * **When might I actually use this?**
        - Building a task manager
        - Modeling traffic patterns
        - Printing a document (or several documents) in proper order
  

Attributes
==========

* top
* is_empty
* size
 

Operations
==========

* enqueue()
* dequeue()
* clear()
