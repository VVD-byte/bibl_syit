from django.shortcuts import render, redirect
import logging
from .models import life, work, lines
from django.http import FileResponse
from .forms import linesForms, workForms, lifeForms
passwd = 'vo'

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

life_left_years = {
    '0':{
        '2000': 0,
        '2010': 0,
        '2020': 0,
    },
    '1':{
        '2001': 0,
        '2011': 0,
        '2021': 0,
    },
    '2':{
        '2002': 0,
        '2012': 0,
        '2022': 0,
    },
    '3':{
        '2003': 0,
        '2013': 0,
        '2023': 0,
    },
    '4':{
        '2004': 0,
        '2014': 0,
        '2024': 0,
    },
    '5':{
        '2005': 0,
        '2015': 0,
        '2025': 0,
    },
    '6':{
        '2006': 0,
        '2016': 0,
        '2026': 0,
    },
    '7':{
        '2007': 0,
        '2017': 0,
        '2027': 0,
    },
    '8':{
        '2008': 0,
        '2018': 0,
        '2028': 0,
    },
    '9':{
        '2009': 0,
        '2019': 0,
        '2029': 0,
    },
}

work_left_years = {
                   '0':{
                       '2000': 0,
                       '2010': 0,
                       '2020': 0,
                   },
                   '1':{
                       '2001': 0,
                       '2011': 0,
                       '2021': 0,
                   },
                   '2':{
                       '2002': 0,
                       '2012': 0,
                       '2022': 0,
                   },
                   '3':{
                       '2003': 0,
                       '2013': 0,
                       '2023': 0,
                   },
                   '4':{
                       '2004': 0,
                       '2014': 0,
                       '2024': 0,
                   },
                   '5':{
                       '2005': 0,
                       '2015': 0,
                       '2025': 0,
                   },
                   '6':{
                       '2006': 0,
                       '2016': 0,
                       '2026': 0,
                   },
                   '7':{
                       '2007': 0,
                       '2017': 0,
                       '2027': 0,
                   },
                   '8':{
                       '2008': 0,
                       '2018': 0,
                       '2028': 0,
                   },
                   '9':{
                       '2009': 0,
                       '2019': 0,
                       '2029': 0,
                   },
               }

for i in life_left:
    life_left[i] = life.objects.filter(tag = i).count()

for i in life_left_years:
    for j in life_left_years[i]:
        life_left_years[i][j] = life.objects.filter(date__year = j).count()

for i in work_left_years:
    for j in work_left_years[i]:
        work_left_years[i][j] = work.objects.filter(date__year = j).count()
#logger = logging.getLogger(__name__)

def line_add(requests):
    return add_s(requests, 'page/add_line.html', linesForms, '/line')

def life_add(requests):
    return add_s(requests, 'page/add_life.html', lifeForms, '/life')

def work_add(requests):
    return add_s(requests, 'page/add_work.html', workForms, '/work')

def page(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - page")
    return render(requests, "syit/base.html")

def cv(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - cv")
    return render(requests, "page/cv.html", context = {'theme':'CV', 'conn':True})

def line(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - line")
    data = list(lines.objects.all())
    data.reverse()
    return adm(requests, "page/line.html", {'theme':'ЛИНЕЙКА РОСТА', 'conn':True, 'data':data, 'admin':check_admin(requests)})

def about(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - about")
    return render(requests, "page/about.html", context = {'theme':'ABOUT', 'conn':True})

def _work(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - work")
    data = work.objects.all()
    return adm(requests, "page/work.html", {'theme':'ПО ДЕЛУ', 'data':data, 'work_years':work_left_years, 'admin':check_admin(requests)})

def _work_year(requests, year):
    data = work.objects.filter(date__year = year)
    return render(requests, "page/work.html", context = {'theme':'ПО ДЕЛУ', 'data':data, 'work_years':work_left_years})

def lifes(requests):
    datas = life.objects.all().order_by('date')[:3]
    data = list(datas)
    data.reverse()
    #logger.info(f"{requests.META['REMOTE_ADDR']} - life")
    return adm(requests, "page/life.html", {'theme':'ПО ЖИЗНИ', 'data':data, 'left':life_left, 'years':life_left_years, 'admin':check_admin(requests)})

def lifes_read(requests, slug):
    try:
        data = life.objects.filter(slug = slug)[0]
    except:
        data = ''
    return render(requests, "page/life_text.html", context = {'theme':'ПО ЖИЗНИ', 'data':data, 'left':life_left, 'years':life_left_years})

def left_life_tag(requests, slug):
    if slug in life_left:
        data = life.objects.filter(tag = slug)
    else:
        data = life.objects.filter(date__year = slug)
    return render(requests, "page/life.html", context = {'theme':'ПО ЖИЗНИ', 'data':data, 'left':life_left, 'years':life_left_years})

def text(requests):
    #logger.info(f"{requests.META['REMOTE_ADDR']} - text")
    return render(requests, "page/text.html", context = {'theme':'ЛИНЕЙКА РОСТА', 'conn':True})

#def err404(requests):
    #logger.warning(f"{requests.META['REMOTE_ADDR']} - ERROR404")

#########обработчики

def add_s(requests, templates, Form, tem):
    if check_admin(requests):
        if requests.method == 'GET':
            return render(requests, templates, context = {'form':Form()})
        elif requests.method == 'POST':
            add_form = Form(requests.POST, requests.FILES)
            if add_form.is_valid():
                add_form.save()
                return redirect(tem)
            else:
                print(add_form.errors)
                return render(requests, templates, context={'form': add_form})
    return redirect(tem)

def check_admin(q):
    try:
        try:
            if q.COOKIES['dats_A'] == passwd:
                return True
            elif q.GET['admin'] == passwd:
                return True
            else: return False
        except: return q.GET['admin'] == passwd
        else: return False
    except:
        return False

def adm(requests, templ, contex):
    a = render(requests, templ, context = contex)
    if check_admin(requests): a.set_cookie('dats_A', passwd)
    else:
        a.set_cookie('dats_A', 'yxadi')
    return a