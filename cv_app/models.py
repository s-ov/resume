from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=50)
    motto = models.CharField(max_length=80)
    avatar = models.ImageField(upload_to='avatars/')
    cv_file = models.FileField(upload_to='cv/', blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Skill(models.Model):
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    skill = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return "Skill"


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    title = models.CharField(max_length=100)
    project_url = models.URLField(max_length=200, unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PersonalInfo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-time_create']
