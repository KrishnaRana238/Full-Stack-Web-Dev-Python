# quiz/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Quiz, Question, Attempt
from .serializers import QuizSerializer, AttemptSerializer, UserSerializer
from django.contrib.auth.models import User

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_quiz(request):
    quiz_id = request.data.get('quiz_id')
    answers = request.data.get('answers')  # {question_id: chosen_option}
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    
    score = 0
    for q in questions:
        if str(q.id) in answers and answers[str(q.id)] == q.correct_option:
            score += 1

    attempt = Attempt.objects.create(user=request.user, quiz=quiz, score=score)
    return Response({'score': score})

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "User created"})
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scores(request):
    attempts = Attempt.objects.filter(user=request.user)
    data = AttemptSerializer(attempts, many=True).data
    return Response(data)