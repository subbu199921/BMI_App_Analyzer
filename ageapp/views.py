from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
import datetime
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
from .forms import ImageUploadForm
from .models import UploadedImage

# 🚀 New User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'ageapp/register.html', {'form': form})

# 🎯 Function to Calculate BMI and Category
def calculate_bmi(weight, height):
    """Calculate BMI and return the category"""
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category

# 🚀 Protected Upload View (Only for Logged-in Users)
@login_required
def upload(request):
    age = None
    bmi = None
    bmi_category = None
    graph_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user  # Associate image with logged-in user
            image_instance.save()

            # 🎂 Calculate Age from Birthdate
            birthdate = form.cleaned_data['birthdate']
            today = now().date()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

            # 📏 Get Height & Weight and Compute BMI
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bmi, bmi_category = calculate_bmi(weight, height)

            # 📊 Generate Dynamic BMI Graph
            fig, ax = plt.subplots(figsize=(6, 4))
            categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
            bmi_values = [18.5, 24.9, 29.9, 35]

            # Color each bar differently based on category
            colors = ['blue', 'green', 'orange', 'red']
            ax.bar(categories, bmi_values, color=colors, alpha=0.7)

            # 📌 Mark the User's BMI on the Graph
            ax.axhline(y=bmi, color='black', linestyle='dashed', linewidth=2, label=f'Your BMI: {bmi}')
            ax.legend()
            ax.set_ylabel("BMI Value")
            ax.set_title("BMI Chart")

            # Convert Graph to Base64 URL
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            graph_url = f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode('utf-8')}"
            buffer.close()

    else:
        form = ImageUploadForm()

    return render(request, 'ageapp/upload.html', {
        'form': form,
        'age': age,
        'bmi': bmi,
        'bmi_category': bmi_category,
        'graph_url': graph_url
    })
