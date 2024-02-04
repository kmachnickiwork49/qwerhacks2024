import random
from django.http import Http404
from django.shortcuts import render

from prompts.models import *

def main(request):
    question_list = Question.objects.all()
    context = {
        "prompt": random.choice(question_list),
    }
    return render(request, "home/main.html", context)