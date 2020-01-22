from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^editprofile/$',views.edit_profile,name= 'edit_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)