# Generated by Django 2.2 on 2019-10-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereg', '0003_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Mail_ID',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]