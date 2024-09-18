from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def indexx(request):
    return render(request, 'index.html')