from django import forms

__all__ = ['ProfileValidator', 'PValidationError']


class CAError(Exception):
    pass


class PValidationError(CAError, ValueError):
    pass


MIN_YEARS_OF_EXPERIENCE = 0
MAX_YEARS_OF_EXPERIENCE = 100


class ProfileValidator:
    @staticmethod
    def validate(rq_data):
        experience = rq_data.get('experience')

        if not isinstance(experience, int):
            raise forms.ValidationError('Only integer values are supported')

        elif not MIN_YEARS_OF_EXPERIENCE < experience < MAX_YEARS_OF_EXPERIENCE:
            raise forms.ValidationError(
                f'Enter correct data (from {MIN_YEARS_OF_EXPERIENCE} to'
                f' {MAX_YEARS_OF_EXPERIENCE})')

        return experience
