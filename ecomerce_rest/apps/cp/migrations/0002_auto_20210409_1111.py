# Generated by Django 3.1.7 on 2021-04-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cp',
            name='c_CP',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='c_cve_ciudad',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='c_estado',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='c_mnpio',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='c_oficina',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='c_tipo_asenta',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='d_CP',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='d_zona',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cp',
            name='id_asenta_cpcons',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
