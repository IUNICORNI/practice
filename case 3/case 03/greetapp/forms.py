from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'})
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError('Поле имени не должно быть пустым.')
        return name
