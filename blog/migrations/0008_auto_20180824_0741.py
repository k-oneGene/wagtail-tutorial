# Generated by Django 2.0.8 on 2018-08-24 07:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0040_page_draft_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('blog', '0007_blogpage_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfilePage',
            new_name='BlogProfilePage',
        ),
    ]
