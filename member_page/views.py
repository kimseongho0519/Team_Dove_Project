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

