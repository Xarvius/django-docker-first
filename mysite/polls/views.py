from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   context = {
       'latest_question_list': latest_question_list,
   }
   return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("Question id: " % question_id)


def results(request, question_id):
    response = "Results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Voting on question" % question_id)
