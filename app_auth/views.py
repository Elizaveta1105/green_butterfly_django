from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import SignupForm


class SignupView(View):
    template_name = 'app_auth/signup.html'
    form_class = SignupForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="app_spendings:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save() # save to DB
            username = form.cleaned_data["username"]
            messages.success(request, message=f"Thank you, {username}. Account created successfully.")
            return redirect(to="app_auth:login")
        return render(request, self.template_name, context={"form": form})

