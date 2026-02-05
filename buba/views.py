from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import GalleryImage, Project

class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Вітаємо, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Неправильний логін або пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація успішна!')
            return redirect('home')
        else:
            messages.error(request, 'Помилка реєстрації.')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'Ви вийшли з акаунту.')
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, "users/profile.html")

class TopicListView(View):
    def get(self, request):
        return render(request, "forum/topic_list.html")


class TopicDetailView(View):
    def get(self, request, pk):
        return render(request, "forum/topic_detail.html", {"topic_id": pk})


class PostCreateView(View):
    def get(self, request, pk):
        return render(request, "forum/post_create.html", {"topic_id": pk})

class GradeListView(View):
    def get(self, request):
        return render(request, "diary/grade_list.html")


class GradeCreateView(View):
    def get(self, request):
        return render(request, "diary/grade_add.html")

class EventListView(View):
    def get(self, request):
        return render(request, "events.html")


class EventCreateView(View):
    def get(self, request):
        return render(request, "events/event_add.html")


class EventUpdateView(View):
    def get(self, request, pk):
        return render(request, "events/event_edit.html", {"event_id": pk})


class EventDeleteView(View):
    def get(self, request, pk):
        return render(request, "events/event_delete.html", {"event_id": pk})

class PollView(View):
    def get(self, request, pk):
        return render(request, "polls/poll.html", {"poll_id": pk})


class VoteView(View):
    def get(self, request, pk):
        return render(request, "voting/vote.html", {"vote_id": pk})

class AnnouncementListView(View):
    def get(self, request):
        return render(request, "announcements.html")


class MaterialListView(View):
    def get(self, request):
        return render(request, "materials/list.html")

@login_required
def portfolio_view(request):
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'portfolio.html', {'projects': projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        Project.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            technologies=request.POST.get('technologies', ''),
            project_url=request.POST.get('project_url', ''),
            github_url=request.POST.get('github_url', ''),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Проєкт додано!')
    return redirect('portfolio')

def gallery_view(request):
    images = GalleryImage.objects.filter(is_public=True).select_related('user')
    return render(request, 'gallery.html', {'all_gallery_images': images})


@login_required
def add_gallery_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        description = request.POST.get('description', '')

        if photo:
            GalleryImage.objects.create(
                user=request.user,
                photo=photo,
                description=description
            )
            messages.success(request, 'Фото додано в галерею!')
        else:
            messages.error(request, 'Оберіть фото.')

    return redirect('gallery')

