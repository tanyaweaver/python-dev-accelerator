=====
Heap
=====

Definition
==========

A *Binary Heap* is the first tree-type data structure you'll encounter. You create this structure by feeding in an array (Python ``list``). It is a binary tree with two main properties:

* Shape property: The tree is mostly complete with only the deepest level left unfilled. This level is filled with new nodes from left to right.
* Heap property: The heap property has two modes dictating relationships between parent and child nodes
    - **Max Heap:** Each node is greater than or equal to its child nodes
    - **Min Heap:** Each node is less than or equal to its child nodes (see the image below)

**Insertion:** When inserting a new node into a Binary Heap, put it at the first open space. Once inserted, shift it into the proper position by comparing it to its parent node. Repeat as necessary.

.. image:: https://upload.wikimedia.org/wikipedia/commons/6/60/Binary_heap_indexing.png
    :width: 250px
    :alt: An example of a Binary Heap. Source: https://en.wikipedia.org/wiki/Heap_(data_structure)

Motivation
==========

* Efficient search
* Sorts in place
* Easy to retrieve top N items
* **When might I actually use this?**
    - Quick minimum or quick maximum value in a set of values
    - (For the future): Djikstra's algorithm
    - (For the future): Priority Queues


Attributes
==========

* Nodes
    - left
    - right
    - parent

* Heap
    - length, size


Operations
==========

* heapify()
* insert()/push()
* extract()/pop()

