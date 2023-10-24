from django.contrib import admin

# Register your models here.
from .models import Login

#admin page에 Login 모델 표시
admin.site.register(Login)