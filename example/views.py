# example/views.py
from datetime import datetime

from django.http import HttpResponse, render

def index(request):

    return render(request, "index.html")