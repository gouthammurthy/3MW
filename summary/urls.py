from django.conf.urls import url
from . import views

app_name = 'summary'

urlpatterns = [
    # summary/
    url(r'^/$', views.index, name='index'),
    # summary-average/
    url(r'^-average/$', views.average, name='average'),
]
