from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list),
    path("article/<int:id>/", views.article),
    path("news/", views.news),
]