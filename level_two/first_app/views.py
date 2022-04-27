from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord
# Create your views here.

# you can use dict to pass anything to a template

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/index.html', context=date_dict)
