# Generated by Django 4.2.5 on 2023-09-05 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate', models.FloatField(default=0.0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_donate', to='sponsors.sponsorwallet')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_wallet', to='students.studentwallet')),
            ],
        ),
    ]
