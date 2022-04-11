from django.urls import path
from . import views

urlpatterns = [
    path("",views.Homepage, name ="home"),
    path("/chart",views.chart_bar, name ="chart_bar"),
    path("/db",views.GrainList.as_view()),
]
