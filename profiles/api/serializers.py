from rest_framework import serializers
from profiles.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _ # translate to a different language if you choose!



# create a user
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        # fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                },
                'min_length': 6
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

 

# Token Serializer(User Authentication)
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user: 
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        
        attrs['user'] = user
        return attrs