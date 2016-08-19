==================
Doubly-Linked List
==================

Definition
==========

* A *Doubly-Linked List* consists of *Nodes*, each of which contains some data and pointers to the next and previous nodes.
* Self-referential (naturally recursive)

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png
    :width: 400px
    :alt: A Doubly-Linked List. Source: https://en.wikipedia.org/wiki/Linked_list

Motivation
==========

* Similar benefits as the singly-linked list
* Allows for traversal forward AND backward
* **When might I actually use this?**
    - traversing through pages of blog posts
    - images in a slider

Attributes
==========

* Nodes:
    - data
    - next
    - previous

* Doubly-Linked List:
    - head
    - tail

Operations
==========

* add(value, next=head, previous)
* remove(value)
* search(value)
* display()
* pop()
    - note: pop() is a remove-and-return operation

