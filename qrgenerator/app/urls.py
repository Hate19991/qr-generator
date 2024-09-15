from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="Home page"),
    path('display/<str:modal_name>/<int:pk>', views.qrcode , name="Display")
]
