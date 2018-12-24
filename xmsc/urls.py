from django.conf.urls import url
from xmsc.views import read_index, read_xiangqing, read_liebiao

urlpatterns = [
    url(r"index/", read_index, name="gotoindex"),
    url(r'xiangqing/(?P<pk>.*)$', read_xiangqing, name= "gotoxiangqing"),
    url(r'liebiao/(?P<pk>.*)$', read_liebiao, name="gotoliebbiao"),


]
