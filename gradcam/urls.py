from django.urls import path
from .views import gradcam_image, gradcam_page

urlpatterns = [
    path('gradcam/', gradcam_image, name='gradcam_image'),
    path('show-gradcam/', gradcam_page, name='show_gradcam'),
]

