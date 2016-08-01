.. slideconf:: 
    :autoslides: False

.. slide:: Deque
    :level: 1

    .. rst-class:: left

    A *Deque* is a Queue that works at both ends. Data can be inserted at the head or tail, and retrieved from the head or the tail.


    .. image:: http://www.codeproject.com/KB/recipes/669131/deque.png
        :width: 400px
        :alt: An example of a data Deque. Source: http://www.codeproject.com

.. slide:: Motivation 
    :level: 2

    .. rst-class:: build

    * Sequential 
    * Limited access
    * **When might I actually use this?**
        - Tracking the running minimum and maximum run times for code being tested
        - Modeling how passengers board and deboard an airplane with two entrances/exits
       

.. slide:: Attributes 
    :level: 2

    .. rst-class:: build

    * head
    * tail
    * is_empty
    * size


.. slide:: Operations 
    :level: 2

    .. rst-class:: build

    * add_first()
    * add_last()
    * delete_first()
    * delete_last()
    * clear()



=====
Deque
=====

Definition
==========

A *Deque* is a Queue that works at both ends. Data can be inserted at the head or tail, and retrieved from the head or the tail.

.. image:: http://www.codeproject.com/KB/recipes/669131/deque.png
    :width: 400px
    :alt: An example of a Deque. Source: http://www.codeproject.com

Motivation
==========

* Sequential 
* Limited access
* **When might I actually use this?**
    - Tracking the running minimum and maximum run times for code being tested
    - Modeling how passengers board and deboard an airplane with two entrances/exits


Attributes
==========

* head
* tail
* is_empty
* size


Operations
==========

* add_first()
* add_last()
* delete_first()
* delete_last()
* clear()

