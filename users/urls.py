from django.conf.urls import url, include
from users.views import read_login, read_register, login, logout, register, comment, read_self, read_gouwuche, addgouwuche, pay

urlpatterns = [
    url(r"tologin/", read_login, name="gotologin"),
    url(r"toregister", read_register, name="gotoregister"),
    url(r'toself_info',read_self, name="gotoself"),
    url(r'togouwuche/(?P<pk>.*)$', read_gouwuche, name="gotogouwuche"),

    url(r"login", login, name="user_login"),
    url(r"logout", logout, name="user_logout"),
    url(r"register", register, name="user_register"),
    url(r"comment", comment, name="user_comment"),
    url(r'addgouwuche', addgouwuche, name="addgouwhche"),
    url(r'pay', pay, name="pay")


]