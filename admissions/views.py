from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import admissions
from admissions.forms import StudentModelForm, VendorForm
from admissions.models import Student, Teacher


# Create your views here.

# function based views

@login_required
def homepage(request):
    return render(request, 'index.html')

def userlogout(request):
    return render(request, 'logout.html')


@login_required
@permission_required('admissions.add_Student')
def add_admission(request):
    # return HttpResponse("This is admission view")
    # return render(request, 'admissions/add-admission.html', {'name': 'Saikiran', 'greeting': 'Welcome'})

    form = StudentModelForm
    studentform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request, 'admissions/add-admission.html', studentform)


@login_required
@permission_required('admissions.view_Student')
def admission_report(request):
    result = Student.objects.all()  # get all records from the table, SELECT * FROM students
    # return HttpResponse("<h1>This is admission report view.</h1>")
    students = {'allstudents': result}
    return render(request, 'admissions/admissions-report.html', students)


@login_required
def add_vendor(request):
    form = VendorForm
    vendorform = {'vendor_form': form}

    if request.method == 'POST':
        form = VendorForm(request.POST)
        # if form.is_valid():
            # print(form.cleaned_data['vendor_name'])
            # print(form.cleaned_data['item'])
            # print(form.cleaned_data['contact_details'])
            # print(form.cleaned_data['number_of_items'])
        # return homepage(request)


        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['address']
            c = form.cleaned_data['contact']
            i = form.cleaned_data['item']

            response = render(request, 'index.html')


            # Cookie implementation
            # response.set_cookie('name', n)
            # response.set_cookie("address", a)
            # response.set_cookie("contact", c)
            # response.set_cookie("item", i)

            #Session implementation
            request.session['name'] = n
            request.session['address'] = a
            request.session['contact'] = c
            request.session['item'] = i

        return response

    return render(request, 'admissions/add-vendor.html', vendorform)


@login_required
@permission_required('admissions.delete_Student')
def delete_student(request, id):
    s = Student.objects.get(id=id)
    s.delete()

    return admission_report(request)


@login_required
@permission_required('admissions.change_Student')
def update_student(request, id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return admission_report(request)

    return render(request, 'admissions/update-admission.html', dict)


# class based views
class FirstClassBasedView(View):
    def get(self, request):
        return HttpResponse("<h1>First Class Based View</h1>")


class TeacherRead(ListView):  # read the data in the model and pass to template
    model = Teacher
    # context_object_name = 'teacher_result_list'
    # template_name = 'teacher-report.html'


class GetTeacher(DetailView):  # retrieve the details of a single row (single teacher) and pass to template
    model = Teacher
    # context_object_name = 'teacherdetail'
    # template_name = 'teacher-detail.html'


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name', 'subject', 'experience', 'contact')


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name', 'subject', 'experience', 'contact')
    # success_url = 'url to be redirected after successful update' if this is not specified then django
    # redirects to the absolute url defined in the model class on model.py


class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacherlisturl')

