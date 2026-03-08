from django.urls import path, include
from rest_framework import routers
from .views import (
    EventViewSet,
    MemberViewSet,
    LinkViewSet,
    ApplicationViewSet,
    ContactViewSet,
    admin_login,
    check_auth,
)

router = routers.DefaultRouter()
router.register("events", EventViewSet)
router.register("members", MemberViewSet)
router.register("links", LinkViewSet)
router.register("applications", ApplicationViewSet)
router.register("contacts", ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/", check_auth),
    path("admin-login/", admin_login),
]
