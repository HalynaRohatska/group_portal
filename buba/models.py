from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class User(AbstractUser):
    ROLE_CHOICES = (
        ("user", "User"),
        ("moderator", "Moderator"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")





# Теми форуму (кожна тема – окрема дискусія)
class Topic(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Повідомлення у темі форуму
class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Електронний щоденник: оцінки учнів
class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)


# Події / календар: показує події групи
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.title



# Опитування: багатоступеневі або прості
class Poll(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

# Питання в опитуванні
class PollQuestion(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

# Відповіді на питання
class PollAnswer(models.Model):
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

# Результати опитування користувачів
class PollResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answer = models.ForeignKey(PollAnswer, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)


# Голосування: кожне голосування має варіанти
class Voting(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

# Варіанти голосування
class VotingOption(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

# Результати голосування користувачів
class VotingResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    option = models.ForeignKey(VotingOption, on_delete=models.CASCADE)


# Оголошення: новини та важливі повідомлення групи
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Матеріали: файли, посилання, відео
class Material(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="materials/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Портфоліо: роботи учнів, проекти
class Portfolio(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)


# Галерея: фото та відео учнів
class GalleryItem(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="gallery/")
    approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class GalleryImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_images')
    photo = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)  # можна додати, якщо захочеш колись приватні фото

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.user.username} - {self.description or 'Без назви'}"