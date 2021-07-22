from rest_framework import serializers
from .models import Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
          'title'
        ]


class ActiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
          'quiz',
          'question_text',
          'question_type',
          'is_active'
        ]
