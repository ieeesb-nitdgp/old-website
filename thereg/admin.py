from django.contrib import admin

# Register your models here.
from django.contrib import admin
from thereg.models import UserProfileInfo, User
from .models import Post
# Register your models here.
admin.site.register(UserProfileInfo)



from thereg.models import Feedback
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_filter = ('date',)
    search_fields = ('message',)
 
    class Meta:
        model = Feedback
 
 
admin.site.register(Feedback, FeedbackAdmin)




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)