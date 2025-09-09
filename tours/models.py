from django.db import models

class Tourist(models.Model):
    name = models.CharField(max_length=10, verbose_name='как вас зовут ?')
    surname = models.CharField(max_length=15, verbose_name='Ваша фамилия ?')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туриста"


class Tour(models.Model):
    tourist = models.OneToOneField(Tourist, on_delete=models.CASCADE, related_name='tourist')
    date = models.CharField(max_length=100, verbose_name="Введите дату тура")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tourist} - {self.date}'
    

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"




    

