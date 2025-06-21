
from django.shortcuts import render
from homepage import *
from django.shortcuts import redirect


def rediret_(request):
    if request.method == 'POST':

        return redirect('/home')
    return render(request, 'contactus.html')
