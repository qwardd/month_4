from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import book_ru, book_en, book_us, book_detail, book_list
from tours.views import tour_list, tourist_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_ru/', book_ru, name='book_ru'),
    path('book_en/', book_en, name='book_en'),
    path('book_us/', book_us, name='book_us'),
    path('book_list/', book_list, name='book_list'),
    path('book_list/<int:id>/', book_detail, name='book_detail'),
    path('tour_list/', tour_list, name='tour_list'),
    path('tour_list/<int:id>/', tourist_detail, name='tourist_detail'),
]
urlpatterns     += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns     += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)