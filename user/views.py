from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterationForm

# Create your views here.
def register(request):

    if request.method == "POST":
        ## form = UserCreationForm(request.POST)
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegisterationForm()

    return render(request, 'users/register.html', {'form':form})


def login(request):
    return render(request, 'users/login.html')
