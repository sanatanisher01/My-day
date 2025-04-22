from django.db import migrations


class Migration(migrations.Migration):
    """
    This migration merges the conflicting migrations in the chat app.
    """

    dependencies = [
        ('chat', '0001_initial'),
        ('chat', '0002_remove_chatmessage_image_remove_chatmessage_room_and_more'),
    ]

    operations = [
        # No operations needed, this just merges the migrations
    ]
