from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from datetime import date
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with teh given email and password.

        """

        if not email:
            raise ValueError(_("Vous devez renseigner un email!"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.BigIntegerField(default="0000000000", blank=True)
    send_email = models.BooleanField(default=False)
    send_text_message = models.BooleanField(default=False)
    user_language = models.CharField(max_length=20, blank=False, default='fr')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [_("first_name"), _("second_name"), _("send_email"), _("send_text_message")]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_absolute_url(self):
        return "/users/%s/" % (self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.second_name)
        return full_name.strip()


class History(models.Model):
    """ Class to define the History table."""

    user = models.ForeignKey("CustomUser", related_name=_('User'), null=True, on_delete=models.CASCADE)
    sorted_cards_date = models.DateField(default=date.today, auto_created=True)
    sorted_cards = models.ManyToManyField("clairvoyance.Majorarcana", verbose_name=_("Tiragem"))
    daily_sorted_cards = models.CharField( default= "list of cards", max_length=200) #rec the daily_cards


    class Meta:
        db_table = "history"""
