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

- templates
- template tags
- template filters
- views
- urls

Credits
======
This module is based partially on Graham Dumpleton's [autowrapt](https://github.com/GrahamDumpleton/autowrapt/).