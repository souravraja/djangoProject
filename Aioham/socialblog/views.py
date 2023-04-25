from django.shortcuts import render,redirect
from .models import Post,StoryPost
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .froms import PostForm
from django.contrib.auth.decorators import login_required
from django.views import View


class home(ListView):
    model=Post
    template_name='socialblog/home1.html'
    context_object_name='context'
    
    ordering="?"
def ShortVideo(request):
    story=StoryPost.objects.all()
    return render(request,'socialblog/story.html',{'story':story})

# class CreatePost(LoginRequiredMixin,CreateView):
#     model=Post
#     # fields=['title','description','image']
#     fields=['title','description']
#     template_name="socialblog/newpost.html"
#     success_url="../"
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         return super().form_valid(form) 
    
class CreatePost(View):
    def get(self,request):
        form=PostForm
        return render(request,"socialblog/newpost.html",{'form':form})
    def post(self,request):
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            image=form.cleaned_data['image']
            print(user)
            reg=Post(user=user,title=title,description=description,image=image)
            reg.save()
            return redirect('/socialblog/')
            
            return render(request,'socialblog/home1.html')


class PostDetails(DetailView):
    model=Post
    template_name="socialblog/detail.html"


class DelateView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="../"
    template_name="socialblog/delete.html"
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.user:
            return True
        return False
    success_url='/'


class Update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','description','Image',]
    template_name="socialblog/update.html"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.user:
            return True
        return False
    success_url="/socialblog/"