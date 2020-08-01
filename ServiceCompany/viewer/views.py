from django.shortcuts import render

def user(request):
    return render(request, template_name='user.html')