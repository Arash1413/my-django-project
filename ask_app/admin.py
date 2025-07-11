from django.contrib import admin
from .models import Story_v2
from .services import generate_story_continuation




@admin.action(description='تولید داستان با AI برای موارد انتخاب شده')
def generate_story_action(modeladmin, request, queryset):
    updated_count = 0
    for story in queryset:
        try:
            ai_text = generate_story_continuation(story.user_prompt)
            story.ai_generated_story = ai_text
            story.save(update_fields=['ai_generated_story'])
            updated_count += 1
        except Exception as e:
            modeladmin.message_user(request, f"خطا برای داستان با ID {story.pk}: {e}", level='error')
    
    modeladmin.message_user(request, f"{updated_count} داستان با موفقیت به‌روزرسانی شد.")



@admin.register(Story_v2)
class StoryV2Admin(admin.ModelAdmin):
    list_display = ('id', 'user_prompt', 'ai_generated_story')
    list_display_links = ('id', 'user_prompt')
    search_fields = ('user_prompt', 'ai_generated_story')
    
    readonly_fields = ('ai_generated_story',)
    

    
    actions = [generate_story_action]

    
# @admin.register(Story_v2)
# class StoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('title', 'user_prompt')


# Register your models here.
