from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Login(models.Model):
    user_email = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
    level = models.CharField(max_length=5)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_email)

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.event_name)

class Student(models.Model):
    login = models.OneToOneField(Login, related_name='logins')
    student_name = models.CharField(max_length=25)
    student_address = models.CharField(max_length=250)
    student_phone = models.CharField(max_length=12)
    student_class_grade = models.CharField(max_length=10)

    def __str__(self):
        return str(self.student_name)

    #def initial_stock_value(self):
     #   return self.shares * self.purchase_price


class Parent(models.Model):
    login = models.OneToOneField(Login, related_name='logins')
    parent_name = models.CharField(max_length=25)
    parent_address = models.CharField(max_length=250)
    parent_phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.parent_name)

    #def initial_stock_value(self):
     #   return self.shares * self.purchase_price

class Teacher(models.Model):
    login = models.OneToOneField(Login, related_name='logins')
    teacher_name = models.CharField(max_length=25)
    teacher_address = models.CharField(max_length=250)
    teacher_phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.teacher_name)

    #def initial_stock_value(self):
     #   return self.shares * self.purchase_price

class Invoice(models.Model):
    parent = models.ForeignKey(Parent, related_name='parents')
    student = models.ForeignKey(Student, related_name='students')
    invoice_name = models.CharField(max_length=20)
    invoice_description = models.CharField(max_length=200)
    invoice_due_date = models.DateField()
    invoice_status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.invoice_name)

class Event_Registration(models.Model):
    event = models.ForeignKey(Event, related_name='events')
    parent = models.ForeignKey(Parent, related_name='parents')

class Student_Parent(models.Model):
    student = models.ForeignKey(Student, related_name='students')
    parent = models.ForeignKey(Parent, related_name='parents')

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='teachers')
    course_name = models.CharField(max_length=25)
    course_description = models.CharField(max_length=200)
    course_syllabus = models.CharField(max_length=200)
    course_schedule_date = models.DateField()
    course_announcement = models.CharField(max_length=200)

    def __str__(self):
        return str(self.course_name)

class Exam(models.Model):
    course = models.ForeignKey(Course, related_name='courses')
    exam_name = models.CharField(max_length=20)
    exam_details = models.CharField(max_length=250)

    def __str__(self):
        return str(self.exam_name)

class Grade(models.Model):
    course = models.ForeignKey(Course, related_name='courses')
    student = models.ForeignKey(Student, related_name='students')
    grade_value = models.CharField(max_length=2)
    grade_comment = models.CharField(max_length=200)
    grade_attendance = models.CharField(max_length=20)

    def __str__(self):
        return str(self.grade_name)

class Mark(models.Model):
    exam = models.ForeignKey(Exam, related_name='exams')
    course = models.ForeignKey(Course, related_name='courses')
    student = models.ForeignKey(Student, related_name='students')
    marks_value = models.IntegerField(blank=False, null=False)
    marks_feedback = models.CharField(max_length=250)

    def __str__(self):
        return str(self.marks.value)
