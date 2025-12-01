from django.urls import path
from myapp import views

urlpatterns = [
    path('register/', views.reg, name="register"),
    path('login/', views.login, name="login"),
    path('get/', views.get_data, name="get"),
    path('del/', views.delete_data, name="del"),

    path('update/', views.update_data, name="update"),
]