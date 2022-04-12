from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.Homepage, name ="home"),
    path("chart/",views.chart_bar, name ="chart_bar"),
    path("monthly_chart",views.monthly_chart, name = "monthyl_chart")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
