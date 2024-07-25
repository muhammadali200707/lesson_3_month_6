# Generated by Django 5.0.7 on 2024-07-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=60)),
                ('price', models.FloatField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('published_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
