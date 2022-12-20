from django.db import models
class Category(models.Model):
    title =models.CharField(max_length=50)
class Films(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.TextField()
    Date_is_published = models.DateField(auto_now_add=True)
    date_showed = models.CharField(max_length=50)