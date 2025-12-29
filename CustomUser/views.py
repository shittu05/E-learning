from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm
from django.shortcuts import render, redirect
from django.shortcuts import render

from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



# Create your models here.

def index(request):
    if request.user.is_authenticated:
        return redirect("/learn/courses/")
    return render(request, 'registration.html')



def register(request):
    if request.user.is_authenticated:
        return redirect("/learn/courses/")

    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('/register/')

        else:
            user = User.objects.create_user(
                email=email,
                password=password,
                name=name
            )
            user.save()
            user = authenticate(email=email,password = password)
            # auth.login(request, user)  # Use login instead of auth.login
            # messages.success(request, "Student account created successfully")
            # return redirect('/login/')
            if user is not None:
                auth.login(request,user)
                return redirect('/learn/courses/')

      
    else:
        # form = RegForm()
        return render(request, 'registration.html')

    


def login(request):

    # if request.user.is_authenticated:
    #     return redirect('/login/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            auth.login(request,user)
            return redirect('/learn/courses/')
        else:
            messages.error(request, 'invalid login details')
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
    
    
 
def logout(request):
    request.session.clear()
    messages.info(request, "You have been logged out")
    return redirect('login')


from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from django.contrib.admin.views.decorators import staff_member_required
import json
from Myapp.models import Submission

@staff_member_required
def export_page(request):
    return render(request, 'export.html')


@staff_member_required
def export_survey_one(request):
    """Export Survey One submissions to Excel"""
    submissions = Submission.objects.filter(title='Survey One').select_related('user')
    
    # Create workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Survey One"
    
    # Header style
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    # Headers
    headers = ['User ID', 'Name', 'Email', 'Answer', 'Submitted At']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Data rows
    for row, submission in enumerate(submissions, 2):
        ws.cell(row=row, column=1, value=submission.user.id)
        ws.cell(row=row, column=2, value=submission.user.name)
        ws.cell(row=row, column=3, value=submission.user.email)
        ws.cell(row=row, column=4, value=submission.answers.get('survey1', 'N/A'))
        ws.cell(row=row, column=5, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    # Create response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=survey_one_export.xlsx'
    wb.save(response)
    return response


@staff_member_required
def export_survey_two(request):
    """Export Survey Two submissions to Excel"""
    submissions = Submission.objects.filter(title='Survey Two').select_related('user')
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Survey Two"
    
    # Header style
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    # Headers
    headers = ['User ID', 'Name', 'Email', 'Answer', 'Submitted At']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Data rows
    for row, submission in enumerate(submissions, 2):
        ws.cell(row=row, column=1, value=submission.user.id)
        ws.cell(row=row, column=2, value=submission.user.name)
        ws.cell(row=row, column=3, value=submission.user.email)
        ws.cell(row=row, column=4, value=submission.answers.get('survey2', 'N/A'))
        ws.cell(row=row, column=5, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=survey_two_export.xlsx'
    wb.save(response)
    return response


@staff_member_required
def export_problem_to_solve(request):
    """Export Problem to Solve (Pre-Test) submissions to Excel"""
    submissions = Submission.objects.filter(title='Problem to Solve').select_related('user')
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Problem to Solve"
    
    # Header style
    header_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    # Headers - User info + 10 questions + submitted date
    headers = ['User ID', 'Name', 'Email', 
               'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
               'Submitted At']
    
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Data rows
    for row, submission in enumerate(submissions, 2):
        ws.cell(row=row, column=1, value=submission.user.id)
        ws.cell(row=row, column=2, value=submission.user.name)
        ws.cell(row=row, column=3, value=submission.user.email)
        
        # Add answers for each question
        for i in range(1, 11):
            ws.cell(row=row, column=3+i, value=submission.answers.get(f'question{i}', 'N/A'))
        
        ws.cell(row=row, column=14, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=problem_to_solve_export.xlsx'
    wb.save(response)
    return response


@staff_member_required
def export_post_test(request):
    """Export Post Test submissions to Excel"""
    submissions = Submission.objects.filter(title='Post Test').select_related('user')
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Post Test"
    
    # Header style
    header_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    # Headers - User info + 10 questions + correct count + submitted date
    headers = ['User ID', 'Name', 'Email', 
               'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
               'Correct Answers', 'Score (%)', 'Submitted At']
    
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Data rows
    for row, submission in enumerate(submissions, 2):
        ws.cell(row=row, column=1, value=submission.user.id)
        ws.cell(row=row, column=2, value=submission.user.name)
        ws.cell(row=row, column=3, value=submission.user.email)
        
        # Add answers for each question
        for i in range(1, 11):
            ws.cell(row=row, column=3+i, value=submission.answers.get(f'post{i}', 'N/A'))
        
        # Add correct count and percentage
        correct = submission.answers.get('correct', 0)
        ws.cell(row=row, column=14, value=correct)
        ws.cell(row=row, column=15, value=f"{(correct/10)*100:.1f}%")
        ws.cell(row=row, column=16, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=post_test_export.xlsx'
    wb.save(response)
    return response


@staff_member_required
def export_all_submissions(request):
    """Export all submissions in separate sheets"""
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Define exports
    exports = [
        ('Survey One', 'Survey One', ['survey1']),
        ('Survey Two', 'Survey Two', ['survey2']),
        ('Problem to Solve', 'Problem to Solve', [f'question{i}' for i in range(1, 11)]),
        ('Post Test', 'Post Test', [f'post{i}' for i in range(1, 11)] + ['correct']),
    ]
    
    for sheet_name, title_filter, answer_keys in exports:
        submissions = Submission.objects.filter(title=title_filter).select_related('user')
        
        ws = wb.create_sheet(title=sheet_name)
        
        # Header style
        header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        header_font = Font(bold=True, color="FFFFFF")
        
        # Build headers
        headers = ['User ID', 'Name', 'Email']
        
        # Add answer column headers
        if sheet_name in ['Survey One', 'Survey Two']:
            headers.append('Answer')
        elif sheet_name == 'Problem to Solve':
            headers.extend([f'Q{i}' for i in range(1, 11)])
        elif sheet_name == 'Post Test':
            headers.extend([f'Q{i}' for i in range(1, 11)])
            headers.extend(['Correct Answers', 'Score (%)'])
        
        headers.append('Submitted At')
        
        # Write headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center')
        
        # Write data
        for row, submission in enumerate(submissions, 2):
            ws.cell(row=row, column=1, value=submission.user.id)
            ws.cell(row=row, column=2, value=submission.user.name)
            ws.cell(row=row, column=3, value=submission.user.email)
            
            col_offset = 4
            
            # Add answers based on type
            if sheet_name in ['Survey One', 'Survey Two']:
                ws.cell(row=row, column=col_offset, value=submission.answers.get(answer_keys[0], 'N/A'))
                col_offset += 1
            else:
                for key in answer_keys[:-1] if sheet_name == 'Post Test' else answer_keys:
                    ws.cell(row=row, column=col_offset, value=submission.answers.get(key, 'N/A'))
                    col_offset += 1
                
                if sheet_name == 'Post Test':
                    correct = submission.answers.get('correct', 0)
                    ws.cell(row=row, column=col_offset, value=correct)
                    ws.cell(row=row, column=col_offset + 1, value=f"{(correct/10)*100:.1f}%")
                    col_offset += 2
            
            ws.cell(row=row, column=col_offset, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Auto-adjust column widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=all_submissions_export.xlsx'
    wb.save(response)
    return response
    """Export all submissions in separate sheets"""
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Define exports
    exports = [
        ('Survey One', 'Survey One', ['survey1']),
        ('Survey Two', 'Survey Two', ['survey2']),
        ('Problem to Solve', 'Problem to Solve', [f'question{i}' for i in range(1, 11)]),
        ('Post Test', 'Post Test', [f'post{i}' for i in range(1, 11)] + ['correct']),
    ]
    
    for sheet_name, title_filter, answer_keys in exports:
        submissions = Submission.objects.filter(title=title_filter).select_related('user')
        
        ws = wb.create_sheet(title=sheet_name)
        
        # Header style
        header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        header_font = Font(bold=True, color="FFFFFF")
        
        # Build headers
        headers = ['User ID', 'Full Name', 'Email']
        
        # Add answer column headers
        if sheet_name in ['Survey One', 'Survey Two']:
            headers.append('Answer')
        elif sheet_name == 'Problem to Solve':
            headers.extend([f'Q{i}' for i in range(1, 11)])
        elif sheet_name == 'Post Test':
            headers.extend([f'Q{i}' for i in range(1, 11)])
            headers.extend(['Correct Answers', 'Score (%)'])
        
        headers.append('Submitted At')
        
        # Write headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center')
        
        # Write data
        for row, submission in enumerate(submissions, 2):
            ws.cell(row=row, column=1, value=submission.user.id)
            ws.cell(row=row, column=2, value=submission.user.name)
            ws.cell(row=row, column=3, value=submission.user.email)
            
            col_offset = 5
            
            # Add answers based on type
            if sheet_name in ['Survey One', 'Survey Two']:
                ws.cell(row=row, column=col_offset, value=submission.answers.get(answer_keys[0], 'N/A'))
                col_offset += 1
            else:
                for key in answer_keys[:-1] if sheet_name == 'Post Test' else answer_keys:
                    ws.cell(row=row, column=col_offset, value=submission.answers.get(key, 'N/A'))
                    col_offset += 1
                
                if sheet_name == 'Post Test':
                    correct = submission.answers.get('correct', 0)
                    ws.cell(row=row, column=col_offset, value=correct)
                    ws.cell(row=row, column=col_offset + 1, value=f"{(correct/10)*100:.1f}%")
                    col_offset += 2
            
            ws.cell(row=row, column=col_offset, value=submission.submitted_at.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Auto-adjust column widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width
    
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=all_submissions_export.xlsx'
    wb.save(response)
    messages.success(request, 'All submissions exported successfully.')
    return response