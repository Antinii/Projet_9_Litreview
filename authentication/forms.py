from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    """
    Formulaire d'inscription qui hérite de UserCreationForm
    """

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']
