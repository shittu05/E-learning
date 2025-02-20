from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Course
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .filters import CourseFilter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoEvent
import json

# Create your views here.





def courses(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to access the course content!')
        return redirect('login')

    courses = Course.objects.all()
    myFilter = CourseFilter(request.GET, queryset=courses)
    filtered_courses = myFilter.qs  # Apply search filter

    # Pagination
    paginator = Paginator(filtered_courses, 12)  # Show 6 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'courses': page_obj,  
        'myFilter': myFilter,
        'paginator': paginator,  
        'page_obj': page_obj,  
    }

    return render(request, 'courses.html', context)


def course_detail(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'content.html', {'item': course})





@csrf_exempt
def track_video_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_id = data.get('video_id')
        event_type = data.get('event_type')
        timestamp = data.get('timestamp')
        course_title = data.get('course_title')  # Get the course title
        course_id = data.get('course_id')  # Assuming you are also sending course_id

        # Optionally, get the user from the request if authenticated
        user = request.user if request.user.is_authenticated else None

        # Optionally, you can get the course object if you need to store it (useful for the foreign key)
        course = Course.objects.get(id=course_id) if course_id else None

        # Create and save the video event
        video_event = VideoEvent.objects.create(
            user=user,
            video_id=video_id,
            event_type=event_type,
            timestamp=timestamp,
            course_title=course_title,  # Store the course title in the event
            course=course  # Link to the Course model if needed
        )

        return JsonResponse({'message': 'Video event tracked successfully'})