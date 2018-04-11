from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^q1/$', views.q1, name='q1'),
    url(r'^q2/$', views.q2, name='q2'),
    url(r'^q3/$', views.q3, name='q3'),
    url(r'^q4/$', views.q4, name='q4'),
    url(r'^conclusion/$', views.conclusion, name='conclusion'),
]
urlpatterns += staticfiles_urlpatterns()
