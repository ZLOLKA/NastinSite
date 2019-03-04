from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'(?P<product_slug>[-\w]+)', views.product_view, name='product'),
    url(r'^test$', views.test, name='test'),
]
