from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class AddPostForm(forms.ModelForm):
    DOOR_OPEN = [
        ('yes', 'Да'),
        ('no', 'Нет'),
    ]
    OPINION = [
        ('positive', 'позитивно',),
        ('neutral', 'нейтрально',),
        ('negative', 'негативно',),
    ]

    camp = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}), label="Кампания")
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), label="Город")
    street = forms.ModelChoiceField(queryset=Streets.objects.all(), label="Улица")
    home = forms.ModelChoiceField(queryset=Homes.objects.all(), label="Дом номер")
    entrance = forms.ModelChoiceField(queryset=Entrances.objects.all(), label="Подъезд номер")
    flat = forms.ModelChoiceField(queryset=Flats.objects.all(), label="Квартира номер")
    is_door_open = forms.ChoiceField(widget=forms.RadioSelect(), choices=DOOR_OPEN, label="Дверь открыли?")
    flat_owner = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}),
                                 required=False, label="Владелец квартиры")
    opinion = forms.ChoiceField(widget=forms.RadioSelect, choices=OPINION, label="Мнение", required=False)
    is_published = forms.BooleanField(label="Публикация", initial=True, required=False)

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug

    def clean_title(self):
        camp = self.cleaned_data['camp']

        if len(camp) > 200:
            raise ValidationError('Длинна превышает 200 символов')
        return camp

    def clean_flat_owner(self):
        flat_owner = self.cleaned_data['flat_owner']

        if len(flat_owner) > 200:
            raise ValidationError('Длинна превышает 200 символов')
        return flat_owner

    class Meta:
        model = Promo
        fields = ('camp', 'slug', 'city', 'street', 'home', 'entrance', 'flat', 'is_door_open', 'flat_owner', 'opinion',
                  'is_published')



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Информация', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
