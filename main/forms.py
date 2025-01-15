from django import forms
from catalog.models import Gallery

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label='reCAPTCHA')



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True



class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result



class UploadMultipleImagesForm(forms.ModelForm):
    photo = MultipleFileField(label='Файл', required=False)
    gos_number = forms.CharField(max_length=10, label="Гос.номер")

    class Meta:
        model = Gallery
        fields = ['photo', ]


#class UploadMultipleImagesForm(forms.Form):
    #images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), label="Файл")
    #gos_number = forms.CharField(max_length=10, label="Гос.номер")