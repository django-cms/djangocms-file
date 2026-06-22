#!/usr/bin/env python
from setuptools import find_packages, setup

from djangocms_file import __version__


REQUIREMENTS = [
    'django-cms>=5.0',
    'django-filer>=3.0',
    'djangocms-attributes-field>=1',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.14',
    'Framework :: Django',
    'Framework :: Django :: 5.2',
    'Framework :: Django :: 6.0',
    'Framework :: Django CMS',
    'Framework :: Django CMS :: 5.0',
    'Framework :: Django CMS :: 5.1',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='djangocms-file',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.ch',
    maintainer='Django CMS Association and contributors',
    maintainer_email='info@django-cms.org',
    url='https://github.com/django-cms/djangocms-file',
    license='BSD-3-Clause',
    description='Adds file plugin to django CMS',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
