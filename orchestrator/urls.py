from django.conf.urls import url
from orchestrator import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^login/user/$', views.LoginUserList.as_view()),
    url(r'^login/user/(?P<pk>([0-9]|[a-z]|[A-Z])+)/$', views.AppUserDetail.as_view()),
    
    ## remover en produccion
    url(r'^login/users/$', views.AppUserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)