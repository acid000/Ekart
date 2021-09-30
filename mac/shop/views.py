from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,orders,orderupdate
from math import ceil
import json
def index(request):
    products=product.objects.all()
    print(products)
    n=len(products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides':nslides, 'range': range(1,nslides),'product': products}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contactt(request):
    if request.method=="POST":

        name=request.POST.get('name','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        print(name,phone,email,desc)
        contacts= contact(name=name,phone=phone,email=email,desc=desc)
        contacts.save()
    return render(request,'shop/contact.html')
def productdetails(request,id):
    prod=product.objects.filter(id=id)
    print(prod)
    return render(request,'shop/products.html',{'prod':prod[0]})
def search(request):
    return HttpResponse("search page")
def tracker(request):
    if request.method == "POST":
        id=request.POST.get('id','')
        email=request.POST.get('email','')


        try:
            order=orders.objects.filter(order_id=id,email=email)
            if len(order)>0:
                update=orderupdate.objects.filter(order_id=id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})

                for i in updates:
                    x=i['text']
                    y=i['time']
                return HttpResponse(f"{x} ON {y}")

            else:
                return HttpResponse("error")
        except Exception as e:
            return HttpResponse("exception")

    return render(request, 'shop/tracker.html')

def checkout(request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            item_json=request.POST.get('item_json', '')
            state = request.POST.get('state', '')
            city = request.POST.get('city', '')
            zip = request.POST.get('zip', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address','')
            ord = orders(item_json=item_json,name=name, phone=phone, email=email, state=state,city=city,zip=zip,address=address,)
            ord.save()
            update=orderupdate(order_id=ord.order_id,update_desc="Your Order Has Been Placed")
            update.save()
            thank=True
            id=ord.order_id
            return render(request, 'shop/checkout.html', { 'thank':thank,'id': id})
        return render(request,'shop/checkout.html')
