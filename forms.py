from django import forms
from django.contrib.auth import authenticate, get_user_model

# login class
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            validation = authenticate(username=username, password=password)

            if not validation:
                raise forms.ValidationError('This user does not exist')
            if not validation.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not validation.is_active:
                raise forms.ValidationError('this user is not active')
        
        return super(UserLoginForm, self).clean(*args, **kwargs)
        

User = get_user_model()		# get the custom model

# register class
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
		