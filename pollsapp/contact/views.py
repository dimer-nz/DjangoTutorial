from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView

from .forms import MailForm


class SuccessView(TemplateView):
    template_name = "contact/success.html"


class ContactView(FormView):
    form_class = MailForm
    template_name = "contact/index.html"

    def get_success_url(self):
        return reverse("contact_success")

    def form_valid(self, form):
        email = form.cleaned_data.get("mail_address")
        subject = form.cleaned_data.get("subject_line")
        message = form.cleaned_data.get("message_content")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        form.save()
        
        return super(ContactView, self).form_valid(form)
