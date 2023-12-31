# Generated by Django 5.0.1 on 2024-01-05 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.DecimalField(decimal_places=0, max_digits=6)),
                ('bookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
        ),
    ]
