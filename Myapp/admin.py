from django.contrib import admin
from .models import Course
from unfold.admin import ModelAdmin

from unfold.contrib.filters.admin import RangeDateFilter, RangeDateTimeFilter

from easyaudit.models import RequestEvent
from easyaudit.admin import RequestEventAdmin

# Register your models here.

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('title',  'created_at', 'updated_at')




  # Import the existing admin

# ✅ Unregister the default RequestEventAdmin
admin.site.unregister(RequestEvent)

# ✅ Re-register with the corrected admin configuration
@admin.register(RequestEvent)
class CustomRequestEventAdmin(RequestEventAdmin, ModelAdmin):
    search_fields = ('user__email',)  # Fix the username issue
    list_filter_submit = True  # Enable submit button for filters
    
    # Preserve existing filters while adding Unfold filters
    list_filter = RequestEventAdmin.list_filter + [
        ("datetime", RangeDateFilter),  # Date filter
        ("datetime", RangeDateTimeFilter),  # Datetime filter
    ]