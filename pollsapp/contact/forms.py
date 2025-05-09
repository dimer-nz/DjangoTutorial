from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail",'class': 'form-control'})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject",'class': 'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message",'class': 'form-control'})
    )
    