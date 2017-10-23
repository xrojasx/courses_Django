from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course 

def index(request): 
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "course/index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')

    else:
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
        )
        return redirect('/')

def confirm(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, "course/delete.html", context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/course')
