from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print('第一个视图')
    return HttpResponse('ok')