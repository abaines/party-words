from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from players.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'players/index.html', context)


def detail(request, player_id):
    return HttpResponse("You're looking at question %s." % player_id)

def results(request, player_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % player_id)

def vote(request, player_id):
    return HttpResponse("You're voting on question %s." % player_id)

