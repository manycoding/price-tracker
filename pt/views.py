from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from graphos.renderers.gchart import LineChart
from graphos.sources.model import ModelDataSource

from .models import Entry
from .models import Price
from .forms import EntryForm
import pt.fetcher as f
import pt.parser as p


def index(request):
    """The home page for Price Tracker"""
    return render(request, 'pt/index.html')


@login_required
def entries(request):
    """Show all entries"""
    entries = Entry.objects.filter(owner=request.user).order_by('id')
    context = {'entries': entries}
    return render(request, "pt/entries.html", context)


@login_required
def entry(request, entry_id):
    """Show an entry"""
    entry = get_object_or_404(Entry, id=entry_id)
    # Make sure the entry belongs to the current user.
    if entry.owner != request.user:
        raise Http404

    prices = entry.price_set.order_by('date')
    data_source = ModelDataSource(prices, fields=['date', 'price'])
    chart = LineChart(data_source)

    context = {'entry': entry, 'prices': prices, 'chart': chart}
    return render(request, "pt/entry.html", context)


@login_required
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
            new_entry.owner = request.user
            new_entry.url = p.clip_parameters(new_entry.url)
            price, date = f.get_price_data(new_entry.url)
            if price:
                # new_entry.date = date
                # new_entry.price = price
                new_entry.owner = request.user
                new_entry.save()
                new_price = Price(entry=new_entry, price=price, date=date)
                new_price.save()

                return HttpResponseRedirect(reverse('pt:entries'))

    context = {'form': form}
    return render(request, 'pt/new_entry.html', context)


@login_required
def remove_entry(request, entry_id):
    """Remove an entry"""
    entry = Entry.objects.get(id=entry_id)
    if entry.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # DELETE entry
        entry.delete()
        return HttpResponseRedirect(reverse('pt:entries'))

    context = {'entry': entry, 'form': form}
    return render(request, 'pt/remove_entry.html', context)
