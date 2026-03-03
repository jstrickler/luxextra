from django import forms

# Create your forms here.

class ArtistSearchForm(forms.Form):
    name = forms.CharField(max_length=64, required=False, label="Name (partial match OK)")
    min_birth_year = forms.IntegerField(required=False, label="Year born in or after")
    max_birth_year = forms.IntegerField(required=False, label="Year born in or before")
    min_death_year = forms.IntegerField(required=False, label="Year died in or after")
    max_death_year = forms.IntegerField(required=False, label="Year died in or before")
    birthplace = forms.CharField(max_length=64, required=False, label="Place of birth")
    deathplace = forms.CharField(max_length=64, required=False, label="Place of death")