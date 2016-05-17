from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class SharedModel(models.Model):
    name = models.CharField(max_length=255)
    related_obj = models.ForeignKey('shared_app.RelatedModel')
    tags = TaggableManager()


class ToBeDeletedModel(models.Model):
    name = models.CharField(max_length=255)
    related_obj = models.ForeignKey('shared_app.RelatedModel')
    tags = TaggableManager()


class RelatedModel(models.Model):
    name = models.CharField(max_length=255)
