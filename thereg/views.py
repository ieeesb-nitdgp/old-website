from django.shortcuts import render , redirect
from thereg.models import Feedback,Post
# Create your views here.
import random
from django.contrib.auth import get_user_model
from django.shortcuts import render
from thereg.forms import UserForm,UserProfileInfoForm,FeedbackForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    form = FeedbackForm()
    return render(request,'thereg/index2.html', {'feedbackform': form})
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    flag =1
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        User = get_user_model()
        if user_form.is_valid() and profile_form.is_valid():
            for User in User.objects.filter():
                if user_form.cleaned_data['email'] == User.email:
                    flag =0
                    user_form.cleaned_data['username'] = " "
                    print("This mail address already exists!")
     
            if flag ==1:
                user = user_form.save()
                print("user saved")
                user.set_password(user.password)
                user.save()
                
                profile = profile_form.save(commit=False)
                profile.user = user
                varificationId = random.randrange(1000, 9999)
                profile.varification_id = varificationId
                message = "your Varification Id is:" + str(varificationId)
                send_mail(
                    'varify your mail',
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )

                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
            else :
                print("not-saved")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'thereg/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'flag':flag})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'thereg/login.html', {})






def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'thereg/index2.html', {'feedbackform': form})
    else:
        form = FeedbackForm()
    return render(request, 'thereg/index2.html', {'feedbackform': form})




def members(request):
    
    return render(request,'thereg/members.html',{})


class PostList(generic.ListView):
    model = Post
    template_name = 'thereg/events.html'
    


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'thereg/event_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context['post_list'] = Post.objects.all()
        return context



















def varification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        thevarificationid = request.POST.get('Varificationid')
        user = authenticate(username=username, password=password)
        if user:
            print(type(user.UserProfileInfo.varification_id))
            print(type(thevarificationid))
            if user.UserProfileInfo.varification_id == int(thevarificationid):
                user.UserProfileInfo.varified = True
                user.UserProfileInfo.save()
                print("varification-done")
                print(user.UserProfileInfo.varified)
                if user.UserProfileInfo.varified:
                    print("updated")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("invalid varification details!")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login or varification details details given")
    else:
        return render(request, 'thereg/varifyid.html', {})

