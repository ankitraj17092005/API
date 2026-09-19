from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name='index'),
    path('api/student/',csrf_exempt(views.apiView.as_view()),name='profile'),
    path('api/student/<int:id>/',csrf_exempt(views.apiView.as_view()),name='one_profile')
]
