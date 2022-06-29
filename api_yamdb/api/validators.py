from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_user_is_me(value):
    if value == 'me':
        raise ValidationError(
            'Запрещено использовать имя пользователя me'
        )


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год %(value)s больше текущего!'),
            params={'value': value},
        )
