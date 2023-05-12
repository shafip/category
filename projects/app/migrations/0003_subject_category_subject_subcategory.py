# Generated by Django 4.1.7 on 2023-03-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.subcategory'),
            preserve_default=False,
        ),
    ]
