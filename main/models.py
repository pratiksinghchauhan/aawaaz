# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class listedTransfers(models.Model):
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    payeeva = models.CharField(max_length=200)
    payerva = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    payeemobile =  models.CharField(max_length=200)
    payermobile = models.CharField(max_length=200)
    selleraccount = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.buyer 
