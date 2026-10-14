from django import forms
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        help_text="Введите ваше имя.",
        initial="Иван",
        error_messages={"required": "Поле имени обязательно для заполнения."},
    )
    email = forms.EmailField(
        required=False,
        label="Ваш Email",
        help_text="Введите ваш действующий адрес электронной почты.",
        initial="example@example.com",
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        help_text="Укажите дату рождения.",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    password = forms.CharField(
        label="Пароль",
        help_text="Пароль должен содержать не менее 8 символов.",
        widget=forms.PasswordInput,
        min_length=8,
        error_messages={"min_length": "Пароль должен содержать как минимум 8 символов."},
    )
    resume = forms.FileField(
        label="Резюме",
        help_text="Загрузите файл с резюме.",
        required=False,
    )
