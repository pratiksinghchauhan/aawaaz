# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import listed_projects

# Register your models here.


class listed_projects_admin(admin.ModelAdmin):
	list_display=["transaction_id","payee","payer","payeeva","payerva","amount","recurrance","project_name","cutoff_votes","status","ts"]


admin.site.register(listed_projects,listed_projects_admin)