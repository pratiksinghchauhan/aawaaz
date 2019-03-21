# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import listedTransfers
import whois

# Create your views here.
# def transferDomain(request):
#      if request.method == "POST":
#          sellerName = request.POST['sellerName']
#          buyerName = request.POST['buyerName']
#          sellerUpi = request.POST['sellerUpi']


def sendmessage(sellerName,buyerName,mobileSeller,domain,amount):
    try:

        url = "http://2factor.in/API/293832-67745-11e5-88de-5600000c6b13/ADDON_SERVICES/SEND/TSMS"
        mobileSeller = cname
        amount_fin = str(amount) +"Rs"
        msg = "Hi" + str(sellerName) + ", a mandate request for domain "+ domain + "has been created by user " + buyerName + "please transfer to recive payment of "+ amount +" Thanks."
        payload={"From":"DISINTERMEDIATE","To":str(mobileSeller),"Msg":msg }
        response = requests.request("POST", url, data=payload)
        result_js=response.json()
        print(result_js)
    except Exception,e:
        print e
    return

def transferDomain(request):
    if request.method == "POST":
        return render(request,"index.html",{"msg":"Your Vote is recorded! Thanks for voting"})
    return render(request,"index.html",{"msg":""})

def contractorDashboard(request):
    return render(request,"dashboard.html")