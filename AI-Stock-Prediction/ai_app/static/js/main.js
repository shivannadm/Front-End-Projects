// main.js

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Stock Prediction Frontend Loaded');

    // Handle File Upload Preview
    const fileInput = document.getElementById('file-input');
    const fileLabel = document.getElementById('file-label');
    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', (event) => {
            const fileName = event.target.files[0]?.name || 'No file selected';
            fileLabel.textContent = `Selected: ${fileName}`;
        });
    }

    // Dataset Selection Dropdown Event
    const datasetSelect = document.getElementById('dataset-select');
    if (datasetSelect) {
        datasetSelect.addEventListener('change', (event) => {
            const selectedDataset = event.target.value;
            if (selectedDataset) {
                console.log(`Dataset Selected: ${selectedDataset}`);
            }
        });
    }

    // Smooth Scroll for Hero Section Buttons
    const heroButtons = document.querySelectorAll('.hero-buttons a');
    heroButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const target = event.target.getAttribute('href');
            if (target) {
                window.location.href = target;
            }
        });
    });

    // Display Confirmation for Dataset Submission
    const uploadForm = document.getElementById('upload-form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const confirmation = confirm('Are you sure you want to upload this dataset?');
            if (confirmation) {
                uploadForm.submit();
            }
        });
    }

    // Show Loader Animation (if present)
    const loader = document.getElementById('loader');
    const predictButton = document.getElementById('predict-button');
    if (predictButton && loader) {
        predictButton.addEventListener('click', () => {
            loader.style.display = 'block';
        });
    }
});
