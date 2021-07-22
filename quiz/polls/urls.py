from django.urls import path
from .views import Quiz, ActiveQuestion

app_name = 'polls'

urlpatterns = [
  path('', Quiz.as_view(), name='quiz'),
  path('r/<str:active>/', ActiveQuestion.as_view(), name='active'),
]
