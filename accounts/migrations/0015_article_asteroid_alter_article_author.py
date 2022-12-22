# Generated by Django 4.0.8 on 2022-12-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_article_author_article_post_date_article_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='asteroid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.object'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.contributor'),
            preserve_default=False,
        ),
    ]
