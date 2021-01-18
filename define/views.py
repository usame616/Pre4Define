from django.shortcuts import render


def define(request):
    return render(request, 'define.html')
