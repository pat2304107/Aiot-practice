# Generated by Django 4.0.4 on 2022-06-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_badmintoninfo_nums_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badmintoninfo',
            name='occupied',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
