# Generated by Django 3.0.6 on 2020-06-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
