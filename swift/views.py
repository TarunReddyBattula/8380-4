from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .serializers import CustomerSerializer
from django.db.models import Sum

def home(request):
    return render(request, 'swift/home.html', {'swift': home})
'''
@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'swift/customer_list.html', {'customers': customer})

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'swift/customer_list.html', {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
        return render(request, 'swift/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('swift:customer_list')

'''
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request,'swift/student_list.html', {'students': students})


@login_required
def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_date = timezone.now()
            student.save()
            students = Student.objects.all()
            return render(request, 'swift/student_list.html', {'students': students})
    else:
        form = StudentForm()
        # print("Else")
        return render(request, 'swift/student_new.html', {'form': form})


@ login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            # student.customer = student.id
            student.updated_date = timezone.now()
            student.save()
            students = Student.objects.all()
            return render(request, 'swift/student_list.html', {'students': students})
    else:
        # print("else")
        form = StudentForm(instance=student)
        return render(request, 'swift/student_edit.html', {'form': form})


@ login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk =pk)
    student.delete()
    students = Student.objects.all()
    return render(request, 'swift/student_list.html', {'students': students})

@login_required
def parent_list(request):
    parents = Parent.objects.all()
    return render(request,'swift/parent_list.html', {'parents': parents})


@login_required
def parent_new(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save(commit=False)
            parent.created_date = timezone.now()
            parent.save()
            parents = Parent.objects.all()
            return render(request, 'swift/parent_list.html', {'parents': parents})
    else:
        form = ParentForm()
        # print("Else")
        return render(request, 'swift/parent_new.html', {'form': form})

@ login_required
def parent_edit(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == "POST":
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            parent = form.save()
            # parent.customer = parent.id
            parent.updated_date = timezone.now()
            parent.save()
            parents = Parent.objects.all()
            return render(request, 'swift/parent_list.html', {'parents': parents})
    else:
        # print("else")
        form = ParentForm(instance=parent)
        return render(request, 'swift/parent_edit.html', {'form': form})


@ login_required
def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk =pk)
    parent.delete()
    parents = Parent.objects.all()
    return render(request, 'swift/parent_list.html', {'parents': parents})

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request,'swift/teacher_list.html', {'teachers': teachers})


@login_required
def teacher_new(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.created_date = timezone.now()
            teacher.save()
            teachers = Teacher.objects.all()
            return render(request, 'swift/teacher_list.html', {'teachers': teachers})
    else:
        form = TeacherForm()
        # print("Else")
        return render(request, 'swift/teacher_new.html', {'form': form})

@ login_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save()
            # teacher.customer = teacher.id
            teacher.updated_date = timezone.now()
            teacher.save()
            teachers = Teacher.objects.all()
            return render(request, 'swift/teacher_list.html', {'teachers': teachers})
    else:
        # print("else")
        form = TeacherForm(instance=teacher)
        return render(request, 'swift/teacher_edit.html', {'form': form})

@ login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk =pk)
    teacher.delete()
    teachers = Teacher.objects.all()
    return render(request, 'swift/teacher_list.html', {'teachers': teachers})

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request,'swift/event_list.html', {'events': events})


@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_date = timezone.now()
            event.save()
            events = Event.objects.all()
            return render(request, 'swift/event_list.html', {'events': events})
    else:
        form = EventForm()
        # print("Else")
        return render(request, 'swift/event_new.html', {'form': form})

@ login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            # event.customer = event.id
            event.updated_date = timezone.now()
            event.save()
            events = Event.objects.all()
            return render(request, 'swift/event_list.html', {'events': events})
    else:
        # print("else")
        form = EventForm(instance=event)
        return render(request, 'swift/event_edit.html', {'form': form})


@ login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk =pk)
    event.delete()
    events = Event.objects.all()
    return render(request, 'swift/event_list.html', {'events': events})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request,'swift/invoice_list.html', {'invoices': invoices})


@login_required
def invoice_new(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.created_date = timezone.now()
            invoice.save()
            invoices = Invoice.objects.all()
            return render(request, 'swift/invoice_list.html', {'invoices': invoices})
    else:
        form = InvoiceForm()
        # print("Else")
        return render(request, 'swift/invoice_new.html', {'form': form})

@ login_required
def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            # invoice.customer = invoice.id
            invoice.updated_date = timezone.now()
            invoice.save()
            invoices = Invoice.objects.all()
            return render(request, 'swift/invoice_list.html', {'invoices': invoices})
    else:
        # print("else")
        form = InvoiceForm(instance=invoice)
        return render(request, 'swift/invoice_edit.html', {'form': form})


@ login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk =pk)
    invoice.delete()
    invoices = Invoice.objects.all()
    return render(request, 'swift/invoice_list.html', {'invoices': invoices})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request,'swift/course_list.html', {'courses': courses})

@login_required
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_date = timezone.now()
            course.save()
            courses = Course.objects.all()
            return render(request, 'swift/course_list.html', {'courses': courses})
    else:
        form = CourseForm()
        # print("Else")
        return render(request, 'swift/course_new.html', {'form': form})

@ login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            # course.customer = course.id
            course.updated_date = timezone.now()
            course.save()
            courses = Course.objects.all()
            return render(request, 'swift/course_list.html', {'courses': courses})
    else:
        # print("else")
        form = CourseForm(instance=course)
        return render(request, 'swift/course_edit.html', {'form': form})


@ login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk =pk)
    course.delete()
    courses = Course.objects.all()
    return render(request, 'swift/course_list.html', {'courses': courses})

@login_required
def grade_list(request):
    grades = Grade.objects.all()
    return render(request,'swift/grade_list.html', {'grades': grades})

@login_required
def grade_new(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.created_date = timezone.now()
            grade.save()
            grades = Grade.objects.all()
            return render(request, 'swift/grade_list.html', {'grades': grades})
    else:
        form = GradeForm()
        # print("Else")
        return render(request, 'swift/grade_new.html', {'form': form})

@ login_required
def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            grade = form.save()
            # grade.customer = grade.id
            grade.updated_date = timezone.now()
            grade.save()
            grades = Grade.objects.all()
            return render(request, 'swift/grade_list.html', {'grades': grades})
    else:
        # print("else")
        form = GradeForm(instance=grade)
        return render(request, 'swift/grade_edit.html', {'form': form})


@ login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk =pk)
    grade.delete()
    grades = Grade.objects.all()
    return render(request, 'swift/grade_list.html', {'grades': grades})

@login_required
def mark_list(request):
    marks = Mark.objects.all()
    return render(request,'swift/mark_list.html', {'marks': marks})

@login_required
def mark_new(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.created_date = timezone.now()
            mark.save()
            marks = Mark.objects.all()
            return render(request, 'swift/mark_list.html', {'marks': marks})
    else:
        form = MarkForm()
        # print("Else")
        return render(request, 'swift/mark_new.html', {'form': form})

@ login_required
def mark_edit(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    if request.method == "POST":
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            mark = form.save()
            # mark.customer = mark.id
            mark.updated_date = timezone.now()
            mark.save()
            marks = Mark.objects.all()
            return render(request, 'swift/mark_list.html', {'marks': marks})
    else:
        # print("else")
        form = MarkForm(instance=mark)
        return render(request, 'swift/mark_edit.html', {'form': form})


@ login_required
def mark_delete(request, pk):
    mark = get_object_or_404(Mark, pk =pk)
    mark.delete()
    marks = Mark.objects.all()
    return render(request, 'swift/mark_list.html', {'marks': marks})

@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request,'swift/exam_list.html', {'exams': exams})

@login_required
def exam_new(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.created_date = timezone.now()
            exam.save()
            exams = Exam.objects.all()
            return render(request, 'swift/exam_list.html', {'exams': exams})
    else:
        form = ExamForm()
        # print("Else")
        return render(request, 'swift/exam_new.html', {'form': form})

@ login_required
def exam_edit(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == "POST":
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            exam = form.save()
            # exam.customer = exam.id
            exam.updated_date = timezone.now()
            exam.save()
            exams = Exam.objects.all()
            return render(request, 'swift/exam_list.html', {'exams': exams})
    else:
        # print("else")
        form = ExamForm(instance=exam)
        return render(request, 'swift/exam_edit.html', {'form': form})


@ login_required
def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk =pk)
    exam.delete()
    exams = Exam.objects.all()
    return render(request, 'swift/exam_list.html', {'exams': exams})
'''
@ login_required
def investment_list(request):
    investments = Investment.objects.filter( acquired_date__lte=timezone.now())
    return render(request, 'swift/investment_list.html' , {'investments': investments})


@ login_required
def investment_new(request):
    if request.method == "POST" :
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.created_date = timezone.now()
            investment.save()
            investments = Investment.objects.filter( acquired_date__lte=timezone.now())
            return render(request, 'swift/investment_list.html', {'investments': investments})
    else :
        form = InvestmentForm()
        # print("Else")
        return render(request, 'swift/investment_new.html', { 'form': form})


@ login_required
def investment_edit(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.method == "POST":
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            investment = form.save()
            # investment.customer = investment.id
            investment.updated_date = timezone.now()
            investment.save()
            investments = Investment.objects.filter(acquired_date__lte=timezone.now())
            return render(request, 'swift/investment_list.html', {'investments': investments})
    else:
        # print("else")
        form = InvestmentForm(instance=investment)
        return render(request, 'swift/investment_edit.html', {'form': form})


@ login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk =pk)
    investment.delete()
    investments = Investment.objects.filter( acquired_date__lte=timezone.now())
    return render(request, 'swift/investment_list.html', { 'investments': investments})


@ login_required
def swift(request,pk):

    customer = get_object_or_404(Customer, pk =pk)
    customers = Customer.objects.filter( created_date__lte =timezone.now())
    investments =Investment.objects.filter( customer =pk)
    stocks = Stock.objects.filter( customer =pk)
    mutualfunds = Mutualfund.objects.filter(customer=pk)

     #for investment
    sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value')).get('recent_value__sum', 0.00)
    sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value')).get('acquired_value__sum', 0.00)

    sum_purchase_value = Mutualfund.objects.filter(customer=pk).aggregate(Sum('purchased_value')).get('purchased_value__sum', 0.00)
    sum_recent_value_mutual = Mutualfund.objects.filter(customer=pk).aggregate(Sum('recent_value')).get('recent_value__sum', 0.00)

    return render(request, 'swift/swift.html', { 'customers': customers, 'investments' :investments,'stocks' : stocks,  'mutualfunds' :mutualfunds,
                                                          'sum_acquired_value': sum_acquired_value, 'sum_recent_value': sum_recent_value,
                                                          'sum_purchase_value':sum_purchase_value, 'sum_recent_value_mutual': sum_recent_value_mutual,
                                                           })

# def swift(request):
#     customers = Customer.objects.filter(created_date__lte=timezone.now())
#     investments =Investment.objects.all()
#     stocks = Stock.objects.all()
#     sum_recent_value = Investment.objects.all().aggregate(Sum('recent_value'))
#     sum_acquired_value = Investment.objects.all().aggregate(Sum('acquired_value'))
#     return render(request, 'customers/swift.html', {'customers': customers, 'investments': investments, 'stocks': stocks, 'sum_recent_value': sum_recent_value, 'sum_acquired_value': sum_acquired_value,})

# Lists all customers
class CustomerList(APIView):
    def get(self,request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)


#Mutualfund added

def mutualfund_list(request):
    mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
    return render(request, 'swift/mutualfund_list.html' , {'mutualfunds': mutualfunds})


@ login_required
def mutualfund_new(request):
    if request.method == "POST" :
        form = MutualfundForm(request.POST)
        if form.is_valid():
            mutualfund = form.save(commit=False)
            mutualfund.created_date = timezone.now()
            mutualfund.save()
            mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
            return render(request, 'swift/mutualfund_list.html', {'mutualfunds': mutualfunds})
    else :
        form = MutualfundForm()
        # print("Else")
        return render(request, 'swift/mutualfund_new.html', { 'form': form})


@ login_required
def mutualfund_edit(request, pk):
    mutualfund = get_object_or_404(Mutualfund, pk=pk)
    if request.method == "POST":
        form = MutualfundForm(request.POST, instance=mutualfund)
        if form.is_valid():
            mutualfund = form.save()
            # investment.customer = investment.id
            mutualfund.updated_date = timezone.now()
            mutualfund.save()
            mutualfunds = Mutualfund.objects.filter(purchased_date__lte=timezone.now())
            return render(request, 'swift/mutualfund_list.html', {'mutualfunds': mutualfunds})
    else:
        # print("else")
        form = MutualfundForm(instance=mutualfund)
        return render(request, 'swift/mutualfund_edit.html', {'form': form})


@ login_required
def mutualfund_delete(request, pk):
    mutualfund = get_object_or_404(Mutualfund, pk =pk)
    mutualfund.delete()
    mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
    return render(request, 'swift/mutualfund_list.html', { 'mutualfunds': mutualfunds})

@login_required
def stock_list(request):
    stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
    return render(request,'swift/stock_list.html', {'stocks': stocks})


@login_required
def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'swift/stock_list.html', {'stocks': stocks})
    else:
        form = StockForm()
        # print("Else")
        return render(request, 'swift/stock_new.html', {'form': form})


@ login_required
def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            # stock.customer = stock.id
            stock.updated_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'swift/stock_list.html', {'stocks': stocks})
    else:
        # print("else")
        form = StockForm(instance=stock)
        return render(request, 'swift/stock_edit.html', {'form': form})


@ login_required
def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk =pk)
    stock.delete()
    stocks = Stock.objects.filter( purchase_date__lte=timezone.now())
    return render(request, 'swift/stock_list.html', {'stocks': stocks})


@ login_required
def investment_list(request):
    investments = Investment.objects.filter( acquired_date__lte=timezone.now())
    return render(request, 'swift/investment_list.html' , {'investments': investments})


@ login_required
def investment_new(request):
    if request.method == "POST" :
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.created_date = timezone.now()
            investment.save()
            investments = Investment.objects.filter( acquired_date__lte=timezone.now())
            return render(request, 'swift/investment_list.html', {'investments': investments})
    else :
        form = InvestmentForm()
        # print("Else")
        return render(request, 'swift/investment_new.html', { 'form': form})


@ login_required
def investment_edit(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.method == "POST":
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            investment = form.save()
            # investment.customer = investment.id
            investment.updated_date = timezone.now()
            investment.save()
            investments = Investment.objects.filter(acquired_date__lte=timezone.now())
            return render(request, 'swift/investment_list.html', {'investments': investments})
    else:
        # print("else")
        form = InvestmentForm(instance=investment)
        return render(request, 'swift/investment_edit.html', {'form': form})


@ login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk =pk)
    investment.delete()
    investments = Investment.objects.filter( acquired_date__lte=timezone.now())
    return render(request, 'swift/investment_list.html', { 'investments': investments})


@ login_required
def swift(request,pk):

    customer = get_object_or_404(Customer, pk =pk)
    customers = Customer.objects.filter( created_date__lte =timezone.now())
    investments =Investment.objects.filter( customer =pk)
    stocks = Stock.objects.filter( customer =pk)
    mutualfunds = Mutualfund.objects.filter(customer=pk)

     #for investment
    sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value')).get('recent_value__sum', 0.00)
    sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value')).get('acquired_value__sum', 0.00)

    sum_purchase_value = Mutualfund.objects.filter(customer=pk).aggregate(Sum('purchased_value')).get('purchased_value__sum', 0.00)
    sum_recent_value_mutual = Mutualfund.objects.filter(customer=pk).aggregate(Sum('recent_value')).get('recent_value__sum', 0.00)

    return render(request, 'swift/swift.html', { 'customers': customers, 'investments' :investments,'stocks' : stocks,  'mutualfunds' :mutualfunds,
                                                          'sum_acquired_value': sum_acquired_value, 'sum_recent_value': sum_recent_value,
                                                          'sum_purchase_value':sum_purchase_value, 'sum_recent_value_mutual': sum_recent_value_mutual,
                                                           })

# def swift(request):
#     customers = Customer.objects.filter(created_date__lte=timezone.now())
#     investments =Investment.objects.all()
#     stocks = Stock.objects.all()
#     sum_recent_value = Investment.objects.all().aggregate(Sum('recent_value'))
#     sum_acquired_value = Investment.objects.all().aggregate(Sum('acquired_value'))
#     return render(request, 'customers/swift.html', {'customers': customers, 'investments': investments, 'stocks': stocks, 'sum_recent_value': sum_recent_value, 'sum_acquired_value': sum_acquired_value,})

# Lists all customers
class CustomerList(APIView):
    def get(self,request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)


#Mutualfund added

def mutualfund_list(request):
    mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
    return render(request, 'swift/mutualfund_list.html' , {'mutualfunds': mutualfunds})


@ login_required
def mutualfund_new(request):
    if request.method == "POST" :
        form = MutualfundForm(request.POST)
        if form.is_valid():
            mutualfund = form.save(commit=False)
            mutualfund.created_date = timezone.now()
            mutualfund.save()
            mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
            return render(request, 'swift/mutualfund_list.html', {'mutualfunds': mutualfunds})
    else :
        form = MutualfundForm()
        # print("Else")
        return render(request, 'swift/mutualfund_new.html', { 'form': form})


@ login_required
def mutualfund_edit(request, pk):
    mutualfund = get_object_or_404(Mutualfund, pk=pk)
    if request.method == "POST":
        form = MutualfundForm(request.POST, instance=mutualfund)
        if form.is_valid():
            mutualfund = form.save()
            # investment.customer = investment.id
            mutualfund.updated_date = timezone.now()
            mutualfund.save()
            mutualfunds = Mutualfund.objects.filter(purchased_date__lte=timezone.now())
            return render(request, 'swift/mutualfund_list.html', {'mutualfunds': mutualfunds})
    else:
        # print("else")
        form = MutualfundForm(instance=mutualfund)
        return render(request, 'swift/mutualfund_edit.html', {'form': form})


@ login_required
def mutualfund_delete(request, pk):
    mutualfund = get_object_or_404(Mutualfund, pk =pk)
    mutualfund.delete()
    mutualfunds = Mutualfund.objects.filter( purchased_date__lte=timezone.now())
    return render(request, 'swift/mutualfund_list.html', { 'mutualfunds': mutualfunds})

'''
