from django.shortcuts import render
from django.views import View


# Головна сторінка
class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
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
        return render(request, "events/event_list.html")


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
        return render(request, "announcements/list.html")


class MaterialListView(View):
    def get(self, request):
        return render(request, "materials/list.html")

class PortfolioListView(View):
    def get(self, request):
        return render(request, "portfolio/list.html")


class GalleryListView(View):
    def get(self, request):
        return render(request, "gallery/list.html")
