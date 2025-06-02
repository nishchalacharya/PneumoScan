


from django.contrib import admin
from django.urls import path,include
from django.conf import settings #for image
from  django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('loginapp.urls')),
    path("blogapp/",include('blogapp.urls')),
    path("gradcam/",include('gradcam.urls'))
    
    # path("chatapp/",include('chatapp.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
