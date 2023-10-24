from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app1 import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('Login', views.LoginView, 'Login')

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('', HomeTemplateView.as_view(), name='home'),
]



