from ssl import OP_NO_COMPRESSION
from strategy.LUIS_strategy import *
from CogAsst.util  import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse


@csrf_exempt
def index(request):
    context = {}
    context['sentence'] = 'test sentence'
    return render(request, 'index.html', context)


@csrf_exempt
def result_web(request):
    print(request.POST)
    userid = request.POST.get("userid")
    context = OnMessage(userid, request.POST.get("sentence"))
    context['id'] = userid
    return render(request, 'result.html', context)

@csrf_exempt
def result(request):
    print(request.POST)
    userid = request.POST.get("userid")
    context = OnMessage(userid, request.POST.get("sentence"))
    context['id'] = userid
    return JsonResponse({
        'code': 200,
        'data': context
    }, status=200)