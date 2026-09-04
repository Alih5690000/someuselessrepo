from django.http import HttpResponse

def hello(request,id):
    return HttpResponse(f"lmfao {id}")

def goodbye(request,code):
    return HttpResponse(f"lmfao {code}")

def lol(request, one, two):
    return HttpResponse(f"one-{one}, two-{two}")

def request_info(request):
    return HttpResponse(f"""
    Method: {request.method}<br>
    Path: {request.path}<br>
    Headers: {dict(request.headers)}<br>
    """)

def parameters(request,name,age):
    return HttpResponse(f"""
    Name: {name}
    Age: {age}
    """)

def custom(request):
    response=HttpResponse("Check headers in developer console!")

    response["Number"]=67
    return response