===============
 django-grains
===============

This reusable Django app lets you
store snippets of text ("grains") in the database
keyed by arbitrary strings.
It's the same idea implemented previously 
in django-chunks_, django-flatblocks_, django-tinycontent_
and others_.

Usage
=====

Install with ``pip install django-grains``.

Add ``grains`` to ``INSTALLED_APPS`` in your project's Django settings.

Run ``manage.py syncdb`` or ``manage.py migrate`` (if you're using South)
to create the database tables.

In your templates, create placeholders for grains::

    {% load grains_tags %}

    {% grain "front-page-title" %}The default title of the front page{% endgrain %}

    {% grain "front-page-subtitle" "text/plain" %}The default subtitle of the front page{% endgrain %}

    {% grain "front-page-content" "text/html" %}
        <p>This is the default HTML content of the front page.</p>
    {% endgrain %}

The first argument to ``{% grain %}`` is the unique identifier of the grain.
The second argument is the content type
which could be used to choose the editor widget for the value
in Django's admin interface.
The second argument can be omitted in which case it defaults to ``text/plain``.

A WYSIWYG editor is automatically used in the admin interface
for grains with the ``text/html`` content type,
if you have django-wysiwyg_ installed and added to ``INSTALLED_APPS``.

.. _django-chunks: https://github.com/clintecker/django-chunks
.. _django-flatblocks: https://github.com/zerok/django-flatblocks
.. _django-tinycontent: https://github.com/dominicrodger/django-tinycontent
.. _others: https://www.djangopackages.com/grids/g/layout/
.. _django-wysiwyg: https://github.com/pydanny/django-wysiwyg
