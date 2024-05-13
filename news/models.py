from django.contrib.auth.models import AbstractUser
from django.db import models


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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='editor_profile')
    social_links = models.JSONField(default=dict)  # Můžete použít i modely místo JSONField
    color = models.CharField(max_length=7, default='#FFFFFF')  # Ukládá HEX barvu

    class Meta:
        verbose_name = 'Redaktor'
        verbose_name_plural = 'Redaktoři'

    def __str__(self):
        return f'Editor profile of {self.user.username}'


class ReviewerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='reviewer_profile')
    public_profile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Recenzent'
        verbose_name_plural = 'Recenzenti'

    def __str__(self):
        return f'Reviewer profile of {self.user.username}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='category_logos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Rubrika'
        verbose_name_plural = 'Rubriky'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='article_photos/', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Článek'
        verbose_name_plural = 'Články'

    def __str__(self):
        return self.title


class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        return f'Autor: {self.reviewer.username}, článek: {self.article.title}'
