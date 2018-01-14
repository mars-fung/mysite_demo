from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from login.templates import models

def AllIndex(request):
    return HttpResponse("全网站的index页面")

def index(request):
    # return HttpResponse("这个APP：login的index页面")
    return render(request,'login/index.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:  # 确保用户名和密码都不为空
#             username = username.strip()
#             # 用户名字符合法性验证
#             # 密码长度验证
#             # 更多的其它验证.....
#             try:
#                 user = models.User.objects.get(name=username)
#             except:
#                 return render(request, 'login/login.html')
#             if user.password == password:
#                 return redirect('/login/index')
#     return render(request, 'login/login.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/login/index')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')

def register(request):
    # return HttpResponse("这个APP：login的index页面")
    return render(request,'login/register.html')