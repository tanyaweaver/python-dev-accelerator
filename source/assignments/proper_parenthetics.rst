.. slideconf::
    :autoslides: False

****************************************
Interview Challenge: Proper Parenthetics
****************************************

.. slide:: Interview Challenge: Proper Parenthetics
    :level: 1

    This document contains no slides.

My first programming language was Lisp.  If you're at all familiar with it,
you'll probably know that in Lisp there are a lot of parentheses.

Your assignment is to build a quick Python function **incorporating one of this 
week's data structures** that takes a unicode string (text) as input and returns 
one of three possible values:

* Return 1 if the string is "open" (there are open parens that are not closed)
* Return 0 if the string is "balanced" (there are an equal number of open and
  closed parentheses in the string)
* Return -1 if the string is "broken" (a closing parens has not been proceeded
  by one that opens)

For the purposes of this assignment, open and closed parens must match. As an
example, consider this string::

    ')))((('

Although there are an equal number of open and closed parens, they are not
properly paired.  This string is "broken".

Add this function--and tests that demonstrate that it works properly--to your
data structures repository.  Document it in the README file. Make sure to add
notes about and resources or collaborators you worked with in solving this
problem.

Do your work on a branch and make a pull request before merging your completed
work back to master.  Submit the URL of your pull request.

Use the comments feature to add any questions, comments or reflections on this
assignment and your approach to it.
