# Generated by Django 4.1 on 2022-08-11 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('attendance', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.team')),
            ],
        ),
    ]
