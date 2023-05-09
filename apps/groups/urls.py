from django.urls import path
from .views import LoginView, ProfileView, AnswerList
from django.contrib.auth.decorators import login_required

# from django import events


urlpatterns = [
    path('login', view=LoginView.as_view(), name="login_site"),
    path("profile", login_required(ProfileView.as_view(), login_url="/login"), name="profile"),
    path("scoreboard", AnswerList.as_view(), name="scoreboard"),
    # path("profile", events.as_channel(path="socket.io")),
]
