# Generated by Django 3.0 on 2020-02-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_remove_event_register_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambassador_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('referal_code', models.CharField(max_length=50)),
            ],
        ),
    ]
