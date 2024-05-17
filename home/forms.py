from django import forms


class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
