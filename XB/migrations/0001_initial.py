# Generated by Django 2.1.5 on 2019-03-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('videourl', models.CharField(max_length=500)),
                ('photourl', models.CharField(max_length=500)),
            ],
        ),
    ]
