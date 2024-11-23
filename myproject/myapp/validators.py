import re
from django.core.exceptions import ValidationError

def validate_password_strength(value):

    if len(value) < 6:
        raise ValidationError('Mật khẩu phải có ít nhất 6 ký tự.')
    if not any(char.isupper() for char in value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 chữ số.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt.')

