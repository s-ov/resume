from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('cv_info', PersonalInfoView.as_view(), name='cv_info')
]
