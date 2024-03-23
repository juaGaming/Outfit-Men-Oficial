# Generated by Django 4.2.7 on 2024-02-21 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppOufitMen', '0006_remove_carritocompra_car_id_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Usu_Documento', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='N° Documento')),
                ('Usu_Nombre', models.TextField(max_length=40)),
                ('Usu_Apellido', models.TextField(max_length=40)),
                ('Password', models.TextField(max_length=30)),
                ('Usu_Correo', models.EmailField(max_length=50, verbose_name='Correo Electronico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='carritocompra',
            name='Car_Id_Usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AppOufitMen.usuario', verbose_name='ID Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentarios',
            name='Ct_Id_Usu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AppOufitMen.usuario', verbose_name='ID Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='Detap_Id_Usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AppOufitMen.usuario', verbose_name='ID Usuario'),
            preserve_default=False,
        ),
    ]