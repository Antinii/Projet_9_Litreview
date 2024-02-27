from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    """
    Form used to create and edit a ticket
    """

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}


class DeleteTicketForm(forms.Form):
    """
    Form used to delete an existing ticket
    """

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    """
    Form used to create and edit a review
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
    Form used to delete an existing review
    """

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    """
    Form used to follow another user
    """

    user = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class SearchUserForm(forms.Form):
    """
    Form used to be able to search for other users
    """

    username = forms.CharField(
        label='',
        error_messages={'required': ''},

        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': "Nom d'utilisateur"})
    )
