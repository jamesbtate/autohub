# Generated by Django 3.1.4 on 2020-12-17 03:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AMQPConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('server', models.CharField(max_length=128)),
                ('port', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
            ],
        ),
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('enabled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField()),
                ('task_type', models.CharField(choices=[('executable', 'Execute a program'), ('amqp_publish', 'Publish a message to a queue')], max_length=16)),
                ('command_line', models.CharField(max_length=1024)),
                ('queue_name', models.CharField(max_length=128)),
                ('amqp_connection', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='portal.amqpconnection')),
                ('automation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.automation')),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
                ('successful', models.BooleanField()),
                ('error', models.TextField()),
                ('stdout', models.TextField()),
                ('stderr', models.TextField()),
                ('return_code', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='portal.task')),
            ],
        ),
        migrations.CreateModel(
            name='QueueTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField()),
                ('queue_name', models.CharField(max_length=128)),
                ('amqp_connection', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='portal.amqpconnection')),
                ('automation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.automation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('automation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.automation')),
            ],
        ),
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1024)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='portal.parameter')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.run')),
            ],
        ),
    ]
