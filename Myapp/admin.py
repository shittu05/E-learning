from django.contrib import admin
from .models import Course, VideoEvent
from easyaudit.models import RequestEvent
from easyaudit.admin import RequestEventAdmin
import csv
from django.http import HttpResponse

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):  
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_per_page = 30 # Increase pagination for better usability

# Unregister the default RequestEventAdmin from EasyAudit
admin.site.unregister(RequestEvent)

# Re-register RequestEvent with Django's ModelAdmin
@admin.register(RequestEvent)
class CustomRequestEventAdmin(RequestEventAdmin, admin.ModelAdmin):  
    search_fields = ('user__email',)  
    list_per_page = 30  
   

# ✅ Register VideoEvent with Django's ModelAdmin
@admin.register(VideoEvent)
class VideoEventAdmin(admin.ModelAdmin):  
    list_display = ('course', 'user', 'event_type', 'timestamp')  # Use 'course' directly
    search_fields = ('event_type', 'course__title', 'user__email')  # Fix course lookup
    list_filter = ('event_type', 'course')
    list_per_page = 10  

    readonly_fields = ('video_id', 'event_type', 'timestamp', 'course', 'user')


    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        """Export selected VideoEvent entries as a CSV file"""
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="video_events.csv"'

        writer = csv.writer(response)
        writer.writerow(["User", "Course Title", "Video ID", "Event Type", "Timestamp"])

        for event in queryset:
            writer.writerow([
                event.user.email if event.user else "Anonymous",
                event.course_title if event.course_title else "N/A",
                event.video_id,
                event.event_type,
                event.timestamp
            ])

        return response

    export_as_csv.short_description = "Export Selected Video Events to CSV"
