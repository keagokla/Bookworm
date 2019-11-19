# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookwormAccountForm

def index(request):
    return HttpResponse("Up and running!")

# Create your views here.
def register(response):
    if response.method == "POST":
        form = BookwormAccountForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = BookwormAccountForm()

    return render(response, "bookworm/register.html", {"form": form})
