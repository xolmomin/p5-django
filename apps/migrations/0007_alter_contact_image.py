# Generated by Django 4.1.2 on 2022-10-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(upload_to='contacts/%Y/%m/%d'),
        ),
    ]