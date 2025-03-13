#  Age & BMI Calculator - Django Web App

Website Link :  http://bmiapp.pythonanywhere.com/

##  Overview

This Django web application allows users to **upload an image, enter personal details** Like (birthdate, height, weight), and calculates:

-  **Age** (based on birthdate)
-  **BMI (Body Mass Index)**
-  **BMI Category** (Underweight, Normal, Overweight, Obese)
-  **Graph Representation** of BMI category

The project features **user authentication** (registration & login) and ensures only logged-in users can upload images and check their BMI.

---

##  Features

**User Registration & Login**\
**Upload Image & Enter Details**\
**Automatic Age Calculation**\
**BMI Calculation & Category**\
**BMI Graph Visualization** (Plotted using Matplotlib)\
**Secure Logout System**\
**Glassmorphic UI Design with Transparent Background**

---

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default, can be changed)
- **Visualization**: Matplotlib
- **Icons**: FontAwesome

---

## Setup Instructions

 **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

 **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```
 **3. Install Dependencies**

```bash
p
```

### pip install -r requirements.txt🔹 **4. Apply Migrations**

```bash
python manage.py migrate
```

**5. Run the Server**

```bash
python manage.py runserver
```

Now, open **`http://127.0.0.1:8000/`** in your browser.

---

 Project Structure

```
age_bmi_app/
│── ageapp/                    # Django App
│   ├── migrations/            # Database Migrations
│   ├── templates/             # HTML Templates
│   │   ├── ageapp/
│   │   │   ├── upload.html    # Main Upload Page
│   ├── views.py               # Application Logic
│   ├── models.py              # Database Models
│   ├── forms.py               # Django Forms
│── manage.py                   # Django Entry Point
│── db.sqlite3                   # Default SQLite Database
│── requirements.txt             # Dependencies
│── README.md                    # Project Documentation
```

---

##  User Authentication

- **Register** a new account: `/register/`
- **Login**: `/login/`
- **Logout**: `/logout/`
- **Upload Page (Protected)**: `/upload/`

---

##  How It Works?

1 **User logs in**\
2 **Uploads an image** and enters details (birthdate, height, weight)\
3 **App calculates** age and BMI automatically\
4 **BMI Category is displayed**\
5 **A graphical BMI representation** is generated using **Matplotlib**

---

##  BMI Categories

| BMI Value       | Category      |
| --------------- | ------------- |
| **< 18.5**      | Underweight   |
| **18.5 - 24.9** | Normal Weight |
| **25 - 29.9**   | Overweight    |
| **30+**         | Obese         |


##  License

This project is **open-source** and free to use.

---

##  Author

 **Subhash Chandra**\
 Email: [subhashofficial411@gmail.com](mailto\:subhashofficial411@gmail.com)

---

## Future Enhancements

-  **Database for Storing User Data & History**
-  **Admin Dashboard for Managing Users**
-  **Add More Health Metrics (Heart Rate, Calories, etc.)**
-  **Deploy on PythonAnywhere/Aiven Console**
 

