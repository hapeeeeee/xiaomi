from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import authenticate, login as user_login, logout as user_logout, get_user_model
from users.forms import UserLoginFORM, UserRegForm, GouWuCheSaveForm
from comments.forms import CommentForm, CommentSaveForm
from xmsc.views import read_xiangqing
from comments.models import Comment
from xmsc.models import Phone
from users.models import GouWuche



from django.conf.urls import url

# Create your views here.
User = get_user_model()

def read_login(request):
    loginform = UserLoginFORM()

    return render(request, "login.html", {"loginform": loginform})


def read_register(request):
    regform = UserRegForm()
    return render(request, "register.html", {"regform": regform})


def read_self(request):
    return render(request, "self_info.html")

def read_gouwuche(requset, pk):

    gouwuche_data = GouWuche.objects.filter(user_id=pk)

    total = 0
    for data in gouwuche_data:
        total += data.phone.price
    return render(requset, "gouwuche.html", {"gouwuche_data": gouwuche_data, "total": total})

def login(request):

    data = UserLoginFORM(request.POST)
    if not data.is_valid():
        errors_msg = data.errors
        loginform = UserLoginFORM()
        return render(request, "login.html", {"errors": errors_msg, "loginform": loginform})

    res = data.cleaned_data
    user = authenticate(**res)

    try:
        user_login(request, user)
    except AttributeError:
        loginform = UserLoginFORM()
        return render(request, "login.html", {"errors": "账号或密码错误", "loginform": loginform})

    return redirect("/xiaomi/index/")

def logout(request):
    user_logout(request)
    url_source= request.META['HTTP_REFERER']
    return redirect(url_source)

def register(request):
    data = UserRegForm(request.POST)

    if not data.is_valid():
        error_msg = data.errors
        regform = UserRegForm()
        return render(request, "register.html", {"errors": error_msg, "regform": regform})



    res = data.cleaned_data
    if res['password'] != res['password_again']:

        error_msg = "两次密码不一致"
        regform = UserRegForm()

        return render(request, "register.html", {"errors": error_msg, "regform": regform})

    res.pop('password_again')
    user = User.objects.create_user(**res)
    user_login(request, user)


    return redirect("/xiaomi/index/")


def comment(request):

    comment_data = dict()
    comment_data["user"] = request.user.id
    comment_data["content"] = request.POST.get("content", None)
    comment_data["phone"] = request.POST.get("phone_id", None)
    data = CommentSaveForm(comment_data)

    url_source = request.META['HTTP_REFERER']
    if not data.is_valid():
        return redirect(url_source)

    data.save()
    return redirect(url_source)

def addgouwuche(request):
    print(1111111)
    gouwuche_data = dict()
    phone_id = request.POST.get("phone_id", None)
    gouwuche_data['phone'] = phone_id
    gouwuche_data['user'] = request.user.id

    data = GouWuCheSaveForm(gouwuche_data)


    if not data.is_valid():
        error_msg = request.errors
        return render(request, "xiangqing.html", {"flag": False, "msg": request.errors})


    data.save()


    phone = get_object_or_404(Phone.objects.filter(id=phone_id))
    comments = Comment.objects.filter(phone_id= phone_id)
    commentform = CommentForm()

    return render(request, "xiangqing.html", {"flag": True, "msg": "加入购物车成功", "phone": phone, "commentform": commentform, "comments": comments})


def pay(request):
    pay_user_id = request.user.id
    data = GouWuche.objects.filter(user_id=pay_user_id)
    # for data1 in data:
    #     print(data1)
    data.delete()

    url_source = request.META.get('HTTP_REFERER')
    return redirect(url_source)
