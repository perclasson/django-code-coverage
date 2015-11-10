Trail
=========

A Python module for triggering monkey patching of a Python application,
without the need to actually modify the Python application itself to
setup the monkey patches.

To test it out, run the wrapper script with Python:

    trail python

Goals
=====

Using Django 1.5, this package should be able to identify unused:

- template tags
- template filters
- views
- urls

Investigation
=============

- Is it possible to find unused blocks in templates (e.g. block extra_wapper in the Jacksons project)?
- Use something like Paranoid Django templates to find unsued context variables, http://excess.org/article/2012/04/paranoid-django-templates/
- To get all urlpatterns, use show_urls https://github.com/django-extensions/django-extensions/blob/master/django_extensions/management/commands/show_urls.py

How much better is coverage
===========================
Test and compare with coverage run:

    coverage run ./manage.py runserver --noreload

Comparsion with static analysis
===============================

- This tool will work "almost" like coverage but specifically made for Django. Can we also make a tool like vulture for Django? On example of such work is: https://github.com/AMeng/django-unused-templates
- There is also already pylint with django: https://blog.landscape.io/using-pylint-on-django-projects-with-pylint-django.html
- Can also look at prospector: pip install prospector

Credits
======
This module is based partially on Graham Dumpleton's [autowrapt](https://github.com/GrahamDumpleton/autowrapt/).