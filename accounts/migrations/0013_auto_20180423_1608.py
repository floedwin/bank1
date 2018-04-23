# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-23 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180423_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='account_number',
            new_name='Account_number',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='amount',
            new_name='Amount',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='full_name',
            new_name='Full_name',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='transaction_date',
            new_name='transcation_date',
        ),
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='transaction_type',
            new_name='transcation_type',
        ),
    ]
