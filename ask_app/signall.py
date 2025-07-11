from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Story_v2
import os
from django.utils.text import slugify
from django.conf import settings
from .services import generate_story_continuation


@receiver(post_save, sender=Story_v2)
def save_story_to_file(sender, instance, created, **kwargs):
    if created:
        output_dir = settings.GENERATED_STORIES_DIR
        safe_title = slugify(instance.title, allow_unicode=False)
        file_name = f"story_{instance.pk}_{safe_title}.txt"
        file_path = os.path.join(output_dir, file_name)

        content = f"title: {instance.title}\n"
        content += "text of story:\n\n"
        content += instance.ai_generated_story


        try:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"story with {instance.pk} primery key succesfully storge in {file_path} ")
        except IOError as e:
            print(f"error in {instance.pk}: {e}")


@receiver(post_save, sender=Story_v2)
def generate_story_with_gemini(sender, instance, created, **kwargs):
    if created and not instance.ai_generated_story:
        title = instance.title
        user_prompt = instance.user_prompt

        try:
            ai_generated_story= generate_story_continuation(user_prompt)

            Story_v2.objects.filter(pk=instance.pk).update(ai_generated_story=ai_generated_story)

        except Exception as e:
            # در صورت بروز خطا، آن را در فیلد داستان ذخیره می‌کنیم تا قابل مشاهده باشد
            error_message = f"An error occurred while generating the story: {str(e)}"
            Story_v2.objects.filter(pk=instance.pk).update(ai_generated_story=error_message)
