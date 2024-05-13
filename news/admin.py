from django.contrib import admin
from .models import CustomUser, EditorProfile, ReviewerProfile, Article, Category, Review

admin.site.register(CustomUser)
admin.site.register(EditorProfile)
admin.site.register(ReviewerProfile)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Review)
