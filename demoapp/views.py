from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print('第一个视图')
    return HttpResponse('ok')

def login(request):
    print('成功')
    return HttpResponse('ok')

def login_logic(request):
    print('登录逻辑ok')
    return HttpResponse('ok')