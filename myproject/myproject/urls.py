from django.contrib import admin
from django.urls import path, re_path, include
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/<int:id>/", views.hello),
    re_path("^item/(?P<code>[a-zA-z0-9]+)/$",views.goodbye),
    path("one/<str:one>/two/<int:two>",views.lol),
    path("info/",views.request_info),
    path("par/<str:name>/<int:age>",views.parameters),
    path("custom",views.custom),
    path("blog/", include("blog.urls")),
]