# Generated by Django 4.2 on 2023-04-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]