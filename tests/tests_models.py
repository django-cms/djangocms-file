# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO

from filer.models import File as FilerFile
from filer.models import Folder as FilerFolder

from djangocms_file.models import File


class FileTestCase(TestCase):

    def setUp(self):
        filer_file = FilerFile.objects.create(
            file='test.jpg',
        )
        File.objects.create(
            file_src=filer_file,
            file_name='test',
        )

    def test_file_instance(self):
        """File instance has been created"""
        test_file = File.objects.get(file_name='test')
        self.assertEqual(test_file.file_name, 'test')


class FolderTestCase(TestCase):

    def setUp(self):
        FilerFolder.objects.create(
            name='test',
        )

    def test_folder_instance(self):
        """Folder instance has been created"""
        test_folder = FilerFolder.objects.get(name='test')
        self.assertEqual(test_folder.name, 'test')


class MigrationTestCase(TestCase):

    def test_makemigrations(self):
        """Fail if there are schema changes with no migrations."""
        app_name = 'djangocms_file'
        out = StringIO()
        call_command('makemigrations', dry_run=True, no_input=True, stdout=out)
        output = out.getvalue()
        self.assertNotIn(app_name, output, (
            '`makemigrations` thinks there are schema changes without'
            ' migrations.'
        ))
