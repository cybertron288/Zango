from django.urls import path, re_path
from .views import AppTaskView, AppTaskDetailView

urlpatterns = [
    path("", AppTaskView.as_view()),
    re_path(r"(?P<task_id>\d+)/", AppTaskDetailView.as_view()),
]
