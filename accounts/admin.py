from django.contrib import admin
from .models import CustomUser, EditorProfile, ReviewerProfile, SocialLink

admin.site.register(CustomUser)
admin.site.register(EditorProfile)
admin.site.register(ReviewerProfile)
admin.site.register(SocialLink)

