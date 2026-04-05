from flask import Flask, jsonify, render_template
from monitor import get_metrics, log_metrics, get_logs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    m = get_metrics()
    log_metrics(m)
    return jsonify(m)

@app.route('/logs')
def logs():
    return jsonify(get_logs())

if __name__ == '__main__':
    app.run(debug=True)