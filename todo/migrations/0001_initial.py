# Generated by Django 4.2.1 on 2023-05-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2)),
                ('is_done', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
