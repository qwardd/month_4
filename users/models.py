from django.db import models
from django.contrib.auth.models import User 

GENDER = (
    ('М', "М"),
    ('Ж', 'Ж')
)

VACANCY = (
    ('frontend', 'frontend'),
    ('backend', 'backend'),
    ('SMM', 'SMM')
)
class CustomerUser(User):
    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    phone_number = models.CharField(max_length=11, default='+996')
    expirience = models.CharField(max_length=300)
    vacancy = models.CharField(max_length=100, choices=VACANCY )
    info_about_you = models.CharField(max_length=500)

    def __str__(self):
        return self.username

