from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Basket(models.Model):
    CHOICE_TYPE = (
        ('Выполнено', 'Выполнено'),
        ('Не выполнено', 'Не выполнено')
    )
    name = models.CharField(max_length=10, verbose_name='Введите имя')
    surname = models.CharField(max_length=15, verbose_name='Введите фамилию')
    phone_number = PhoneNumberField(region="KG", unique=True)
    card_number = models.CharField(max_length=16, verbose_name='Введите номер карты')
    choice_type = models.CharField(max_length=100, verbose_name='выберите статус заказа', choices=CHOICE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} - {self.choice_type}'
