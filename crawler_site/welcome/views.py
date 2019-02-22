from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("Hello~  for Test!")
    return render(request, 'test.html')       # 使用templates測試