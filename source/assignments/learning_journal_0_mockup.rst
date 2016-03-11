.. slideconf::
    :autoslides: False

************************
Learning Journal Mockups
************************

.. slide:: Learning Journal Mockups
    :level: 1

    This document contains no slides.

Over the first weeks of this course, you've been using the class learning journal for your daily journal entries.
It's time now to begin working on a journal of your own.

You'll be spending quite a bit of time looking at this journal, so you might as well make it look nice and behave well.
To that end, I want you to make a mockup of the site in HTML and CSS.
A mockup is a functional HTML prototype of the site you want to create.
It should look like a real site, with forms, buttons and navigation links, but with no actual functionality.

Tasks
=====

Create a Repository in GitHub called learning-journal.  The repository should have a README.md file and a standard Python .gitignore file. Clone the repository to your development machine. In the repository, create a new folder called mockups. In that folder, create four HTML files and a CSS stylesheet with the following specifications:

* The first should be a home page that shows a list of journal entries with just the title and date created.
* The second should be a detail page that shows a single entry.
  The title, text and created date should be displayed on this page.
* The third should be an HTML form page you will use to create a new entry.
  The title and text of the entry should be inputs in this form, empty at first.
* The fourth should be an HTML form page you will use to edit an existing entry.
  The title and text of the entry should be inputs in this form as well, pre-populated with the text from an entry.
* Each entry in the list on the home page should have a link that leads to the detail page.
* The home page should also have a UI element that allows you to start to create a new entry.
  It should link to the page with the create form.
* The detail page should have a UI element that allows editing the entry.
  It should link to the edit form page.
* There should be a UI element that leads back to the home page from anywhere in the site.
* You should make an effort to make the pages in your mockup look as unified as possible.
  Ensure that there is a common header, footer and navigation system shared among all the pages.

You must also include a CSS stylesheet in your repository that contains the styles needed to display the site.
If any javascript is required for the site to function properly, make sure it is included as well.

The HTML mockup pages should use this stylesheet via a "link" tag in the HTML head section.

You may use pre-existing CSS frameworks, like Bootstrap or Zurb Foundation, if you like.

Submitting Your Work
====================

When you are satisfied with your mockup, please submit a link to the repository URL in GitHub.
I will clone your repository and verify that it displays correctly and has all the required elements.

Make the site as pleasing and personally attractive as you can.
As I said earlier, you'll be seeing a lot of the site during the course.
