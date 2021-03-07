from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Question, Choice
from .serializer import QuestionSerializer
# Create your views here.


@csrf_exempt
@api_view(['GET'])
def questions(request):
    query = Question.objects.order_by('-pub_date')[:5]
    serializer = QuestionSerializer(query, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    serializer = QuestionSerializer(question, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])
        serializer = QuestionSerializer(selected_choice, many=False)
        return JsonResponse(serializer.data, safe=False)
    except (KeyError, Choice.DoesNotExist):
        return JsonResponse("choices does not exist")
