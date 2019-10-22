from django.db import models

# Create your models here.
#class Topic(models.Model):

class Entry(models.Model):
    '''A topic the user is learning about'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return string representation of the model'''
        return self.text