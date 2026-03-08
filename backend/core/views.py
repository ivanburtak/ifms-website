from django.contrib.auth import authenticate
from rest_framework import viewsets, filters
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Event, Member, Link, Application, ContactMessage
from .serializers import (
    EventSerializer,
    MemberSerializer,
    LinkSerializer,
    ApplicationSerializer,
    ContactSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.order_by("-date")
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["title", "description"]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action in ["list", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [p() for p in permission_classes]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_auth(request: Request) -> Response:
    user = request.user
    if not user.is_staff:
        return Response({"detail": "Not staff"}, status=403)
    return Response({"username": user.username, "is_staff": user.is_staff})


@api_view(["POST"])
def admin_login(request: Request) -> Response:
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=401)

    if not user.is_staff:
        return Response({"error": "Not staff"}, status=403)

    refresh = RefreshToken.for_user(user)
    return Response({"access": str(refresh.access_token), "refresh": str(refresh)})
