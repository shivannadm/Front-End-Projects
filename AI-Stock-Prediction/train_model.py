import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, LSTM, Conv1D, MaxPooling1D, Dropout
import math
from sklearn.metrics import mean_squared_error
import os

# 1. Load Dataset
dataset_path = os.path.join('ai_app', 'datasets', 'TATA.csv')  # Adjust path if needed
df = pd.read_csv(dataset_path)

# 2. Extract necessary columns
dates = df['Date']
df1 = df['Close']

# 3. Plot original data (Optional)
plt.figure(figsize=(12, 6))
plt.plot(dates, df1, label="Actual Prices")
plt.title("Stock Price Data")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.legend()
plt.show()
# 4. Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
df1 = scaler.fit_transform(np.array(df1).reshape(-1, 1))

# 5. Prepare training and testing datasets
def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - time_step - 1):
        dataX.append(dataset[i:(i + time_step), 0])
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)

training_size = int(len(df1) * 0.65)
test_size = len(df1) - training_size
train_data, test_data = df1[0:training_size, :], df1[training_size:len(df1), :]

time_step = 100
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Reshape input data into [samples, time steps, features]
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# 6. Build CNN-LSTM Model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(100, 1)))
model.add(MaxPooling1D(pool_size=2))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# 7. Train the Model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=64, verbose=1)

# 8. Save the Trained Model
model_save_path = os.path.join('ai_app', 'models', 'cnn_lstm_model.h5')
model.save(model_save_path)
print(f"Model saved at {model_save_path}")

# 9. Make Predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Reverse Scaling
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# 10. Calculate RMSE
train_rmse = math.sqrt(mean_squared_error(y_train, scaler.inverse_transform(y_train.reshape(-1, 1))))
test_rmse = math.sqrt(mean_squared_error(y_test, scaler.inverse_transform(y_test.reshape(-1, 1))))

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")

# 11. Plot Predictions
# Plot Predictions with Correct Alignment
plt.figure(figsize=(12, 6))

# Plot Actual Stock Prices
plt.plot(dates, scaler.inverse_transform(df1), label="Actual Prices", color='blue')

# Plot Training Predictions
train_dates = dates[time_step:time_step + len(train_predict)]  # Align train predictions with dates
plt.plot(train_dates, train_predict, label="Train Prediction", color='green')

# Plot Testing Predictions
test_dates = dates[training_size + time_step:training_size + time_step + len(test_predict)]  # Align test predictions with dates
plt.plot(test_dates, test_predict, label="Test Prediction", color='orange')

# Plot Formatting
plt.title("Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.legend()
plt.show()

