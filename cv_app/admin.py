from django.contrib import admin
from .models import *

admin.site.register([UserProfile, Skill, Portfolio, PersonalInfo, Message])
