from django.test import TestCase

from .forms import UserRegistrationForm


class UserRegistrationFormTests(TestCase):
    def test_fields_are_configured_for_registration_form(self):
        form = UserRegistrationForm()

        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("birth_date", form.fields)
        self.assertIn("password", form.fields)
        self.assertIn("resume", form.fields)

        self.assertEqual(form.fields["name"].label, "Имя")
        self.assertEqual(form.fields["email"].label, "Ваш Email")
        self.assertEqual(form.fields["birth_date"].label, "Дата рождения")
        self.assertEqual(form.fields["password"].label, "Пароль")
        self.assertEqual(form.fields["resume"].label, "Резюме")

        self.assertTrue(form.fields["name"].help_text)
        self.assertTrue(form.fields["email"].help_text)
        self.assertTrue(form.fields["birth_date"].help_text)
        self.assertTrue(form.fields["password"].help_text)
        self.assertTrue(form.fields["resume"].help_text)

    def test_required_name_and_password_length_are_validated(self):
        form = UserRegistrationForm({
            "name": "",
            "email": "user@example.com",
            "birth_date": "2000-01-01",
            "password": "short",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("password", form.errors)

        self.assertIn("Поле имени обязательно для заполнения.", form.errors["name"])
        self.assertIn("Пароль должен содержать как минимум 8 символов.", form.errors["password"])

    def test_valid_form_passes_validation(self):
        form = UserRegistrationForm({
            "name": "Иван",
            "email": "user@example.com",
            "birth_date": "2000-01-01",
            "password": "password123",
        })

        self.assertTrue(form.is_valid())
