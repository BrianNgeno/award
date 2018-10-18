from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm
from django.contrib.auth.models import User
import datetime as dt

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

# Create your views here.
def home_page(request):
    date = dt.date.today()
    project = Project.objects.all()
    return render(request,'home.html',{'date':date,'project':project})

@login_required(login_url='/accounts/login')
def upload_project(request):
    if request.method == 'POST':
        uploadform = ProjectForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page')
    else:
        uploadform = ProjectForm()
    return render(request,'project.html',{'uploadform':uploadform})

def view_project(request):
    project = Project.objects.get_all()
    return render(request,'home.html',{'project':project})

def search_results(request):
    category= Categorys.objects.all()
    location= Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_image,'category':category,"location":location})

    else:
        message = "You haven't searched for any term"
        return render(request,'/search.html',{"message":message})
