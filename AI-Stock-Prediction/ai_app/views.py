from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def upload_dataset(request):
    if request.method == 'POST':
        dataset = request.FILES.get('dataset_file')
        # Handle file upload logic here
    return render(request, 'upload.html')

def select_dataset(request):
    if request.method == 'POST':
        selected_dataset = request.POST.get('dataset')
        # Handle dataset selection logic here
    return render(request, 'select.html')
