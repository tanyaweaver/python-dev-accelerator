******************
Django: Tagging
******************

Thus far we've been making an effort to run a library, talking about Patrons and all their properties.
However, we have yet to talk about any books!
Let's fill our library with some stuff that it can house, that we can then categorize with tags.


Getting Started
===============

Let's start a new app with ``python manage.py startapp library_assets``.
Inside, let's create a new model:

.. code-block:: python

    from django.db import Models

    class Book(models.Model):
        pass

Our library books should have a couple of relevant fields.
Let's keep it simple:

* Books
    - Title
    - Author
    - Year
    - Date Added to Library
    - Last Date Checked Out

.. code-block:: python

    import datetime
    from django.db import models

    # Create your models here.

    YEARS = [(year, year)
             for year in range(1, datetime.datetime.now().year + 1)][::-1]


    class Book(models.Model):
        title = models.CharField(max_length=250)
        author = models.CharField(max_length=250)
        year = models.IntegerField(choices=YEARS)
        date_added = models.DateTimeField(auto_now_add=True)
        date_taken = models.DateTimeField(auto_now=True)

Of course we want to be able to look at this model from our Django Admin, so register them in this directory's ``admin.py``.

.. code-block:: python

    from django.contrib import admin

    from library_assets.models import Book

    # Register your models here.
    admin.site.register(Book)

Finally, let's make sure that Django can see and installs our newest app.
In the project's ``settings.py`` add it to the list of ``INSTALLED_APPS``.


Bringing in Tagging
===================

The books in our simple library app currently don't have a way for us to categorize them.
You might imagine that in a real library, this would result in utter chaos as individual books would be very difficult to find.
One thing that we could do is group them by their genres!
Now, we could go and make a whole new model just to refer to genres, establishing a many-to-many relationship between them and books but why do all that?
There's already a Django app that does it for us!

Install Django-Taggit like any other Python package.

.. code-block:: shell

    $ pip install django-taggit

Add it to the list of our project's ``INSTALLED APPS``

.. code-block:: python

    ...
    INSTALLED_APPS = [
        ...
        "taggit",
    ]

Django-Taggit is an independent app, so it has its own migrations to apply to your database.
After adding it to your list of ``INSTALLED APPS``, apply those migrations.


Adding Tags to a Model
======================

To add tagging to a model is fairly straightforward.
In ``library_app/book_app/models.py`` we'll need to import the ``TaggableManager`` from ``taggit.managers``, then use that ``TaggableManager`` to add a field onto our model.

.. code-block:: python

    ...
    from taggit.managers import TaggableManager
    ...

    class Book(models.Model):
        # all the other fields

        tags = TaggableManager()

Our books now have tags, and we can see those tags if we migrate then pop open the Django admin.
At the bottom of the landing page for the admin, we now have a third category: ``Taggit -> Tags``.
Currently we have no tags, so let's add some.
Still inside of the admin, lets go to one of our existing Book instances.
We can see that there's now a field for adding a comma-separated list of tags!


Incorporating Tags into Views
=============================

Because tags are a field on model instances, we should be able to query and filter based on that tag.
Let's modify our app's views to give us that functionality.
The result we want is a list of books that match the tag we've given.

In ``library_assets/views.py`` we add the following code:

.. code-block:: python

    from django.shortcuts import render
    from django.views.generic import ListView

    from .models import Book

    class BookListView(ListView):
        """The listing for all books."""
        template_name = "library_assets/books/list.html"
        context_object_name = "books"

    class TagListView(ListView):
        """The listing for tagged books."""
        template_name = "library_assets/books/list.html"

        def get_queryset(self):
            return Book.objects.filter(tags__slug=self.kwargs.get("slug")).all()

        def get_context_data(self, **kwargs):
            context = super(TagListView, self).get_context_data(**kwargs)
            context["tag"] = self.kwargs.get("slug")
            return context

    def book_detail(request, id):
        """The detail view for one book"""
        return render(request, "library_assets/books/detail.html")


The first two class-based views will both return a list of books.
The ``TagListView`` will only return those where the tag contains some input slug.
That slug will come from the keyword arguments in the URL.
We've also modified the context to include the tag itself.
This way we actually have access to the tag in the template.

The last view will serve as the detail view for a single book.
We're just creating a base for it now.
We'll fill it out later on to take advantage of tagging.

Let's create this app's ``urls.py`` and write the url patterns that will deliver these books to the front-end.

.. code-block:: python

    # in urls.py

    from django.conf.urls import url

    from .views import TagListView, BookListView, book_detail

    urlpatterns = [
        url(r'^$', BookListView.as_view(), name="book_list")
        url(r'^tagged/(?P<slug>[-\w]+)/$', TagListView.as_view(), name="tagged_books"),
        url(r'^(?P<id>\d+)$', book_detail, name="book_page")
    ]

Finally, let's hook a URL into this app by modifying the ``urls.py`` file in our project's configuration root:

.. code-block:: python

    # in blogsite/urls.py

    urlpatterns = [
        # the other URL patterns
        url(r'^books/', include("library_assets.urls", namespace="library_assets", app_name="library_assets"))
    ]

Now our URL patterns will look like

* ``http://www.example.com/books/`` for the listing of all of our books
* ``http://www.example.com/books/tagged/foo`` for the listing of all books tagged with "foo"
* ``http://www.example.com/books/42`` for the book with the ID of 42


Getting Tagged Items into Templates
===================================

So now we have our URL patterns that point to our views for serving up books and tagged books.
The final piece of the puzzle is creating some templates that will display these books in list and in detail form.

Recall the path we've provided in our views to the templates we're interested in.
Let's create a templates directory and populate it with templates at those locations.

.. code-block:: shell
    
    # assuming your current directory is "library_assets"

    $ mkdir templates templates/library_assets templates/library_assets/books

    $ touch templates/library_assets/books/list.html

    $ touch templates/library_assets/books/detail.html


The List Template
-----------------

The book listing and the tagged-book listing are extremely similar.
We should save time and use the same template for both, adding in conditionals for when there are tagged items.

.. code-block:: html

    {% extends "library_project/layout.html" %}
    {% block content %}
    <h1>Books</h1>

    {% if tag %}
        <h2>Books Tagged As {{ tag }}</h2>
    {% endif %}

    <ul>
        {% for book in books %}
            <li>
                <h3>
                    <a href="{% url "library_assets:book_page" book.id %}">{{ book.title }}</a>
                </h3>
                <p><strong>Author:</strong> {{ book.author }} </p>
            </li>
        {% endfor %}
    </ul>

    {% endblock %}


Tags in the Detail Template
---------------------------

The main benefit of including a tagging system in your site is that it allows you to categorize things.
These tags should also be able to help you find other items like the one you're looking at.
In the detail for a single book we can accomplish this in two ways.
The first is to simply include the tags for a book in the template.

Let's modify our simple function-based detail view so that we return a book.
There's no new magic here, this is the same basic view function you've written before.

.. code-block:: python

    ... other package imports

    from django.shortcuts import render, get_object_or_404

    ... the other views

    def book_detail(request, id):
        """The detail view for one book."""
        book = get_object_or_404(Book, id=id)

        return render(request, "library_assets/books/detail.html", {"book": book})

Now in our detail template, we can look at the book's details, as well as its tags.
It's straightforward to incorporate tags here, as they're just another field on a model.
The tags field itself is iterable, so we can treat it as such in the template.

.. code-block:: html

    {% extends "library_project/layout.html" %}
    {% block content %}

    <h1>Title: {{ book.title }}</h1>
    <ul>
        <li>Author: {{ book.author }}</li>
        <li>Published: {{ book.year }}</li>
        <li>Tags:
            {% for tag in book.tags.all %}
                <a href="{% url "library_assets:tagged" tag.slug %}">{{ tag }}</a>,
            {% endfor %}
        </li>
        <li>Added to Library: {{ book.date_added }}</li>
        <li>Last Checked Out: {{ book.date_taken }}</li>
    </ul>

    {% endblock %}

Now, not only do we have the list of tags for each book embedded in the detail view, but the tags themselves are clickable, serving as links to lists of other books with the same tag.


Using Tags to Find Similar Books
--------------------------------

The second way to harness the power of tags is to include within the book detail a handful of other books with similar tags.
This does not mean just pick one tag and find the books corresponding to it.
*For every tag that a book has*, we should be able to have some other books we can find from it.
This type of item retrieval should be handled by our view, so we'll be adding to it.

Recall that our tags are in fact model instances handled by the ``django-taggit`` add-on.
As such, every tag that's been created can be queried.
We can see this by looking at our Book instances in the Django shell

.. code-block:: ipython

    In [1]: from library_assets.models import Book

    In [2]: book = Book.objects.first()

    In [3]: print(book.tags)
    Out[3]: <taggit.managers._TaggableManager at 0x1050ebeb8>

    In [4]: print(book.tags.all())
    Out[4]: <QuerySet [<Tag: easter>, <Tag: egg>]>

Great we can get the tags.
Here's what we want to do now:

1. Harvest all of the tags belonging to an individual book.

2. Get every book with a tag matching one of the harvested tags.

3. Make sure to exclude the book we already have.

4. Make the result set into a unique list.

.. code-block:: ipython

    In [5]: all_tags = book.tags.all()

    In [6]: similar_books = Book.objects.filter(tags__in=all_tags)

    In [7]: not_current = similar_books.exclude(id=book.id)

    In [8]: unique_books = not_current.distinct()

Let's port this back into our detail view!

.. code-block:: python

    def book_detail(request, id):
        """The detail view for one book."""
        book = get_object_or_404(Book, id=id)

        # List of similar books
        tags = book.tags.all()
        similar_books = Book.objects.filter(
            tags__in=tags
        ).exclude(
            id=book.id
        ).distinct()

        return render(request, 
                      "library_assets/books/detail.html", 
                      {"book": book, 
                       "similar_books": similar_books})

Now that we've gotten our similar books in hand, we can access them from the detail template like any other model that we've passed into context.

.. code-block:: html

    {% extends "library_project/layout.html" %}
    {% block content %}

    <h1>Title: {{ book.title }}</h1>
    <ul>
        <li>Author: {{ book.author }}</li>
        <li>Published: {{ book.year }}</li>
        <li>Tags:
            {% for tag in book.tags.all %}
                <a href="{% url "library_assets:tagged" tag.slug %}">{{ tag }}</a>,
            {% endfor %}
        </li>
        <li>Added to Library: {{ book.date_added }}</li>
        <li>Last Checked Out: {{ book.date_taken }}</li>
    </ul>

    <h2>Books in the same category:</h2>
    <ul>
        {% for next_book in similar_books %}
            <li>
                <a href="{% url "library_assets:book_page" next_book.id %}">{{ next_book.title }}</a>
            </li>
        {% endfor %}
    </ul>

    {% endblock %}


Recap
=====

Categorization is a powerful tool for allowing your site to talk to itself, and allowing the user to find "like" things.
In Django this categorization ability is made fairly simple with tags, coming from the add-on ``django-taggit``.
It treats tags as model instances, and lets us use tags as many-to-many relationships with whatever it is we're tagging, be it cars, books, movies, blog posts, images, whatever.
Find ways to incorporate tags into your work, and make your site more user friendly!
