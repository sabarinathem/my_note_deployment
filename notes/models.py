from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Note(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    description = models.TextField()
    syntax = models.TextField(null=True,blank=True)
    example = models.TextField(null=True,blank=True)
    important_note = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="img",null=True,blank=True)

    def __str__(self):
        return self.heading

