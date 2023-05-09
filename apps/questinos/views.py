from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.questinos.models import AnswerAtemp
from apps.questinos.models import Answer
from apps.questinos.models import Question

from apps.groups.models import GroupMedias


# Create your views here.
class QuestionContent(LoginRequiredMixin, CreateView):
    model = GroupMedias
    template_name = "questions_content.html"
    login_url = "/login"
    fields = ['file', 'file_type']
    success_url = '/profile'

    def get_queryset(self) :
        return Question.objects.filter(is_active=True).first()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        if self.get_queryset():
            return {
                "group_name": self.request.user.name,
                "title": self.get_queryset().name,
                "question_content": self.get_queryset().description,
                "question_example": self.get_queryset().example,
                "question_title": self.get_queryset().name,
                "q": self.get_queryset().id,
                "atemped": 3-AnswerAtemp.objects.filter(group=self.request.user).all().__len__()
            }
        else:
            return {
                "group_name": self.request.user.name,

                "title": None
            }

    def form_valid(self, form):
        form.instance.group = self.request.user
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        group = self.request.user
        type = self.get_form_kwargs()['data']['type']
        id = self.get_form_kwargs()['data']['q']
        file = self.get_form_kwargs()['files']['file']

        if (self.get_queryset() and self.get_queryset().is_active and self.get_queryset().id == int(id)):
            answer = Answer.objects.filter(question=self.get_queryset()).filter(group=group).delete()
            
            Answer.objects.create(
                file=file,
                question=self.get_queryset(),
                group=group,
                file_type=type
            )

            AnswerAtemp.objects.create(
                group=group,
                question=self.get_queryset(),
            ) 
        else:
            return render(request, self.template_name,{
                "group_name": self.request.user.name,

                "title": None
            })
        return super().post(request, *args, **kwargs)