# Generated by Django 3.0.6 on 2020-07-01 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_estoqueitens_produto'),
        ('pedido', '0006_auto_20200630_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitens',
            name='estoque',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='estoque', to='estoque.Estoque'),
            preserve_default=False,
        ),
    ]
