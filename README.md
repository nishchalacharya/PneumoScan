# 🩺 PneumoScan - Pneumonia Detection System
PneumoScan is an intelligent healthcare web application that uses deep learning models to detect **pneumonia** and **tuberculosis** from chest X-ray images. 
The system is integrated with a Django backend and features a responsive frontend for patient interaction, doctor appointments, blog posts, and medical awareness.

---

## 🔍 Features

- 🧠 Deep learning models (DenseNet121, VGG16) for pneumonia detection
- 🖼 Upload chest X-ray and get instant prediction
- 🌐 Web interface built with Django
- 📊 Grad-CAM heatmap visualization for model interpretability
- 🔒 Secure login/signup for doctors and patients
- 📅 **Doctor Appointment UI** (frontend system)
- 📝 **Blog System** — post & read health-related article
  


---

## 🚀 Technologies Used

- Python
- Django
- TensorFlow / Keras
- HTML, CSS, JavaScript
- Bootstrap (optional)
- SQLite 
- Git & GitHub

---

## 🧠 Model Information

- Pre-trained models: DenseNet121 and VGG16
- Fine-tuned on pneumonia dataset (Chest X-ray Images)
- Input size: 224x224
- Output: Pneumonia or Normal

> > Models are stored **locally** in `ai_models/` folder .

---
## 📦 Project Structure

```

PneumoScan/                            # 🔹 Main project folder
│
├── loginSignUp/                       # 🔹 Django project directory (contains settings.py)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── login/                             # 🔐 Handles user registration, login, about us, profile
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
│
├── blogapp/                           # 📝 Blog system (create/view blog posts)
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
├── gradcam/                           # 🔍 Pneumonia & TB prediction via Grad-CAM
│   ├── views.py
│   ├── ai_models/                     # 🔬 Pretrained .h5 model files (excluded from GitHub)
│   └── utils/                         # Grad-CAM utilities
│
├── media/                             # 🖼 Stores uploaded images (X-rays, profile photos, etc.)
│
├── static/                            # 🎨 Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── assets/
│
├── templates/                         # 🌐 HTML templates
│   ├── base.html
│   ├── login.html
│   ├── blogapp/                       # Blog-related HTMLs
│   ├── gradcam/                       # Model interface pages
│   └── ...                            # Other HTML files (about, contact, etc.)
│
├── screenshots/                       # 📸 Project UI screenshots
│
├── manage.py
└── requirements.txt

```
## 📱 Screenshots
---
![Regsiter](Screenshots/1.png)
  **Signup Screen:** New users can register to access the app features.

![Login](Screenshots/2.png)
 **Login Screen:** Users can securely log into the PneumoScan .

![Dashboard](Screenshots/dashboard.png)
**Dashboard:** Overview of user activities and quick access to main features.

![Upload](Screenshots/upload.png)
**Upload** upload to check.

![Detectedfile](Screenshots/penumoniadetected.png)
**Result Displaying** user can click on check gradcam result to see their infected parts

![GradcamResult](Screenshots/gradcam.png)
**Displaying Effected parts** users can see their probable infected parts .

![Services](Screenshots/services.png)
**Available Services** users can see their services .

![Graph](Screenshots/3.png)
**Graph** to see performance of model

![Blogs](Screenshots/4.png)
**Blogs** to see create,see,like and comment blogs related to health sectors
---

---

***For more detailed views and additional screenshots, please refer to the `screenshots` folder in the repository.***

---


```

## ⚙️ Getting Started
## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/nishchalacharya/Pneumo-Scan-major_Project-.git
cd Pneumo-Scan-major_Project-

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


# Run migrations
python manage.py makemigrations
python manage.py migrate


# Start development server
python manage.py runserver
