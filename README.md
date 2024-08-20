# Image Processing Web Application

This project is a web-based image processing application built using Flask, OpenCV, and Bootstrap. The application allows users to upload an image, which is then processed to generate grayscale, inverted, blurred, and pencil sketch versions of the image. The processed images are displayed on a results page.

## Features

- **Image Upload:** Users can upload an image in various formats (e.g., JPEG, PNG).
- **Grayscale Conversion:** Converts the uploaded image to grayscale.
- **Inverted Grayscale:** Inverts the grayscale image.
- **Gaussian Blur:** Applies a Gaussian blur to the inverted grayscale image.
- **Pencil Sketch:** Generates a pencil sketch effect from the grayscale image.
- **Display Results:** Displays the original and processed images on a results page.

## Demo

[Watch the Demo Video](https://drive.google.com/file/d/1sJuLooFsAdI_eLSEJyceBINsoY8Y2nEq/view?usp=share_link)  


## File Structure

```plaintext
project/
├── app.py               # Main Flask application
├── uploads/             # Directory for temporarily storing uploaded images
├── static/
│   ├── processed/       # Directory for storing processed images
│   └── css/
│       └── styles.css   # Custom CSS for styling the web pages
├── templates/
│   ├── index.html       # Homepage template for image upload
│   └── results.html     # Results page template for displaying processed images
```

## Technologies Used

- **Flask:** A lightweight WSGI web application framework in Python.
- **OpenCV:** A powerful library for image processing.
- **Bootstrap:** A popular CSS framework for creating responsive web designs.
- **HTML/CSS:** For structuring and styling the web pages.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/image-processing-app.git
   cd image-processing-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

6. **Open your browser and visit:**

   ```
   http://127.0.0.1:5000/
   ```

## How It Works

1. **Upload Image:** The user uploads an image using the form on the homepage.
2. **Process Image:** The uploaded image is processed by the Flask application using OpenCV.
   - Grayscale conversion, inversion, Gaussian blur, and pencil sketch effects are applied.
3. **Display Results:** The processed images are displayed on the results page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

<img width="1728" alt="Screenshot 2024-08-20 at 09 08 47" src="https://github.com/user-attachments/assets/b3a16f75-26cd-4e59-a460-3ae0c991d530">


<img width="1728" alt="Screenshot 2024-08-20 at 09 09 18" src="https://github.com/user-attachments/assets/dd43b04f-fa58-4feb-8a75-cf3c86085c91">

