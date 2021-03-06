import datetime

from django.test import TestCase

from .forms import UserUpdateForm

__all__ = ['ProfileFormTest']


class ProfileFormTest(TestCase):

    def test_valid_form(self):
        form = UserUpdateForm(data={
            'experience': 10,
            'date_of_birth': datetime.date(1999, 12, 1),
            'education': 'Higher',
            'gender': 'Male',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserUpdateForm(data={
            'experience': -1,
            'date_of_birth': datetime.date(1999, 12, 1),
            'education': 'Higher',
            'gender': 'Male',
        })
        self.assertFalse(form.is_valid())
