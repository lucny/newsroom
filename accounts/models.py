from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name = 'Sociální síť'
        verbose_name_plural = 'Sociální sítě'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Uživatel'
        verbose_name_plural = 'Uživatelé'

    def __str__(self):
        return self.username


class EditorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='editor_profile',
    )
    social_links = models.ForeignKey(SocialLink, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.CharField(max_length=7, default='#FFFFFF')  # Ukládá HEX barvu

    class Meta:
        verbose_name = 'Redaktor'
        verbose_name_plural = 'Redaktoři'

    def __str__(self):
        return f'Editor profile of {self.user.username}'


class ReviewerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviewer_profile',
    )
    public_profile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Recenzent'
        verbose_name_plural = 'Recenzenti'

    def __str__(self):
        return f'Reviewer profile of {self.user.username}'
