# Generated by Django 4.2 on 2023-05-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='noidung',
            field=models.FileField(null=True, upload_to='pdfs/'),
        ),
    ]