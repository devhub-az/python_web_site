from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    fullName = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','fullName']

    def get_fullName(self,obj):
        return obj.get_full_na



class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs ={
                    'password': {'write_only': True}
        }

    def save(self):
        user = User(
                username=self.validated_data['username'],
                email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'Şifrələr uygun gəlmir'})
        user.set_password(password)
        user.save()








