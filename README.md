Trail
=========

A Python module for triggering monkey patching of a Python application,
without the need to actually modify the Python application itself to
setup the monkey patches.

To test it out, run the wrapper script with Python:

    trail python

At the Python interpreter prompt then enter:

    import this

This should print out the Zen of Python as normal, but with an extra line
added to the end.

Credits
======
This module is based upon Graham Dumpleton's [autowrapt](https://github.com/GrahamDumpleton/autowrapt/).