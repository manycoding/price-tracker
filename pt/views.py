from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm


def index(request):
    """The home page for Price Tracker"""
    return render(request, 'pt/index.html')


def entries(request):
    """Show all entries"""
    entries = Entry.objects.order_by('date_updated')
    context = {'entries': entries}
    return render(request, "pt/entries.html", context)


def new_entry(request):
    """Add a new entry"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('pt:entries'))

    context = {'form': form}
    return render(request, 'pt/new_entry.html', context)
