from django.test import TestCase

# Create your tests here.
from .models import *
from datetime import datetime, timedelta

def test_quiz(db):
  date_start = datetime.datetime.now()
  date_start =  datetime.datetime.strftime(date_start, "%Y-%m-%d T %H:%M:%S%z")
  date_end = date_start + + timedelta(days=2)
  category = Category.objects.create(name="Активные вопросы")
  quiz = Quiz.objects.create(title="Опросы для интернет-бизнеса", description="Оценка интернет-магазина",
                             date_start=date_start, date_end=date_end, category=category)
  question = Question.objects.create(quiz=quiz, title="Опрос для интернет магазина",type="" )
