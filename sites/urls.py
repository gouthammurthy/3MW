from django.conf.urls import url
from . import views

app_name = 'sites'

urlpatterns = [
    #  Default
    url(r'^$', views.IndexView.as_view(), name='index'),
    # sites/
    url(r'^sites/$', views.IndexView.as_view(), name='index'),
    # sites/213/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
