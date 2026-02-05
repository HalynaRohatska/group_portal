from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery/', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('events/', TemplateView.as_view(template_name='events.html'), name='events'),
    path('announcements/', TemplateView.as_view(template_name='announcements.html'), name='announcements'),

    # Auth views (require templates under users/ or default)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
