from django import forms
from .models import lines, work, life
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

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

class workForms(forms.Form):
    name_file = forms.FileField(required = False)
    url = forms.CharField(required=False)
    date = forms.DateTimeField(required = False)
    title = forms.CharField(required = False)
    title_low = forms.CharField(required = False)

    def save(self):
        from .views import work_left_years
        try:
            for item, i in work_left_years.items():
                if str(self.cleaned_data['date'].year) in i.keys():
                    i[str(self.cleaned_data['date'].year)] += 1
                    break
        except:
            pass
        if self.cleaned_data['name_file']:
            default_storage.save(r'./work_document/' + self.cleaned_data['name_file'].name, ContentFile(self.cleaned_data['name_file'].read()))
        new_work = work.objects.create(
            name_file = self.cleaned_data['name_file'] or self.cleaned_data['url'],
            date = self.cleaned_data['date'],
            title = self.cleaned_data['title'],
            title_low = self.cleaned_data['title_low']
        )
        return new_work

class lifeForms(forms.Form):
    file_name = forms.CharField(required = False)
    date = forms.DateTimeField(required = False)
    str_date = forms.CharField(required = False)
    tag = forms.CharField(required = False)
    heading = forms.CharField(required = False)
    page_text = forms.CharField(widget=forms.Textarea, required = False) #текст на главной странице под постом
    text = forms.CharField(widget=forms.Textarea, required = False)
    slug = forms.CharField(required = False)

    def save(self):
        pass