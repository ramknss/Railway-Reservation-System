# Generated by Django 3.0 on 2024-04-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0004_train_trainnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='trainnum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
