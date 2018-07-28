from django.conf.urls import url, include
from . import views, GreetingView

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'about/', GreetingView.GreetingView.as_view(), name="greeter"),
    url(r'name/', views.get_name, name="simple_form")
    # url(r'thanks/', include('posts/thanks.html'))
]