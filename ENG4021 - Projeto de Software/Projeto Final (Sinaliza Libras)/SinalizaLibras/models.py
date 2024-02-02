from django.db import models

class Videos(models.Model):
  titulo = models.CharField(max_length=50)
  url = models.CharField(max_length=200)
  
    
