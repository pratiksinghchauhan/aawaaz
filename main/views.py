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
        sellerName = request.POST['seller']
        buyerName = request.POST['buyer']
        domain = request.POST['domain']
        payeeVa = request.POST['payee-va']
        payerVa = request.POST['payer-va']
        mobileBuyer = request.POST['mobile-buyer']
        mobileSeller = request.POST['mobile-seller']
        accountno = request.POST['payee-ac']
        amount = request.POST['amount']
        obj = listedTransfers(buyer = buyerName,seller = sellerName,payeeva = payeeVa,payerva = payerVa,domain = domain,payeemobile = mobileBuyer,payermobile = mobileSeller,selleraccount = accountno,amount = amount)
        obj.save()
        return render(request,"index.html",{"msg":"Your mandate is created, Leave rest on us, payment will automatically be done when the domain is transfered"})
    return render(request,"index.html",{"msg":""})