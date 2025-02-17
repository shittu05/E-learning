from django.shortcuts import render, redirect

from .models import Course
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .filters import CourseFilter


# Create your views here.


def courses(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to access the course content!')
        return redirect('login')
    else:
        messages.success(request, f'Welcome {request.user}')

    courses = Course.objects.all()
    myFilter = CourseFilter(request.GET, queryset=courses)
    courses = myFilter.qs
    if request.htmx:
        return render(request, 'partial.html', {'courses': courses, 'myFilter': myFilter})
    return render(request, 'courses.html', {'courses': courses, 'myFilter': myFilter})

def course_detail(request, slug):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to access the course content!')
        return redirect('login')
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'content.html', {'item': course})

