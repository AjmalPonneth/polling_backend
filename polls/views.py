from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.utils import GeoIP
from rest_framework.decorators import api_view
from .models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer
# Create your views here.


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@csrf_exempt
def vote(request, pk):
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=pk)
        selected_choice = question.choice_set.all()
        serializer = ChoiceSerializer(selected_choice, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=pk)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        serializer = ChoiceSerializer(selected_choice, many=False)
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect("http://127.0.0.1:8080")
