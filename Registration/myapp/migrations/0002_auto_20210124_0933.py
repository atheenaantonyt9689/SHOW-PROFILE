# Generated by Django 2.1.7 on 2021-01-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('userid', models.EmailField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Register',
            new_name='Registration',
        ),
    ]
