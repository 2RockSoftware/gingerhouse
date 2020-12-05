from django import forms
from django.utils.safestring import mark_safe

from gingerhouse.houses.models import Vote


class VoteForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"placeholder": "Email Address"}),
                             help_text=mark_safe("<a href='#email-required'>Why do we need this?</a>"))

    def __init__(self, *args, **kwargs):
        self.ginger_house = kwargs.pop("ginger_house", None)
        super(VoteForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        # is there a vote with this email to same house category?
        email = cleaned_data.get("email")
        already_voted = Vote.objects.filter(email=email, ginger_house__category=self.ginger_house.category).exists()
        if already_voted:
            raise forms.ValidationError("You have already voted in this category")
        return cleaned_data
