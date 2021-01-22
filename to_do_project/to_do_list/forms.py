from django import forms


class ToDoForm(forms.Form):
    text = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={"class": "todo-add__text"}))
