# Generated by Django 2.0.5 on 2018-06-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20180604_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Phone'),
        ),
    ]
