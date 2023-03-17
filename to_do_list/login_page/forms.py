from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', 
        widget=forms.TextInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your username', #max_length=100,
            'autofocus': True,
            'required': 'required'
        })
    )
    password = forms.CharField(label='Password', #max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your password',
            'required': 'required'
        })
    )
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', #max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your first name',
            'required': 'required'
        })
    )
    last_name = forms.CharField(label='Last name', #max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your last name',
            'required': 'required'
        })
    )
    username = forms.CharField(label='Username', 
        widget=forms.TextInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your username', #max_length=100,
            'autofocus': True,
            'required': 'required'
        })
    )
    password = forms.CharField(label='Password', #max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'field_class',
            'placeholder': 'Enter your password',
            'required': 'required'
        })
    )
    password2 = forms.CharField(label='Repeat password', #max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'field_class',
            'placeholder': 'Repeat your password',
            'required': 'required'
        })
    )
    
    def is_valid(self) -> bool:
        valid = super().is_valid()
        if self.clean_password2():
            raise forms.ValidationError('Passwords do not match')
        return valid
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        return password == password2