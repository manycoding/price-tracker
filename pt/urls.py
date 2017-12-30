"""Defines URL patterns for pt."""

from django.urls import path
from . import views

app_name = 'pt'

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),

    # Show all entries
    path(r'entries/', views.entries, name='entries'),

    # Entry page
    path('entries/<int:entry_id>/', views.entry,
         name='entry'),

    # Page for adding a new entry
    path(r'new_entry/', views.new_entry, name='new_entry'),

    # Page for removing an entry
    path('remove_entry/<int:entry_id>/', views.remove_entry,
         name='remove_entry'),
]
