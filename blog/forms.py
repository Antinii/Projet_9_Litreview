from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    """
    Formulaire pour la création et la modification d'un ticket
    """

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}


class DeleteTicketForm(forms.Form):
    """
    Formulaire pour la suppression d'un ticket
    """

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    """
    Formulaire pour la création et la modification d'une critique
    """

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(choices=[(0, ' 0'), (1, ' 1'), (2, ' 2'), (3, ' 3'), (4, ' 4'), (5, ' 5')],)}
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
            }


class DeleteReviewForm(forms.Form):
    """
    Formulaire pour la suppression d'une critique
    """

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    """
    Formulaire pour l'abonnement à d'autres utilisateurs
    """

    user = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class SearchUserForm(forms.Form):
    """
    Formulaire pour la recherche d'utilisateurs
    """

    username = forms.CharField(
        label='',
        error_messages={'required': ''},

        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': "Nom d'utilisateur"})
    )
