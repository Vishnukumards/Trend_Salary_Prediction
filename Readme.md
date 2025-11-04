# 🧠 Salary Trend Prediction

Predict and analyze salary trends from **2005 onwards** using advanced **time series forecasting models** like **ARIMA**, **SARIMA**, and **Prophet**.  
This project predicts average salary for a selected **month** and **year**, and provides a simple **web interface** built with Django.

---

## 🚀 Features
- Predicts salary for a given **month** and **year**
- Uses multiple ML models (ARIMA, SARIMA, Prophet)
- Automatically selects the **best-performing model** (based on accuracy)
- Clean and responsive **Django web interface**
- Built entirely in **Python**

---

## 🛠️ Tech Stack

| Layer | Technology |
|:------|:------------|
| **Backend** | Python 3, Django |
| **ML Models** | ARIMA, SARIMA, Prophet |
| **Frontend** | HTML5, CSS3, Django Templates |
| **Libraries** | pandas, numpy, scikit-learn, statsmodels, fbprophet |
| **Version Control** | Git & GitHub |

---

## Project Demo 🎥

Watch the demo video here:  
[▶️ Click to view the project video]()


## 📸 Interface Preview

| Screenshot |
|:-----------:|
| ![App Screenshot](docs/screenshot.png) |

*(Optional: place your screenshot image at `docs/screenshot.png` in your repo)*

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vishnukumards/salary-trend-prediction.git
   cd salary-trend-prediction
2. **Create and activate virtual environment**
    ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)


3. **Install dependencies**

   ```bash
   pip install -r requirements.txt


4. **Run migrations**
   ```bash
   python manage.py migrate


5. **Start the development server**
   ```bash
   python manage.py runserver
   

6. **Open in browser**
 ```bash
   http://127.0.0.1:8000/
