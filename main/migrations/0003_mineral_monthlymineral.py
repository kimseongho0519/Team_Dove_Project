# Generated by Django 4.0.3 on 2022-04-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_monthlyal_monthlydomesticoil_monthlygrain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('날짜', models.DateField(blank=True, null=True)),
                ('알루미늄', models.FloatField(blank=True, null=True)),
                ('니켈', models.FloatField(blank=True, null=True)),
                ('동', models.FloatField(blank=True, null=True)),
                ('아연', models.FloatField(blank=True, null=True)),
                ('주석', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mineral',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MonthlyMineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('날짜', models.TextField(blank=True, null=True)),
                ('알루미늄', models.FloatField(blank=True, null=True)),
                ('니켈', models.FloatField(blank=True, null=True)),
                ('동', models.FloatField(blank=True, null=True)),
                ('아연', models.FloatField(blank=True, null=True)),
                ('주석', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'monthly_mineral',
                'managed': False,
            },
        ),
    ]
