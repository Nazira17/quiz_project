from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.CharField(max_length=255, verbose_name=_("Description"))
    date_start = models.DateTimeField(
      auto_now_add=True, verbose_name=_("Date Start"))
    date_end = models.DateTimeField(
      auto_now_add=True, verbose_name=_("Date End"))
    category = models.ForeignKey(
      Category, on_delete=models.DO_NOTHING)


class Question(models.Model):
    TYPES = (
      ('radio', 'radio'),
      ('checkbox', 'checkbox'),
      ('text', 'text'),
    )
    quiz = models.ForeignKey(
      Quiz, related_name='question', on_delete=models.DO_NOTHING
    )
    question_text = models.CharField(max_length=255, verbose_name=_("Title"))
    question_type = models.CharField(max_length=8, choices=TYPES, default='radio')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __unicode__(self):
        return self.question_text


class Answer(models.Model):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
      Question, related_name='answer', on_delete=models.DO_NOTHING
    )
    answer_text = models.CharField(
      max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

