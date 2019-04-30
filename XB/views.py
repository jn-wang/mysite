from django.shortcuts import render
from XB import models
# Create your views here.
def XB(request):
    movie = models.XB.objects.filter(type='0').order_by('-id')[:6]
    variety = models.XB.objects.filter(type='1').order_by('-id')[:6]
    teleplay = models.XB.objects.filter(type='2').order_by('-id')[:6]
    return render(request, 'XB/index.html',{'movie':movie,'variety':variety,'teleplay':teleplay,})
def video(request):
    return render(request, 'XB/video.html')
def movies(request):
    return render(request, 'XB/movies.html')
def music(request):
    return render(request, 'XB/music.html')

def addVideo(request):
    if request.method =="POST":
        name = request.POST.get('name')
        photourl = request.POST.get('photourl')
        videourl = request.POST.get('videourl')
        type = request.POST.get('type')
        models.XB.objects.create(name=name,photourl=photourl,videourl=videourl,type=type)
        return render(request, 'XB/addVideo.html')
    else:
        return render(request, 'XB/addVideo.html')


def single(request):
    if request.method =="POST":
        url = request.POST.get('url')
        api = request.POST.get('api')
        if api == None:
            api='https://api.bbbbbb.me/jx/?url='

        return render(request, 'XB/single.html',{'url':url,'api':api})
    else:
        return render(request, 'XB/single.html')