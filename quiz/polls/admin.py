from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'title',
    'description',
    'date_start',
    'date_end'
  ]


class AnswerInlineModel(admin.TabularInline):
  model = models.Answer
  fields = [
    'answer_text',
    'is_right',
  ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
  fields = [
    'question_text',
    'quiz',
    'question_type',
  ]
  list_display = [
    'question_text',
    'quiz',
    'question_type',
  ]
  inlines = [
    AnswerInlineModel,
  ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
        ]
