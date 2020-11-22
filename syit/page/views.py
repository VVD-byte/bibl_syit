from django.shortcuts import render
import logging
from .models import life

#раздел "по жизни" левый блок
life_left = {
    'АРТЕК': 0,
    'ИТ': 0,
    'КИНО': 0,
    'ЛИТЕРАТУРА': 0,
    'ЛИЧНОЕ': 0,
    'МИР ВОКРУГ': 0,
    'МУЗЫКА': 0,
    'ОБРАЗОВАНИЕ': 0,
    'ПУТЕШЕСТВИЯ': 0,
    'СОБЫТИЯ': 0,
    'УПРАВЛЕНИЕ': 0,
}

for i in life_left:
    life_left[i] = life.objects.filter(tag = i).count()

#logger = logging.getLogger(__name__)

def page(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - page")
    return render(requests, "syit/base.html")

def cv(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - cv")
    return render(requests, "page/cv.html", context = {'theme':'CV', 'conn':True})

def line(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - line")
    return render(requests, "page/line.html", context = {'theme':'ЛИНЕЙКА РОСТА', 'conn':True})

def about(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - about")
    return render(requests, "page/about.html", context = {'theme':'ABOUT', 'conn':True})

def work(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - work")
    return render(requests, "page/work.html", context = {'theme':'ПО ДЕЛУ'})

def lifes(requests):
    datas = life.objects.all().order_by('date')[:3]
    data = list(datas)
    data.reverse()
    #logger.info(f"{requests.META['REMOTE_ADDR']} - life")
    return render(requests, "page/life.html", context = {'theme':'ПО ЖИЗНИ', 'data':data, 'left':life_left})

def lifes_read(requests, slug):
    data = life.objects.filter(slug = slug)[0]
    return render(requests, "page/life_text.html", context = {'theme':'ПО ЖИЗНИ', 'data':data, 'left':life_left})

#def err404(requests):
    #logger.warning(f"{requests.META['REMOTE_ADDR']} - ERROR404")