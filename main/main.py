import requests
from flask import Flask, render_template

app = Flask(__name__)

TASKS_SERVICE_URL = 'http://localhost:5001/tasks'

@app.route('/')
def index():
    tasks_response = requests.get("http://localhost:5001/tasks")
    tasks = tasks_response.json()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
