from django.http import HttpResponse
from django.shortcuts import render
from .models import New

allNews = New.objects.all()
jahonCat1 = "sa563663893d5ds6a45443ff"
uzbCat2 = "ds1d1ss3535ef2ds23d3f6ee6e"
JahonNews = New.objects.filter(news_tag='Jahon')
UzbekNews = New.objects.filter(news_tag="O'zbekiston")
def home(request):
    news = New.objects.all()
    tk1 = request.GET.get('tk_c_1')
    if tk1 == jahonCat1:
        news = JahonNews
    elif tk1 == uzbCat2:
        news = UzbekNews
    return render(request, 'index.html', {'news': news, 'tk_c_1': jahonCat1, 'tk_c_2': uzbCat2})

def veiw_new(request):
    global rs1
    newRequest = request.GET.get('new')
    if New.objects.filter(news_token=newRequest):
        objectReqNew = New.objects.filter(news_token=newRequest)
        for rq in objectReqNew:
            rs1 = rq
        return render(request, 'view_news.html', {'new_object': rs1})
    else:
        return render(request, '404.html', status=404)

def Page404Html(request, exception):
    return render(request, '404.html', status=404)
