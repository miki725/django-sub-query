===============================
Django SubQuery
===============================

.. image:: https://badge.fury.io/py/django-sub-query.png
    :target: http://badge.fury.io/py/django-sub-query

.. image:: https://travis-ci.org/miki725/django-sub-query.png?branch=master
	:target: https://travis-ci.org/miki725/django-sub-query

Django app which uses SQL sub-queries to solve some ORM limitations

* Free software: MIT license
* GitHub: https://github.com/miki725/django-sub-query
* Documentation: https://django-sub-query.readthedocs.org.

Installing
----------

You can install ``django-sub-query`` using pip::

    $ pip install django-sub-query

Testing
-------

To run the tests you need to install testing requirements first::

    $ make install

Then to run tests, you can use ``nosetests`` or simply use Makefile command::

    $ nosetests -sv
    # or
    $ make test
