from django.urls import path
from .views import page, cv, line, about, work, lifes, lifes_read, left_life_tag
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', page),
    path('cv/', cv),
    path('line/', line),
    path('about/', about),
    path('work/', work),
    path('life/', lifes),
    path('life/<str:slug>', lifes_read),
    path('<str:slug>', left_life_tag),
]