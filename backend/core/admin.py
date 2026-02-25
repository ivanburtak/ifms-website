from django.contrib import admin
from .models import Event, Member, Link, Application, ContactMessage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "date")
    list_filter = ("type",)
    search_fields = ("title", "description")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "bio")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("created_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("created_at",)
