from django.urls import path 
from . import views 


urlpatterns = [
    path('basket_list/', views.ReadBasketViews.as_view(), name='basket_list'),
    path('create_basket/', views.CreateBasket.as_view(), name='create_basket'),
    path('update_basket/<int:id>/', views.UpdateBasketViews.as_view(), name='update_basket'),
    path('delete_basket/<int:id>/', views.DeleteBasketViews.as_view(), name='delete_basket'),
    
]