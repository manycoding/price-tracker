from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry
from .forms import EntryForm
import pt.fetcher as f


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
            new_entry = form.save(commit=False)
            price, date = f.get_price_data(new_entry.url)
            new_entry.date_updated = date
            new_entry.price = price
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('pt:entries'))

    context = {'form': form}
    return render(request, 'pt/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pt:entry',
                                                args=[entry.id]))
    context = {'entry': entry, 'form': form}

    return render(request, 'pt/edit_entry.html', context)
