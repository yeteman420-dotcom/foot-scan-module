from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-scan', methods=['POST'])
def upload_scan():
    # Verify file existence in request payload
    if 'foot_image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image partition found'}), 400
        
    file = request.files['foot_image']
    side = request.form.get('foot_side', 'right')
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Empty filename submission'}), 400

    # Log operational metadata directly to Render console logs
    print(f"[SCANNER LOG] Received operational upload target for {side.upper()} foot alignment processing.")
    print(f"[SCANNER LOG] Filename: {file.filename} | Content-Type: {file.content_type}")

    # Return acknowledgement response payload to browser frontend interface
    return jsonify({
        'status': 'success',
        'message': 'Image successfully transferred to Python server environment.',
        'side': side,
        'filename': file.filename
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
