from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.home_page,name = 'home_page'),
    url(r'^upload/$', views.upload_project, name='upload_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)