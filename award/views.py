from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm
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
    profile= Profile.objects.all()
    project= Project.objects.all()
    if 'Project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"project": searched_project,'profile':profile,'project':project})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def profile(request, username):
    projo = Project.objects.all()
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    projo = Project.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile.html', locals())
    '''
    editing user profile fillform & submission
    '''
@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals())