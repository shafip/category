# Generated by Django 4.1.7 on 2023-03-20 04:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_subject_category_remove_subject_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Name must contain only letters and spaces.', regex='^[a-zA-Z ]+$')]),
        ),
    ]
