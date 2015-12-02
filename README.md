djangocms-file
==============

A file plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-file``.
* Add ``'djangocms_file'`` to your ``INSTALLED_APPS`` setting.
* If using Django 1.6 and South < 1.0.2 add ``'djangocms_file': 'djangocms_file.south_migrations',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it
  does not exists);
* Run ``manage.py migrate djangocms_file``.


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-file/

