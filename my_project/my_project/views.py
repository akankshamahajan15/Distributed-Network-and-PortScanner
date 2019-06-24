# Create your views here.

from django.shortcuts import render_to_response

def home(request):
    return render_to_response('my_project/index.html')
