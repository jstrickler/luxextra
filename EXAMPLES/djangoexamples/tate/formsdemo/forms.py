from django import forms
from superheroes.models import Superhero
from .validators import date_validator


class DemoForm(forms.Form):
    DEMO_CHOICES = {'1': 'apple', '2': 'banana', '3': 'cherry'}

    demo_boolean = forms.BooleanField(label="Do you love Python?", required=False)
    demo_char = forms.CharField(max_length=10, strip=True)
    demo_choice = forms.ChoiceField(choices=DEMO_CHOICES.items())
    demo_date = forms.DateField(label="Date", validators=[date_validator])
    demo_email = forms.EmailField(label="Email address")
    demo_float = forms.FloatField(help_text="Please enter a float")
    demo_int = forms.IntegerField(label="Any integer")
    demo_regex = forms.RegexField(regex=r'(?i)^a[a-z]{1,5}$', 
        label="Please enter a string starting with 'a' followed by 1-5 lower case letters")

    # add clean functions here...
    def clean_demo_boolean(self):
        loves_python = self.cleaned_data['demo_boolean']
        return "love" if loves_python else "hate"

    def clean_demo_choice(self):
        choice = self.cleaned_data['demo_choice']
        return self.DEMO_CHOICES.get(choice).title()


class HeroDeleteForm(forms.Form):

    hero_name = forms.CharField(
        label='Hero',
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Hero name'}),
    )


class HeroDeleteDropdownForm(forms.Form):

    hero = forms.ModelChoiceField(
        label='Hero', queryset=Superhero.objects.all(), initial=0
    )


class HeroModelForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'real_name', 'city', 'secret_identity', 'powers', 'enemies']
        labels = {
            'name': 'Hero Name',
        }


