from django.urls import path
from .views import *

app_name = 'Image'

urlpatterns = [
    path('image/', ImageUpload.as_view(), name='image'),
    path('view', ImageView.as_view(), name='view'),
    path('delete/<int:id>', delete_image, name='delete')
]