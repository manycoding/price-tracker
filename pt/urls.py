"""Defines URL patterns for pt."""

from django.urls import path
from . import views

app_name = 'pt'

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),

    # Show all entries
    path(r'entries/', views.entries, name='entries'),

    # Page for adding a new entry
    path(r'new_entry/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path(r'edit_entry/(?P<entry_id>\d+)/', views.edit_entry,
         name='edit_entry'),
]
