# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class listed_projects(models.Model):
    transaction_id = models.CharField(max_length=200,primary_key=True)
    payee = models.CharField(max_length=200)
    payer = models.CharField(max_length=200)
    payeeva = models.CharField(max_length=200)
    payerva = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    recurrance = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    cutoff_votes = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    votes = models.IntegerField(null=True)
    ts = models.DateTimeField(auto_now_add=True)
