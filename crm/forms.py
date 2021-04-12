from django import forms

class CarsForm(forms.Form):
    brand = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'ccs_input'}) )
    model = forms.CharField(max_length=200)
    engine = forms.FloatField(max_value=8, required=False)
