from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ShopCategory,Product,Ownshop
from django.views import View
from .forms import AddShop,AddProduct
from django.contrib import messages

# from django.http import HttpResponse

# Create your views here.
def typeofshop(request):
    # return HttpResponse(" ia m ownshop")
    typeofshop=ShopCategory.objects.all()
    return render(request,"ownshop/typeofshop.html",{'data':typeofshop})

class nameofshop(View):
    def get(self,request,pk):
        k=ShopCategory.objects.get(id=pk)
        print(pk)
        shopname=[p for p in Ownshop.objects.all() if p.type1.name == k.name]
        shopname1={
            'shopname':shopname,
            'k':k,
            'pk':pk
        }
        return render(request,"ownshop/nameofshop.html",shopname1)
    def post(self,request):
        return HttpResponse(request,'post method')


class ownshop(View):
    def get(self,request,pk,data=None):
        # data=ShopCategory.objects.all()
        if data == "Resturant":
            print(data)
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            print('raja')
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/restudent/home.html",k)
        
        if data == "strret":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print('raja')
            return render(request,"ownshop/Street food/home.html",k)
        
        if data == "chiken":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Chiken/home.html",k)
        
        if data == "medicine":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print('raja')
            return render(request,"ownshop/Medicine/home.html",k)
        
        if data == "cloths":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print('raja')
            return render(request,"ownshop/cloths/home.html",k)
        
        if data == "fruit":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print('raja')
            return render(request,"ownshop/Fruits/home.html",k)
        
        if data == "Groceroy":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print('raja')
            return render(request,"ownshop/Grocery/home.html",k)
        
        if data == "Stationary":
            # k=[Ownshop.objects.get(id=pk)]
            k1=[p for p in Ownshop.objects.all() if p.id == pk ]
            k={
                "k":k1,
                'data':data,
                'pk':pk
            }
            print(k)
            return render(request,"ownshop/Stationary/home.html",k)
        
        # if data == 'Resturent':
        #     # k=[p for p in Ownshop.objects.all() if p.id == pk ]
        #     return render(request,"ownshop/restudent/home.html",{'k':k})






class manu(View):
    def get(self,request,pk,data=None):
        if data == "Resturant":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            print(pk)
            print()
            k={
                "k":food,
                'data':data,
                "pk":pk
            }
            return render(request,"ownshop/restudent/manu1.html",k)
        
        if data == "strret":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Street food/manu.html",k)
        
        if data == "medicine":
            k=[Ownshop.objects.get(id=pk)]
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk,
                'p':k
            }
            return render(request,"ownshop/Medicine/manu.html",k)
        if data == "chiken":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Chiken/manu.html",k)
        if data == "cloths":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/cloths/manu.html",k)
        if data == "fruit":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Fruits/manu.html",k)
        if data == "Groceory":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Grocery/manu.html",k)
        if data == "Stationary":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Stationary/manu.html",k)
        else:
            return HttpResponse("raja")
        

class addmanyitems(View):
    def get(self,request):
        form=AddProduct
        return render(request,'ownshop/additems.html',{'form':form})
    def post(self,request):
        form=AddProduct(request.POST,request.FILES)
        if form.is_valid():
            
            product=form.cleaned_data['product']
            price=form.cleaned_data['price']
            prodict_details=form.cleaned_data['product_details']
            product_img=form.cleaned_data['product_image']
            
            print(product)
            print(price)
            print(prodict_details)
            print(product_img)
            return redirect("addmanuitems")

class addshop(View):
    
    def get(self,request):
        print()
        form=AddShop
        return render(request,'ownshop/addshop.html',{'form':form})
    def post(self,request):
        form=AddShop(request.POST,request.FILES)
        if form.is_valid():
            shopname=form.cleaned_data['shop_name']
            shop_ownername=form.cleaned_data['shop_ownername']
            ph_no=form.cleaned_data['ph_no']
            address=form.cleaned_data['address']
            print(shopname)
            print(shop_ownername)
            print(ph_no)
            print(address)
            return redirect("nameofshop")