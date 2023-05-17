from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

    first_name = forms.CharField(label='Họ')
    last_name = forms.CharField(label='Tên')
    username = forms.CharField(label='Tên đăng nhập')
    password = forms.CharField(label='Mật khẩu')


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

    first_name = forms.CharField(label='Tên')
    last_name = forms.CharField(label='Họ')
    username = forms.CharField(label='Tên đăng nhập')
    password = forms.CharField(label='Mật khẩu')

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']

    enrollment = forms.CharField(label='Mã sinh viên')
    branch = forms.CharField(label='Ngành')

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category','image','noidung']

    name = forms.CharField(label='Tên sách')
    author = forms.CharField(label='Tác giả')
    category = forms.CharField(label='Thể loại')
    image = forms.ImageField(label='Ảnh')
    noidung = forms.FileField(label='Nội dung')
class IssuedBookForm(forms.Form):
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Tên sách và mã sách", to_field_name="isbn",label='Tên sách và mã sách')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Tên sinh viên và mã sinh viên",to_field_name='enrollment',label='Tên sinh viên và mã sinh viên')
    
