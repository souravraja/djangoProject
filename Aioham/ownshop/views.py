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
            
            return render(request,"ownshop/Stationary/home.html",k)
        
        # if data == 'Resturent':
        #     # k=[p for p in Ownshop.objects.all() if p.id == pk ]
        #     return render(request,"ownshop/restudent/home.html",{'k':k})






class manu(View):
    def get(self,request,pk,data=None):
        print(data)
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
        
        elif data == "strret":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Street food/manu.html",k)
        
        elif data == "medicine":
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
        elif data == "chiken":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Chiken/manu.html",k)
        elif data == "cloths":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/cloths/manu.html",k)
        elif data == "fruit":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Fruits/manu.html",k)
        elif data == "Groceroy":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            print('raja')
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Grocery/manu.html",k)
        elif data == "Stationary":
            food=[p for p in Product.objects.all() if p.shopname.id == pk]
            k={
                "k":food,
                'data':data,
                'pk':pk
            }
            return render(request,"ownshop/Stationary/manu.html",k)
        elif data == None:
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
    pk=None
    def get(self,request,pk):
        self.pk=pk
        form=AddProduct
        return render(request,'ownshop/additems.html',{'form':form})
    
    def post(self,request,pk):
        k=[p for p in Ownshop.objects.all() if p.id == pk]
        k1=[p.type1.name for p in Ownshop.objects.all() if p.id == pk]
        data=k1[0]
        form=AddProduct(request.POST,request.FILES,)
        if form.is_valid():
            
            product=form.cleaned_data['product']
            price=form.cleaned_data['price']
            prodict_details=form.cleaned_data.get('product_details')
            product_img=form.cleaned_data['product_image']
            reg=Product(shopname=k[0],product=product,price=price,product_details=prodict_details,product_image=product_img,)
            reg.save()
        return redirect("manu",pk=pk,data=data)

class addshop(View):
    pk=None
    def get(self,request,pk):
        k=[ShopCategory.objects.get(id=pk)]
        self.pk=pk
        form=AddShop
        return render(request,'ownshop/addshop.html',{'form':form})
    def post(self,request,pk):
        print(pk)
        # k=[ShopCategory.objects.get(id=pk)]
        # k1=[p for p in Ownshop.objects.all() if p.id == pk ]
        k=[p for p in ShopCategory.objects.all() if p.id == pk]
        form=AddShop(request.POST,request.FILES)
        if form.is_valid():
            shopcategory=k[0]
            shopname=form.cleaned_data['shop_name']
            shop_ownername=form.cleaned_data['shop_ownername']
            ph_no=form.cleaned_data['ph_no']
            address=form.cleaned_data['address']
            reg=Ownshop(type1=shopcategory,shop_name=shopname,shop_ownername=shop_ownername,ph_no=ph_no,address=address)
            reg.save()
            return redirect('nameofshop',pk=pk)