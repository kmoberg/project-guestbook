from django.shortcuts import render
from .models import GuestbookEntry
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

API_KEY = 'demo'


@api_view(['POST'])
def add_guestbook_entry(request):
    """
    Allows API access to add entries to the guestbook with the correct API key.
    """
    api_key = request.headers.get('X-API-Key')

    if api_key != API_KEY:
        return Response({"detail": "Invalid API key"}, status=status.HTTP_403_FORBIDDEN)

    name = request.data.get('name')
    message = request.data.get('message')
    rating = request.data.get('rating', 5)  # Default to 5 if not provided

    if not name or not message:
        return Response({"detail": "Name and message are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        rating = int(rating)
    except ValueError:
        return Response({"detail": "Rating must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

    if not (1 <= rating <= 5):
        return Response({"detail": "Rating must be between 1 and 5."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the new guestbook entry
    GuestbookEntry.objects.create(name=name, message=message, rating=rating)

    return Response({"detail": "Entry added successfully!"}, status=status.HTTP_201_CREATED)


def guestbook_list(request):
    entries = GuestbookEntry.objects.filter(hidden=False).order_by('-created_at')
    for entry in entries:
        entry.rating = entry.rating if entry.rating is not None else 5
        entry.unfilled_stars = 5 - entry.rating  # Calculate the unfilled stars

    environment = settings.ENVIRONMENT  # Access the ENVIRONMENT value from settings
    data_store = settings.DATA_STORE  # Access the DATA_STORE value from settings

    return render(request, 'guestbook_list.html', {
        'entries': entries,
        'environment': environment,
        'data_store': data_store,
    })


def hello_world(request):
    return render(request, 'hello_world.html', {})
