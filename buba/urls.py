from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile_view, name='profile'),

    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/add/', views.add_project, name='add_project'),

    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/add/', views.add_gallery_photo, name='add_gallery_photo'),

    path('forum/', views.TopicListView.as_view(), name='forum'),
    path('forum/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('forum/<int:pk>/post/', views.PostCreateView.as_view(), name='post_create'),
    path('grades/', views.GradeListView.as_view(), name='grades'),
    path('grades/add/', views.GradeCreateView.as_view(), name='grade_add'),

    path('events/', views.EventListView.as_view(), name='events'),
    path('events/add/', views.EventCreateView.as_view(), name='event_add'),
    path('events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_edit'),
    path('events/<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_delete'),

    path('poll/<int:pk>/', views.PollView.as_view(), name='poll'),
    path('vote/<int:pk>/', views.VoteView.as_view(), name='vote'),

    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('materials/', views.MaterialListView.as_view(), name='materials'),
]
