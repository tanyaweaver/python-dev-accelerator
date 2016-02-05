.. slideconf::
    :autoslides: False

***********************
Code Fellows 401 Python
***********************

.. slide:: Code Fellows 401 Python
    :level: 1

    This document contains no slides.

The materials in this documentation support the Python Dev Accelerator program
at Code Fellows in Seattle, WA.

Overview
========

A quick read on the objectives, philosophy and values held by Code Fellows and
followed by this Course.

Course Objectives
-----------------

- Acquire strong and idiomatic skills as a Python programmer
- Achieve a deep understanding of the full environment in which web programming
  occurs, from sockets up to frameworks.
- Develop the evaluative criteria to choose the right tool for the job.
- Build facility with associated technologies: git, HTML, CSS, Javascript.
- Gain mastery of the fundamental skills of agile development, testing,
  deployment and teamwork.


Learning Philosophy
-------------------

- Give students new super powers:
  http://assets.codefellows.org/UserSuperPowers.pdf
- Use experiential teaching techniques to make learning easier & faster
- David Kolb's Experiential Learning Cycle and Learning Styles:

    "David Kolb identified four types activities in the adult education process
    that must all be performed to achieve true understanding: Concrete
    Experience -> Reflective Observation -> Abstract Conceptualization ->
    Active Experimentation. Each stage is mutually supportive of and feeds into
    the next. It is possible to enter the cycle at any stage and follow it
    through around the circle."

Review: http://www.simplypsychology.org/learning-kolb.html

.. nextslide::

- Kathy Sierra's Badass User Talk and Edge Practice

  - Practice Makes Permanent

    - If you could do one thing to make your users more badass, provide them
      with repeated exposure to the performance, process, and results of badass
      users. (models)

  - Edge Practice: a progressive series of exercises, each designed to build a
    fine-grained skill within 1 to 3 sessions.
  - Edge / deliberate practice is NOT the same as tutorials. High-quality,
    low-latency feedback. Example: play this short musical passage with no
    mistakes, at this speed in this key.
  - Optional further reading:
    http://justingoeres.tumblr.com/post/32669772969/live-from-bos2012-building-a-minimum-badass-user

.. nextslide::

- Chunking

  - Break down a given skill into smaller and smaller pieces
  - Master the small pieces one at a time
  - Combine these pieces bit by bit, working out how they fit together
  - Optional further reading:
    http://www.theatlantic.com/health/archive/2012/09/using-pattern-recognition-to-enhance-memory-and-creativity/261925/

.. nextslide::

- Tight feedback loops

  - The sooner you know you are off course, the quicker you can correct
  - Spending time practicing the *right* things will most effectively improve
    your skills

.. nextslide::

- Approach this bootcamp like a Graduate Seminar

  - I'm standing in the front of the room, but you all have your own areas of
    expertise
  - I respect your areas of expertise
  - I expect you to bring them to bear in this class.
  - I will show you a door, but I expect you to go through it and journey on
    beyond

.. nextslide::

- Code Fellows Values

  - Best practices

.. ifnotslides::

    Learning to program in Python is about more than just learning logic,
    algorithms and data structures.  It's about learning to write idiomatic
    Python.  Python lends itself to clear, expressive programs, and learning to
    write the most pythonic Python will result in programs that are clean and
    easy to understand.  But more than that, idiomatic Python is Python that
    operates to the strengths of the language. Throughout the course, an
    emphasis will be placed on writing truly pythonic Python, and on learning
    to evaluate what is pythonic.

  - BDD

.. ifnotslides::

    Behavior Driven Development outlines an application's expected features and
    functionality first, before the coding begins. As Dan North says "Behavior
    is a more useful word than test". Focusing on the behavior of an
    application reduces question of what to test, what to call the tests, and
    which things to test.

    - Read:
      http://www.agile-doctor.com/2012/03/06/10-reasons-why-bdd-changes-everything/

    - Read the original article: http://dannorth.net/introducing-bdd/

  - Engaging communication. We help people pay attention. 

.. ifnotslides::

    "Activities are designed to fully engage the learning process. We encourage
    reflection, experimentation, play, communication and professional growth."

  - Build upon fundamentals. Break it in to pieces, put the pieces together.

  - Paths and Sandboxes

.. ifnotslides::

    "A path is a prescribed series of steps that get completed one after
    another. It's your classic tutorial. A sandbox is a collaborative learning
    space that values exploration, play, and generating autonomy.  While there
    are many paths to Python learning online, it's harder to provide a great
    example of a sandbox. That is why we are gathered here together in person
    at this Code Fellows Bootcamp. It's why we don't focus on creating yet
    another path for you to follow. "

    - http://assets.codefellows.org/paths_vs_sandboxes_stephen_p_anderson.png

The Honor Code:
---------------

As members of the Code Fellows community, each of us upholds and supports a
high standard of personal, and community, honesty and integrity.  We believe
these values are critical to a community dedicated to learning, personal
development, and a search for understanding. We consider them essential in
promoting personal responsibility, moral and intellectual leadership, and pride
in ourselves and our organization.

.. nextslide::

Therefore, each of us agrees to represent ourselves truthfully, claim only work
that is our own, properly attribute collaborations, and engage honestly in all
assignments.  Moreover, each of us shares the responsibility for encouraging
and reinforcing the importance of integrity in other community members.
Members of the Code Fellows community who misrepresent themselves or their work
through cheating, fabrication, facilitation, plagiarism, etc, or who suspect
another of such misrepresentation are expected to follow the Reporting
Procedures outlined. Code Fellows instructors and leaders reserve the right to
remove any students or graduates who fail to live up to these standards from
bootcamps, classes, or other parts of community membership, as appropriate.

.. nextslide::

Consistent with the basic expectations of the Honor Code, students who believe
they may have violated Code Fellows’ standards of integrity are expected to
acknowledge their concerns to the instructor in the class or to Code Fellows
staff.  Moreover, a student who observes what may be any dishonest behavior on
the part of another student is expected to share that concern with the student
immediately. At that point, if either student believes that an Honor Code
violation may have occurred, the student observed is expected to self-report
the incident immediately to the instructor in the class or to his or her or
administrative adviser. Self-reporting does not constitute an admission of
guilt but is an essential step, necessary to prevent misunderstanding and
apprehensions. Within three class days, the observer will also contact a member
of Code Fellows management to insure that the self-report has indeed taken
place. The instructor will review the elements of the complaint, and if the
instructor believes that the Honor Code has been violated, he or she will
contact a member of Code Fellows management, who will take appropriate action.

Diversity and Equality
----------------------

Don't be a hater, we are all here in this together, and want to create a
welcoming environment for everyone here. A Code Fellow works to widen access to
computer science education and ensure it is open to all.

Non-discrimination policy:
--------------------------

As a part of our honor code, in order to maintain personal and communal
integrity, Code Fellows is committed to the principle that all persons shall
have equal access to programs, facilities, services, and employment without
regard to personal characteristics not related to ability, performance, or
qualifications as determined by Code Fellows policy and/or applicable laws.

.. nextslide::

Code Fellows prohibits discrimination, harassment and bullying against any
person because of age, ancestry, color, disability or handicap, national
origin, race, religion, gender, sexual or affectional orientation, gender
identity, appearance, matriculation, political affiliation, marital status,
veteran status or any other characteristic protected by law.  Code Fellows
expects that its students, employees, volunteers, members, and other
constituents of Code Fellows, when and where ever those individuals are
conducting Code Fellows business or participating in Code Fellows classes,
events, or activities, shall maintain an environment free of discrimination,
including harassment, bullying, or retaliation.

Course Schedule
===============

To find the assignments, readings, lecture notes and other materials for a
given day, please select the day from the list below.

.. toctree::
    :maxdepth: 3

    Weekly Schedule <schedule/index>

All Course materials
====================

Direct links to all course materials, without reference to schedule

.. toctree::
    :maxdepth: 3

    Lecture Notes <lectures/index>
    Assignments <assignments/index>
    Readings <readings/index>
    Sample Code <downloads/index>
