# Generated by Django 4.2.7 on 2024-01-04 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateField(auto_now_add=True)),
                ('owned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
    ]
