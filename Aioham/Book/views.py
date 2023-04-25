from django.shortcuts import render
from .models import CreateBook,Category
from django.views import View

def home(request):
    return render(request,"Book/home.html")
class book12(View):
    def get(self,request):
        books=CreateBook.objects.all() 
        return render(request,"Book/book.html",{'books':books})

class book(View):
    def get(self,request,pk=None):
        print(pk)
        p=Category.objects.get(id=pk)
        data=p.Name
        print(data)
        if data=="AI":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]

        elif data=="programming languages":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]
        elif data=="horror":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]
        elif data=="network":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]
        elif data=="suspence":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]
        elif data=="thriller":
            books=[p for p in CreateBook.objects.all() if p.Category.id == pk]
        else:
            books=CreateBook.objects.all()    
        return render(request,"Book/book.html",{'books':books})    

def arrivals(request):
    return render(request,"Book/arrivals.html")

def blog(request):
    return render(request,"Book/blog.html")

class category(View):
    def get(self,request):
        cata=Category.objects.all()
        return render(request,"Book/category.html",{'cata':cata})

def reviews(request):
    return render(request,"Book/reviews.html")

class book1(View):
    def get(self,request,pk):
     p=CreateBook.objects.get(id=pk)
     
     print(p.document)
     return render(request,'Book/book1.html',{"pk":p.document})