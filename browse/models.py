from __future__ import unicode_literals

from django.db import models

class BaseDirectory(models.Model):
    dir_path = models.CharField(max_length=1024)

class FileRecord(models.Model):
    basedir = models.ForeignKey(BaseDirectory, on_delete=models.CASCADE)
    file_path = models.TextField()
    mime_type = models.CharField(max_length=1024)
    date_modified = models.DateTimeField('date modified')

