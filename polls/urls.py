from django.urls import path
from .views import questions, question_detail, vote

app_name = 'polls'
urlpatterns = [
    path("", questions, name="index"),
    path("<int:pk>/", question_detail, name="detail"),
    # path("<int:pk>/result/", ResultView.as_view(), name="results"),
    path("<int:pk>/vote/", vote, name="vote")
]
