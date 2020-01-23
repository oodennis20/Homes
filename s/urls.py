from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^editprofile/$',views.edit_profile,name= 'edit_profile'),
    url(r'^createpost/$', views.create_post, name = 'create_post'),
    url(r'^createhood/$', views.create_hood, name='create_house'),
    url(r'^deletepost/(\d+)',views.delete_post,name = 'delete_post'),
    url(r'^search/$',views.search,name= 'search'),
    url(r'^deletehood/(\d+)',views.delete_hood,name = 'delete_house'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)