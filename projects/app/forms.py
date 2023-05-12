from django import forms
from .models import *
from django.core import validators
from django.core.exceptions import ValidationError
class CategoryForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }),validators=[validators.MinLengthValidator(3,"minimum Three character"),validators.ValidationError],

    )

    def clean_my_field(self):
        data = self.cleaned_data['Name']
        if len(data) == "":
            raise forms.ValidationError("Input must be at least 5 characters long")
        return data




    class Meta:
        model = Category
        fields = ['Name']



class SubCategoryForm(forms.ModelForm):


        Field_Name=forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),validators=[
            RegexValidator(
                '^[a-zA-Z ]+$',
                message="Name"
            ),validators.MinLengthValidator(3,"minimum Three character")
        ])

        def clean_my_field(self):
            data = self.cleaned_data['Field_Name']
            if len(data) < 0:
                raise forms.ValidationError("Input must be at least 5 characters long")
            return data




        class Meta:
            model = SubCategory
            fields = ['Category_name', 'Field_Name']


class CourseForm(forms.ModelForm):
    course_name= forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), validators=[
        RegexValidator(
            '^[a-zA-Z ]+$',
            message="Name"
        ), validators.MinLengthValidator(1, "minimum Three character")
    ])

    def clean_my_field(self):
        data = self.cleaned_data['Field_Name']
        if len(data) < 4:
            raise forms.ValidationError("Input must be at least 5 characters long")
        return data

    class Meta:
        model=Course
        fields='__all__'



class TopicForm(forms.ModelForm):



    class Meta:
        model=Subject
        fields='__all__'


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email:forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control'}),

        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)