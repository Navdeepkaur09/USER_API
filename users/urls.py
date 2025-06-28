from django.urls import path
from . import views

urlpatterns=[
    path('users/',views.user_view,name='users'),
    path('users/<str:user_id>/',views.user_view,name='users_detail')
]