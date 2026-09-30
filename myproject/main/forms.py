from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        help_text="Введите ваше имя.",
        initial="Иван",
    )
    email = forms.EmailField(
        label="Ваш Email",
        help_text="Введите ваш действующий адрес электронной почты.",
        initial="example@example.com",
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        help_text="Укажите дату рождения.",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    resume = forms.FileField(
        label="Резюме",
        help_text="Загрузите файл с резюме.",
        required=False,
    )
