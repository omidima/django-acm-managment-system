from django.urls import path
from .views import QuestionContent

urlpatterns = [
    path("", QuestionContent.as_view(), name="question-name"),
    # path('', view=UploadFileView.as_view(), name="upload_files"),

]