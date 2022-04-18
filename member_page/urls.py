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
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)