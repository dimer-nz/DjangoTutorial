from django.db import models

class Mail(models.Model):
    mail_address = models.EmailField(max_length=200)
    subject_line = models.CharField(max_length=200)
    message_content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mail from {self.mail_address} <{self.subject_line}> - {self.message_content}"