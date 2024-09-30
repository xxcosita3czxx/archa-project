from flask import Flask, request, jsonify, send_from_directory, redirect
import os

app = Flask(__name__)

# Default route to serve the HTML page
@app.route('/')
def index():
    return send_from_directory('', 'drawing.html')  # Serve index.html from the current directory

# Create an endpoint for handling uploads
@app.route('/upload', methods=['POST'])
def upload():
    if 'canvas_image' in request.files:
        canvas_image = request.files['canvas_image']
        # Save the canvas image
        canvas_image_path = os.path.join('uploads', canvas_image.filename)
        canvas_image.save(canvas_image_path)
        print(f"Canvas image saved as: {canvas_image_path}")

    if 'original_image' in request.form:
        original_image_url = request.form['original_image']
        print(f"Original image URL: {original_image_url}")

    return jsonify({
        'message': 'Images uploaded successfully!', 
        'canvas_image_path': canvas_image_path,
        'original_image_url': original_image_url
    })

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)  # Create uploads directory if it doesn't exist
    app.run(debug=True)
