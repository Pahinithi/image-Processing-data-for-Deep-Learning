from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

def process_image(image_path):
    img = cv2.imread(image_path)

    # Save the original image for reference
    cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], 'original.jpg'), img)

    # Convert to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted = cv2.bitwise_not(grayscale)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    # Create pencil sketch
    sketch = cv2.divide(grayscale, 255 - blurred, scale=256)

    # Save processed images
    cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], 'grayscale.jpg'), grayscale)
    cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], 'inverted.jpg'), inverted)
    cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], 'blurred.jpg'), blurred)
    cv2.imwrite(os.path.join(app.config['PROCESSED_FOLDER'], 'pencil_sketch.jpg'), sketch)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = 'uploaded_image.jpg'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            process_image(file_path)
            return redirect(url_for('results'))
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)
    app.run(debug=True)
