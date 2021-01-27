from django import forms
from django.forms.widgets import TextInput, CheckboxSelectMultiple, Select

from .models import ToDo, Category, Tag


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['text', 'category', 'tags']
        widgets = {
            'text': TextInput(attrs={'class': 'todo-add__text'})
        }

    category = forms.ModelChoiceField(Category.objects.all(),
                                      widget=Select(attrs={'class': 'todo-add__category'}),
                                      required=False)
    tags = forms.ModelMultipleChoiceField(Tag.objects.all(),
                                          widget=CheckboxSelectMultiple(attrs={'class': 'todo-add__tags'}),
                                          required=False)
