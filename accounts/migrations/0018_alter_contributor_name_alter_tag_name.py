# Generated by Django 4.0.8 on 2022-12-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_rename_phone_contributor_institution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]