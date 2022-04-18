from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    
    path("member_ssh/", views.member_ssh, name="member_ssh"),
    path("ssh_pt1/", views.ssh_pt1, name="ssh_pt1"),
    path("ssh_pt2/", views.ssh_pt2, name="ssh_pt2"),
    path("ssh_pt3/", views.ssh_pt3, name="ssh_pt3"),
    path("ssh_pt4/", views.ssh_pt3, name="ssh_pt4"),

    path("member_ksh/", views.member_ksh, name="member_ksh"),
    
    path('member_pjy/', views.member_pjy, name="member_pjy"),
    path('pjy_po1/', views.pjy_po1, name="pjy_po1"),
    path('pjy_po2/', views.pjy_po2, name="pjy_po2"),
    path('pjy_po3/', views.pjy_po3, name="pjy_po3"),
    path('pjy_po4/', views.pjy_po4, name="pjy_po4"),
    path('pjy_po5/', views.pjy_po5, name="pjy_po5"),
    path('pjy_po6/', views.pjy_po6, name="pjy_po6"),

    path('member_hh/', views.member_hh, name="member_hh"),
    path("info/", views.info, name="info"),
    path("uam/", views.uam, name="uam"),
    path("sport/", views.sport, name="sport"),
    path("textmining/", views.textmining, name="textmining"),
    path("r_analysis/", views.r_analysis, name="r_analysis"),
    path("dplyr/", views.dplyr, name="dplyr"),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)