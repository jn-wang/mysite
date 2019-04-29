from django.shortcuts import render,redirect,HttpResponse
from Dome.pay import AliPay
import time
from Dome import models
# Create your views here.
from django.http import FileResponse

def file_down(request):
    file=open('/home/www/mysite/static/123.exe','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="123.exe"'
    return response

def calculate(request):
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    return HttpResponse(result)

def index(request):
    return render(request,'index.html')

def resume(request):
    if request.method == "POST":
        Message = request.POST.get('Message')
        email = request.POST.get('email')
        user = request.POST.get('user')
        models.Message.objects.create(Message=Message, email=email, user=user)
        return render(request, 'resume.html')
    else:
        return render(request, 'resume.html')
def img(request):
    return render(request, 'img.html')

def hbdl(request):
    if request.method == "POST":
        i = request.POST.get('i')
        i = int(i)
        if request.POST.get('top') == 'top':
            if i ==1:
                i = i+1
            i=i-1
        elif request.POST.get('bottom')== 'bottom':
            if i ==368:
                i = i-1
            i=i+1
        first = models.powerquestionbank.objects.get(SID=i)
        return render(request, 'hbdl.html',{'first':first})
    else:
        i = request.GET.get('sid')
        if i != None:
            first = models.powerquestionbank.objects.get(SID=i)
            return render(request, 'hbdl.html', {'first': first})
        else:
            first = models.powerquestionbank.objects.get(SID='1')
            return render(request, 'hbdl.html', {'first': first})

def search(request):
    value = request.POST.get('value')
    data = models.powerquestionbank.objects.filter(icontains=value)
    return render(request, 'hbdlss.html',{'data':data})

def pay(request):
    if request.method == 'GET':
        return render(request,'pay.html')
    else:
        money = float(request.POST.get('price'))

        alipay = AliPay(
            appid="2016093000628548",
            app_notify_url="https://www.jn-wang.cn/updata_order/",
            # POST,发送支付状态信息 校验是否支付成功
            return_url="https://www.jn-wang.cn/pay_result/",
            # GET,将用户浏览器地址重定向回原网站
            app_private_key_path="keys/app_private_2048.txt",
            # 用户的私钥
            alipay_public_key_path="keys/alipay_public_2048.txt",
            # 阿里公钥
            debug=True,  # 默认True测试环境、False正式环境
        )
        query_params = alipay.direct_pay(
            subject='兰博基尼Murcielago蝙蝠',
            # 商品描述
            out_trade_no='x2'+str(time.time()),
            # 商品订单号
            total_amount=money,
            # 保留后俩位小数
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
        return redirect(pay_url)

def pay_result(request):
    params = request.GET.dict()
    sign = params.pop('sign',None)
    alipay = AliPay(
        appid="2016093000628548",
        app_notify_url="https://www.jn-wang.cn/updata_order/",
        # POST,发送支付状态信息 校验是否支付成功
        return_url="https://www.jn-wang.cn/pay_result/",
        # GET,将用户浏览器地址重定向回原网站
        app_private_key_path="keys/app_private_2048.txt",
        # 用户的私钥
        alipay_public_key_path="keys/alipay_public_2048.txt",
        # 阿里公钥
        debug=True,  # 默认True测试环境、False正式环境
    )
    status = alipay.verify(params,sign)
    if status:
        return HttpResponse('支付成功')
    return HttpResponse('支付失败')

def updata_order(request):
    """
    支付成功后，返回的POST请求，用于修改订单状态
    :param request:
    :return:
    """
    if request.method == 'POST':
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict ={}
        for k,v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        alipay = AliPay(
            appid="2016093000628548",
            app_notify_url="https://www.jn-wang.cn/updata_order/",
            # POST,发送支付状态信息 校验是否支付成功
            return_url="https://www.jn-wang.cn/pay_result/",
            # GET,将用户浏览器地址重定向回原网站
            app_private_key_path="keys/app_private_2048.txt",
            # 用户的私钥
            alipay_public_key_path="keys/alipay_public_2048.txt",
            # 阿里公钥
            debug=True,  # 默认True测试环境、False正式环境
        )
        sign = post_dict.pop('sign',None)
        status = alipay.verify(post_dict,sign)
        if status:
            # out_trade_no = post_dict.get('out_trade_no')
            # print(out_trade_no)
            print(post_dict)
            return HttpResponse('123')
        else:
            return HttpResponse('456')
    return HttpResponse('')