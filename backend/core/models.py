from django.db import models


class Event(models.Model):
    TYPE_CHOICES = [
        ("conference", "Conference"),
        ("seminar", "Seminar"),
        ("workshop", "Workshop"),
        ("webinar", "Webinar"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.type})"


class Member(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    CATEGORY_CHOICES = [
        ("society", "Other societies"),
        ("interesting", "Interesting links"),
    ]
    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application from {self.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"
