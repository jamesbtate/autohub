# Generated by Django 3.1.4 on 2021-01-08 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20210107_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='amqp_connection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='portal.amqpconnection'),
        ),
    ]
