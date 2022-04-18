from django.urls import path, include
from . import views

urlpatterns = [
    #pjy
    path('member_pjy/', views.member_pjy),
    path('pjy_po1/', views.pjy_po1),
    path('pjy_po2/', views.pjy_po2),
    path('pjy_po3/', views.pjy_po3),
    path('pjy_po4/', views.pjy_po4),
    path('pjy_po5/', views.pjy_po5),
    path('pjy_po6/', views.pjy_po6),


    #hh
    # path('member_hh/', views.member_hh),


    #ssh
    # path('member_ssh/', views.member_ssh),


    #ksh
    # path('member_ksh/', views.member_ksh),
    
]