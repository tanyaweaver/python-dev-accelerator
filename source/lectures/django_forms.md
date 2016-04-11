# sea_d35_day28_django_forms

Day 28: Form Handling in Django, and the Form-handling CBVs

-----

We will need to work with the form system in Django if you want to add or update photos in our app.

[Django's form system](https://docs.djangoproject.com/en/1.9/ref/forms/) has a couple of layers to it.

(Cris is on whiteboard here)

We'll make an analogy. "Models are to Database as Forms are to request/response cycle." The job of a model in Django is to translate data between python and the database. The job of a form in Django is to translate data back and forth between python and the request/reponse cycle. A form takes in information that comes from the request and translates it into pythonic values. Remember, every time you get information coming in on the request, that information is coming in to you as a bytestring. When you pass a primary key back and forth across a URL, that comes into you as a bytestring. You want to turn that into an integer so you can interact with the database. The Django form is going to make that happen for you.

This can start to get weird because Models have fields, and Forms have fields. They look similar, but they are very different from each other. The model field holds the responsibility of translating a particular python value into some sort of database query. Also it takes the return value and turns it back into a python value. The form does the same thing except it does it with data from the request and response. It turns one item of information into a pythonic value.

Forms serialize and deserialize. They do it with a structure called a widget. The widget renders out visible elements (or hidden) that renders that data into a HTML page.

Let's say we have something that's a `forms.text` field. It will have a widget that has a text input. When you call the widget's `render` method, it will give you inputtype = text and value = field contents. This is the overall structure of how form libraries everywhere work.

(Back to computer)

(6:08)

So how do forms in Django work? A form is just a collection of fields.

Let's start up our Django shell:

```python
In [4]: from django import forms

In [8]: class foo(forms.Form):
    name = forms.TextInput()
    description = forms.Textarea()
   ...:     

In [9]: foo
Out[9]: __main__.foo

In [10]: type(foo)
Out[10]: django.forms.forms.DeclarativeFieldsMetaclass

In [11]:  foo_form = foo()

In [12]: foo_form
Out[12]: <foo bound=False, valid=Unknown, fields=()>

In [13]: type(foo_form)
Out[13]: __main__.foo

```

There are a few things to think about here. Our form can be in one of two states: either bound or unbound. The difference is that a bound form knows about data. It has some information that has been passed into it. An unbound form doesn't have any data in it.

(We go back to the Django shell, but the `foo_form` isn't really working. We grab a working snippet from the Django docs:)

```python
In [16]: %paste
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

## -- End pasted text --

In [17]: form1 = NameForm()

In [18]: form1
Out[18]: <NameForm bound=False, valid=Unknown, fields=(your_name)>
```

Now we have a working form called `form1`. It tells us that it's unbound. It doesn't know if it's valid, and it has some fields. If we just call `str()` on our `form1`, it will render out into HTML:

```python
In [19]: str(form1)
Out[19]: '<tr><th><label for="id_your_name">Your name:</label></th><td><input id="id_your_name" maxlength="100" name="your_name" type="text" /></td></tr>'
```

The `form1.as_p()` method will render our form with `<p>` tags:

```python
In [21]: form1.as_p()
Out[21]: u'<p><label for="id_your_name">Your name:</label> <input id="id_your_name" maxlength="100" name="your_name" type="text" /></p>'
```

There is also an `as_table()` method. This is the default and the same as our `str()` rendering.

Notice that the `<form>` tag is missing. Nor is there a `<submit>` button. That's up to you.

It gives us an `id="id_your_name"` attribute. It's constructed by default as the name of the field with `id_` prepended to it. Notice there is no value on the input either.

### (14:45) Bound Form

Let's make another form. We'll pass in some data as a dictionary, and then the form will be bound.

```python
In [22]: form2 = NameForm({'your_name': u'Cris Ewing'})

In [23]: form2
Out[23]: <NameForm bound=True, valid=Unknown, fields=(your_name)>
```

Now we can use that information to fill out the form with the data that exists. Notice the `value="Cris Ewing"` attribute:

```python
In [24]: form2.as_p()
Out[24]: u'<p><label for="id_your_name">Your name:</label> <input id="id_your_name" maxlength="100" name="your_name" type="text" value="Cris Ewing" /></p>'
```

We can also render forms as a list with `as_ul()`.

Forms are also iterators. These objects come out in the order that you specify the attributes. If you want to change the ordering of a form, change it in the Django form definition.

```python
In [25]: for field in form2:
   ....:     print field
   ....:     
<input id="id_your_name" maxlength="100" name="your_name" type="text" value="Cris Ewing" />
```

If you aren't happy with the way Django is rendering `<p>` forms or whatever, you can address the field properties directly and lay them out how you like:

```python
In [31]: field.id_for_label
Out[31]: u'id_your_name'

In [32]: field.label
Out[32]: 'Your name'

In [33]: field.value()
Out[33]: u'Cris Ewing'
```

It's probably best to let Django render out the fields for you.

(21:21)

The `valid` value of a form is also important. When a form is bound, you can do validation checks on it.

```python
In [35]:  form2.is_valid()
Out[35]: True
```

This allows us access to `cleaned_data`:

```python
In [36]: form2.cleaned_data
Out[36]: {'your_name': u'Cris Ewing'}
```

`cleaned_data` is a dictionary of key, value pairs that correspond to the field names and the values those fields contain. It is **super important**. Because: `form2` also has a `data` attribute:

```python
In [37]: form2.data
Out[37]: {'your_name': u'Cris Ewing'}
```

It looks the same in this case, but the difference is that the `cleaned_data` has gone through validation. What this means is that you can be sure that if someone is trying to be inject malicious data, Django has already sterilized it and it is safe for python to use. Whenever you're reading data from a form, always validate the data first, and then use the `cleaned_data` attribute of your form to get access to the information.

Let's build one that might not be validated.

```python
In [38]: form3 = NameForm({'your_name': u'My name is reallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreally loooooooong'})

In [39]: form3
Out[39]: <NameForm bound=True, valid=Unknown, fields=(your_name)>
```

Notice it is bound, but we don't know yet if it is valid. When we check the validity:

```python
In [40]: form3.is_valid()
Out[40]: False

In [41]: form3.cleaned_data
Out[41]: {}
```

This particular form will have an `errors` attribute now:

```python
In [42]: form3.errors
Out[42]: {'your_name': [u'Ensure this value has at most 100 characters (it has 167).']}
```

You can use this to send error messages back to your forms.

```python
In [45]: if foo.name in form3.errors:
    print("There's a mistake here: {}".format(form3.errors['your_name']))
   ....:     
There's a mistake here: <ul class="errorlist"><li>Ensure this value has at most 100 characters (it has 167).</li></ul>
```

Django makes some nice default error messages for us with HTML markup too. There is ample API documentation for forms like how to substitute css classes and things like that.

### (27:44) [`ModelForm`](https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/#django.forms.ModelForm)

There's something else you should know about forms, and that is that this way of building forms is not the only way. Your system is filled up with models. One things you would like to do is present forms that allow you to create and edit those models. Django provides you with a construct called a `ModelForm`.

What a `ModelForm` does is it looks at your model, and it looks at the fields on the model, and it creates a form that has all the equivalent form fields that are on your model.

- Create a class that subclasses `ModelForm`.
- Provide a `class Meta`
  - This informs the form object about some options that you can set for it.

```python
[46]: from imager_images.models import Photo

In [47]: Photo
Out[47]: imager_images.models.Photo

In [48]: class PhotoForm(forms.ModelForm):
  ....:     class Meta:
  ....:         model = Photo
  ....:         exclude = []
  ....:         

In [49]: PhotoForm
Out[49]: __main__.PhotoForm

In [50]: pf1 = PhotoForm()

In [51]: pf1
Out[51]: <PhotoForm bound=False, valid=Unknown, fields=(user;image;title;description;date_published;published;location)>
```

This looks similar. Our fields include all of the fields on the Photo model automatically now.

Let's look at a photo object:

```python
In [53]: Photo.objects.all()
Out[53]: [<Photo: PuPPy>]

In [54]: p1 = _[0]

In [55]: p1
Out[55]: <Photo: PuPPy>
```

When we create a PhotoForm, if we want to bind it to an instance, we can use the instance keyword argument to instantiate our new PhotoForm:

```python
In [56]: lovely_form = PhotoForm(instance=p1)

In [57]: lovely_form
Out[57]: <PhotoForm bound=False, valid=Unknown, fields=(user;image;title;description;date_published;published;location)>

In [58]: lovely_form.as_p()
Out[58]: u'<p><label for="id_user">User:</label> <select id="id_user" name="user">\n<option value="">---------</option>\n<option value="2" selected="selected">joel</option>\n</select></p>\n<p><label for="id_image">Image:</label> Currently: <a href="/media/photo_files/2016-01-20/puppy_tshirt_1.jpg">photo_files/2016-01-20/puppy_tshirt_1.jpg</a> <br />Change: <input id="id_image" name="image" type="file" /></p>\n<p><label for="id_title">Title:</label> <input id="id_title" maxlength="256" name="title" type="text" value="PuPPy" /></p>\n<p><label for="id_description">Description:</label> <textarea cols="40" id="id_description" name="description" rows="10">\r\nPuPPy logo</textarea></p>
...'
```

Django gives us all sorts of options here that allows us to manipulate our model.

Notice the `lovely_form` is not bound:

```python
In [60]: lovely_form
Out[60]: <PhotoForm bound=False, valid=False, fields=(user;image;title;description;date_published;published;location)>
```

Why do we suppose that is? Because we haven't passed in any data. Just giving it an instance doesn't bind it to anything. If we make a change, the form will become bound, and the `selected` attribute will now be `'bob'` (our user 3 in this case):

```python
In [73]: changed_form = PhotoForm({'user': 3}, instance=p1)

In [74]: changed_form
Out[74]: <PhotoForm bound=True, valid=Unknown, fields=(user;image;title;description;date_published;published;location)>

In [75]: str(changed_form)
Out[75]: '<tr><th><label for="id_user">User:</label></th><td><select id="id_user" name="user">\n<option value="">---------</option>\n<option value="2">joel</option>\n<option value="3" selected="selected">bob</option>\n</select></td></tr>\n<tr><th><label for="id_image">Image:</label></th>......
```

`<option value="3" selected="selected">bob</option>`

What this means is the data you send in that the form is bound to, will override and take precedence over the data that's attached to the object that represents the base instance of that form.

Is the form valid?

```python
In [78]: changed_form.is_valid()
Out[78]: False

In [79]: changed_form.errors
Out[79]:
{'published': [u'This field is required.'],
 'title': [u'This field is required.']}
```

So let's fix our errors:

```python
In [88]: changed_form = PhotoForm({'user': 3, 'title': 'PuPPy Logo', 'published': 'public'}, instance=p1)

In [89]: changed_form.is_valid()
Out[89]: True

In [90]: p1
Out[90]: <Photo: PuPPy Logo>

In [91]: p1.user
Out[91]: <User: bob>
```

Our user instance has already been updated by the fact that we bound some data to a form. Once we save the form, it will be updated in the database too.

(41:14)

We saw how we passed in an instance of a form and some data. Where does the data come from? In Django you have a `request` object inside any view you create.

(Cris is at whiteboard here)

`request` will have 2 attributes on it. These attributes will contain any form data that got sent to you from the browser. `request.post`, `request.get`. Using forms you'll probably want to use `post`.

Most of this process will be similar to what you have done already on edit views and create views. `request.post` is a dictionary, and you can pass it in as part of the data that comes to you.

You are going to want to upload images. This might be a bit odd. Those images will be coming to you not in `request.post` or `get`. The come in a completely different place called `request.files`. There's one more trick to this. In order to get image data, you have to do something to your `<form>` tag. There's another attribute to forms called the [`enctype`](https://www.w3.org/TR/html401/interact/forms.html#adef-enctype). In order to upload images, you need to set [`enctype="multipart/form-data"`](https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/#basic-file-uploads)

(Back to the computer)

On the other end, you need to make sure you bind your form not only to the first dictionary, but also to the second:

```python
In [92]: changed_form = PhotoForm({'user': 3, 'title': 'PuPPy Logo', 'published': 'public'}, {'file': <file upload object>}, instance=p1)
```

Django is responsible for dealing with all of this. All you need to is pass in `request.post, request.files, instance=original_instance` If you're creating a new instance, just don't pass in an instance and Django will build a new one for you when you call `form.save()`

### (48:23) [Authenticating Users](https://docs.djangoproject.com/en/1.9/topics/auth/default/#authenticating-users)

One last thing. Think about authentication. How will you deal with testing your users and whether or not they will have access to things. You've already seen one decorator you can use in a view, or put in your urlconf, and that's `login_required`. If you're using class-based views, you must put the decorator in the urlconf.

Beyond the idea of [`login_required`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.decorators.login_required), there are other ones you can use as well:

[`permission_required`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#the-permission-required-decorator). Django has some default permissions. Every new model you make has permissions associated with it: `create`, `edit`, and `delete`. The user has a `has_perm` attribute.

This decorator allows you at the view level, you can say they must have a particular permission. So you could say inactive users don't have permission to change files. Be aware the permissions are table level permissions. You would also need to make sure the user is the owner of the object in question.

Both `login_required` and `permission_required` are special instances of a more generalized decorator that's available called [`user_passes_test`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.decorators.user_passes_test). That takes a function, the function takes the user object, and returns either `True` or `False`. When this decorator is applied to a view, if the logged in user does not pass that test, they are sent off to the login page.

So Django gives us with specific instances of the `user_passes_test`, but you can come up with your own if you need to.
