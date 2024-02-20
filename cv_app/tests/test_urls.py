from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cv_app.views import *


class TestUrls(SimpleTestCase):
    
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_skils_url(self):
        url = reverse('skills')
        self.assertEqual(resolve(url).func.view_class, SkillsView)

    def test_portfolio_url(self):
        url = reverse('portfolio')
        self.assertEqual(resolve(url).func.view_class, PortfolioView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterUserView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginUserView)

    def test_logout_url(self):
        url = reverse('logout_user')
        self.assertEqual(resolve(url).func, logout_user)

    def test_contact_url(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_cv_info_url(self):
        url = reverse('cv_info')
        self.assertEqual(resolve(url).func.view_class, PersonalInfoView)

    def test_blog_url(self):
        url = reverse('blog')
        self.assertEqual(resolve(url).func.view_class, BlogView)
