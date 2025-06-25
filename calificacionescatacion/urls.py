from django.urls import path
from . import views
urlpatterns = [
    #path('', views.registro_login_usuario, name='registro'),
    path('', views.admindasboard, name='dashboard'),
    path('formularioCata',views.formcoex, name='formcoex')

]