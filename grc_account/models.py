from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class SocialAccount(models.Model):
    """
        Social account model
    """

    class SocialType(models.IntegerChoices):
        LINKEDIN = 1
        FACEBOOK = 2
        GOOGLE = 3

    social_id = models.CharField(max_length=150)
    account = models.ForeignKey(
        get_user_model(), verbose_name='social_account',
        null=False, on_delete=models.CASCADE
    )
    social_type = models.IntegerField(choices=SocialType.choices)

    class Meta:
        db_table = 'social_account'
        verbose_name = 'Social account'
        verbose_name_plural = 'Social accounts'


def get_password_reset_token_expiry_time():
    """
    Returns the password reset token expiry time in hours (default: 24)
    """
    # get token validation time
    return getattr(settings, 'RESET_PASSWORD_EXPIRY', 24)


class User(models.Model):
    """
        This model contains users info.
        Required:
            - created_at
            - area
            - account
            - language
    """

    # 0 - applicant
    # 1 - employer
    created_at = models.DateTimeField()
    area = models.ForeignKey('grc_common.Area', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    account = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    language = models.CharField(max_length=2)
