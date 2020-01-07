from django.db import models
# Create your models here.

class ToDo(models.Model):
    time=models.DateTimeField((u"Conversation Time"),auto_now_add=True,blank=True)
    head=models.CharField(max_length=100,default='headline / time')
    todo=models.TextField(default='brief on what to do')

    def __str__(self):
        return '{}'.format(self.head)

    class Meta:
        verbose_name_plural='ToDo'
