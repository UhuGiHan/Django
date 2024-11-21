from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def validate_password_strength(value):
    """
    Kiểm tra độ mạnh của mật khẩu:
    - Ít nhất 6 ký tự
    - Ít nhất 1 chữ cái viết hoa
    - Ít nhất 1 số
    - Ít nhất 1 ký tự đặc biệt
    """
    if len(value) < 6:
        raise ValidationError('Mật khẩu phải có ít nhất 6 ký tự.')
    if not any(char.isupper() for char in value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 chữ số.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError('Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt.')

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Mật khẩu",
        validators=[validate_password_strength]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Nhập lại mật khẩu"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        # Kiểm tra nếu mật khẩu và xác nhận mật khẩu không khớp
        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu và mật khẩu xác nhận không khớp.")
        
        return cleaned_data
