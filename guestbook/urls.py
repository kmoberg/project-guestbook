from django.urls import path
from guestbook import views
from guestbook.views import add_guestbook_entry

urlpatterns = [
    path('', views.guestbook_list, name='guestbook'),
    path('api/add-entry', add_guestbook_entry, name='add_guestbook_entry'),
]

