from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question
from .serializers import QuizSerializer, ActiveQuestionSerializer
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class ActiveQuestion(APIView):

    def get(self, request, **kwargs):
        question = Question.objects.filter(is_active=True)
        serializer = ActiveQuestionSerializer(question, many=True)
        return Response(serializer.data)
