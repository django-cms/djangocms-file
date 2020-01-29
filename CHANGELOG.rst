=========
Changelog
=========


2.3.1 (unreleased)
==================

* Added support for Django 3.0
* Added further tests to raise coverage
* Fixed smaller issues found during testing


2.3.0 (2019-04-30)
==================

* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Added isort and adapted imports
* Adapted code base to align with other supported addons


2.2.0 (2018-12-12)
==================

* Fixed test matrix
* Exclude ``tests`` folder from release build
* Added missing migrations for Django 2.1
* Added abstract models for ``File`` and ``Folder``
* Improved readability of ``Folder.get_files``


2.1.0 (2018-11-13)
==================

* Removed support for Django 1.8, 1.9, 1.10


2.0.3 (2018-11-05)
==================

* Add support for Django 1.10, 1.11, 2.0 and 2.1
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.5 and 4.0


2.0.2 (2016-11-22)
==================

* Prevent changes to ``DJANGOCMS_FILE_XXX`` settings from requiring new
  migrations
* Changed naming of ``Aldryn`` to ``Divio Cloud``
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.4 and dropped 3.2
* Updated translations


2.0.1 (2016-20-09)
==================

* Fixes an issue where images throw an ``AttributeError``


2.0.0 (2016-13-09)
==================

* Added tests
* Cleaned up file structure
* Removed Django < 1.8 support
* Adapted ``README.txt``
* Added translations


1.0.0 (2016-03-04)
==================

* Use this version for Django < 1.8 support
