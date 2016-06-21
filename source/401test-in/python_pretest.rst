============================
Test-in For Code 401: Python
============================

Guidelines
==========

**Create a Python module** that creates a K-12 school with students and teachers at every grade level. You should be able to run this module from the command line, with that functionality outlined below. Make sure to appropriately document your code.

Data Representation
-------------------

1. Your school should have a name, and can have many students and many teachers.
2. Students should have names, GPAs (out of 100), grade level (K - 12), and a teacher name.
3. Teachers should have names and grade levels, and should be able to have multiple students.
4. A teacher should have no more than 10 students.
5. If there are no teachers, there should be no students.

Functionality
-------------

1. You should be able to retrieve the GPA averaged over all students in the school, as well as the average GPA broken down by grade level.
2. You should be able to retrieve the total number of students in the school, with the option to get a count of the whole student body OR a count of the student body broken down by grade level.
3. If there are no students in the school, numbers **[1]** and **[2]** should say so with an appropriate message.
4. You should be able to retrieve the total number of teachers in the school, with the option to get a count of the number of teachers by grade level.
5. You should be able to retrieve the average GPA of all students broken down by teacher.
6. You should be able to retrieve the average GPA for a specific grade level, broken down by teacher.
7. If there are no teachers in your school, numbers **[4]**, **[5]**, and **[6]** should say so with an appropriate message.
8. Your school should be able to enroll new students. A newly-enrolled student should be able to either be assigned to a specific teacher or have one randomly assigned to them. Once assigned to a teacher, their grade level should be automatically assigned. They should also get a random GPA.
9. If the assigned teacher in the above process already has 10 students, then that student should be randomly assigned to a different teacher at the same grade level. If all teachers at that level are full, then that student shouldn't be allowed to enroll in the school. Your script should indicate either case with appropriate messages.
10. Your school should be able to hire new teachers. When a new teacher is hired, they should have an empty classroom, and be assigned to a random grade level if no grade level is specified.

Command Line and Command Line UI
--------------------------------

1. When run from the command line, your script should create a new school and fill it with teachers and students. Fill with at least 81 students.

2. When run from the command line, your script should produce a report of the school including:

    - The school name
    - The total number of students in the school
    - The total number of teachers in the school
    - The average student GPA throughout the school
    
3. After **[2]** happens, your script should prompt the user to either: 

    - produce a grade report broken down by grade level (so GPA per grade level)
    - produce a grade report for an individual grade level broken down by teacher (e.g. average GPA per teacher in grade 9)
    - exit the script
    
4. When run from the command line, if the option to exit is chosen, your script should ask if you're sure you want to quit. If you decide to quit, your script should exit. If not, your script should take you back to the menu in **[3]**

5. When run from the command line, if the parameter "roll_call" is provided, your script should list all the students, separated by grade level. Once done, your script should quit. **This behavior should ONLY occur if "roll_call" is provided.**
  
.. 16. Your school should be able to expel students. If a student is expelled, an appropriate message should be returned. Once expelled, that student should no longer belong to a teacher.

.. 18. Your school should be able to fire teachers. When a teacher is fired, their students should be distributed to the remaining teachers at that grade level (either randomly or not). If all other teachers in that grade level fill up on students, the remaining students get expelled. Appropriate messages should be raised for these.

.. 22. After [20] happens, your script should re-prompt for the above choices.


Submitting Your Work
====================

* You will create a public GitHub repository for your work and email in the link to that repository.
* In the README of that repository, you'll include a description of the module that you built and links to any code that you may have used. In that description, you'll include explanations of any functions/objects/methods you write. Also include instructions as to how your code should be run from the command line.

