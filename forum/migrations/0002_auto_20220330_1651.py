# Generated by Django 3.2.7 on 2022-03-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['updated', 'created']},
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
