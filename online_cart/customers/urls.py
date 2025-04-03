
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("account",views.show_account,name='account'),
    path("about",views.show_about,name='about'),
    path("logout",views.signout,name='logout'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)