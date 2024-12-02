from django import forms



class VKParserForm(forms.Form):
    token = forms.CharField(label="VK Access Token", widget=forms.TextInput(attrs={'placeholder': 'Введите VK токен'}))
    group_id = forms.CharField(label="ID группы", widget=forms.TextInput(attrs={'placeholder': 'Введите ID группы'}))
