from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import re

from .models import *
from .forms import *
from .utils import validate_email


def base_view(request):
    return render(request, 'cv_app/base.html')


class IndexView(ListView):
    model = UserProfile
    template_name = 'cv_app/index.html'
    context_object_name = 'profile'


class SkillsView(ListView):
    model = Skill
    template_name = 'cv_app/skills.html'
    context_object_name = 'skills'


def about(request):
    return render(request, 'cv_app/about.html')


class PortfolioView(ListView):
    model = Portfolio
    template_name = 'cv_app/portfolio.html'
    context_object_name = 'portfolio'


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'cv_app/register.html'
    success_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'cv_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authorization'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'cv_app/contact.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Page'
        return context
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['content']
        
        if not validate_email(email):
            form.add_error('name', 'Invalid email.')
            return self.form_invalid(form)
        
        Message.objects.create(name=name, email=email, message=message)
        
        return super().form_valid(form)


class PersonalInfoView(ListView):
    model = PersonalInfo
    template_name = 'cv_app/partials/cv_info.html'
    context_object_name = 'personal_info'


class BlogView(ListView):
    model = Message
    template_name = 'cv_app/blog.html'
    context_object_name = 'messages'
    paginate_by = 5

    def get_queryset(self):
        return Message.objects.filter(is_published=True)
