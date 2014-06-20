from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from assist.models import Item, ItemDetail, Good, GoodDetail
from assist.forms import ItemDetailForm


def assist(request):
    return render(request,'basesite.html')


def add_ItemDetail(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = ItemDetailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = ItemDetailForm()

    return render_to_response('add_ItemDetail.html', {'form': form}, context)

def add_GoodDetail(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = GoodDetailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = GoodDetailForm()

    return render_to_response('add_GoodDetail.html', {'form': form}, context)

# Create your views here.
