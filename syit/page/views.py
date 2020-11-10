from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def page(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - page")
    return render(requests, "syit/base.html")

def cv(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - cv")
    return render(requests, "page/cv.html", context = {'theme':'CV', 'conn':True})

def line(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - line")
    return render(requests, "page/line.html", context = {'theme':'ЛИНЕЙКА РОСТА', 'conn':True})

def about(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - about")
    return render(requests, "page/about.html", context = {'theme':'ABOUT', 'conn':True})

def work(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - work")
    return render(requests, "page/work.html", context = {'theme':'ПО ДЕЛУ'})

def life(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - life")
    return render(requests, "page/life.html", context = {'theme':'ПО ЖИЗНИ'})

def connect(requests):
    logger.info(f"{requests.META['REMOTE_ADDR']} - connect")
    return render(requests, "page/connect.html", context = {'theme':'ОТДЕЛЕНИЕ СВЯЗИ'})

def err404(requests):
    logger.warning(f"{requests.META['REMOTE_ADDR']} - ERROR404")