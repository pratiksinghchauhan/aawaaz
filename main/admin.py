# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import listedTransfers

# Register your models here.


class listedTransfersAdmin(admin.ModelAdmin):
	list_display=["seller","buyer","payeeva","payerva","payeemobile","payermobile","selleraccount","domain","amount","state","ts"]


admin.site.register(listedTransfers,listedTransfersAdmin)