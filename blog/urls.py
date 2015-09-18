from dango.cof.urls import include, urls
from . import views

urlspatterns =[
    urls(r'^$', views.post_list),
]
