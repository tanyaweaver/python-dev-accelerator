******************************************
Deploying a Simple WSGI Application on AWS
******************************************

Let's walk through manually deploying a simple WSGI application to an AWS EC2
instance we've created.


Setup
=====

.. code-block:: bash

    $ python3 -m venv wsgiapp
    $ cd wsgiapp
    $ . bin/activate
    (wsgiapp)$

In the new ``wsgiapp`` directory, create a very simple WSGI application. Start by
creating a new file ``myapp.py`` and opening it in your editor. In the file,
type the following Python code:

.. code-block:: python

    # -*- coding: utf-8 -*-
    def app(environ, start_response):
        data = "Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    if __name__ == '__main__':
        from wsgiref.simple_server import make_server
        srv = make_server('localhost', 8080, app)
        srv.serve_forever()

Test your application to be sure it works by running it from the command line:

.. code-block:: bash

    (wsgiapp)$ python myapp.py

Point your web browser at http://localhost:8080/ and verify that you can see "Hello World!" printed.

Next, provision a new EC2 instance on AWS using the through-the web provisioner.
Make sure you are using an Ubuntu image, either version 12.04 or 14.04.

Next, use the shell command ``scp`` to securely copy your wsgi application to the new server instance.
You'll need to update the path to your private key file and the public DNS name of your EC2 instance from the values shown here.

.. code-block:: bash

    (wsgiapp)$ scp -i ~/.ssh/pk-cpe.pem myapp.py ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com:~/
    ...
    Are you sure you want to continue connecting (yes/no)? yes
    ...
    myapp.py                                      100%  381     0.4KB/s   00:00
    (wsgiapp)$


Manual Configuration
====================

We are going to do this manually once together.
Later, you'll have a chance to repeat the process using a configuration management tool.

Configure Nginx
---------------

The first step is to configure ``nginx`` to proxy HTTP requests to our simple application.

If you know, or are more comfortable with the ``Apache`` webserver, you can also use that.
However, the trend I've seen over the last few years is toward the use of ``nginx`` over the old stand-by.

Nginx stores site configuration on Ubuntu in the ``/etc/nginx/sites-available`` directory.
This is in fact a pattern you'll get used to.
On most Linux machines, configuration of individual applications can be found in the ``/etc`` directory.

Let's shell into our new instance and look at what's there:

.. code-block:: bash

    (wsgiapp)$ ssh -i ~/.ssh/pk-cpe.pem ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com
    Welcome to Ubuntu 12.04.4 LTS (GNU/Linux 3.2.0-58-virtual x86_64)
    ...
    Last login: Wed Feb 26 19:10:01 2014 from 199.231.242.170
    ubuntu@ip-10-254-159-140:~$ ls /etc/nginx/sites-available/
    default
    ubuntu@ip-10-254-159-140:~$ more /etc/nginx/sites-available/default
    # You may add here your
    # server {
    #   ...
    # }
    # statements for each of your virtual hosts to this file
    ...

    ubuntu@ip-10-254-159-140:~$

The ``sites-available`` directory will hold individual site configuration for **all** sites that **might** be available on a server.

**Active** site configuration is listed in the ``/etc/nginx/sites-enabled``:

.. code-block:: bash

    ubuntu@ip-10-254-159-140:~$ ls /etc/nginx/sites-enabled/
    default
    ubuntu@ip-10-254-159-140:~$ ls -l /etc/nginx/sites-enabled/
    total 0
    lrwxrwxrwx 1 root root 34 Feb 26 19:09 default -> /etc/nginx/sites-available/default
    ubuntu@ip-10-254-159-140:~$

Notice that in fact, although ``default`` is in that directory too,
it's actually a soft link to the file in ``sites-available``.

Let's move aside the existing ``default`` config and replace it with a simple one of our own.

On your local machine, in the ``wsgiapp`` directory, make a new file ``simple_nginx_config``.
Open that file in your editor and add the following:

.. code-block:: nginx

    server {
        listen 80;
        server_name ec2-54-184-162-20.us-west-2.compute.amazonaws.com;
        access_log  /var/log/nginx/test.log;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

Remember, you want to use the name of your actual server on aws, not the example used above.

Now, copy that file up to your server too:

.. code-block:: bash

    (wsgiapp)$ scp -i ~/.ssh/pk-cpe.pem simple_nginx_config ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com:~/
    simple_nginx_config                           100%  363     0.4KB/s   00:00
    (wsgiapp)$

Next, on the server, move the original default configuration file aside and put your new one in its place:

.. code-block:: bash

    ubuntu@ip-10-254-159-140:~$ ls
    myapp.py  simple_nginx_config
    ubuntu@ip-10-254-159-140:~$ sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.orig
    ubuntu@ip-10-254-159-140:~$ sudo mv simple_nginx_config /etc/nginx/sites-available/default
    ubuntu@ip-10-254-159-140:~$ ls -l /etc/nginx/sites-enabled/
    total 0
    lrwxrwxrwx 1 root root 34 Feb 26 19:09 default -> /etc/nginx/sites-available/default
    ubuntu@ip-10-254-159-140:~$

Once that's complete, you can restart nginx to have it pick up your changes:

.. code-block:: bash

    ubuntu@ip-10-254-159-140:~$ sudo service nginx restart
    ...
    ubuntu@ip-10-254-159-140:~$

If you now try to load the public DNS name for your EC2 instance, you'll see that nginx has updated and is now throwing an error::

    http://ec2-54-184-162-20.us-west-2.compute.amazonaws.com

This should tell you **Bad Gateway**.
That's the error that means "I am a proxy, but the thing I'm proxying to is not running!"

Running a WSGI Server
---------------------

Let's make our wsgi app run, so we can fix that.

On your server, run the wsgi app:

.. code-block:: bash

    ubuntu@ip-10-254-159-140:~$ python myapp.py

And now reload your web browser and verify that you can see "Hello, World!"


Automation
==========

The steps we took there allowed us to upload an application and some configuration to our server,
apply the configuration to the ``nginx`` web server we installed,
and then run our WSGI application in a terminal to get a response via public DNS.

Your task is to repeat this process for homework.
Later, we'll learn how to automate this task using configuration management tools.
