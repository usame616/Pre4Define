from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)