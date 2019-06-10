from django.shortcuts import render
from django.http import HttpResponse,Http404
import random
# Create your views here.
def index(request):
    random_int = random.randint(0,99)
    if random_int%2 == 0:
        return HttpResponse("Hello, world. You're at the polls index.")
    raise Http404("Page Not Found")
