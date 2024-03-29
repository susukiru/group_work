# Generated by Django 3.2.7 on 2022-07-12 01:51

import diary.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, validators=[diary.validate.validate_admin], verbose_name='メールアドレス')),
            ],
        ),
    ]
