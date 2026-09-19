from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

    # def validate_pincode(self,value):
    #     if len(value) != 6:
    #         raise serializers.ValidationError('pincode is only 6 digit')
    #     if not value.isdigit():
    #         raise serializers.ValidationError('pincode only contains digit')
    #     return value
    # def validate_mobile(self,value):
    #     if len(value) != 10:
    #         raise serializers.ValidationError('Your mobile number must be only 10 digits')
    #     if not value.isdigit():
    #         raise serializers.ValidationError('mobile number should only be digits')
    #     return value
    def validate(self,attrs):
        mobile=attrs.get('mobile')
        pincode=attrs.get('pincode')
        if len(mobile) !=10:
            raise serializers.ValidationError('Mobile number should only be 10 digits')
        if not mobile.isdigit():
            raise serializers.ValidationError('Mobile number only be a digits')
        if len(pincode)!=6:
            raise serializers.ValidationError('Pincode is only 6 digits')
        if not pincode.isdigit():
            raise serializers.ValidationError('Pincode is only digits')
        return attrs