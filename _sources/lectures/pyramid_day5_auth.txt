******************
Controlling Access
******************

.. ifnotslides::

    One thing you may have noticed while testing your app in a browser is that you did not have to log in.
    Convenient, but not really all that safe.
    Knowing the kind of place the internet is,
    you probably don't want to allow just anyone to post journal entries in your journal.

    The process of verifying the identity of a user visiting your website is called **authentication** (AuthN for short).
    The closely related, but different process of determining what *rights* an authenticated user has in your website
    is called **authorization** (AuthZ).

    Next, we'll be adding *authentication* and *authorization* to your journal.
    This will allow you to display entries to the general public while reserving the ability to write new entries to a known user (you).

.. ifslides::

    Adding Authentication (AuthN) and Authorization (AuthZ)

Principals
==========

.. ifnotslides::

    Both AuthN and AuthZ depend on identity.
    In a website, Identity is tied to the concept of *principals*.
    Principals can be called users, groups, roles, or any of a number of other names.
    But behind them all stands the basic idea of an identifier that can be used for both authentication and authorization.

    For the purposes of a single-user learning journal, we won't really need to be too complicated.
    A *user* is probably enough to get the job done.

    You could implement an entire database table for the purpose of storing your user information,
    but really that's overkill for a system that only has one user.
    You should never implement more code than you need.

    So how can you solve the problem of storing the data needed to authenticate a single user?

.. ifslides::

    .. rst-class:: build
    .. container::

        AuthN and AuthZ depend on identity

        Identity is provided by *principals*

        Princpals can be users, groups, roles ...

        Can use a database to store information about principals

        Too complex for a simple one-user journal application

        What should we use instead?

.. nextslide::

.. ifnotslides::

    How about *configuration*?

    You remember that we've been using ``os.environ`` to hold the URL for our database connection.
    We can do the same thing for an identifier (*principal*) representing our user.
    We'll call this principal a *username*

.. ifslides::

    .. rst-class:: build
    .. container::

        Why not use *configuration*?

        We have stored our database password in the OS Environment

        We can do the same with a **username**:

.. rst-class:: build
.. code-block:: python

    os.environ.get('AUTH_USERNAME', '')

.. ifnotslides::

    What else would we require in order to prove that a user is who they claim to be?
    Generally, this is done by asking the user to provide a *password*.
    If the password provided by the user matches the one stored by the system,
    then the user has proven their identity.
    We can use the same mechanism to store our one user's password:

.. ifslides::

    .. rst-class:: build
    .. container::

        Another requirement for identification might be a password

        Store the user's **password** in the same fashion:

.. rst-class:: build
.. code-block:: python

    os.environ.get('AUTH_PASSWORD', '')




Policies
========

.. ifnotslides::

    To *authenticate* a user, the most basic pattern is to confirm a username and password.
    In general the steps are to:

.. ifslides::

    Simple Authentication confirms a username and password

.. rst-class:: build

* accept a username and password as provided by a visitor
* reject them if either is missing
* reject them if they cannot be confirmed to be correct
* otherwise, persist the fact that the user is authenticated

.. nextslide::

.. ifnotslides::

    HTTP is a **stateless** protocol.
    That means that no individual request can know anything about any other request.
    So how do you accomplish that fourth goal?
    The usual method is to send an encrypted *cookie* back to the user in an HTTP response.
    This cookie is saved and re-transmitted to the server with each successive request.
    This gets around the *stateless* nature of HTTP by sending the required information back and forth.

.. ifslides::

    .. rst-class:: build
    .. container::

        HTTP is **stateless**

        No request can know anything about any other request

        How to persist authentication?

        Many approaches, common is to use a *cookie*

        Information about authentication is stored in client browser

        Re-transmitted with every subsequent request

.. nextslide::

.. ifnotslides::

    By default, Pyramid does not enable authentication.
    There are a lot of use-cases for building an application that does not require any login.
    Our application really does need it, though, so we'll need to enable AuthN and AuthZ

    In pyramid, both AuthN and AuthZ are implemented using *policies*.
    These *policies* are classes with a specific set of methods and attributes that fulfill a required contract.

    Policies for AuthN are made available in the `pyramid.authentication <http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authentication.html>`_ package.
    For our authentication policy we'll be using the ``AuthTktAuthenticationPolicy``.
    This policy issues an encrypted, `specially formatted cookie <http://stackoverflow.com/questions/1844623/what-is-the-auth-tkt-cookie-format>`_ to the user's browser.
    Whenever a new request comes in,
    Pyramid unencrypts the cookie and establishes the identity of the user from the data it contains.

.. ifslides::

    .. rst-class:: build
    .. container::

        Pyramid does not enable authn or authz by default

        We need it, so we'll have to turn it on

        Implemented in Pyramid using *policies*

        Classes which fulfill a specific contract

        We'll use ``AuthTktAuthenticationPolicy`` from ``pyramid.authentication``

        Uses a specially formatted cookie to transmit data about user identity

.. nextslide::  AuthN Policy

.. ifnotslides::

    To enable authentication we must *configure* our app to include an authentication policy.
    We could do this in our apps ``__init__.py`` file, but we've been following a pattern of breaking related configuration into separate modules.
    We'll *include* this module in our app ``__init__.py``.
    So it will need an ``includeme`` function:

.. ifslides::

    .. rst-class:: build
    .. container::

        We must configure our app to add AuthN policy

        Could do so in global config (``__init__.py``)

        Use a ``security.py`` module instead (clean factoring)

.. rst-class:: build
.. code-block:: python

    # security.py
    import os
    from pyramid.authentication import AuthTktAuthenticationPolicy


    def includeme(config):
        """security-related configuration"""
        auth_secret = os.environ.get('AUTH_SECRET', 'itsaseekrit')
        authn_policy = AuthTktAuthenticationPolicy(
            secret=auth_secret,
            hashalg='sha512'
        )
        config.set_authentication_policy(authn_policy)

.. ifnotslides::

    We can use the OS environment pattern we've been establishing to get a **auth_secret**.
    This value will serve as a *key* for encrypting and decrypting the cookie sent back and forth from the client.
    Then, we create an instance of the ``AuthTktAuthenticationPolicy`` class,
    initialized with our secret and with the name of the algorithm we'll use to perform the encryption.
    Finally, we set this instance as the authentication policy for our app configuration.

.. nextslide:: AuthZ Policy

.. ifnotslides::

    Once you know *who* someone is, you will also want to know *what rights* they should be given in your website.
    Pyramid provides for this through an **Authorization Policy**.
    There is a version of such a policy made available in the `pyramid.authorization <http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authorization.html>`_ package.
    It's called the ``ACLAuthorizationPolicy``.
    It works by allowing you to specify permissions that should be granted or denied to certain principals.

    To enable this policy, we must add configuration to our new ``security.py`` module:

.. ifslides::

    .. rst-class:: build
    .. container::

        Also need to establish *rights* for our user

        We'll add the ``ACLAuthorizationPolicy`` from ``pyramid.authorization``

.. rst-class:: build
.. code-block:: python

    # security.py
    import os
    from pyramid.authentication import AuthTktAuthenticationPolicy
    from pyramid.authorization import ACLAuthorizationPolicy

    def includeme(config):
        """security-related configuration"""
        auth_secret = os.environ.get('AUTH_SECRET', 'itsaseekrit')
        authn_policy = AuthTktAuthenticationPolicy(
            secret=auth_secret,
            hashalg='sha512'
        )
        config.set_authentication_policy(authn_policy)
        # add the following new lines of configuration and the new import above.
        authz_policy = ACLAuthorizationPolicy()
        config.set_authorization_policy(authz_policy)

.. nextslide:: Wiring It Up

.. ifnotslides::

    Now that we have a policy for AuthN and AuthZ configured, we can include our security module in our global app configuration.
    Back in our ``__init__.py``, let's include it:

.. ifslides::

    .. rst-class:: build
    .. container::

        We have an AuthN Policy that will handle Authentication

        And an AuthZ policy that will handle Authorization

        We need to include this configuration in our app global config (``__init__.py``):

.. rst-class:: build
.. code-block:: python

    # __init__.py

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.include('.security') #<-- add this
        config.scan()
        return config.make_wsgi_app()


Permissions
===========

.. ifnotslides::

    Once policies have been configured for authentication and authorization,
    we are ready to make assertions about what *permissions* we want to require for our views.

    Once again, Pyramid does not, by default, require any permissions for any views.
    There are many applications where none are required.
    But our app should.
    We can start by setting a *default* permission,
    one that will be used for all views.
    We can use the ``set_default_permission`` method of the Configuration class:

.. ifslides::

    We are ready to require *permissions* now

    .. rst-class:: build
    .. container::

        By default, pyramid does not require any permissions

        Our app should have some

        We can ( but do not have to) set a *default permission* for all views:

.. rst-class:: build
.. code-block:: python

    def includeme(config):
        """security-related configuration"""
        auth_secret = os.environ.get('AUTH_SECRET', 'itsaseekrit')
        authn_policy = AuthTktAuthenticationPolicy(
            secret=auth_secret,
            hashalg='sha512'
        )
        config.set_authentication_policy(authn_policy)
        # add the following new lines of configuration and the new import above.
        authz_policy = ACLAuthorizationPolicy()
        config.set_authorization_policy(authz_policy)
        config.set_default_permission('view')

.. ifnotslides::

    Now, all our views will require that our visitor has a permission called ``'view'`` before they will display.
    If the visitor does not have the required permission, Pyramid will automatically raise a ``403 Forbidden`` error.

.. nextslide:: Per-View Permissions

.. ifnotslides::

    We can also set permissions on individual views.
    We use the ``view_config`` decorator to do so:

.. ifslides::

    Use ``view_config`` to set permissions on individual views

.. code-block:: python

    @view_config(route_name='private', renderer='string', permission='secret')
    def private(request):
        return "I am a private view"

.. nextslide:: What Happens Now

.. ifnotslides::

    When we use the ``permission`` keyword argument to ``view_config``,
    the decorated view will require that the *principal* who has made a request for this view has the named permission.
    If we have set a default permission in our security configuration, that permission will be *overridden* by this new one.

.. ifslides::

    We have set permissions on views now

    .. rst-class:: build
    .. container::

        When a visitor makes a request for our views they will be checked

        The framework will determine which permission is required

        The framework will also determine what permissions a user has

        If the user is not allowed the required permission:

        ``403 Forbidden``

.. nextslide:: Default Permissions

.. ifnotslides::

    Any view that is not marked with permission will use the default permission we configured.
    If we configured no default, then no permission will be required.

.. ifslides::

    If no permission is specified in ``view_config``, default is used

    If no default has been set, no permission is required

.. code-block:: python

    @view_config(route_name='public', renderer='string')
    def public(request):
        return "I am a public view"

.. ifnotslides::

    As we have said, declaring a default permission means *every* view that does not explicitly require a permission will require the default.
    If you need to exempt a view from this requirement, Pyramid provides a special marker.
    You can use ``pyramid.security.NO_PERMISSION_REQUIRED`` as the permission argument to your `view_config` decorator:

.. ifslides::

    .. rst-class:: build
    .. container::

        Default permission is applied to all views

        Exempt views with ``pyramid.security.NO_PERMISSION_REQUIRED``:

.. rst-class:: build
.. code-block:: python

    from pyramid.security import NO_PERMISSION_REQUIRED

    @view_config(route_name='login', renderer='string', permission=NO_PERMISSION_REQUIRED)
    def login(request):
        # log in a user

Permissions, Context and ACLs
-----------------------------

.. ifnotslides::

    In Pyramid, *views* are responsible for requiring a permission.
    But how do we determine what permissions are assigned to a specific *principal*?
    That is a task that falls to *context*.

    Context is best defined as *where you are* in an application.
    In a basic Pyramid app, context is provided by a *root* object.
    The root object is created when an incoming request is handled.
    A *root factory* is a class that can be instantiated with a request.
    A specific instance of the *root factory* serves as the root for a given request.

    When a visitor to a site requests a particular view, the Pyramid framework inspects the configuration of that view to determine which permission is required.
    Then the framework finds the root object and asks it for information about what permissions are granted to the current *principal*.
    The root object must provide an ``__acl__`` special attribute.

.. ifslides::

    *Views* are responsible for requiring a permission

    .. rst-class:: build
    .. container::

        *Context* is responsible for assigning permissions to principals

        *Context* is provided by a **root object**

        A *root factory* generates a new root object for each request

        The *root object* has an ``__acl__`` special attribute

        A list of permission assignments

.. nextslide:: What is an ACL?

.. ifnotslides::

    An ACL is an *access control list*.
    It is expressed as a list of tuples, each of which specifies a relationship between a principal and a permission.
    Each tuple contains exactly three values:

    * An action (one of ``pyramid.security.Allow`` or ``pyramid.security.Deny``)
    * A *principal* (a string or special value that is matched against the current principal)
    * A *permission* (a string or special value that is matched against the required permission)

    The *principal* in an ACL tuple may be a simple string, like a username.
    Or it might be one of two special values provided by the framework.
    The ``pyramid.security`` module provides ``Everyone`` to represent any principal at all.
    And ``Authenticated`` is provided to represent anyone who has passed an authentication check by the authentication policy.

    The *permission* in an ACL tuple will generally be a simple string.
    It should match one of the permissions configured for views,
    or the permission set as the default permission for the app.
    These strings are arbitrary, you can make up permissions that fit your needs.
    Alternantively, the ``pyramid.security`` module provides the special value ``ALL_PERMISSIONS``.
    This value will match any permission required, and can be use to grant blanket access to any view.

    If the current principal for a request is found in a tuple with the required permission,
    and the action in that tuple is ``Allow``,
    then the view can be called.
    If no tuple is found, or one is found where the action is ``Deny``,
    then the framework will automatically raise a ``403 Forbidden`` exception.

.. ifslides::

    *Access Control List*

    .. rst-class:: build
    .. container::

        List of tuples with three values.

        Values are an action, a *principal* identifier and a *permission* identifier

        .. rst-class:: build

        * action: ``pyramid.security.Allow`` or ``pyramid.security.Deny``
        * *principal*: string, ``pyramid.security.Everyone``, or ``pyramid.security.Authenticated``
        * *permission*: string or ``pyramid.security.ALL_PERMISSIONS``

.. nextslide:: Custom ACLs

.. ifnotslides::

    ACLs are found on roots, which are built using root factories.
    Pyramid provides a default root factory.
    It does not have any ``__acl__``,
    so unless we replace it no-one will be allowed to request any view which requires a permission.
    We can replace the default factory in our ``security.py`` module.
    We create a root factory class that takes the request as an argument for initialization,
    and provides an ``__acl__`` special attribute with appropriate ACL entries:

.. ifslides::

    Pyramid provides a default root factory, but it has no ACL

    .. rst-class:: build
    .. container::

        A custom root factory takes ``request`` when initialized.

        Has an ``__acl__`` special attribute

.. rst-class:: build
.. code-block:: python

    # in security.py

    from pyramid.security import Everyone, Authenticated
    from pyramid.security import Allow

    class MyRoot(object):

        def __init__(self, request):
            self.request = request

        __acl__ = [
            (Allow, Everyone, 'view'),
            (Allow, Authenticated, 'secret'),
        ]

.. nextslide:: Adding Our Root Factory

Then, we set this as the root factory for our app in ``includeme``:

.. code-block:: python

    def includeme(config):
        """security-related configuration"""
        auth_secret = os.environ.get('AUTH_SECRET', 'itsaseekrit')
        authn_policy = AuthTktAuthenticationPolicy(
            secret=auth_secret,
            hashalg='sha512'
        )
        config.set_authentication_policy(authn_policy)
        authz_policy = ACLAuthorizationPolicy()
        config.set_authorization_policy(authz_policy)
        config.set_default_permission('view')
        config.set_root_factory(MyRoot) #<-- add this line


Authenticating Users
====================

.. ifnotslides::

    We've now secured a simple application.
    We allow anyone to request views that have no specific permission declaration.
    And we require that a user be authenticated in order to view our private view.
    All that remains is to allow a user to authenticate.

    We stated at the beginning that we would use the OS environment to store a username and password.
    We could implement a model for our user, but since we'll only need one, it's a bit of overkill to do so.

.. ifslides::

    Our app is secured.

    We'll store our username and password in the OS environment:

.. code-block:: python

    os.environ.get('AUTH_USERNAME', '')
    os.environ.get('AUTH_PASSWORD', '')

.. ifnotslides::

    Given this plan, we can implement a simple function that would allow us to authenticate a user.
    It will take as arguments the username and password provided by a visitor.
    Then it will compare these against the values we stored in the environment.
    If they match, then we know the user is who they claim to be.

.. ifslides::

    We need a function to tell us if provided username and password match stored values:

.. code-block:: python

    def check_credentials(username, password):
        stored_username = os.environ.get('AUTH_USERNAME', '')
        stored_password = os.environ.get('AUTH_PASSWORD', '')
        is_authenticated = False
        if stored_username and stored_password:
            if username == stored_username:
                if password == stored_password:
                    is_authenticated = True
        return is_authenticated

.. nextslide:: A Flaw!

.. ifnotslides::

    This would work, but there's a critical flaw in our plan.
    Can you spot it?

.. ifslides::

    Can you spot the problem with this approach?


Encryption
----------

.. ifnotslides::

    The problem is that our password is being stored in plain text.
    If anyone breaks into our server, they will be able to read the password.
    We should prevent this.

    .. warning:: **NEVER** store user passwords in plain text.


    Passwords should always be stored in a hashed form.
    This means that we should put the plain text password through a one-way algorithm that changes it in a way we cannot undo.
    When the user provides their password, we put it through the same algorithm.
    If the result matches the hashed value we stored, then the starting point must have been the same.
    The passwords are matched, and the user has proven their identity.

.. ifslides::

    Our password is stored in plain text

    .. rst-class:: build
    .. container::

        If someone breaks in to our server, they can read it

        **NEVER STORE PLAIN TEXT PASSWORDS IN ANY LOCATION EVER**

        Passwords should always be stored in a hashed form

        Hash provided credentials in the same way

        Compare the results

        If the hashes match, the provided credentials were the same as the original

.. nextslide:: Hashing Libraries

.. ifnotslides::

    There are a number of libraries in Python that can help us solve this problem.
    I recommend one called ``passlib``.
    It provides a clear, uncomplicated API both for hashing a plain-text password and verifying a plain-text password against the hashed version.
    The library uses a single object called a *context* to implement this API.
    The context can be configured to use any of a number of different hashing algorithms.
    It can even be configured to transition from one algorithm to another over time.
    It is quite sophisticated.

    Let's create a context for our app to use, as instructed by the `passlib quickstart documentation <https://pythonhosted.org/passlib/new_app_quickstart.html>`_:

.. ifslides::

    Use one of the many Python libraries to help with this

    .. rst-class:: build
    .. container::

        **Do not** implement hashing on your own

        I recommend ``passlib``

        It provides a *password context* which has a clean API

        Make one context for your app, use it wherever you need it

.. rst-class:: build
.. code-block:: python

    # in security.py

    from passlib.apps import custom_app_context as pwd_context

.. nextslide:: Using ``pwd_context``

.. ifnotslides::

    This `pwd_context` object provides two useful methods.
    The ``encrypt`` method returns a hashed version of the provided password.
    The ``verify`` method takes a plain-text password and a hash and comparies them.

    We can store a hashed version of our password in the environment:

.. ifslides::

    Use ``pwd_context.encrypt`` to hash an original password

    Use ``pwd_context.verify`` to compare a plain-text password with the hash

.. rst-class:: build
.. code-block:: python

    os.environ['AUTH_PASSWORD'] = pwd_context.encrypt('secret password')

.. ifnotslides::

    And we can verify the encrypted result against provided password:

.. rst-class:: build
.. code-block:: python

    hashed = os.environ.get('AUTH_PASSWORD', '')
    verify('secret password', hashed) #<-- returns True

    verify('not my password', hashed) #<-- returns False

.. nextslide:: Update ``check_credentials``

.. ifnotslides::

    If we make the assumption that the password stored in our OS environment is encrypted,
    we can write a more secure version of our ``check_credentials`` function.

    Add the following to our ``security.py`` file:

.. ifslides::

    Use this new tool to implement a more secure ``check_credentials``:

.. code-block:: python

    # in security.py

    from passlib.apps import custom_app_context as pwd_context

    def check_credentials(username, password):
        stored_username = os.environ.get('AUTH_USERNAME', '')
        stored_password = os.environ.get('AUTH_PASSWORD', '')
        is_authenticated = False
        if stored_username and stored_password:
            if username == stored_username:
                try:
                    is_authenticated = pwd_context.verify(password, stored_password)
                except ValueError:
                    # ValueError is raised if the stored password is not hashed
                    pass
        return is_authenticated

.. nextslide:: Wire It Up

.. ifnotslides::

    Remember, because we've now written code that depends on the ``passlib`` library,
    we must add that library to our list of dependencies in ``setup.py``:

.. ifslides::

    Don't forget to add ``passlib`` to our app dependencies in ``setup.py`` (and re-install):

.. code-block:: python

    requires = [
        'pyramid',
        'pyramid_jinja2',
        'pyramid_debugtoolbar',
        'pyramid_tm',
        'SQLAlchemy',
        'transaction',
        'zope.sqlalchemy',
        'waitress',
        'passlib', #<-- add this line
    ]

.. ifnotslides::

    Then re-install your application to pick up the new dependency


Logging In
----------

.. ifnotslides::

    Remember the four steps we outlined back at the beginning of our discussion:

* accept a username and password as arguments
* raise an appropriate error if either is missing
* raise an appropriate error if they cannot be confirmed to be correct
* persist the fact that the user is authenticated

.. ifnotslides::

    We now have a way to do the first three, but we must write a *view* to allow a visitor to our site to access this functionality.
    We can then accomplish the last step, by adding an appropriate cookie to the response we send back.
    Then, each time that visitor requests a page, the fact that they have authenticated will be remembered.
    And we'll be able to allow the visitor access to restricted pages.

.. ifslides::

    .. rst-class:: build
    .. container::

        We can accomplish the first three.

        But we need a *view* to allow visitors to access this

        We can create a cookie using our authentication policy and send it back

        Subsequent requests will have that cookie

        We can know who the authenticated user is

        We can grant appropriate permissions with our ACL

.. nextslide:: Login View

.. ifnotslides::

    Let's add this view to our views file:

.. code-block:: python

    # in views/default.py

    from pyramid.httpexceptions import HTTPFound
    from pyramid.security import remember, forget
    from test_transactions.security import check_credentials

    @view_config(route_name='login', renderer='templates/login.jinja2')
    def login(request):
        if request.method == 'POST':
            username = request.params.get('username', '')
            password = request.params.get('password', '')
            if check_credentials(username, password):
                headers = remember(request, username)
                return HTTPFound(location=request.route_url('home'), headers=headers)
        return {}

.. nextslide:: Login Template

.. ifnotslides::

    We can also create a simple template to serve as our login form:

.. code-block:: jinja

    <!-- templates/login.jinja2 -->

    <h2>Login</h2>
    <form action="" method="POST">
    <div class="field">
        <label for="username">Username</label>
        <input type="text" name="username" id="username"/>
    </div>
    <div class="field">
        <label for="password">Password</label>
        <input type="password" name="password" id="password"/>
    </div>
    <div class="control_row">
        <input type="submit" name="Login" value="Login"/>
    </div>
    </form>

.. nextslide:: How It Works

.. ifnotslides::

    Our login view is a typical form-handling view.
    If the request method is not "POST", then no form handling is performed, and the form template is rendered with an empty context.
    But if the request method *is* "POST", the username and password provided by the visitor are read.
    The values are verified using our ``check_credentials`` function.

    If the credentials the visitor provided check out,
    then we can use the ``remember`` function from the ``pyramid.security`` module.
    This function uses the authorization policy we have configured to create headers to set an ``auth_tkt`` cookie to send back to the visitor.
    We can then redirect the visitor to the home page, adding these headers to the response.
    Subsequent requests from this visitor will include this cookie, and our application will be aware that this visitor is authenticated.

    Once this is done, then ``request.authenticated_userid`` will return the username we passed to the ``remember`` function.
    We can use this to perform checks in page templates.
    We can show or hide HTML elements based on whether there is an authenticated user.

.. ifslides::

    ``login`` is a typical form-handling view.

    .. rst-class:: build
    .. container::

        On GET requests, the template is rendered with an empty context

        On POST requests, the *username* and *password* are verified with ``check_credentials``

        If they are correct, use ``pyramid.security.remember`` to create ``auth_tkt`` headers

        Redirect to home page with these headers

        Cookie is set in Browser, following requests will include it

        Now, request.authenticated_userid returns the username

        Use this to show/hide UI elements

Logging Out
-----------

.. ifnotslides::

    We should also provide a mechanism for de-authenticating ourselves.
    If we don't then a visitor to our site using a public computer might leave behind a browser with access to the site.

    To log out, we need to implement a view that removes the cookie that is used to persist our authentication information.
    Once this cookie is gone, then subsequent requests to the site will no longer contain information needed to prove authenication.
    Requests for views that require permissions will again cause ``403 Forbidden`` errors.

.. ifslides::

    We want to be able to de-authenticate

    Implement a view that will remove the cookie

    Use ``pyramid.security.forget`` to unset the ``auth_tkt`` cookie headers

    No renderer is required:

.. rst-class:: build
.. code-block:: python

    # in views/default.py

    @view_config(route_name='logout')
    def logout(request):
        headers = forget(request)
        return HTTPFound(request.route_url('home'), headers=headers)

.. ifnotslides::

    Notice that we need not provide any renderer for this view.
    It will never return a response that can be viewed by a visitor.

.. nextslide:: Wire It Up

Finally, to make this all work properly, we have to add routes for our login and logout views.

.. code-block:: python

    # in routes.py

    def includeme(config):
        # ...
        config.add_route('login', '/login')
        config.add_route('logout', '/logout')

Wrap-Up
=======

.. ifnotslides::

    In this lecture, we've learned a bit about security in Pyramid apps.
    We've learned that we can represent identity using *principals*.
    We've configured an application to use security by adding AuthN and AuthZ *policies*.
    We've seen that we can control access to views by configuring them to require *permissions*.
    And we've seen how we can grant or deny permissions to principals using ACLs, which are found on *root objects*.

    We've seen how we can store authentication information for a single user in our OS environment.
    We've learned how to use a Python library to hash and verify our user's password.
    And we've written the views needed to allow our user to log in and out of our application.

    That should be about enough for now.

.. ifslides::

    Pyramid apps can use AuthN and AuthZ

    .. rst-class:: build
    .. container::

        Identify users, groups, roles with *principals*

        Determine how to handle AuthN and AuthZ with *policies*

        Control access to views by requiring *permissions*

        Grant permissions to principals using ACLs on *root objects*

        Store identities (in ``os.environ`` or a database)

        **Only store hashed passwords**

        Use login/logout views to authenticate and de-authenticate
