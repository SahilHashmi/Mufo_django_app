# Generated by Django 4.2.2 on 2023-10-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_delete_social_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow1',
            name='date',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
