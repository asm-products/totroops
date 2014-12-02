
=======
totroops
========

Care packages for service members!

Full description and breakdown @
https://assembly.com/totroops


===
Contributing to the codebase
===
Please start by cloning the repository to your local machine.

    git clone git@github.com:phillyc/totroops.git

Then, to work on a bounty, just checkout a new branch from master. Once you've completed the work, post a pull request to merge your code back into master. I'll review it and either provide feedback or accept the pull request and award the bounty.

===
Development Setup
===

You'll have to add a file, totroops/local_settings.py

This will point your local install at your local postgres database.

    # Settings for local host.
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(default='postgres://<user>:<password>@localhost/<database>')
    }

    DEBUG = True

Replace <user> <password> and <database> variables with credentials for your local database.

Python comes preinstalled on Macs these days. From the command line you can type "python" to open a shell and verify what version you are running. ToTroops is built on 2.7.5.

More info on Python here: https://www.python.org/about/

The next thing you'll need once you've cloned the repo is a virtualenv. This is just like RVM in Ruby. Python has packages (eggs) just like Ruby (gems). Once you "source .virtualenvs/totroopsenv/bin/activate" you're inside the environment. From here you can list, install, update, or uninstall packages without harming other Python apps you may be working on. In Ruby "gem" is the command used to manage gems, in Python it's "pip". So "pip list" will show you the packages you have inside your virtualenv.

You'll need to run: 

    pip install -r requirements.txt 

This tells pip to install all of the requirements listed in the requirements.txt file. One of these includes Django.

http://virtualenv.readthedocs.org/en/latest/virtualenv.html

After that's setup, you should be able to run "python manage.py runserver" from the project directory to start the server locally:

Django version 1.6.6, using settings 'totroops.settings'

Starting development server at http://127.0.0.1:5000/

Quit the server with CONTROL-C.

Now we're running our app on the command line!

=== 
Development Tools
===

There are two main ways to get more info out of Django while running locally.

The first is [ipdb](https://pypi.python.org/pypi/ipdb) which is an extension of Python Debugger, aka pdb. This is already part of the requirements.txt file, so once you're setup, you should have access to it. The quick way to use it is place "import ipdb; ipdb.set_trace()" somewhere in your python code. Once the server tries to execute that line it will drop you into a console shell where you can inspect variables, manipulate the stack, look around, etc.

The second tool is Python's logger. Use it like you would use print statements. First, make sure it's setup in the .py file you're working on:

    import logging
    logger = logging.getLogger('testlogger')

Then, when you want to get some output in the console, format it like this:

    logger.info("A simple message.")

You can select different levels of messages like so:

    logger.warning("Something funny happened")
    logger.error("This is a more serious problem")

Finally, you can include variables using Python's string methods:

    logger.info("User %s just signed up" % user)

The advantage of logging versus ipdb is that once you're done coding, all you have to do is change;

    logger = logging.getLogger('testlogger')

to;

    logger = logging.getLogger('console')

and Heroku will start tracking these logs. This is very very nice for future production debugging. Remember, a noisy app makes developers happy!
