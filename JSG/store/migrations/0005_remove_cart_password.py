# Generated by Django 5.0.3 on 2024-04-11 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='password',
        ),
    ]