# Generated by Django 2.0.5 on 2018-06-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'MySubscriber',
                'verbose_name_plural': 'A lot of Subscribers',
            },
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]
