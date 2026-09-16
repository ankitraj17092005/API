from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("api/student/",views.api_post,name='api_post')
]
