from django.contrib import admin
from .models import EducationContent,EducationCategory,EducationCourse,EducationTeamMember,EducationSubject


@admin.register(EducationContent)
class ContentModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','category']


@admin.register(EducationCategory)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description']


@admin.register(EducationTeamMember)
class TeamMemberModelAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','image']

@admin.register(EducationCourse)
class CourseModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','course_image']
    
@admin.register(EducationSubject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display=['id','category','sub_name']