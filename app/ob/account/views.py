from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import *

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            new_user.refresh_from_db()
            return render(request, 'registration/finish.html', {'new_user': new_user})
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/registr.html', {'user_form': user_form})

'''
def check_email(request):
    if request.method == 'GET':
        user_form = CheckEmailForm(request.POST)

        if user_form.is_valid():

            return render(request, 'registration/finish.html')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/registr.html')'''
