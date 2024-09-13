# Generated by Django 5.1 on 2024-09-12 04:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
    ]
