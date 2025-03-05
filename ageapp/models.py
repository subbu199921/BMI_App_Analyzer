from django.db import models
from datetime import date
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    birthdate = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Image"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    height = models.FloatField(help_text="Height in meters")  # Height input
    weight = models.FloatField(help_text="Weight in kg")  # Weight input
    image = models.ImageField(upload_to='uploads/')  # Image upload

    def calculate_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def calculate_bmi(self):
        if self.height > 0:
            bmi = self.weight / (self.height ** 2)
            return round(bmi, 2)
        return None

    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi is None:
            return "Invalid BMI"
        elif bmi < 2.5:
            return "Underweight"
        elif 2.5 <= bmi < 15.9:
            return "Normal weight"
        elif 17 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
        return self.name
