# Generated by Django 4.2.7 on 2024-02-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOufitMen', '0004_categoria_producto_pedido_usuario_metodo_pago_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]