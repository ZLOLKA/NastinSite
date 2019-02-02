from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='ret'),
    url(r'^test$', views.test, name='test'),
]
