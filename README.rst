===============
django CMS File
===============

|pypi| |build| |coverage| |python| |django| |djangocms|

**django CMS File** is a set of plugins for `django CMS <http://django-cms.org>`_
that allow you to add files to your site You can either choose a single file or
an entire folder.

It uses files managed by `Django Filer <https://github.com/divio/django-filer>`_.

This addon is compatible with `Divio Cloud <http://divio.com>`_
for easy installation.

.. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

We're grateful to all contributors who have helped create and maintain this package.
Contributors are listed at the `contributors <https://github.com/divio/djangocms-file/graphs/contributors>`_
section.

One of the easiest contributions you can make is helping to translate this addon on
`Transifex <https://www.transifex.com/projects/p/djangocms-file/>`_.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-file/blob/master/setup.py>`_
file for additional dependencies:

* Django Filer 1.7 or higher

Make sure `django-filer <http://django-filer.readthedocs.io/en/latest/installation.html>`_
is installed and configured appropriately.


Installation
------------

For a manual install:

* run ``pip install djangocms-file``
* add ``djangocms_file`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_file``


Configuration
-------------

Note that the provided templates are very minimal by design. You are encouraged
to adapt and override them to your project's requirements.

This addon provides a ``default`` template for all instances. You can provide
additional template choices by adding a ``DJANGOCMS_FILE_TEMPLATES``
setting::

    DJANGOCMS_FILE_TEMPLATES = [
        ('feature', _('Featured Version')),
    ]

You'll need to create the ``feature`` folder inside ``templates/djangocms_file/``
otherwise you will get a *template does not exist* error. You can do this by
copying the ``default`` folder inside that directory and renaming it to
``feature``.


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r test_requirements/base.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/djangocms-file.svg
    :target: http://badge.fury.io/py/djangocms-file
.. |build| image:: https://travis-ci.org/django-cms/djangocms-file.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-file
.. |coverage| image:: https://codecov.io/gh/django-cms/djangocms-file/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-file

.. |python| image:: https://img.shields.io/badge/python-3.5+-blue.svg
    :target: https://pypi.org/project/djangocms-file/
.. |django| image:: https://img.shields.io/badge/django-2.2--4.0-blue.svg
    :target: https://www.djangoproject.com/
.. |djangocms| image:: https://img.shields.io/badge/django%20CMS-3.7%2B-blue.svg
    :target: https://www.django-cms.org/


Updating from `cmsplugin-filer <https://github.com/django-cms/cmsplugin-filer>`_
--------------------------------------------------------------------------------

`cmsplugin-filer` was used a few times ago to create file, folder, image, link, teaser & video plugins on your DjangoCMS projects. Now the project is archived, and you might be wondering how to migrate your old instances without having to copy them manually to the new `djangocms-<file|picture|link|...>` plugins.

Don't be afraid, we have you covered! Here's a management command that you can use to get started with this tasks:

`migrate_cmsplugin_filer.py <https://gist.github.com/corentinbettiol/84a6ea7e4d047fc01861b0af15fd60f0>`_

This management command is only a starting point. It *may* work out of the box for some people, but we encourage you to read the code, understand what it does, and try it on a development environment before running it on your production server. The management command is only configured to transfer your `cmsplugin_link`, `cmsplugin_file`, `cmsplugin_folder` and `cmsplugin_image` plugins to modern `djangocms_*` plugins. If you need to transfer other `cmsplugin_*` plugins, you'll have to write your own code.
