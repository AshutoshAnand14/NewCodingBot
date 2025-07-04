from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Store tasks in memory (for simplicity)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return redirect(url_for('index'))

@app.route('/toggle_task/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 
    
    