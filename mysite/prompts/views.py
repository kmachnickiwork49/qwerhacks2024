from django.http import Http404
from django.shortcuts import render

from .models import *

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "prompts/index.html", context)

def details(request, prompt_id):
    try:
        question = Question.objects.get(pk=prompt_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    responses = Response.objects.filter(question_id=question)
    return render(request, "prompts/detail.html", {"question": question,  "responses": responses})