from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.Textarea()
