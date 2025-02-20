from django.db import models
# from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.conf import settings
import csv

User = settings.AUTH_USER_MODEL




class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    # content = CKEditor5Field('Content', config_name='default')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class VideoEvent(models.Model):  # Use EasyAudit instead of AuditModel
    video_id = models.CharField(max_length=255)  # ID of the video
    event_type = models.CharField(max_length=50)  # 'play', 'pause', 'ended'
    timestamp = models.DateTimeField(auto_now_add=True)  # When the event occurred
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optionally track the user
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)  # Link to the course
    course_title = models.CharField(max_length=255, null=True, blank=True)  # Store the course title in the event



    def __str__(self):
        return f"{self.event_type} event for video {self.video_id} in course {self.course_title}"
