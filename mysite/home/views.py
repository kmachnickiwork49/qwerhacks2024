import random
from django.http import Http404
from django.shortcuts import render

from prompts.models import *

def main(request):
    question_list = Question.objects.all()
    randPrompt = random.choice(question_list)
    context = {
        "prompt": randPrompt,
        "respPostURL": request.build_absolute_uri('/'),
        "responses": Response.objects.filter(question_id=randPrompt.id),
    }
    return render(request, "home/main.html", context)