from django.db import models

class Post(models.Model): # each class defines DATABASE over here 
    title = models.CharField(max_length = 140)   # each variable is table column and then datatypes
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title