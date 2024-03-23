# Generated by Django 5.0.3 on 2024-03-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_school_name', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=20)),
                ('school_location', models.CharField(max_length=20)),
                ('teaching_experience', models.IntegerField()),
                ('teacher_age', models.IntegerField()),
                ('teacher_address', models.CharField(max_length=30)),
            ],
        ),
    ]
