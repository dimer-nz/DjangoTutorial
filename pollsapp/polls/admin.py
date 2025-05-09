from django.contrib import admin

from .models import Question, Choice
from contact.models import Mail

admin.site.site_header = "PollsAppAdmin"
admin.site.site_title = "PollsApp Admin Area"
admin.site.index_title = "Welcome to the PollsApp admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class MailAdmin(admin.ModelAdmin):
    list_display = ('mail_address', 'subject_line', 'message_content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('mail_address', 'subject_line', 'message_content')

admin.site.register(Mail, MailAdmin)