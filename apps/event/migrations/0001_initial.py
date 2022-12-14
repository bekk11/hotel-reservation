# Generated by Django 4.1.2 on 2022-11-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('where', models.CharField(max_length=50)),
                ('when', models.DateTimeField()),
                ('image', models.ImageField(upload_to='events/')),
            ],
            options={
                'db_table': 'event',
                'ordering': ['-when'],
            },
        ),
    ]
