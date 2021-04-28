from django import forms


class BlogpostForm(forms.Form):
    title = forms.CharField(max_length=140, required=True)
    slug = forms.CharField(max_length=50, required=True)
    content = forms.CharField(widget=forms.Textarea, required=False)