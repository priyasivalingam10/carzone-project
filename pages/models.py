from django.db import models

# Create your models here.

class Team(models.Model):
    first_name=models.CharField( max_length=255,blank='False')
    last_name=models.CharField( max_length=255,blank='False')
    designation=models.CharField( max_length=255,blank='False')
    photo=models.ImageField( upload_to='photo/%Y/%m/%d/')
    facebook_link=models.CharField( max_length=255,blank='False')
    twitter_link=models.CharField( max_length=255,blank='False')
    google_plus_link=models.CharField( max_length=255,blank='False')
    created_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name