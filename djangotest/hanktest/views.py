from django.contrib import auth
from hanktest import forms
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hanktest.models import Profile
from hanktest.models import Poll
from hanktest.models import PollItem
'''
from django.core.mail import send_mail
from django.conf import settings
'''
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        username = request.user.username

    polls = Poll.objects.all()

    return render(request, 'index.html', locals())


def login(request):
    if request.user.is_authenticated():
        return redirect("/")
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                auth.login(request, user)
                print("Success")
                messages.add_message(request, messages.SUCCESS, '成功登入')
                return redirect("/")
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位')
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出")
    '''
    user_mail_topic = '登出囉'
    user_message = '123'
    to_list = ['hank.yang@istayreal.com']
    send_mail(user_mail_topic, user_message,
              settings.EMAIL_HOST_USER, to_list, fail_silently=False)
    '''
    return redirect("/")


@login_required
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = Profile.objects.get(user=user)
        except:
            pass
    return render(request, 'userinfo.html', locals())


def poll(request, pollid):
    try:
        poll = Poll.objects.get(id=pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = PollItem.objects.filter(poll=poll).order_by('-vote')

    return render(request, 'poll.html', locals())


def vote(request, pollid, pollitemid):
    try:
        pollitem = PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()

    target_url = '/poll/' + pollid

    return redirect(target_url)
