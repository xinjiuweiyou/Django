from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        un = request.POST.get('username','')
        pw = request.POST.get('password','')
        #if un == 'admin' and pw == 'qwe123':
        user = auth.authenticate(username=un,password=pw)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',un,3600) #添加浏览器cookie
            request.session['user'] = un #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'用户名或密码错误'})

#发布会管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','') #读取浏览器cookie
    username = request.session.get('user','') #读取浏览器session
    return render(request,"event_manage.html" ,{"aa":username})