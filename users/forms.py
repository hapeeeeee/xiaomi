from django import forms

from django.contrib.auth import get_user_model
import re
from django.core.exceptions import ValidationError
from users.models import GouWuche

User = get_user_model()

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class UserLoginFORM(forms.ModelForm):
    username = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields= ("password",)
        widgets = {
            "password": forms.PasswordInput()
        }

class UserRegForm(forms.ModelForm):
    username = forms.CharField(max_length=30, min_length=2, error_messages={'required':u'用户名必须大于两个字符'})
    password = forms.CharField(max_length=20, min_length=8, error_messages={'required':u'密码必须大于8位'},widget=forms.PasswordInput())
    password_again = forms.CharField(max_length=20, min_length=8)
    phone = forms.CharField(validators=[mobile_validate, ],
                                error_messages = {'required': u'手机不能为空'},)

    class Meta:
        model = User
        fields = ("username", "password", "phone")
        widgets = {
            "password": forms.PasswordInput(),
            "password_again": forms.PasswordInput()
        }

class GouWuCheSaveForm(forms.ModelForm):

    class Meta:
        model = GouWuche
        fields = ('phone', 'user')