# Generated by Django 4.1.3 on 2022-12-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_alter_ad_ad_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]