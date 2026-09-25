from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"
    extra_context = {
        "title": "Главная страница",
        "intro": "Статические файлы и базовые шаблоны в Django",
    }


class ContactView(TemplateView):
    template_name = "main/contact.html"
    extra_context = {
        "title": "Контакты",
        "email": "student@example.com",
    }

def hello(request,id):
    response=HttpResponse(f"lmfao {id}")
    response.set_cookie("mycookie", id)
    return response

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

def contact_us(request):
    return HttpResponse("We dont have number lmao")

def idk(request):
    return redirect("/contact-us/")

def not_found(request, unmatched_route):
    return HttpResponse("404 Not Found", status=404)

def things(request):
    j={
        "Bag": 100,
        "Box": 50,
        "Gun": 0
    }
    return JsonResponse(j)

def get_cookie(request):
    cookie_value=request.COOKIES.get("mycookie")
    if cookie_value:
        return HttpResponse(f"Cookie value: {cookie_value}")
    else:
        return HttpResponse("Cookie not found")


def form_example(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message = (request.POST.get("message") or "").strip()

        if not name or not email:
            return render(request, "main/form.html", {
                "error": "Заполните имя и email.",
                "name": name,
                "email": email,
                "message": message,
            })

        return render(request, "main/form.html", {
            "success": True,
            "name": name,
            "email": email,
            "message": message,
        })

    return render(request, "main/form.html")


def tasks(request):
    return render(request, "main/tasks.html", {
        "tasks": [
            "купить продукты",
            "изучить шаблоны Django",
            "сделать домашнее задание",
        ],
    })