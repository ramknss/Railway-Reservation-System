# Generated by Django 3.2.5 on 2024-04-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0020_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writername', models.CharField(max_length=100)),
                ('story', models.TextField()),
            ],
        ),
    ]
