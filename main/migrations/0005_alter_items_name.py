# Generated by Django 5.1 on 2024-12-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_items_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(default='Default Name', max_length=20),
        ),
    ]
