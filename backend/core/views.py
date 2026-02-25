from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, Member, Link, Application, ContactMessage
from .serializers import (
    EventSerializer,
    MemberSerializer,
    LinkSerializer,
    ApplicationSerializer,
    ContactSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.order_by("-date")
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["title", "description"]

    @action(detail=False)
    def conferences(self, request):
        qs = self.get_queryset().filter(type="conference")
        return Response(EventSerializer(qs, many=True).data)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
