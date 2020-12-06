from django import forms
from .models import lines

class linesForms(forms.Form):
    years = forms.IntegerField(required = False)
    text = forms.CharField(widget=forms.Textarea, required = False)
    image1 = forms.ImageField(max_length = None, required = False)
    image2 = forms.ImageField(max_length = None, required = False)
    image3 = forms.ImageField(max_length = None, required = False)
    image4 = forms.ImageField(max_length = None, required = False)

    def save(self):
        new_lines = lines.objects.create(
            years = self.cleaned_data['years'],
            text = self.cleaned_data['text'],
            image1 = self.cleaned_data['image1'],
            image2 = self.cleaned_data['image2'],
            image3 = self.cleaned_data['image3'],
            image4 = self.cleaned_data['image4']
        )
        return new_lines