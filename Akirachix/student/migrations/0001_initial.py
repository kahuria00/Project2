# Generated by Django 2.2.1 on 2019-05-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('registration_number', models.CharField(max_length=50)),
                ('place_of_residence', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('guardian_name', models.CharField(max_length=50)),
                ('ID_Number', models.IntegerField(max_length=50)),
                ('DateJoined', models.DateField()),
                ('courses', models.ManyToManyField(to='course.Course')),
            ],
        ),
    ]
