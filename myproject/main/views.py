from django.http import HttpResponse

def hello(request,id):
    return HttpResponse(f"lmfao {id}")

def goodbye(request,code):
    return HttpResponse(f"lmfao {code}")

def lol(request, one, two):
    return HttpResponse(f"one-{one}, two-{two}")