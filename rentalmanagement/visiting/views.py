from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dashboard.models import House
from django.core import serializers

# Create your views here.
def index(request):
    return render(request,'index.html')

def search_house(request):
    if  request.method=='POST':
        house=request.POST['searchdata']
        houseinfo=House.objects.filter(Rooms=house)
        # hs=serializers.serialize('json',houseinfo,fields=('Address'))
        hs=serializers.serialize('json',houseinfo)
        # return render(request,'html pages/search.html',{'houseinfo':houseinfo})
        
        return HttpResponse(hs,content_type="text/json-comment-filtered")
        # return HttpResponse(l)
        

    else:
        return render(request,'html pages/search.html')  