from typing import Any
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from apps.questinos.models import Answer
from .models import GroupMedias, Group, News


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if not self.request.user.is_anonymous and self.request.user.id:
            return redirect('/profile')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username,password, user)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        return render(request, self.template_name, {'error': 'نام کاربری یا رمز عبور شما برای ورود به پنل کاربری گروه اشتباه میباشد.'})


class ProfileView(View):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name, {
            "group_name": self.request.user.name,
            "news": News.objects.all()
        })


class AnswerList(LoginRequiredMixin, ListView):
    template_name = "answer_list.html"
    login_url="/login"

    def get_queryset(self):
        return Answer.objects.filter(group = self.request.user).all()

    def get_context_data(self, **kwargs: Any):
        return {
            "group_name": self.request.user.name,
            "title": "جدول امتیازات",
            "items": self.get_queryset()
        }