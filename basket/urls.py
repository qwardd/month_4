from django.urls import path 
from . import views 


urlpatterns = [
    path('basket_list/', views.read_basket_views, name='basket_list'),
    path('create_basket/', views.create_basket_views, name='create_basket'),
    path('update_basket/<int:id>/', views.update_basket_views, name='update_basket'),
    path('delete_basket/<int:id>/', views.delete_basket_views, name='delete_basket'),
    
]