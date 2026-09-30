from django.test import TestCase

from .forms import UserRegistrationForm


class UserRegistrationFormTests(TestCase):
    def test_fields_are_configured_for_registration_form(self):
        form = UserRegistrationForm()

        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("birth_date", form.fields)
        self.assertIn("resume", form.fields)

        self.assertEqual(form.fields["name"].label, "Имя")
        self.assertEqual(form.fields["email"].label, "Ваш Email")
        self.assertEqual(form.fields["birth_date"].label, "Дата рождения")
        self.assertEqual(form.fields["resume"].label, "Резюме")

        self.assertTrue(form.fields["name"].help_text)
        self.assertTrue(form.fields["email"].help_text)
        self.assertTrue(form.fields["birth_date"].help_text)
        self.assertTrue(form.fields["resume"].help_text)
