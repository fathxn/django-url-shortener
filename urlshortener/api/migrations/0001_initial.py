# Generated by Django 4.0.3 on 2022-03-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField()),
                ('shorturl', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
