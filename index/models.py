from django.db import models

# Create your models here.

class ProjectCategory(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200, null=True, blank=True)

class Project(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)
    github = models.URLField(max_length=300, null=True, blank=True)
    image = models.URLField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)