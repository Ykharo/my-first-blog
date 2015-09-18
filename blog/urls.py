from django.conf.urls import include, urls
from . import views

urlspatterns =[
    url(r'^$', views.post_list),
]
