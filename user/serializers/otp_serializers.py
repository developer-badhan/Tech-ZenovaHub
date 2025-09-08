from rest_framework import serializers
from user.models import EmailOTP
from user.models import User


# OTP Serializer
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOTP
        fields = ["id", "user", "code", "created_at", "is_verified"]
        read_only_fields = ["id", "created_at", "is_verified"]


# Request OTP, Verify OTP, Resend OTP serializers
class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


# Verify OTP serializer
class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get("email")
        code = data.get("code")
        try:
            user = User.objects.get(email=email)
            otp = EmailOTP.objects.get(user=user)
        except (User.DoesNotExist, EmailOTP.DoesNotExist):
            raise serializers.ValidationError("Invalid email or OTP.")
        if otp.code != code:
            raise serializers.ValidationError("Incorrect OTP.")
        if otp.is_verified:
            raise serializers.ValidationError("OTP already verified.")
        if otp.is_expired():
            raise serializers.ValidationError("OTP has expired.")    
        return data


# Resend OTP serializer
class OTPResendSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value
