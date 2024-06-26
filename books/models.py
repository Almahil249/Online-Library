from django.db import models
from profileModel.models import ProfileModel
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.BinaryField(null=True, blank=True)  
    author_name= models.CharField(max_length=50)
    about_author= models.TextField()
    category=models.CharField(max_length=50,null=True,default="no category")
    is_trending=models.BooleanField(default=False)
    user= models.ForeignKey(ProfileModel,models.SET_NULL,blank=True,null=True)
    trending_date= models.DateTimeField(null=True,blank=True)

    def mark_as_trending(self):
        self.is_trending = True
        self.trending_date = timezone.now()
        self.save()

    def __str__(self):
        return f"ID: {self.id}  title: {self.title} author: {self.author_name} category: {self.category} "
    class Meta:
        ordering = ['-created']  