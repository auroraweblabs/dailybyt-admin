from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from apps.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phoneregex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone Number Must be entered in Valid Format")
    phone = models.CharField(_('Phone Number'), validators=[phoneregex],
                             unique=True, max_length=15)
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('Last Login'), auto_now=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/',
                               null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
