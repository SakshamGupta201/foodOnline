from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, username, email, password, **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, first_name, last_name, username, email, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(
            first_name, last_name, username, email, password, **extra_fields
        )


class CustomUser(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    ROLE_CHOICES = ((RESTAURANT, "Restaurant"), (CUSTOMER, "Customer"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class UserProfile(models.Model):
    """
    UserProfile model represents the profile information associated with a user.
    Attributes:
        user (OneToOneField): A one-to-one relationship with the CustomUser model.
        profile_picture (ImageField): An optional profile picture for the user.
        cover_picture (ImageField): An optional cover picture for the user.
        address_line_1 (CharField): The first line of the user's address.
        address_line_2 (CharField): The second line of the user's address.
        country (CharField): The country of the user's address.
        city (CharField): The city of the user's address.
        state (CharField): The state of the user's address.
        postal_code (CharField): The postal code of the user's address.
        longitude (FloatField): The longitude coordinate of the user's address.
        latitude (FloatField): The latitude coordinate of the user's address.
        created_at (DateTimeField): The date and time when the profile was created.
        updated_at (DateTimeField): The date and time when the profile was last updated.
    Methods:
        __str__(): Returns a string representation of the user profile, typically the user's email.
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    cover_picture = models.ImageField(upload_to="cover_pictures", blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}"
