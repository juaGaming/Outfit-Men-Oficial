# Generated by Django 4.2.7 on 2024-01-13 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('prod_Id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del producto')),
                ('prod_Nombre', models.TextField(max_length=40)),
                ('prod_Descripcion', models.TextField(max_length=250)),
                ('prod_Precio', models.CharField(max_length=100)),
                ('prod_Talla', models.TextField(max_length=30)),
                ('prod_Color', models.TextField(max_length=30)),
                ('prod_Imagen', models.ImageField(upload_to='Productos')),
            ],
        ),
    ]
