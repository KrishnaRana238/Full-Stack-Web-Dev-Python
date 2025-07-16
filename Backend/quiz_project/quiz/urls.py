# quiz/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, submit_quiz, register_user, get_scores

router = DefaultRouter()
router.register('quizzes', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('submit/', submit_quiz),
    path('register/', register_user),
    path('scores/', get_scores),
]