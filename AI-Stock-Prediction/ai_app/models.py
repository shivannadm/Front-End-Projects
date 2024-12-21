from django.db import models

class UploadedDataset(models.Model):
    file = models.FileField(upload_to='media\datasets')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PredictionResult(models.Model):
    dataset = models.ForeignKey(UploadedDataset, on_delete=models.CASCADE)
    prediction_date = models.DateTimeField(auto_now_add=True)
    result_image = models.ImageField(upload_to='ai_app\static\images')
    accuracy = models.FloatField()
