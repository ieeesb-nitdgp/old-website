from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
# Create your models here.
YEAR = [('1st','first'),('2nd','second'),('3rd','third'),('4th','fourth'),('HS or Lower','HS or Lower'),('grad','Graduate'),('PG','Post-Graduate')]

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='UserProfileInfo')
	Institute = models.CharField(max_length=200,blank=True)
	Department = models.CharField(max_length=200,blank=True)
	Year = models.CharField(max_length=13,choices=YEAR)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	varification_id = models.IntegerField(default=1245)
	varified = models.BooleanField(default=False)
    

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)



class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

 
    def __str__(self):
        return self.name







STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(upload_to='media/img',blank=True, default="media/img/transparent.jpg")
    image_1 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    image_2 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    image_3 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    event_date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title


