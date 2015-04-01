django-ortb
===========

django app to help with mapping of openrtb object-attribute names to short 2 character codes for use in url params

instructions
============

Initial setup

    $ ./manage.py migrate
    $ ./manage.py shell
    >>> import django
    >>> django.setup()
    >>> from loaddb import load_all
    >>> load_all()
    >>> ^D
    $ ./manage.py runserver
