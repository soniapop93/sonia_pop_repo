from django.shortcuts import render, redirect
from .forms import RegisterForm
from adoptions.models import Cat

def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/cats")
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form":form})


def profile(response):
    if response.user.is_authenticated:
        cats = Cat.objects.filter(human=response.user)
        return render(response, "users/profile.html", {'cats':cats})
    else:
        return redirect('/accounts/login')
