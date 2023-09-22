# Generated by Django 4.1.5 on 2023-09-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_produto_venda', models.IntegerField(verbose_name='Quantidade Produto')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_produto_venda', to='produto.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venda_produto_venda', to='venda.venda')),
            ],
            options={
                'db_table': 'produto_venda',
            },
        ),
    ]