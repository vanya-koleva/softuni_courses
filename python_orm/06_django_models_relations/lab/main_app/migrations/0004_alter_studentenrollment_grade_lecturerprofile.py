# Generated by Django 5.0.4 on 2025-03-01 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_studentenrollment_alter_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrollment',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='LecturerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('office_location', models.CharField(blank=True, max_length=100, null=True)),
                ('lecturer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.lecturer')),
            ],
        ),
    ]
