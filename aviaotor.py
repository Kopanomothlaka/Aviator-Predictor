from flask import Flask, jsonify, render_template, request
import numpy as np

app = Flask(__name__)

# Store user-input crash points
crash_points = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    global crash_points
    data = request.json
    crash_points = [float(x) for x in data['crash_points']]
    
    # Calculate statistics
    avg_multiplier = np.mean(crash_points)
    median_multiplier = np.median(crash_points)
    prob_above_2x = len([x for x in crash_points if x >= 2]) / len(crash_points)
    
    # Suggest cash-out point
    cash_out_point = min(2.0, median_multiplier)  # Conservative suggestion
    
    return jsonify({
        "crash_points": crash_points,
        "avg_multiplier": round(avg_multiplier, 2),
        "median_multiplier": round(median_multiplier, 2),
        "prob_above_2x": round(prob_above_2x, 2),
        "cash_out_point": round(cash_out_point, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)