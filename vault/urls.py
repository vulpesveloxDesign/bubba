from django.urls import path
from .views import home, get_name, contact, product, water_quality, downloads

app_name = 'vault'

urlpatterns = [
    path('', home, name="home"),
    path('get_name/', get_name, name="get_name"),
    path('water_quality/', water_quality, name="water_quality"),
    path('contact/', contact, name="contact"),
    path('product/', product, name="product"),
    path('downloads/', downloads, name="downloads"),
]
