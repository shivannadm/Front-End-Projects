from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import DatasetUploadForm
from .models import UploadedDataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import os

# Upload Dataset
def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('select_dataset')
    else:
        form = DatasetUploadForm()
    return render(request, 'upload.html', {'form': form})

# Select Dataset
def select_dataset(request):
    datasets = UploadedDataset.objects.all()
    return render(request, 'select.html', {'datasets': datasets})

# Predict Stock Prices
def predict_stock(request, dataset_id):
    dataset = UploadedDataset.objects.get(id=dataset_id)
    dataset_path = dataset.file.path
    
    # Load Dataset
    df = pd.read_csv(dataset_path)
    scaler = MinMaxScaler(feature_range=(0, 1))
    df1 = scaler.fit_transform(np.array(df['Close']).reshape(-1, 1))
    
    # Load Model
    model = load_model(os.path.join('ai_app', 'models', 'cnn_lstm_model.h5'))
    
    # Make Predictions
    time_step = 100
    x_input = df1[-time_step:].reshape(1, -1)
    x_input = x_input.reshape((1, time_step, 1))
    yhat = model.predict(x_input)
    future_predictions = scaler.inverse_transform(yhat)
    
    # Plot Results
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label='Actual Prices')
    plt.plot(df['Date'][-1:], future_predictions[0], label='Predicted Prices', marker='o')
    plt.legend()
    plt.savefig('ai_app/static/images/prediction.png')
    plt.close()
    
    return render(request, 'index.html', {'image_path': 'images/prediction.png'})
