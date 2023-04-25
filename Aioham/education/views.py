from django.shortcuts import render
from django.views import View
from .models import EducationCategory,EducationContent,EducationCourse,EducationSubject,EducationTeamMember
# Create your views here.
# def home(request):
    
#     return render(request,'education/index.html',)
class catagory(View):
    def get(self,request):
        caragory=EducationCategory.objects.all()
        return render(request,'education/index.html',{'catagory':caragory})


def courses(request,data=None):
    print('raja 13')
    if data=='programming':
        # course=EducationCourse.objects.filter(title=data)
        course=[p for p in EducationCourse.objects.all() if p.subject.category.title == data]
        return render(request,'education/courses.html',{'course':course})
    elif data=='History':
        course=[p for p in EducationCourse.objects.all() if p.subject.category.title == data]
        return render(request,'education/courses.html',{'course':course})
    elif data=='Geography':
        course=[p for p in EducationCourse.objects.all() if p.subject.category.title == data]
        return render(request,'education/courses.html',{'course':course})
    elif data=='math':
        course=[p for p in EducationCourse.objects.all() if p.subject.category.title == data]
        return render(request,'education/courses.html',{'course':course})
    else:
        print('raja 15')
        course=EducationCourse.objects.all()
        return render(request,'education/courses.html',{'course':course})
    

def contect(request):
    return render(request,'education/contact.html')
# class contect(View):
#     def get(self.request):
#         pass


class about(View):
    def get(self,request):
        team=EducationTeamMember.objects.all()    
        return render(request,'education/about.html',{"team":team})