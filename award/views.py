from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm,RateForm
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
# @login_required(login_url='/accounts/login')
def home_page(request):
    date = dt.date.today()
    project = Project.objects.all()
    # profile = User.objects.get(username=request.user)
    return render(request,'home.html',locals())

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
    return render(request,'update-project.html',locals())

def view_project(request):
    project = Project.objects.get_all()
    return render(request,'home.html', locals())

def search_results(request):
    profile= Profile.objects.all()
    project= Project.objects.all()
    if 'Project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

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
    projo = Project.get_profile_projects(profile.id)
    title = f'@{profile.username} awwward projects and screenshots'

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

    '''
    logs out current user from account
    '''
def logout(request):
    return render(request, 'home.html')

def rate(request):
    profile = User.objects.get(username=request.user)
    return render(request,'rate.html',locals())

@login_required(login_url='/accounts/login')
def rate_project(request,project_id):
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        rateform = RateForm(request.POST, request.FILES)
        if rateform.is_valid():
            rating = rateform.save(commit=False)
            rating.save()
            return redirect('project.html')
    else:
        rateform = RateForm()
    return render(request,'rate.html',locals())

@login_required(login_url='/accounts/login/')
def vote(request,project_id):
   try:
       project = Project.objects.get(id = project_id)
   except DoesNotExist:
       raise Http404()
   return render(request,"project.html", locals())