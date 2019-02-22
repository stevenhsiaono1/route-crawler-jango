from django.shortcuts import render
from django.http import HttpResponse

from .models import Vendor

# Create your views here.
def showtemplate(request):
    # return HttpResponse("Hello~  for Test!")
    # 嘗試把vendor的model取出
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}

    return render(request, 'test.html', context)       # 使用templates測試