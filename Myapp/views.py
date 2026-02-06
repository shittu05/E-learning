from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Course, Submission
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .filters import CourseFilter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoEvent
import json
from django.contrib.auth.decorators import login_required

# Create your views here.



def courses(request):
    return render(request, 'pre-directions.html')

def video(request):
    return render(request, 'video.html')

@login_required
def survey(request):
    if request.method == 'POST':
        title = 'Survey One'
        user = request.user
        answers = {
            'survey1': request.POST.get('survey1'),

        }
        existing_submission = Submission.objects.filter(user=user, title=title).first()
        if existing_submission:
            messages.error(request, 'You have already submitted this survey.')
            return redirect('learning')
        submission = Submission.objects.create(
            title=title,
            user=user,
            answers=answers
        )
        messages.success(request, 'Survey submitted successfully!')
        return redirect('learning')
    else:
        messages.error(request, 'Please fill in all fields.')
        return render(request, 'survey.html')
    return render(request, 'survey.html')


def learning(request):
    return render(request, 'learning.html')

def concept_map(request):
    return render(request, 'concept-map.html')

def concept_map_two(request):
    return render(request, 'concept-map2.html')

def concept_map_three(request):
    return render(request, 'concept-map3.html')

def concept_map_four(request):
    return render(request, 'concept-map4.html')

@login_required
def video_one(request):
    return render(request, 'video1.html')

def video_two(request):
    return render(request, 'video2.html')

@login_required
def video_three(request):
    return render(request, 'video3.html')

@login_required
def video_four(request):
    return render(request, 'video4.html')

@login_required
def problem_to_solve(request):
    if request.method == 'POST':
        # Define the correct answers for the quiz
        correct_answers = {
            'q1': 'C',
            'q2': 'B',
            'q3': 'B',
            'q4': 'C',
            'q5': 'C'
        }
        
        # Collect user's answers with the format expected by the database
        answers = {
            f'question{i}': request.POST.get(f'q{i}', '').strip()
            for i in range(1, 6)
        }

        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]

        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('problem_to_solve')

        # Calculate score
        user_answers = {f'q{i}': request.POST.get(f'q{i}', '').strip() for i in range(1, 6)}
        correct_count = sum(1 for q, ans in user_answers.items() if ans == correct_answers.get(q))
        total_questions = len(correct_answers)
        
        # Check for duplicate submission (optional - uncomment if needed)
        existing = Submission.objects.filter(
            user=request.user,
            title='Problem to Solve'
        ).first()
        
        if existing:
            messages.error(request, 'You have already submitted this quiz.')
            return redirect('problem_to_solve')  # Change to your actual post-test URL name

        # Create submission
        try:
            submission = Submission.objects.create(
                title='Problem to Solve',
                user=request.user,
                answers=answers
            )
            
            # Display score feedback
            messages.success(
                request, 
                f'Quiz submitted successfully! You scored {correct_count}/{total_questions}.'
            )
            return redirect('learning')  # Redirect to learning hub
            
        except Exception as e:
            messages.error(request, f'Error submitting quiz: {str(e)}')
            return render(request, 'problem-to-solve.html')
    
    # GET request - show the form
    return render(request, 'problem-to-solve.html')



@login_required
def problem_to_solve_two(request):
    if request.method == 'POST':
        # Define the correct answers for the quiz
        correct_answers = {
            'q1': 'C',
            'q2': 'B',
            'q3': 'C',
            'q4': 'C',
            'q5': 'C'
        }
        
        # Collect user's answers with the format expected by the database
        answers = {
            f'question{i}': request.POST.get(f'q{i}', '').strip()
            for i in range(1, 6)  # Changed from 11 to 6 (only 5 questions)
        }

        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]

        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('problem_to_solve_two')

        # Calculate score
        user_answers = {f'q{i}': request.POST.get(f'q{i}', '').strip() for i in range(1, 6)}
        correct_count = sum(1 for q, ans in user_answers.items() if ans == correct_answers.get(q))
        total_questions = len(correct_answers)
        
        # Check for duplicate submission (optional - uncomment if needed)
        existing = Submission.objects.filter(
            user=request.user,
            title='Problem to Solve Two'
        ).first()
        
        if existing:
            messages.warning(request, 'You have already submitted this quiz.')
            return redirect('problem_to_solve_two')  # Change to your actual post-test URL name

        # Create submission
        try:
            submission = Submission.objects.create(
                title='Problem to Solve Two',
                user=request.user,
                answers=answers
            )
            
            # Display score feedback
            messages.success(
                request, 
                f'Quiz submitted successfully! You scored {correct_count}/{total_questions}.'
            )
            return redirect('problem_to_solve_two')  # Redirect to learning hub
            
        except Exception as e:
            messages.error(request, f'Error submitting quiz: {str(e)}')
            return render(request, 'problem-to-solve-two.html')
    
    # GET request - show the form
    return render(request, 'problem-to-solve-two.html')


@login_required
def problem_to_solve_three(request):
    if request.method == 'POST':
        # Define the correct answers for the quiz
        correct_answers = {
            'q1': 'A',
            'q2': 'D',
            'q3': 'A',
            'q4': 'D',
            'q5': 'D'
        }
        
        # Collect user's answers with the format expected by the database
        answers = {
            f'question{i}': request.POST.get(f'q{i}', '').strip()
            for i in range(1, 6)  # Changed from 11 to 6 (only 5 questions)
        }

        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]

        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('problem_to_solve_three')

        # Calculate score
        user_answers = {f'q{i}': request.POST.get(f'q{i}', '').strip() for i in range(1, 6)}
        correct_count = sum(1 for q, ans in user_answers.items() if ans == correct_answers.get(q))
        total_questions = len(correct_answers)
        
        # Check for duplicate submission (optional - uncomment if needed)
        existing = Submission.objects.filter(
            user=request.user,
            title='Problem to Solve Three'
        ).first()
        
        if existing:
            messages.warning(request, 'You have already submitted this quiz.')
            return redirect('problem_to_solve_three')  # Change to your actual post-test URL name

        # Create submission
        try:
            submission = Submission.objects.create(
                title='Problem to Solve Three',
                user=request.user,
                answers=answers
            )
            
            # Display score feedback
            messages.success(
                request, 
                f'Quiz submitted successfully! You scored {correct_count}/{total_questions}.'
            )
            return redirect('problem_to_solve_three')  # Redirect to learning hub
            
        except Exception as e:
            messages.error(request, f'Error submitting quiz: {str(e)}')
            return render(request, 'problem-to-solve-three.html')
    
    # GET request - show the form
    return render(request, 'problem-to-solve-three.html')


@login_required
def problem_to_solve_four(request):
    if request.method == 'POST':
        # Define the correct answers for the quiz
        correct_answers = {
            'q1': 'A',
            'q2': 'B',
            'q3': 'C',
            'q4': 'D',
            'q5': 'A'
        }
        
        # Collect user's answers with the format expected by the database
        answers = {
            f'question{i}': request.POST.get(f'q{i}', '').strip()
            for i in range(1, 6)  # Only 5 questions
        }

        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]

        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('problem_to_solve_four')

        # Calculate score
        user_answers = {f'q{i}': request.POST.get(f'q{i}', '').strip() for i in range(1, 6)}
        correct_count = sum(1 for q, ans in user_answers.items() if ans == correct_answers.get(q))
        total_questions = len(correct_answers)
        
        # Check for duplicate submission (optional - uncomment if needed)
        existing = Submission.objects.filter(
            user=request.user,
            title='Problem to Solve Four'
        ).first()
        
        if existing:
            messages.warning(request, 'You have already submitted this quiz.')
            return redirect('problem_to_solve_four')  # Change to your actual post-test URL name

        # Create submission
        try:
            submission = Submission.objects.create(
                title='Problem to Solve Four',
                user=request.user,
                answers=answers
            )
            
            # Display score feedback
            messages.success(
                request, 
                f'Quiz submitted successfully! You scored {correct_count}/{total_questions}.'
            )
            return redirect('problem_to_solve_four')  # Redirect to learning hub
            
        except Exception as e:
            messages.error(request, f'Error submitting quiz: {str(e)}')
            return render(request, 'problem-to-solve-four.html')
    
    # GET request - show the form
    return render(request, 'problem-to-solve-four.html')

@login_required
def post_test(request):
    if request.method == 'POST':
        # Define correct answers
        CORRECT_ANSWERS = {
            'pt1': 'B',
            'pt2': 'C',
            'pt3': 'C',
            'pt4': 'B',
            'pt5': 'C',
            'pt6': 'B',
            'pt7': 'B',
            'pt8': 'C',
            'pt9': 'C',
            'pt10': 'B'
        }
        
        # Collect answers
        answers = {
            f'post{i}': request.POST.get(f'pt{i}', '').strip()
            for i in range(1, 11)
        }
        
        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]
        
        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('post_test')
        
        # Calculate correct answers
        correct_count = sum(
            1 for i in range(1, 11)
            if request.POST.get(f'pt{i}', '').strip() == CORRECT_ANSWERS[f'pt{i}']
        )
        
        # Add correct count to answers dictionary
        answers['correct'] = correct_count
        
        # Check for duplicate submission (optional)
        existing = Submission.objects.filter(
            user=request.user,
            title='Post Test'
        ).first()
        
        if existing:
            messages.error(request, 'Post-test has already been submitted.')
            return redirect('survey_two')  
        
        # Create submission
        try:
            submission = Submission.objects.create(
                title='Post Test',
                user=request.user,
                answers=answers
            )
            messages.success(request, 'Post-test submitted successfully!')
            return redirect('survey_two')  
        except Exception as e:
            messages.error(request, f'Error submitting post-test: {str(e)}')
            return render(request, 'post-test.html')
    
    # GET request - show the form
    return render(request, 'post-test.html')



@login_required
def survey_two(request):
    if request.method == 'POST':
        title = 'Survey Two'
        user = request.user
        
        # Collect answers for all 16 questions (q1 to q16)
        answers = {
            f'question{i}': request.POST.get(f'q{i}', '').strip()
            for i in range(1, 17)  # 16 questions total
        }
        
        # Check if all questions are answered
        unanswered = [k for k, v in answers.items() if not v]
        
        if unanswered:
            messages.error(
                request, 
                f'Please answer all questions. Missing: {len(unanswered)} question(s).'
            )
            return redirect('survey_two')
        
        # Check for duplicate submission (optional - uncomment if needed)
        existing_submission = Submission.objects.filter(
            user=user, 
            title=title
        ).first()
        
        if existing_submission:
            messages.info(request, 'You have already submitted this survey.')
            return redirect('learning')
        
        # Create submission
        try:
            submission = Submission.objects.create(
                title=title,
                user=user,
                answers=answers
            )
            messages.success(request, 'Survey submitted successfully!')
            return redirect('learning')
        except Exception as e:
            messages.error(request, f'Error submitting survey: {str(e)}')
            return render(request, 'survey2.html')
    
    # GET request - just render the form without error messages
    return render(request, 'survey2.html')


# def courses(request):
#     if not request.user.is_authenticated:
#         messages.error(request, 'Please login to access the course content!')
#         return redirect('login')

#     courses = Course.objects.all()
#     myFilter = CourseFilter(request.GET, queryset=courses)
#     filtered_courses = myFilter.qs  # Apply search filter

#     # Pagination
#     paginator = Paginator(filtered_courses, 12)  # Show 6 courses per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'courses': page_obj,  
#         'myFilter': myFilter,
#         'paginator': paginator,  
#         'page_obj': page_obj,  
#     }

#     return render(request, 'courses.html', context)


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



