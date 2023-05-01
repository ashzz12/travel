from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.subtraction,name='subtraction'),
    # path('operations',views.operations,name='operations'),
    # path('mul',views.multiplication,name='multiplication'),
    # path('div',views.division,name='division'),

    # path('about',views.about,name='about'),
    # path('contact',views.contact,name='contact'),
    ]
