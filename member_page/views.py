from django.shortcuts import render

# Create your views here.
def member_ssh(request) :
    return render(request,'member_page/member_ssh.html')

def ssh_pt1(request) :
    return render(request,'member_page/ssh/ssh_pt1.html')

def ssh_pt2(request) :
    return render(request,'member_page/ssh/ssh_pt2.html')

def ssh_pt3(request) :
    return render(request,'member_page/ssh/ssh_pt3.html')
    
def ssh_pt4(request) :
    return render(request,'member_page/ssh/ssh_pt4.html')

def member_ksh(request) :
    return render(request,'member_page/member_ksh.html')

def member_pjy(request):
    return render(
        request,
        'member_page/member_pjy.html'
    )
def pjy_po1(request):
    return render(
        request,
        'member_page/pjy/pjy_po1.html'
    )
def pjy_po2(request):
    return render(
        request,
        'member_page/pjy/pjy_po2.html'
    )
def pjy_po3(request):
    return render(
        request,
        'member_page/pjy/pjy_po3.html'
    )
def pjy_po4(request):
    return render(
        request,
        'member_page/pjy/pjy_po4.html'
    )
def pjy_po5(request):
    return render(
        request,
        'member_page/pjy/pjy_po5.html'
    )
def pjy_po6(request):
    return render(
        request,
        'member_page/pjy/pjy_po6.html'
    )

def member_hh(request):
    return render(
        request,
        'member_page/member_hh.html'
    )
def info(request):
    return render(
        request,
        'member_page/hh_html/info.html'
    )
def uam(request):
    return render(
        request,
        'member_page/hh_html/uam.html'
    )
def sport(request):
    return render(
        request,
        'member_page/hh_html/sport.html'
    )
def textmining(request):
    return render(
        request,
        'member_page/hh_html/textmining.html'
    )
def r_analysis(request):
    return render(
        request,
        'member_page/hh_html/R-analysis.html'
    )
def dplyr(request):
    return render(
        request,
        'member_page/hh_html/Package-Dplyr.html'
    )
