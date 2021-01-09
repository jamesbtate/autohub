from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class AMQPConnection(models.Model):
    name = models.CharField(max_length=128)
    server = models.CharField(max_length=128)
    port = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(65535)])


class Automation(models.Model):
    """ The central/main entity"""
    name = models.CharField(max_length=128)
    enabled = models.BooleanField()


class Parameter(models.Model):
    """ Input parameters of an Automation """
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class BaseTrigger(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    enabled = models.BooleanField()

    class Meta:
        abstract = True


class QueueTrigger(BaseTrigger):
    amqp_connection = models.ForeignKey(AMQPConnection, on_delete=models.RESTRICT)
    queue_name = models.CharField(max_length=128)


class Task(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    enabled = models.BooleanField()
    EXECUTABLE = 'executable'
    AMQP_PUBLISH = 'amqp_publish'
    TASK_TYPE_CHOICES = [
        (EXECUTABLE, 'Execute a program'),
        (AMQP_PUBLISH, 'Publish a message to a queue'),
    ]
    task_type = models.CharField(choices=TASK_TYPE_CHOICES, max_length=16)

    # Executable stuff
    command_line = models.CharField(max_length=1024, blank=True)

    # AMQP stuff
    amqp_connection = models.ForeignKey(AMQPConnection, models.RESTRICT, blank=True, null=True)
    queue_name = models.CharField(max_length=128, blank=True)


class Run(models.Model):
    task = models.ForeignKey(Task, on_delete=models.RESTRICT)
    start = models.DateTimeField()
    stop = models.DateTimeField(blank=True, null=True)
    successful = models.BooleanField()
    error = models.TextField(blank=True)

    # Executable stuff
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)
    return_code = models.IntegerField(blank=True, null=True)

    # AMQP stuff


class Argument(models.Model):
    """ the actual value for a given parameter and a given run """
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.RESTRICT)
    value = models.CharField(max_length=1024, blank=True)


class DaemonLog(models.Model):
    """ A log line from the backend daemon """
    datetime = models.DateTimeField()
    message = models.CharField(max_length=256)
    level_name = models.CharField(max_length=16)
