"""studentManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
# login方法处理登录
def login(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息 （对象）
    :return:
    """
    # 处理get请求
    if request.method == 'GET':
        # 当请求为get请求的的时候，跳转到login.html.需要使用到render
        return render(request,'login.html')
    else:
        # 处理用户发来的post请求
            # 获取表单数据
        u = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 判断用户名和密码是否匹配
        if u =='root' and pwd == '123456':
            # 验证成功,进入index.html
            return redirect('/index/')
        else:
            # render中可以设置请求的地址和携带回页面的数据。
            return render(request,'login.html',{'msg':'用户名或密码错误'})
def index(request):
    return render(request,'index.html',)
# 配置路由信息
urlpatterns = [
    url(r'^login/',login),
    url(r'^index/',index)
]
