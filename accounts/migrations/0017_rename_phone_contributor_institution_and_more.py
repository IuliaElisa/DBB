# Generated by Django 4.0.8 on 2022-12-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_object_mass_remove_object_perihelion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='phone',
            new_name='institution',
        ),
        migrations.AlterField(
            model_name='article',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_tag',
        ),
        migrations.AddField(
            model_name='article',
            name='title_tag',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
