from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
import uuid

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=63)
    price = models.IntegerField()
    rating = models.IntegerField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    
    @property
    def get_formatted_price(self):
        return f"Rp{self.price:,.0f}".replace(",", ".")