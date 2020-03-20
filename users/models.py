from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    LANGUAGE_ENGLISH = 'es'
    LANGUAGE_KOREAN = 'kr'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean')
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, 'KRW')
    )

    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField()
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=6, null=True, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
