from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import book_ru, book_en, book_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_ru/', book_ru, name='book_ru'),
    path('book_en/', book_en, name='book_en'),
    path('book_us/', book_us, name='book_us'),
]
urlpatterns     += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns     += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)