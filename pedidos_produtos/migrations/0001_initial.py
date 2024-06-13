# Generated by Django 5.0.6 on 2024-06-13 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedidos', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos_produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField()),
                ('quantidade', models.FloatField()),
                ('pedido_int', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_id', to='pedidos.pedido')),
                ('produto_int', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_id', to='produtos.produtos')),
            ],
        ),
    ]
