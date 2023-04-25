from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def parlour(request):
    # return HttpResponse("i am parlour")
    return render(request,"parlour/home.html")


from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Parlour_Facilitie,Employee,Parlour,User1




class CreateParlourPost(LoginRequiredMixin,CreateView):
    model=Parlour
    template_name="parlour/addparlour.html"
    fields=["Name","Ph_no"]
    success_url="/"
    def form_valid(self, form):
        # form.instance.user=self.request.user
        return super().form_valid(form)
    


class parlour(ListView):
    model=Parlour
    template_name="parlour/parlourhome.html"
    context_object_name='context'