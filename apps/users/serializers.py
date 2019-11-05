import re
from rest_framework import serializers

from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

from rest_framework.validators import UniqueValidator

from MxShop.settings import REGEX_MOBILE
from apps.users.models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_phone(self, mobile):
        """
        验证手机号码
        :param phone:
        :return:
        """
        # 手机号是否注册
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法!")

        # 验证码发送频率
        one_mintes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_age, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile

class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "gender", "birthday","email","mobile")



class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4, required=True, label="验证码",write_only=True,help_text="验证码", error_messages={
        "required": "请输入验证码",
        "max_length": "验证码长度超过4位",
        "min_length": "验证码长度小于4位",
        "blank": "请输入验证码"
    })

    password = serializers.CharField(style={'input_type':'password'},label="密码",write_only=True)

    username = serializers.CharField(label="用户名",required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")])

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            five_mintes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
            if five_mintes_age > last_record.add_time:
                raise serializers.ValidationError("验证码过期!")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误!")
        else:
            raise serializers.ValidationError("验证码错误!")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile","password")
