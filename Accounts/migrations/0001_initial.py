# Generated by Django 4.1.3 on 2022-11-21 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('marital_status', models.CharField(max_length=10)),
                ('anxiety', models.CharField(max_length=10)),
                ('depression', models.CharField(max_length=10)),
                ('panic_attack', models.CharField(max_length=10)),
                ('seeked_specialist', models.CharField(max_length=10)),
                ('smoking', models.CharField(max_length=10)),
                ('drinking', models.CharField(max_length=10)),
                ('drugs', models.CharField(max_length=10)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
