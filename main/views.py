from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Aluminium, Grain
import pymysql

# class MainList(ListView):
#     model = Grain
#     templat_name = 'main/home.html'

def Homepage(request) :
    db = pymysql.connect(host='15.164.171.72', port=3306, user='joy', passwd='Ghfkddl~1283', db='project_one', charset='utf8')
    cur = db.cursor()

    with db :
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '밀'")
        wheat = cur.fetchall()
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '대두'")
        soybean = cur.fetchall()
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '옥수수'")
        corn = cur.fetchall()
        cur.execute("SELECT * FROM domestic_oil")
        domestic_oil = cur.fetchall()
        cur.execute("SELECT * FROM oversea_oil")
        oversea_oil = cur.fetchall()
        cur.execute("SELECT * FROM aluminium")
        aluminium = cur.fetchall()
        cur.execute("SELECT * FROM monthly_al")
        monthly_al = cur.fetchall()
        cur.execute("SELECT * FROM monthly_domestic_oil")
        monthly_domestic_oil = cur.fetchall()
        cur.execute("SELECT * FROM monthly_grain")
        monthly_grain = cur.fetchall()
        cur.execute("SELECT * FROM monthly_oversea_oil")
        monthly_oversea_oil = cur.fetchall()
        cur.execute("SELECT * FROM monthly_mineral")
        monthly_mineral = cur.fetchall()

    return render(request,"main/home.html",{
        "title" : "곡류 가격 변동",
        "grain1" : "밀",
        "grain2" : "대두",
        "grain3" : "옥수수",
        "wheat" : wheat,
        "soybean" : soybean,
        "corn" : corn,
        "domestic_oil" : domestic_oil,
        "oversea_oil" : oversea_oil,
        "aluminium" : aluminium,
        "monthly_al" : monthly_al,
        "monthly_domestic_oil" : monthly_domestic_oil,
        "monthly_grain" : monthly_grain,
        "monthly_oversea_oil" : monthly_oversea_oil,
         "monthly_mineral" : monthly_mineral
    })

def chart_bar(request):
    db = pymysql.connect(host='15.164.171.72', port=3306, user='joy', passwd='Ghfkddl~1283', db='project_one', charset='utf8')
    cur = db.cursor()

    with db :
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '밀'")
        wheat = cur.fetchall()
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '대두'")
        soybean = cur.fetchall()
        cur.execute("SELECT 날짜,곡류,open,close FROM grain WHERE 곡류 like '옥수수'")
        corn = cur.fetchall()
        cur.execute("SELECT * FROM domestic_oil")
        domestic_oil = cur.fetchall()
        cur.execute("SELECT * FROM oversea_oil")
        oversea_oil = cur.fetchall()
        cur.execute("SELECT * FROM aluminium")
        aluminium = cur.fetchall()
        cur.execute("SELECT * FROM mineral")
        mineral = cur.fetchall()
        

    return render(request,"main/chart.html",{
        "title" : "곡류 가격 변동",
        "grain1" : "밀",
        "grain2" : "대두",
        "grain3" : "옥수수",
        "wheat" : wheat,
        "soybean" : soybean,
        "corn" : corn,
        "domestic_oil" : domestic_oil,
        "oversea_oil" : oversea_oil,
        "aluminium" : aluminium,
        "mineral" : mineral
    })

def monthly_chart(request):
    db = pymysql.connect(host='15.164.171.72', port=3306, user='joy', passwd='Ghfkddl~1283', db='project_one', charset='utf8')
    cur = db.cursor()

    with db :
        cur.execute("SELECT * FROM monthly_al")
        monthly_al = cur.fetchall()
        cur.execute("SELECT * FROM monthly_domestic_oil")
        monthly_domestic_oil = cur.fetchall()
        cur.execute("SELECT * FROM monthly_grain")
        monthly_grain = cur.fetchall()
        cur.execute("SELECT * FROM monthly_oversea_oil")
        monthly_oversea_oil = cur.fetchall()
        cur.execute("SELECT * FROM monthly_mineral")
        monthly_mineral = cur.fetchall()

    return render(request,"main/monthly_chart.html",{
        "monthly_al" : monthly_al,
        "monthly_domestic_oil" : monthly_domestic_oil,
        "monthly_grain" : monthly_grain,
        "monthly_oversea_oil" : monthly_oversea_oil,
        "monthly_mineral" : monthly_mineral
    })


class GrainList(ListView):
    model = Grain

