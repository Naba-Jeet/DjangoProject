from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'about/', GreetingView.GreetingView.as_view(), name="greeter"),
    # url(r'name/', views.get_name, name="simple_form"),
    url(r'test_form/', views.add_model),
    # url(r"base_form/", views.basic_form)
]