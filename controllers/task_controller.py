from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/create_task', methods=['GET'])
def create_task_form():
    return render_template('create_task.html')

@task_blueprint.route('/create_task', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

# Vista para el formulario de actualizar tarea
@task_blueprint.route('/update_task', methods=['GET'])
def update_task_form():
    return render_template('update_task.html')

@task_blueprint.route('/update_task', methods=['POST'])
def update_task():
    data = request.form
    task_id = data.get('task_id')
    name = data.get('name')
    description = data.get('description')

    if not task_id:
        return jsonify({'error': 'Task ID is required'}), 400

    updated = TaskService.update_task(task_id, name, description)
    if not updated:
        return jsonify({'error': 'Task not found'}), 404

    return redirect(url_for('tasks.index'))


@task_blueprint.route('/')
def index():
    return render_template('index.html')