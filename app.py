from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def process_scan():
    if 'image' not in request.files:
        return jsonify({'error': 'No image data'}), 400
    return jsonify({'status': 'success', 'message': 'Scan registered successfully'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
