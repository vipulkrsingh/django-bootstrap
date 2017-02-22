from django.db import models
from django.utils import timezone
import uuid

# TODO add ability to add tags
# TODO support for task types
# TODO support for projects


class Task(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  details = models.TextField()
  owner = models.ForeignKey('auth.User', related_name='owns', null=True)
  assigned = models.ForeignKey('auth.User', related_name='assigned', null=True)
  people = models.ManyToManyField('auth.User', null=True)
  created_datetime = models.DateTimeField(default=timezone.now)
  closed_datetime = models.DateTimeField(null=True)

  def __str__(self):
    return self.title


class TaskActivity(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  task = models.ForeignKey('Task')
  start_datetime = models.DateTimeField(default=timezone.now)
  end_datetime = models.DateTimeField(null=True)
