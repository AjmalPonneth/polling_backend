from django.urls import path
from .views import QuestionList, QuestionDetail, vote

app_name = 'polls'
urlpatterns = [
    path("", QuestionList.as_view(), name="question"),
    path("<int:pk>/", QuestionDetail.as_view(), name="question_detail"),
    path("vote/<int:pk>/", vote, name="vote"),
    # path("choice/<str:question>/", choice_detail, name="choice_detail")
]
