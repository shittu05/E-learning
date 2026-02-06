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


class VideoEvent(models.Model):
    EVENT_TYPES = [
        ('play', 'Play'),
        ('pause', 'Pause'),
        ('ended', 'Ended'),
        ('watch_duration', 'Watch Duration'),
        ('rewatch', 'Rewatch'),
        ('seek_forward', 'Seek Forward'),
        ('playback_speed', 'Playback Speed'),
    ]
    
    video_id = models.CharField(max_length=255)  # ID of the video
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)  # Event type
    timestamp = models.DateTimeField(auto_now_add=True)  # When the event occurred
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Track the user
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)  # Link to the course
    course_title = models.CharField(max_length=255, null=True, blank=True)  # Course title
    video_timestamp = models.FloatField(null=True, blank=True)  # Position in video (seconds)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', 'video_id', '-timestamp']),
            models.Index(fields=['event_type', '-timestamp']),
        ]
    

    def __str__(self):
        return f"{self.event_type} event for video {self.video_id} in course {self.course_title}"


class Submission(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.JSONField()  # Store answers as JSON
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user} for {self.title}"