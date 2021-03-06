# chat/views.py
from django.shortcuts import render, redirect
from django.db import transaction
from haikunator import Haikunator
from . import serializers
from . import models
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# ToDo Item #2 (hopeful for code reuse from src/docker/django-docker/djangoapp/{chat,static}) The game and the chat are not integrated.
# ToDo Item #3 (hopeful for code reuse from src/docker/django-docker/djangoapp/{chat,static}) The chat and the backend are not integrated.
# ToDo Item #4 The chat does not use usernames; it allows you to define your own handle.
# ToDo Item #5 The chat is not stateful. The old chat was stateful (it saved every message to the database) so we should be able to reuse most or all of the backend code there.

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint for games.
    """

    queryset = models.Room.objects.all().order_by("-date_created")
    serializer_class = serializers.RoomSerializer


def about(request):
    return render(request, "chat/about.html")


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    haikunator = Haikunator()
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if models.Room.objects.filter(label=label).exists():
                continue
            new_room = models.Room.objects.create(label=label)
        new_room.save()
    return redirect(chat_room, label=label)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = models.Room.objects.get_or_create(label=label)
    room.save()
    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by("-timestamp")[:50])
    return render(request, "chat/room.html", {"room": room, "messages": messages})
