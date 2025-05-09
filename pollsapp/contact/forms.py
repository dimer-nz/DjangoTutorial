from django import forms as f


from .models import Mail

class MailForm(f.ModelForm):
    class Meta:
        model = Mail
        fields = ["mail_address","subject_line","message_content"]
        widgets = {
            'message_content': f.Textarea(attrs={'rows': 5}),
        }