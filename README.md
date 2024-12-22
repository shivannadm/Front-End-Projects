# Folder: AI-Stock-Prediction 

# 📊 AI-Powered Stock Price Prediction with Django & CNN-LSTM

This project integrates a **CNN-LSTM** deep learning model with a **Django web application** to predict stock prices based on historical data. Users can upload their own datasets or select from preloaded datasets to visualize stock price trends and future predictions.

---

## 🚀 **Project Overview**
- **Frontend:** User-friendly interface for dataset upload and selection.
- **Backend:** Django-powered backend with dataset handling, model integration, and visualization.
- **AI Model:** CNN-LSTM model for accurate stock price predictions.
- **Visualization:** Interactive graphs displaying predictions.

---

## 🛠️ **Technologies Used**
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django Framework
- **Machine Learning:** Python, TensorFlow, Keras
- **Data Visualization:** Matplotlib
- **Database:** SQLite (default Django DB)

---

## 📁 **Project Structure**
```
├── ai_app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── upload.html
│   │   ├── select.html
│   │   ├── predict.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   ├── models/
│   │   ├── cnn_lstm_model.h5
├── media/
│   ├── datasets/
│   ├── plots/
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── train_model.py
├── manage.py
└── README.md
```

---

## ⚙️ **Setup Instructions**

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/stock-prediction.git
cd stock-prediction
```

2. **Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Apply Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run Training Script (if needed):**
```bash
python train_model.py
```

6. **Start Django Server:**
```bash
python manage.py runserver
```

7. **Access the Application:**
- Open: `http://127.0.0.1:8000/`

---

## 📂 **Datasets**
- Place datasets in the `media/datasets/` folder.
- Upload custom datasets through the upload section on the frontend.

---

## 📊 **How It Works**
1. **Upload Dataset:** Upload a CSV file with stock price data.
2. **Select Dataset:** Choose a dataset from the preloaded list.
3. **Predict Prices:** AI model predicts stock prices.
4. **Visualize Results:** Graphs display historical and predicted trends.

---

## 🐞 **Troubleshooting**
- Ensure the `cnn_lstm_model.h5` exists in `ai_app/models/`.
- Verify dataset structure (`Date`, `Close` columns required).
- Check Django logs for errors.

---

## 🤝 **Contributing**
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---


## 🌟 **Acknowledgments**
- TensorFlow & Keras for ML model.
- Django for backend framework.
- Matplotlib for data visualization.

**Happy Coding! 💻✨**
