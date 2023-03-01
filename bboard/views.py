from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb


# Create your views here.


def index(request):
    bbs = Bb.objects.all()

    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))

    return render(request, 'bboard/index.html', {'bbs': bbs})


def about(request):
    return HttpResponse('about')


def hello(request):
    return HttpResponse('hello')
