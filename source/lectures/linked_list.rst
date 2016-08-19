===========
Linked List
===========

Definition
==========

* A *Linked List* consists of *Nodes*, each of which contains some data and a pointer to the next node. 
* Self-referential (naturally recusive)
  
.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png
    :width: 400px
    :alt: A simple singly-linked list. Source: https://en.wikipedia.org/wiki/Linked_list
  
Motivation
==========

* Arrays are great for holding data, but you don't always know the size of the array you need in advance
* Insertion in the middle of an array is expensive
* Linked structures store items linearly and allow quick inserts, though searching for an element becomes expensive
* Linked structure also allows for easy removal operations
* Reduce access time and expand in real time without memory overhead
* **When might I actually use this?** a web crawler cacheing links and the next link from that link

Attributes
==========

* Nodes:
    - data
    - next

* Linked List:
    - head
    - tail
      
Operations 
==========

* insert(value, next=None)
* remove(value)
* search(value)
* display()
* pop()
    - note: pop() is a remove-and-return operation
