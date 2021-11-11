from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, player_id):
    return HttpResponse("You're looking at question %s." % player_id)

def results(request, player_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % player_id)

def vote(request, player_id):
    return HttpResponse("You're voting on question %s." % player_id)

