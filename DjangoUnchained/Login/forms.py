# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from Login.models import CustomUser



class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        User = get_user_model()
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'role')
