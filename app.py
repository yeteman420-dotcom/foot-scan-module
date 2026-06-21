from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-scan', methods=['POST'])
def upload_scan():
    if 'foot_image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image partition found'}), 400
        
    file = request.files['foot_image']
    side = request.form.get('foot_side', 'right')
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Empty filename submission'}), 400

    # Simulate Orthopedic Measurement Analysis (Hallux Valgus Angle calculation)
    # Generates a realistic diagnostic angle between 14.5 and 23.8 degrees
    hva_angle = round(random.uniform(14.5, 23.8), 1)
    
    if hva_angle < 16.0:
        severity = "Mild Alignment Deviation"
        spacer_size = "Standard (Moderate Spread)"
        config_notes = "Ideal for casual footwear alignment preservation."
    elif hva_angle < 21.0:
        severity = "Moderate Bunion Tendency"
        spacer_size = "Medium Progressive"
        config_notes = "Recommended for structural alignment correction during rest periods."
    else:
        severity = "Significant Structural Shift"
        spacer_size = "Large Correction Spacer"
        config_notes = "Maximum spacing configuration optimized for regular therapeutic use."

    return jsonify({
        'status': 'success',
        'side': side.upper(),
        'angle': f"{hva_angle}°",
        'severity': severity,
        'recommendation': spacer_size,
        'notes': config_notes
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
