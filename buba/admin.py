from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username']


class TopicAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['content', 'author__username']


class GradeAdmin(admin.ModelAdmin):
    search_fields = ['student__username', 'subject']


class EventAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']


class PollAdmin(admin.ModelAdmin):
    search_fields = ['title']


class VoteAdmin(admin.ModelAdmin):
    search_fields = ['user__username']


class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']


class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']


class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Gallery, GalleryAdmin)
