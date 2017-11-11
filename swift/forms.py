from django import forms
from .models import Login, Event, Student, Parent, Teacher, Invoice, Course, Exam, Grade, Mark


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('user_email', 'password', 'level', )

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_description', )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('login','student_name','student_address', 'student_phone', 'student_class_grade', )

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('login', 'parent_name', 'parent_address', 'parent_phone', )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('login','teacher_name', 'teacher_address', 'teacher_phone', )

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('student','parent','invoice_name','invoice_description', 'invoice_due_date', 'invoice_status', )

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('teacher','course_name','course_description','course_syllabus', 'course_schedule_date', 'course_announcement', )

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('course','exam_name','exam_details', )

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('course','student', 'grade_value', 'grade_comment', 'grade_attendance',)

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('exam','course','student','marks_value','marks_feedback',)
