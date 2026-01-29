"""
URL configuration for biba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('forum/', TopicListView.as_view(), name='forum'),
    path('forum/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('forum/<int:pk>/post/', PostCreateView.as_view(), name='post_create'),

    path('grades/', GradeListView.as_view(), name='grades'),
    path('grades/add/', GradeCreateView.as_view(), name='grade_add'),

    path('events/', EventListView.as_view(), name='events'),
    path('events/add/', EventCreateView.as_view(), name='event_add'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    path('poll/<int:pk>/', PollView.as_view(), name='poll'),

    path('vote/<int:pk>/', VoteView.as_view(), name='vote'),

    path('announcements/', AnnouncementListView.as_view(), name='announcements'),
    path('materials/', MaterialListView.as_view(), name='materials'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),

    path('gallery/', GalleryListView.as_view(), name='gallery'),
]
