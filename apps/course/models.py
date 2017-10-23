from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re
import md5
import os, binascii

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description must be at least 15 characters"
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    