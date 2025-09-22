from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import  SearchView, BookDetailView, BookenPageView, BookListView, BookruPageView, BookusPageView
from tours.views import ToursDetailView, ToursListViews
from clothes.views import AllClothesViews, ChildClothesViews, TeenClothesViews, AdultClothesViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_ru/', BookruPageView.as_view(), name='book_ru'),
    path('book_en/', BookenPageView.as_view(), name='book_en'),
    path('book_us/', BookusPageView.as_view(), name='book_us'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('tour_list/', ToursListViews.as_view(), name='tour_list'),
    path('tour_list/<int:id>/', ToursDetailView.as_view(), name='tourist_detail'),
    path('', include('basket.urls')),
    path('', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('search/', SearchView.as_view(), name='search'),
    path('all_clothes/', AllClothesViews.as_view(), name='all_clothes'),
    path('child_clothes/', ChildClothesViews.as_view(), name='child_clothes'),
    path('teen_clothes/', TeenClothesViews.as_view(), name='teen_clothes'),
    path('adult_clothes/', AdultClothesViews.as_view(), name='adult_clothes'),
]
urlpatterns     += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns     += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)