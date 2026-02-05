from django.shortcuts import render
from django.views import View


@login_required
def add_gallery_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        description = request.POST.get('description', '')

        if photo:
            image = GalleryImage(
                user=request.user,
                photo=photo,
                description=description
            )
            image.save()
            messages.success(request, 'Фото успішно додано в галерею!')
        else:
            messages.error(request, 'Оберіть фото для завантаження.')

    return redirect('gallery')

@login_required
def portfolio_view(request):
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'portfolio.html', {'projects': projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        project = Project(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            technologies=request.POST.get('technologies', ''),
            project_url=request.POST.get('project_url', ''),
            github_url=request.POST.get('github_url', ''),
            image=request.FILES.get('image')
        )
        project.save()

    return redirect('portfolio')

# Головна сторінка
class HomeView(View):
    def get(self, request):
        return render(request, "index.html")
class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")


class UserLoginView(View):
    def get(self, request):
        return render(request, "users/login.html")


# Вихід із системи
class UserLogoutView(View):
    def get(self, request):
        return render(request, "users/logout.html")


# Профіль користувача
class ProfileView(View):
    def get(self, request):
        return render(request, "users/profile.html")

class TopicListView(View):
    def get(self, request):
        return render(request, "forum/topic_list.html")


# Перегляд однієї теми
class TopicDetailView(View):
    def get(self, request, pk):
        return render(request, "forum/topic_detail.html", {"topic_id": pk})


# Додавання повідомлення
class PostCreateView(View):
    def get(self, request, pk):
        return render(request, "forum/post_create.html", {"topic_id": pk})

# Список оцінок
class GradeListView(View):
    def get(self, request):
        return render(request, "diary/grade_list.html")


# Додавання оцінки
class GradeCreateView(View):
    def get(self, request):
        return render(request, "diary/grade_add.html")

class EventListView(View):
    def get(self, request):
        return render(request, "events.html")


# Додавання події
class EventCreateView(View):
    def get(self, request):
        return render(request, "events/event_add.html")

class EventUpdateView(View):
    def get(self, request, pk):
        return render(request, "events/event_edit.html", {"event_id": pk})


# Видалення події
class EventDeleteView(View):
    def get(self, request, pk):
        return render(request, "events/event_delete.html", {"event_id": pk})

# Перегляд опитування
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

class PortfolioListView(View):
    def get(self, request):
        return render(request, "portfolio.html")


class GalleryListView(View):
    def get(self, request):
        return render(request, "gallery.html")

def gallery_view(request):
    images = GalleryImage.objects.filter(is_public=True).select_related('user')
    return render(request, 'gallery.html', {'all_gallery_images': images})
