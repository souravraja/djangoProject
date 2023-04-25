from django.shortcuts import render
from .forms import Search
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

# Create your views here.

def all(request):
    if request.method=='POST':
        fm=Search(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            if name=="":
                return render(request,"all/home.html",{'form':fm})
                
            else:
                result=[]
                url="https://www.google.com/search?q="+name
                page=requests.get(url).text               
                soup=BeautifulSoup(page,'html.parser')
                print("4")
                listings=soup.find_all(class_="Gx5Zad fP1Qef xpd EtOod pkphOe")
                # print(listings)
                for i in listings:
                    title=i.find(class_="BNeawe vvjwJb AP7Wnd").text
                    description=i.find(class_="BNeawe s3v9rd AP7Wnd").text
                    url=i.a['href']
        
                    result.append((title,description,url))
                context={'result':result}
                print("raja")
                return render(request,"all/result_search.html",context)
    else:
        fm=Search()
    return render(request,"all/home.html",{'form':fm})
