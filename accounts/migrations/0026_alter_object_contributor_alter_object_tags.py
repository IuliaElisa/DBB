# Generated by Django 4.0.8 on 2022-12-21 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_warning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objects', to='accounts.contributor'),
        ),
        migrations.AlterField(
            model_name='object',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='accounts.tag'),
        ),
    ]
