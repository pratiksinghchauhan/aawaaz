# Generated by Django 3.0.5 on 2020-04-16 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200416_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listed_projects')),
            ],
        ),
    ]
