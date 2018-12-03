# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Judge, Demographic

admin.site.register(Judge)
admin.site.register(Demographic)