from django import forms 
from users.models import CustomerUser 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class LoginWithCaptchaForm(AuthenticationForm):
    captcha = CaptchaField()


GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)

VACANCY = (
    ('frontend', 'frontend'),
    ('backend', 'backend'),
    ('SMM', 'SMM')
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    vacancy = forms.ChoiceField(choices=VACANCY, required=True)


    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'expirience',
            'vacancy',
            'info_about_you'
        )
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.phone_number = self.cleaned_data['phone_number']
            if commit:
                user.save()
            return user