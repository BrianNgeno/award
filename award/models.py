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
    rating = models.ManyToManyField('Project', related_name='image',max_length=30)

    def save_profile(self):
        self.save()
class Project(models.Model):
    screenshot = models.ImageField(upload_to = 'images/')
    project_name = models.CharField(max_length =30)
    project_url = models.TextField(max_length =40)
    profile = models.ForeignKey(Profile, null = True,related_name='image')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-pk']

    def save_project(self):
        self.save()

class Rate(models.Model):
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    content = models.CharField(max_length=8)
    average = models.CharField(max_length=8)
    user = models.ForeignKey(User,null = True)
    project = models.ForeignKey(Project,related_name='comment')


    def __str__(self):
        return self.design

    class Meta:
        ordering = ['-id']
