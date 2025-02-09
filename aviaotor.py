from flask import Flask, jsonify, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    crash_points = [float(x) for x in data['crash_points']]
    
    # Calculate basic statistics
    avg = np.mean(crash_points) if crash_points else 0
    median = np.median(crash_points) if crash_points else 0
    prob_2x = len([x for x in crash_points if x >= 2])/len(crash_points) if crash_points else 0
    
    return jsonify({
        "crash_points": crash_points,
        "avg": round(avg, 2),
        "median": round(median, 2),
        "prob_2x": round(prob_2x, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)