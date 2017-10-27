# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import viewsRegion
from . import viewsDepar
from . import viewsLugar


# from siteTour import views

urlpatterns = [
    url(r'^region/$', viewsRegion.region_list),
    url(r'^region/(?P<pk>[0-9]+)/$', viewsRegion.region_detail),
    url(r'^departamento/$', viewsDepar.departamento_list),
    url(r'^departamento/(?P<pk>[0-9]+)/$', viewsDepar.departamento_detail),
    url(r'^departamento/region/(?P<idreg>[0-9]+)/$', viewsDepar.depa_xRegion),
    url(r'^lugar/$', viewsLugar.lugar_list),
    url(r'^lugar/(?P<pk>[0-9]+)/$', viewsLugar.lugar_detail),
    url(r'^lugar/departamento/(?P<idepa>[0-9]+)/$', viewsLugar.lugar_xDepa),
]