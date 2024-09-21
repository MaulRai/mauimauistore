from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
import uuid
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=63)
    price = models.IntegerField()
    rating = models.IntegerField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  
    time = models.DateField(auto_now_add=True)
    
    @property
    def get_formatted_price(self):
        return f"Rp{self.price:,.0f}".replace(",", ".")
    
    # For testing purpose
    @property
    def is_good_product(self):
        return self.rating > 4
    
# class Monster(models.Model):
#     name = models.CharField(max_length=199)
#     email = models.EmailField()
#     age = models.IntegerField()
#     is_happy = models.BooleanField()
#     muncul = models.DateField(auto_now_add=True)