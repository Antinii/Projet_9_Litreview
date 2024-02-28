from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    """
    Form used for the signup, heriting from UserCreationForm
    """

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']
