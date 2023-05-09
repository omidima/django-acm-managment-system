from django.contrib import admin
from .models import Answer, AnswerAtemp, Question

# Register your models here.
admin.site.register(Answer)
admin.site.register(AnswerAtemp)
admin.site.register(Question)
