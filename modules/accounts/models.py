from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group

from modules.accounts.managers import UserManager
from django.core.mail import send_mail


class Constants(models.TextChoices):
    """
    A class to define constants YES and NO for flag fields.
    """

    YES = "Yes", ("Yes")
    NO = "No", ("No")


class TrackingModel(models.Model):
    """
    Abstract base model for tracking creation and update timestamps.
    """

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    updated_flag = models.CharField(
        _("updated flag"),
        max_length=3,
        choices=Constants.choices,
        default=Constants.NO,
    )

    class Meta:
        abstract = True

class RoleChoices(models.TextChoices):
    """
    Enumeration of possible user roles.
    """

    SUPERUSER = "SUPERUSER", ("SUPERUSER")


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    Custom User model representing a user of the application.
    """

    name = models.CharField(_("full name"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.CharField(
        _("phone number"),
        max_length=56,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(_("staff"), default=False)
    is_active = models.BooleanField(_("active"), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    role = models.CharField(
        _("role"),
        max_length=20,
        choices=RoleChoices.choices,
        # default=RoleChoices.,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_("The groups this user belongs to."),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_set",
        related_query_name="user",
    )
    timestamp = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name_plural = "users"
        ordering = ["-id"]

    def __str__(self):
        """
        Returns a string representation of the user object.

        Returns:
            str: The user's email address.
        """
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to the user.

        Args:
            subject (str): The subject of the email.
            message (str): The content of the email.
            from_email (str, optional): The sender's email address.
            Defaults to None.
            **kwargs: Additional keyword arguments accepted by Django's
            `send_mail` function.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def superuser(self):
        """
        Property indicating whether the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.is_superuser

    @property
    def staff(self):
        """
        Property indicating whether the user is a staff member.

        Returns:
            bool: True if the user is a staff member, False otherwise.
        """
        return self.is_staff

    @property
    def active(self):
        """
        Property indicating whether the user account is active.

        Returns:
            bool: True if the user account is active, False otherwise.
        """
        return self.is_active


class GenderChoices(models.TextChoices):
    """
    Enumeration of possible gender choices for individuals.
    """

    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    PREFER_NOT_TO_SAY = "P", _("Prefer not to say")


class Profile(models.Model):
    """
    User profile
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_profile",
    )

    profile_image = models.ImageField(
        _("profile picture"),
        upload_to="profile_images",
        null=True,
        blank=True,
        default="default.png",
    )
    bio = models.TextField(_("bio"), max_length=500, null=True, blank=True)
    gender = models.CharField(
        _("gender"),
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.PREFER_NOT_TO_SAY,
    )
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        abstract = True


class SuperUser(Profile):
    """
    Model representing app Superusers.
    """

    def __str__(self):
        return self.user.email or self.user.phone_no

    class Meta:
        verbose_name_plural = "Super Users"
        ordering = ["-id"]
