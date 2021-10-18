# Generated by Django 3.2.8 on 2021-10-18 11:30

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
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('register_date', models.DateTimeField(verbose_name='date registered')),
                ('energy', models.PositiveIntegerField()),
                ('fat', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('sugars', models.FloatField()),
                ('fibers', models.FloatField()),
                ('proteins', models.FloatField()),
                ('salt', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
