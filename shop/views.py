from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,CarouselImages,Contact,Order,OrderUpdate
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from .paytm import Checksum
# Create your views here.
import math

def index(request):
   
    
    allprods = []
    catprod = Product.objects.values('category', 'id')
    # print(catprod)
    cats = {item['category'] for item in catprod}
    # print(cats)
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        nos = len(prod)
        no_of_slides = ((nos // 4) + math.ceil((nos/4) - (nos//4)))
        allprods.append([prod,no_of_slides,range(1,no_of_slides)])
        
    
    params = {"allprods" : allprods}
   
    return render(request,'shop/index.html' , params)
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        query = request.POST.get('query', '')
        con = Contact(name = name,email = email,desc = query)
        con.save()
        messages.success(request, 'Form submission successful')
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id' , '')
        email = request.POST.get('email', '')
        
        try:
            res =  Order.objects.filter(order_id = order_id , email = email)
            if len(res) > 0:
                result = OrderUpdate.objects.filter(order_id = order_id)
                updates = []
                print(res[0].item_json)
                for item in result:
                    updates.append({'text' : item.order_desc , 'time' : item.update_time , 'date' : item.update_date})
                    response = json.dumps({"status" : "success", "updates" : updates , "item_json" :  res[0].item_json} ,default=str) 
                return HttpResponse(response) 
            else:
                return HttpResponse('{"status" : "Not found"}')

        except Exception as e:
            return HttpResponse('{"status" : "Error"}')

    return render(request,'shop/tracker.html')

def search(request):
    query = request.GET.get('search')
    allprods = []
    
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        # for item in prod:
        #     if query.lower() in item.product_name.lower()  or query.lower() in item.product_desc.lower() or query.lower() in item.category.lower() or query.lower() in item.subCategory.lower():
        #         prods = [item]
        prods = [item for item in prod if query.lower() in item.product_name.lower()  or query.lower() in item.product_desc.lower() or query.lower() in item.category.lower() or query.lower() in item.subCategory.lower()]
        nos = len(prods)
        no_of_slides = ((nos // 4) + math.ceil((nos/4) - (nos//4)))
        if len(prods) > 0:
            allprods.append([prods,no_of_slides,range(1,no_of_slides)])
    params = {"allprods" : allprods , "msg" : ""}
    if len(allprods) == 0:
        params = {'msg' : "Please Enter a Relevant Search Query!!!"}
    return render(request,'shop/search.html' ,params)

def productView(request , myid):
    product  = Product.objects.filter(id = myid)
    return render(request,'shop/productView.html' , {"pro" : product[0]} )

def productView1(request):
    return render(request,'shop/productView.html')

def checkOut(request,mid):
    prod = Product.objects.filter(id = mid)
    return render(request,'shop/checkOut.html' , {"prod" : prod[0]})

def check(request):
    if request.method == "POST":
        item_json = request.POST.get('item_json')
        amount = request.POST.get('amount')
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        address = request.POST.get('address1', '') + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        number = request.POST.get('number', '')
        data = Order(item_json = item_json , name = name,email = email,address = address , city = city , state = state ,zip_code = zip_code,number = number,amount = amount)
        data.save()
        or_id = data.order_id
        update = OrderUpdate(order_id = or_id , order_desc = "The Order Has Been Placed..."  )
        update.save()
        thank = True
        param_dict = {
            'MID':'WZQuzq13014084176041',
            'ORDER_ID': str(or_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,'e6aarV!WScrehy@8')
        return render(request,'shop/paytm.html' , {"param_dict" : param_dict})
        # return render(request,'shop/checkOut.html' , {"thank" : thank, "id" : or_id })
    return render(request,'shop/checkOut.html')

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == "CHECKSUMHASH":
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict,'e6aarV!WScrehy@8',checksum)
    if verify:
        if response_dict["RESPCODE"] == "01":
            print("Order successful")
        else:
            print("Payment Failed because " + response_dict["RESPMSG"])
        
    return render(request, 'shop/paymentstatus.html',{'response' : response_dict})
    