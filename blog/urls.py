from dango.cof.urls import include, urls
from . import views

urlspatterns =[
    url(r'^$', views.post_list),
]
