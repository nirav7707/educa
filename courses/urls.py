from django.urls import path
from . import views

urlpatterns=[
    path('accounts/login',views.signin,name='login'),
    path('accounts/logout',views.logoutUser,name='logout'),
]