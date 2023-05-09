from django.db import models
from django.utils.translation import gettext as _




# Create your models here.
class Question(models.Model):

    class QuestionLevel(models.IntegerChoices):
        low = 0, _("low")
        middle = 1, _("middle")
        high = 2, _("high")

    id = models.AutoField(verbose_name=_("id"), primary_key=True)
    name = models.TextField(verbose_name=_("name"))
    level = models.IntegerField(verbose_name=_("level"), choices=QuestionLevel.choices, default=QuestionLevel.low, max_length=1)
    description = models.TextField(verbose_name=_("question desctiption"))
    example = models.TextField(verbose_name=_("question example"))
    is_active = models.BooleanField(verbose_name=_("is question active"), default=False)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)


    class Meta:
        verbose_name = _("questions")
        verbose_name_plural = _("questions")

    def __str__(self) -> str:
        return self.name


class Answer(models.Model):
    id = models.AutoField(verbose_name=_("id"), primary_key=True)
    file = models.FileField(verbose_name="file", upload_to="uploads")
    file_type = models.CharField(max_length=50)
    question = models.ForeignKey(to="Question", verbose_name= _("questions"), on_delete=models.CASCADE, related_name="answer")
    point = models.FloatField(verbose_name="point", default=0)
    group = models.ForeignKey(to="groups.Group", verbose_name="group", related_name="answer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)


    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answer")

    def __str__(self) -> str:
        return f"{self.group.name} {self.question.name}"


class AnswerAtemp(models.Model):
    id = models.AutoField(verbose_name=_("id"), primary_key=True)
    group = models.ForeignKey(to="groups.Group", verbose_name="group", related_name="answer_atemp", on_delete=models.CASCADE)
    question = models.ForeignKey(to="Question", verbose_name= _("questions"), on_delete=models.CASCADE, related_name="answer_atemp")
    created_at = models.DateTimeField(auto_created=True, auto_now=True)


    class Meta:
        verbose_name = _("AnswerAtemp")
        verbose_name_plural = _("AnswerAtemp")

    def __str__(self) -> str:
        return f"{self.group.name} {self.question.name}"

