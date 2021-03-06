from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def get(request):
    # return HttpResponse('success!')
    return render(request,'booktest/get.html')


def get2(request):
    dict=request.GET
    a=dict.get('a')
    b=dict.get('b')
    c=dict.get('c','1')
    context={'a':a,'b':b,'c':c}
    return render(request,'booktest/get2.html',context)

def get3(request):
    dict=request.GET
    a=dict.getlist('a')
    b=dict.get('b')
    context={'a':a,'b':b}
    return render(request,'booktest/get3.html',context)

# 创建表单
def post1(request):
    return render(request,'booktest/post1.html')
# 接收表单请求的数据
def post2(request):
    dict=request.POST
    uname=dict.get('uname')
    upwd=dict.get('upwd')
    ugender=dict.get('ugender')
    uhobby=dict.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/post2.html',context)
    # return HttpResponse('hello post2')

def index2(request):
    t1 = loader.get_template('booktest/index2.html')
    # 构造上下文
    context = RequestContext(request, {'h1': 'hello'})
    # 使用上下文渲染模板，生成字符串后返回响应对象
    return HttpResponse(t1.render(context))

from django.http import JsonResponse

def json1(request):
    return render(request,'booktest/json1.html')
def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})

