# Generated by Django 3.0.5 on 2020-04-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_listedtransfers_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='listed_projects',
            fields=[
                ('transaction_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('payee', models.CharField(max_length=200)),
                ('payer', models.CharField(max_length=200)),
                ('payeeva', models.CharField(max_length=200)),
                ('payerva', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('recurrance', models.CharField(max_length=200)),
                ('project_name', models.CharField(max_length=200)),
                ('cutoff_votes', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('ts', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='listedTransfers',
        ),
    ]
