from typing import Iterable, Optional
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _


class Group(AbstractUser, PermissionsMixin):
    class GroupRole(models.TextChoices):
        GROUP = "GROUP", _("GROUP admin")
        SYSTEM_ADMIN = "SYSTEM_ADMIN", _("system admin")

    name = models.CharField(verbose_name=_(
        "name"), max_length=32, null=True, blank=True)
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        validators=[RegexValidator(regex="^(09)[0-9]{9}$")],
        max_length=16,
        unique=True,
        blank=True,
        null=True
    )
    email = models.EmailField(verbose_name=_(
        "email address"), null=True, blank=True, unique=True)
    role = models.CharField(
        verbose_name=_("role"),
        max_length=16,
        choices=GroupRole.choices,
        default=GroupRole.SYSTEM_ADMIN,
        help_text=_(
            "role designates user's role at the time it could has only one role "),
    )

    def __str__(self):
        if (self.name):
            return self.name
        else:
            return "بدون نام"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "گروه‌ها"
        verbose_name_plural = "گروه‌ها"


class GroupMedias(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                           editable=False, verbose_name="آیدی فایل")
    file_type = models.CharField(max_length=50)
    file = models.ImageField(verbose_name="فایل ارسالی کاربر")
    group = models.ForeignKey(Group, verbose_name="گروه فرستنده",
                              on_delete=models.CASCADE, related_name="group_media")
    created_at = models.DateTimeField(auto_created=True, auto_now=True)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.title
