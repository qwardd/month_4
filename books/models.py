from django.db import models

class Books(models.Model):
    GENRE_BOOK = (
        ('роман', 'роман'),
        ('рассказ', 'рассказ'),
        ('лирика', 'лирика')
    )
    title = models.CharField(max_length=30, verbose_name='укажите название книги')
    genre_book = models.CharField(max_length=100, choices=GENRE_BOOK, default='рассказ')
    images = models.ImageField(upload_to='books/', verbose_name="загрузите фото книги")
    link_book = models.URLField(verbose_name='вставьте ссылку на оригинал книги')
    description = models.TextField(verbose_name='описание книги')
    author = models.TextField(max_length=50, verbose_name='укажите автора книги')
    author_img = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    video_url = models.URLField(verbose_name='укажите ссылку с youtube', null=True, blank=True)
    comment = models.TextField(verbose_name='оставьте мнение читателей о книге')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


