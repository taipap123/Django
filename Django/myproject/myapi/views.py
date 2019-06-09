from django.http import HttpResponse
from .Items import ItemManager
import json
# Create your views here.
#-------------Items------------------
def getListItem(request):
    if(request.method == 'GET'):
            data = ItemManager.getListItem()
    return HttpResponse(data, content_type='text/json')