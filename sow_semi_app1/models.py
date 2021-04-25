from django.db import models

# Create your models here.


class ShowVal(models.Manager):
    def basic_validator(self,post_data):
        
        errors={}
        
        if len(post_data["title_form"])<2:
            errors["title_form"]="Error in title form, less than 2 charact."
        if len(post_data["network_form"])<3:
            errors["network_form"]="Error in network form, less than 3 charact."
        if len(post_data["desc_form"])<10:
            errors["desc_form"]="Error in description form, less than 10 charact."
    
        
        return errors
        
    def basic_validator1(self,post_data):
        
        errors={}
        
        if len(post_data["title_form_new"])<2:
            errors["title_form_new"]="Error in title form, less than 2 charact."
        if len(post_data["network_form_new"])<3:
            errors["network_form_new"]="Error in network form, less than 3 charact."
        if len(post_data["desc_form_new"])<10:
            errors["desc_form_new"]="Error in description form, less than 10 charact."

        return errors


class Show(models.Model):    
    title = models.CharField(max_length=80)    
    network = models.CharField(max_length=80)  
    release_date=models.DateTimeField()
    desc = models.CharField(max_length=200)  
    
    objects=ShowVal()
