from django.urls import path, include
from rest_framework import routers
from .views import (
    EventViewSet,
    MemberViewSet,
    LinkViewSet,
    ApplicationViewSet,
    ContactViewSet,
)

router = routers.DefaultRouter()
router.register("events", EventViewSet)
router.register("members", MemberViewSet)
router.register("links", LinkViewSet)
router.register("applications", ApplicationViewSet)
router.register("contacts", ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
