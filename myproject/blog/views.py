from django.http import HttpResponse

def article_list(request):
    sort = request.GET.get("sort")
    category = request.GET.get("category")

    return HttpResponse(
        f"Sort: {sort}<br>"
        f"Category: {category}"
    )

def article(request, id):
    return HttpResponse(f"Article ID: {id}")

def news(request):
    return HttpResponse("News")