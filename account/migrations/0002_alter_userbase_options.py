# Generated by Django 3.2.4 on 2021-07-05 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbase',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
    ]
