from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import Http404
from django.template import loader

from players.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'players/index.html', context)


def detail(request, player_id):
    # TODO: https://docs.djangoproject.com/en/3.2/intro/tutorial03/#a-shortcut-get-object-or-404
    try:
        question = Question.objects.get(pk=player_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'players/detail.html', {'question': question})

def results(request, player_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % player_id)

def vote(request, player_id):
    return HttpResponse("You're voting on question %s." % player_id)

