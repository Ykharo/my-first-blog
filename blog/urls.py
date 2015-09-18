from django.conf.urls import include, url
from . import views

urlspatterns =[
    url(r'^$', views.post_list),
]
