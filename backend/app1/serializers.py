from rest_framework import serializers
from .models import Login

## 클래스의 인스턴스를 json 형식으로 바꾸는 방식
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
