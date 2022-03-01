from django import forms

class CatAdoptionForm(forms.Form):
    CHOICES = [("1", "Yes"), ("2", "No")]
    want_the_cat = forms.ChoiceField(label="Do you want to adopt this cat?",
                                     widget=forms.RadioSelect,
                                     choices=CHOICES)
    had_a_cat = forms.ChoiceField(label="Have you adopted a cat in the past?",
                                  widget=forms.RadioSelect,
                                  choices=CHOICES)
    keep_in_contact = forms.ChoiceField(label="Do you want to keep in contact with the person who is currently fostering the cat?",
                                        widget=forms.RadioSelect,
                                        choices=CHOICES)
    other_mentions = forms.CharField(label="Other mentions")
