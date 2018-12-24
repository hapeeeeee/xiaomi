from django.shortcuts import render, get_object_or_404
from xmsc.models import Phone
from comments.forms import CommentForm
from comments.models import Comment
from xmsc.models import Category

# Create your views here.


def read_index(request):
    phones = Phone.objects.all()
    categorys = Category.objects.all()
    return render(request, "index.html", {"phones": phones, "categorys": categorys})

def read_xiangqing(request, pk):
    phone = get_object_or_404(Phone.objects.filter(id=pk))
    comments = Comment.objects.filter(phone_id=pk)
    commentform = CommentForm()
    return render(request, "xiangqing.html", {"phone": phone, "commentform": commentform, "comments": comments})


def read_liebiao(request, pk):
    phones = Phone.objects.filter(kind_id=pk)
    return render(request, "liebiao.html", {"phones": phones})