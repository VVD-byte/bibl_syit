from django.urls import path
from .views import _work, page, cv, line, line_add, about, work_add, _work_year, lifes, life_add, lifes_read, left_life_tag, text
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', page),
    path('cv', cv),
    path('line', line),
    path('line/add', line_add, name = 'line_create'),
    path('about', about),
    path('work', _work),
    path('work/add', work_add, name = 'work_create'),
    path('work/year/<str:year>', _work_year),
    path('life', lifes),
    path('life/add', life_add, name = 'life_create'),
    path('life/<str:slug>', lifes_read),
    path('life/year/<str:slug>', left_life_tag),
    path('text', text),
]