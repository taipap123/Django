from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
urlApi = "http://127.0.0.1:8000/api/"

def index(request):
    try:
        response = requests.get(urlApi + "getListItem")
        data = {"items": json.loads(response.text)}
    except:
        data = {"items": json.dumps([{}])}
    return render(request, 'myapp/content.html', data)