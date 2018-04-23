# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-18 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(default='', max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Contact', models.IntegerField(default=0)),
                ('Residence', models.CharField(default='', max_length=200)),
                ('Work_history', models.CharField(default='', max_length=200)),
                ('Identification_information', models.IntegerField(default=0)),
                ('Next_of_kin', models.CharField(default='', max_length=200)),
                ('Image', models.ImageField(blank=True, upload_to='profile_image')),
                ('Account_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registercustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(default='', max_length=200)),
                ('Last_name', models.CharField(default='', max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Contact', models.IntegerField(default=0)),
                ('Residence', models.CharField(default='', max_length=200)),
                ('Next_of_kin', models.CharField(default='', max_length=200)),
                ('Occupation', models.CharField(default='', max_length=200)),
                ('Image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Registercustomertranscations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(default='', max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Contact', models.IntegerField(default=0)),
                ('Account_number', models.IntegerField(default=0)),
                ('Transcation_type', models.CharField(default='', max_length=200)),
                ('Transcation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]