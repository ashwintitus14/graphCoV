# Generated by Django 3.0.7 on 2020-06-14 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gen_graph', '0004_auto_20200614_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='tested_positive',
        ),
    ]
