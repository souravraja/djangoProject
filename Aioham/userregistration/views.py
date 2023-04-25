from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm

# Create your views here.
# @login_required(login_url='login')
def HomePage(request):
    # pass
    return render (request,'userregistration/home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')

        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'userregistration/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'userregistration/login.html')
# logout 
def LogoutPage(request):    
    logout(request)
    return redirect('login')




# profile

class profileview(LoginRequiredMixin,View):
    def get(self,request):
        # profile=Profile.objects.get(pk=pk)
        # return render(request,"userregistration/profile.html",{'profile':profile})
        return render(request,"userregistration/profile.html")
    
class profileview1(LoginRequiredMixin,View):
    def get(self,request,pk):
        profile=Profile.objects.get(pk=pk)
        
        print("raja1")
        print(profile.user.username)
        print(profile.img)
        print('raja2')
        return render(request,"userregistration/profile1.html",{'profile1':profile})

        # return render(request,"userregistration/profile.html")
    
class Edit_profile(LoginRequiredMixin,View):
    def get(self,request):
        form=ProfileForm
        return render(request, "userregistration/edit_profile.html",{'form':form})
    def post(self,request):
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            bio=form.cleaned_data['bio']
            location=form.cleaned_data['location']
            birth_date=form.cleaned_data['birth_date']
            img=form.cleaned_data['img']
            # reg=Profile(user=user,bio=bio,location=location,birth_date=birth_date,img=img)
            print(bio)
            print(location)
            print(birth_date)
            print(img)
            return redirect('profile_edit')
            
        return render(request, "userregistration/edit_profile.html")





# def home_view(request):
# 	context ={}

# 	# create object of form
# 	form =ProfileForm (request.POST or None, request.FILES or None)
	
# 	# check if form data is valid
	
# 		# save the form data to model
# 		form.save()

# 	context['form']= form
# 	return render(request, "userregistration/edit_profile.html", context)
