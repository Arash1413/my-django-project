from django.contrib import admin
from .models import Story


admin.site.register(Story)

# @admin.register(Story)
# class StoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('title', 'user_prompt')

# Register your models here.
