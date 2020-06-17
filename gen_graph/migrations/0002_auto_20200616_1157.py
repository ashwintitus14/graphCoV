# Generated by Django 3.0.7 on 2020-06-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_graph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='cid',
        ),
        migrations.AlterField(
            model_name='link',
            name='person1',
            field=models.CharField(help_text='Patient/Contact ID of person 1', max_length=10),
        ),
        migrations.AlterField(
            model_name='link',
            name='person2',
            field=models.CharField(help_text='Patient/Contact ID of person 2', max_length=10),
        ),
    ]