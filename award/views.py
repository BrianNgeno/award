from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm
from django.contrib.auth.models import User


# Create your views here.
def home_page(request):
    return render(request,'home.html')

@login_required(login_url='/accounts/login')
def upload_project(request):
    if request.method == 'POST':
        uploadform = ProjectForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page', username=request.user)
    else:
        uploadform = ProjectForm()
    return render(request,'project.html',{'uploadform':uploadform})