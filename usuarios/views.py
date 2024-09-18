from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro de usuario exitoso. ¡Bienvenido al Mundial!')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


# Create your views here.
