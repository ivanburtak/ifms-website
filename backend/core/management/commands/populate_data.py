from django.core.management.base import BaseCommand
from core.models import Event, Member, Link
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **options):
        # Clear existing data
        Event.objects.all().delete()
        Member.objects.all().delete()
        Link.objects.all().delete()

        # Add sample events
        events = [
            Event.objects.create(
                title="Python Conference 2026",
                description="The largest Python conference in Eastern Europe",
                date=datetime.now() + timedelta(days=30),
                type="conference",
            ),
            Event.objects.create(
                title="Web Development Workshop",
                description="Learn modern web development with Vue.js and Django",
                date=datetime.now() + timedelta(days=15),
                type="workshop",
            ),
            Event.objects.create(
                title="AI and Machine Learning Seminar",
                description="Explore the latest trends in AI and ML",
                date=datetime.now() + timedelta(days=45),
                type="seminar",
            ),
            Event.objects.create(
                title="JavaScript Webinar",
                description="Advanced JavaScript concepts and best practices",
                date=datetime.now() + timedelta(days=7),
                type="webinar",
            ),
        ]

        # Add sample members
        members = [
            Member.objects.create(
                name="Іван Петренко",
                bio="Fullstack developer with 5 years of experience",
                photo_url="https://via.placeholder.com/150",
            ),
            Member.objects.create(
                name="Mariya Shevchenko",
                bio="Data scientist and AI enthusiast",
                photo_url="https://via.placeholder.com/150",
            ),
            Member.objects.create(
                name="Dmytro Kovalenko",
                bio="Cloud architect and DevOps expert",
                photo_url="https://via.placeholder.com/150",
            ),
            Member.objects.create(
                name="Olena Bondarenko",
                bio="Frontend specialist with focus on UX/UI",
                photo_url="https://via.placeholder.com/150",
            ),
        ]

        # Add sample links
        links = [
            Link.objects.create(
                title="Python.org", url="https://www.python.org", category="interesting"
            ),
            Link.objects.create(
                title="Vue.js Documentation",
                url="https://vuejs.org",
                category="interesting",
            ),
            Link.objects.create(
                title="Django REST Framework",
                url="https://www.django-rest-framework.org",
                category="interesting",
            ),
            Link.objects.create(
                title="PyCon Ukraine", url="https://pycon.ua", category="society"
            ),
        ]

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with sample data")
        )
