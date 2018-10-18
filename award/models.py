from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    rate = models.ManyToManyField('Project', related_name='image',max_length=30)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    

class Project(models.Model):
    screenshot = models.ImageField(upload_to = 'images/')
    project_name = models.CharField(max_length =10)
    project_url = models.CharField(max_length =30)
    location = models.CharField(max_length =10)
    profile = models.ForeignKey(Profile, null = True,related_name='project')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-pk']

    def save_project(self):
        self.save()
    
    @classmethod
    def get_project(cls, profile):
        image = Project.objects.filter(Profile__pk = profile)
        return image
    
    @classmethod
    def get_all_images(cls):
        images = Project.objects.all()
        return images

    @classmethod
    def search_by_profile(cls,search_term):
        projo = cls.objects.filter(profile__name__icontains=search_term)
        return projo

class Rate(models.Model):
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    content = models.CharField(max_length=8)
    average = models.CharField(max_length=8)
    user = models.ForeignKey(User,null = True)
    project = models.ForeignKey(Project,related_name='rate')


    def __str__(self):
        return self.design

    class Meta:
        ordering = ['-id']
