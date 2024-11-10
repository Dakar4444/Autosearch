from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # Включаем множественный выбор файлов

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs:
            attrs['multiple'] = True