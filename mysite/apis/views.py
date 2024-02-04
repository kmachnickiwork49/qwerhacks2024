import datetime
import json
from django.http import QueryDict
from django.shortcuts import render
from prompts.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def profile(request):
    print("=================================================")
    data = json.loads(request.body)
    print(data)
    newResp = Response()
    newResp.response_text = data.get("response")
    newResp.pub_date = datetime.datetime.now()
    newResp.question_id = Question.objects.get(id=4)
    newResp.save()
    return render(request, "apis/responsePost.html", {"profile": data})