from django.contrib import admin
from .models import Login, Event, Student, Parent, Teacher, Invoice, Event_Registration, Student_Parent, Course, Exam, Grade, Mark

class LoginList(admin.ModelAdmin):
    list_display = ('user_email', 'level', 'password')
    list_filter = ('user_email', 'level')
    search_fields = ('user_email', 'level')
    ordering = ['user_email']

class EventList(admin.ModelAdmin):
    list_display = ('event_name','event_description')
    list_filter = ('event_name','event_description')
    search_fields = ('event_name','event_description')
    ordering = ['event_name']

class StudentList(admin.ModelAdmin):
    list_display = ('login','student_name','student_address', 'student_phone', 'student_class_grade')
    list_filter = ('login','student_name','student_address','student_class_grade')
    search_fields = ('login','student_name','student_address','student_class_grade')
    ordering = ['student_name']

class ParentList(admin.ModelAdmin):
    list_display = ('login','parent_name', 'parent_address', 'parent_phone')
    list_filter = ('login','parent_name', 'parent_address')
    search_fields = ('login','parent_name', 'parent_address')
    ordering = ['parent_name']

class TeacherList(admin.ModelAdmin):
    list_display = ('login','teacher_name', 'teacher_address', 'teacher_phone')
    list_filter = ('login','teacher_name', 'teacher_address')
    search_fields = ('login','teacher_name', 'teacher_address')
    ordering = ['teacher_name']

class InvoiceList(admin.ModelAdmin):
    list_display = ('student','parent','invoice_name','invoice_due_date', 'invoice_status')
    list_filter = ('student','parent','invoice_name')
    search_fields = ('student','parent','invoice_name')
    ordering = ['student','parent']

class Event_RegistrationList(admin.ModelAdmin):
    list_display = ('event','parent')
    list_filter = ('event','parent')
    search_fields = ('event','parent')
    ordering = ['event','parent']

class Student_ParentList(admin.ModelAdmin):
    list_display = ('student','parent')
    list_filter = ('student','parent')
    search_fields = ('student','parent')
    ordering = ['student','parent']

class CourseList(admin.ModelAdmin):
    list_display = ('teacher','course_name','course_description','course_syllabus')
    list_filter = ('teacher','course_name','course_syllabus')
    search_fields = ('teacher','course_name','course_syllabus')
    ordering = ['teacher']

class ExamList(admin.ModelAdmin):
    list_display = ('course','exam_name','exam_details')
    list_filter = ('course','exam_name','exam_details')
    search_fields = ('course','exam_name')
    ordering = ['course']

class GradeList(admin.ModelAdmin):
    list_display = ('course','student', 'grade_value', 'grade_attendance')
    list_filter = ('course','student', 'grade_value')
    search_fields = ('course','student', 'grade_value')
    ordering = ['student']

class MarkList(admin.ModelAdmin):
    list_display = ('exam','course','student','marks_value','marks_feedback')
    list_filter = ('exam','course','student')
    search_fields = ('exam','course','student')
    ordering = ['student']

admin.site.register(Login, LoginList)
admin.site.register(Event, EventList)
admin.site.register(Student, StudentList)
admin.site.register(Parent, ParentList)
admin.site.register(Teacher, TeacherList)
admin.site.register(Invoice, InvoiceList)
admin.site.register(Event_Registration, Event_RegistrationList)
admin.site.register(Student_Parent, Student_ParentList)
admin.site.register(Course, CourseList)
admin.site.register(Exam, ExamList)
admin.site.register(Grade, GradeList)
admin.site.register(Mark, MarkList)
