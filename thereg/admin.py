from thereg.models import Feedback, Member1, Member2, Member3, Member4
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from thereg.models import UserProfileInfo, User
from .models import Post
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Member1)
admin.site.register(Member2)
admin.site.register(Member3)
admin.site.register(Member4)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_filter = ('date',)
    search_fields = ('message',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
