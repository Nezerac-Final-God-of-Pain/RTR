from django.shortcuts import render, redirect
from .forms import CreateUserForm

def home(request):
    return render(request, 'website/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(Request.POST)
        if form.is_valid:
            form.save
            # return redirect

    context = {'form': form}

    return render(request, 'website/register.html', context=context)