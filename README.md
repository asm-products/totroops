
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

$ git clone git@github.com:phillyc/totroops.git

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

Replace <user> <password> and <database> variables with credentials for your local database.

Python comes preinstalled on Macs these days. From the command line you can type "python" to open a shell and verify what version you are running. ToTroops is built on 2.7.5.

More info on Python here: https://www.python.org/about/

The next thing you'll need once you've cloned the repo is a virtualenv. This is just like RVM in Ruby. Python has packages (eggs) just like Ruby (gems). Once you "source .virtualenvs/totroopsenv/bin/activate" you're inside the environment. From here you can list, install, update, or uninstall packages without harming other Python apps you may be working on. In Ruby "gem" is the command used to manage gems, in Python it's "pip". So "pip list" will show you the packages you have inside your virtualenv. You'll need to run "pip install -r requirements.txt". This tells pip to install all of the requirements listed in the requirements.txt file. One of these includes Django.

http://virtualenv.readthedocs.org/en/latest/virtualenv.html

After that's setup, you should be able to run "python manage.py runserver" from the project directory to start the server locally:

Django version 1.6.6, using settings 'totroops.settings'

Starting development server at http://127.0.0.1:5000/

Quit the server with CONTROL-C.

Now we're running our app on the command line!
